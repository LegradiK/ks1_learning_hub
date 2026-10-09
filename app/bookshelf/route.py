"""My Bookshelf: the child's reading log, moved in from the standalone site.

Books belong to whoever is logged in (g.child) — the hub's login check in
app/auth/route.py already guards every page here.
"""

from datetime import datetime

import requests
from flask import abort, flash, g, redirect, render_template, request, send_file, url_for
from markupsafe import escape

from app.bookshelf import bp
from app.bookshelf import books_api as api
from app.extensions import db
from app.models import BOOK_STATUSES, Book, ReadingLog
from app.study import today_uk

PER_PAGE = 20
STATUS_LABELS = {"want_to_read": "Want to read", "reading": "Reading now", "finished": "Finished"}
MILESTONES = [1, 5, 10, 20, 30, 50, 80, 100, 150, 200, 300, 400, 500, 750, 1000]


@bp.app_context_processor
def inject_status_labels():
    return {"status_labels": STATUS_LABELS}


def _mine():
    return Book.query.filter(Book.child_id == g.child.id)


def _my_book(book_id):
    return _mine().filter(Book.id == book_id).first_or_404()


def _status(value, default="want_to_read"):
    return value if value in BOOK_STATUSES else default


# ── The shelf ────────────────────────────────────────────────────────────────
@bp.route("/")
def shelf():
    sort = request.args.get("sort", "recent")
    selected_genre = request.args.get("genre", "")
    selected_author = request.args.get("author", "")
    active_status = request.args.get("status", "all")
    page = max(1, request.args.get("page", 1, type=int))
    query_text = request.args.get("q", "").strip()

    mine = _mine().all()
    # Filter lists come from this child's books only
    genres = sorted({g_ for b in mine for g_ in b.genre_list})
    authors = sorted({b.author for b in mine if b.author})
    counts = {s: sum(1 for b in mine if b.status == s) for s in BOOK_STATUSES}
    counts["all"] = len(mine)

    books = mine
    if active_status in BOOK_STATUSES:
        books = [b for b in books if b.status == active_status]
    if selected_genre:
        books = [b for b in books if selected_genre in b.genre_list]
    if selected_author:
        books = [b for b in books if b.author == selected_author]
    if query_text:
        q = api.normalize_text(query_text)
        books = [b for b in books
                 if q in api.normalize_text(b.title) or q in api.normalize_text(b.author)]

    sorters = {
        "title": lambda b: (b.title or "").lower(),
        "author": lambda b: (b.author or "").lower(),
        "genre": lambda b: (b.categories or "~").lower(),
    }
    if sort in sorters:
        books.sort(key=sorters[sort])
    elif sort == "stars":
        books.sort(key=lambda b: (b.average_stars or 0, b.id), reverse=True)
    else:
        sort = "recent"
        books.sort(key=lambda b: b.id, reverse=True)

    total = len(books)
    shown = books[:page * PER_PAGE]
    return render_template(
        "bookshelf/shelf.html",
        books=shown, total_count=total, has_more=total > len(shown), page=page,
        genres=genres, authors=authors, counts=counts,
        sort=sort, selected_genre=selected_genre, selected_author=selected_author,
        active_status=active_status, query=query_text,
    )


# ── Finding and adding books ─────────────────────────────────────────────────
@bp.route("/add")
def add_page():
    return render_template("bookshelf/add.html")


@bp.route("/api/search")
def api_search():
    q = request.args.get("q", "").strip()
    if not q:
        return {"items": [], "total_items": 0}
    try:
        items, total = api.search_google_books(q, request.args.get("start", 0, type=int))
    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 429:
            return {"error": "Search is busy right now — wait a moment and try again."}
        return {"error": "Something went wrong searching. Try again."}
    except requests.exceptions.RequestException:
        return {"error": "Something went wrong searching. Try again."}
    mine = {b.google_books_id for b in _mine().with_entities(Book.google_books_id)}
    for item in items:
        item["on_shelf"] = item["google_books_id"] in mine
    return {"items": items, "total_items": total}


def _new_book(details, status):
    genres = api.get_genres_from_open_library(details.get("isbn"),
                                              google_categories=details.get("categories"))
    book = Book(
        child_id=g.child.id,
        google_books_id=details["google_books_id"],
        isbn=(details.get("isbn") or "")[:20] or None,
        title=(details.get("title") or "Untitled")[:300],
        author=(details.get("author") or "")[:300],
        cover_url=api.https_cover(details.get("cover_url")),
        categories=(", ".join(genres) if genres else details.get("categories") or "")[:255],
        status="want_to_read", times_read=0,
    )
    book.set_status(status)
    db.session.add(book)
    return book


@bp.route("/add", methods=["POST"])
def add_book():
    gid = request.form.get("google_books_id", "")
    existing = _mine().filter_by(google_books_id=gid).first()
    if existing:
        flash(f"“{existing.title}” is already on your shelf! "
              "Read it again? Log another reading on its page.", "info")
        return redirect(url_for("bookshelf.book", book_id=existing.id))

    book = _new_book({k: request.form.get(k) for k in
                      ("google_books_id", "title", "author", "cover_url", "isbn", "categories")},
                     _status(request.form.get("status")))
    db.session.commit()
    flash(f"📚 “{book.title}” is on your shelf!", "success")
    return redirect(url_for("bookshelf.book", book_id=book.id))


@bp.route("/add-many", methods=["POST"])
def add_many():
    status = _status(request.form.get("status"))
    have = {b.google_books_id: b for b in _mine().all()}
    added, already, skipped = 0, [], 0
    for gid in dict.fromkeys(request.form.getlist("google_books_id")):   # de-dupe, keep order
        if gid in have:
            already.append(have[gid].title)
            continue
        try:
            details = api._fetch_volume_details(gid)
        except requests.RequestException:
            skipped += 1
            continue
        have[gid] = _new_book(details, status)
        added += 1
    db.session.commit()

    if added:
        flash(f"📚 Added {added} book{'s' if added != 1 else ''} to your shelf!", "success")
    if already:
        items = "".join(f"<li>{escape(t)}</li>" for t in already)
        flash(f"Already on your shelf:<ul>{items}</ul>", "info")
    if skipped:
        flash(f"{skipped} book(s) couldn't be added — try again in a moment.", "error")
    return redirect(url_for("bookshelf.shelf"))


# ── One book ──────────────────────────────────────────────────────────────────
@bp.route("/book/<int:book_id>")
def book(book_id):
    return render_template("bookshelf/book.html", book=_my_book(book_id), today=today_uk())


@bp.route("/book/<int:book_id>/status", methods=["POST"])
def update_status(book_id):
    b = _my_book(book_id)
    b.set_status(request.form.get("status"))
    db.session.commit()
    return redirect(url_for("bookshelf.book", book_id=b.id))


@bp.route("/book/<int:book_id>/times-read", methods=["POST"])
def update_times_read(book_id):
    b = _my_book(book_id)
    times = request.form.get("times_read", type=int)
    if b.status == "finished" and times is not None and 1 <= times <= 999:
        b.times_read = times
    db.session.commit()
    return redirect(url_for("bookshelf.book", book_id=b.id))


@bp.route("/book/<int:book_id>/genres", methods=["POST"])
def update_genres(book_id):
    b = _my_book(book_id)
    b.categories = request.form.get("categories", "").strip()[:255]
    db.session.commit()
    return redirect(url_for("bookshelf.book", book_id=b.id))


@bp.route("/api/genres")
def api_genres():
    return {"genres": api.lookup_genres(request.args.get("isbn"),
                                        request.args.get("title", "").strip(),
                                        request.args.get("author", "").strip())}


@bp.route("/book/<int:book_id>/log", methods=["POST"])
def log_reading(book_id):
    """Log a reading: date, stars, review. Each log after the first is a re-read."""
    b = _my_book(book_id)
    try:
        date_read = datetime.strptime(request.form.get("date_read", ""), "%Y-%m-%d").date()
    except ValueError:
        date_read = today_uk()
    date_read = min(date_read, today_uk())              # no readings in the future
    stars = request.form.get("stars", type=int)
    stars = stars if stars in range(1, 6) else None

    had_logs = bool(b.logs)                            # check before adding (autoflush)
    if b.status != "finished":
        b.set_status("finished")
    elif had_logs:                                     # finished and logged before: a re-read
        b.times_read += 1
    db.session.add(ReadingLog(book_id=b.id, date_read=date_read, stars=stars,
                              review=request.form.get("review", "").strip()[:2000] or None))
    b.finished_on = min(b.finished_on or date_read, date_read)
    db.session.commit()
    flash("⭐ Reading saved — well done!", "success")
    return redirect(url_for("bookshelf.book", book_id=b.id))


@bp.route("/book/<int:book_id>/log/<int:log_id>/delete", methods=["POST"])
def delete_log(book_id, log_id):
    b = _my_book(book_id)
    log = ReadingLog.query.filter_by(id=log_id, book_id=b.id).first_or_404()
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for("bookshelf.book", book_id=b.id))


@bp.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    b = _my_book(book_id)
    title = b.title
    db.session.delete(b)                    # logs go too (cascade)
    db.session.commit()
    flash(f"Removed “{title}” from your shelf.", "info")
    return redirect(url_for("bookshelf.shelf"))


@bp.route("/delete-many", methods=["POST"])
def delete_many():
    ids = request.form.getlist("book_id", type=int)
    if ids:
        for b in _mine().filter(Book.id.in_(ids)).all():
            db.session.delete(b)
        db.session.commit()
    return redirect(url_for("bookshelf.shelf"))


# ── Achievements ─────────────────────────────────────────────────────────────
def _finished_count():
    return _mine().filter(Book.status == "finished").count()


@bp.route("/achievements")
def achievements():
    finished = _finished_count()
    achieved = [m for m in MILESTONES if finished >= m]
    nxt = next((m for m in MILESTONES if finished < m), None)
    prev = achieved[-1] if achieved else 0
    pct = int((finished - prev) / (nxt - prev) * 100) if nxt else 100
    return render_template(
        "bookshelf/achievements.html",
        milestones=MILESTONES, achieved=achieved, finished_count=finished,
        next_milestone=nxt, books_to_next=(nxt - finished) if nxt else 0, progress_pct=pct,
    )


@bp.route("/achievements/certificate")
def certificate():
    achieved = [m for m in MILESTONES if _finished_count() >= m]
    if not achieved:
        abort(404)
    from app.bookshelf.certificate import make_certificate
    pdf, filename = make_certificate(g.child.name, achieved[-1], today_uk())
    return send_file(pdf, mimetype="application/pdf", as_attachment=True,
                     download_name=filename)
