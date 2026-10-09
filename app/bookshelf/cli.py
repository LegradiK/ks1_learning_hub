"""Bring books across from the old standalone bookshelf site.

    flask --app run import-bookshelf path/to/reading_tracker.db Leo
    flask --app run import-bookshelf path/to/reading_tracker.db Leo --from-user leo

Copies every book (and any reading logs) owned by the old site's user into
the hub child's shelf. Safe to run twice: books already on the child's shelf
(same Google Books id) are skipped. Run it with DATABASE_URL pointing at the
database you want to fill (the live one is in data.env).
"""

from datetime import date

import click
from sqlalchemy import create_engine, text

from app.bookshelf import bp
from app.bookshelf.books_api import https_cover
from app.extensions import db
from app.models import BOOK_STATUSES, Book, Child, ReadingLog


def _as_date(value):
    if value is None or isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


@bp.cli.command("import-bookshelf")
@click.argument("source")
@click.argument("child_name")
@click.option("--from-user", help="Username on the old site (default: same as CHILD_NAME).")
@click.option("--dry-run", is_flag=True, help="Show what would be copied without saving.")
def import_bookshelf(source, child_name, from_user, dry_run):
    """Copy books from the old bookshelf database SOURCE into CHILD_NAME's shelf.

    SOURCE is a path to the old .db file, or a database URL.
    """
    child = Child.find(child_name)
    if child is None:
        raise click.ClickException(f"No hub login called {child_name}. Create it with add-child first.")

    url = source if "://" in source else f"sqlite:///{source}"
    src = create_engine(url)
    with src.connect() as conn:
        users = conn.execute(text("SELECT id, username FROM user")).all()
        wanted = (from_user or child_name).strip().lower()
        user = next((u for u in users if u.username.strip().lower() == wanted), None)
        if user is None:
            names = ", ".join(u.username for u in users) or "none"
            raise click.ClickException(f"No user '{from_user or child_name}' in the old site (found: {names}). "
                                       "Use --from-user.")
        books = conn.execute(text("SELECT * FROM book WHERE user_id = :u ORDER BY id"),
                             {"u": user.id}).mappings().all()
        logs = conn.execute(text(
            "SELECT reading_log.* FROM reading_log JOIN book ON book.id = reading_log.book_id "
            "WHERE book.user_id = :u"), {"u": user.id}).mappings().all()

    logs_by_book = {}
    for log in logs:
        logs_by_book.setdefault(log["book_id"], []).append(log)

    have = {b.google_books_id for b in Book.query.filter_by(child_id=child.id)}
    added = skipped = log_count = 0
    for old in books:
        if old["google_books_id"] and old["google_books_id"] in have:
            skipped += 1
            continue
        status = old["status"] if old["status"] in BOOK_STATUSES else "want_to_read"
        old_logs = logs_by_book.get(old["id"], [])
        log_dates = [d for d in (_as_date(lg["date_read"]) for lg in old_logs) if d]
        book = Book(
            child_id=child.id,
            title=old["title"], author=old["author"], isbn=old["isbn"],
            cover_url=https_cover(old["cover_url"]), categories=old["categories"],
            google_books_id=old["google_books_id"], status=status,
            added_on=_as_date(old["added_on"]) or date.today(),
            # Only real reading dates count on the progress report; books bulk-added
            # as "finished" have no date, so they don't all land on one day.
            finished_on=min(log_dates) if (status == "finished" and log_dates) else None,
            times_read=old["times_read"] or (1 if status == "finished" else 0),
        )
        db.session.add(book)
        db.session.flush()
        for lg in old_logs:
            db.session.add(ReadingLog(book_id=book.id, date_read=_as_date(lg["date_read"]) or book.added_on,
                                      stars=lg["stars"] or None, review=lg["review"] or None))
            log_count += 1
        have.add(old["google_books_id"])
        added += 1

    if dry_run:
        db.session.rollback()
        click.echo(f"Dry run: would add {added} books and {log_count} readings "
                   f"({skipped} already on {child.name}'s shelf).")
        return
    db.session.commit()
    click.echo(f"Added {added} books and {log_count} readings to {child.name}'s shelf "
               f"({skipped} were already there).")
