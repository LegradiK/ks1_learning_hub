"""Grown-up commands for managing who can log in.

There's no sign-up page on purpose: only you can create accounts.
Run these on your own computer with DATABASE_URL pointing at the live
database (it's in data.env), e.g.

    flask --app run add-child Leo
    flask --app run set-pin Leo
    flask --app run list-children
    flask --app run remove-child Leo
"""

import click

from app.auth import bp
from app.extensions import db
from app.models import Child


def _ask_pin():
    while True:
        pin = click.prompt("4-digit PIN", hide_input=True, confirmation_prompt=True)
        if len(pin) == 4 and pin.isdigit():
            return pin
        click.echo("The PIN must be exactly 4 digits.")


@bp.cli.command("add-child")
@click.argument("name")
def add_child(name):
    """Create a login for NAME (you'll be asked for a PIN)."""
    name = " ".join(name.split())
    if not name or len(name) > 40:
        raise click.ClickException("Name must be 1–40 characters.")
    if Child.find(name):
        raise click.ClickException(f"{name} already has a login. Use set-pin to change the PIN.")
    child = Child(name=name, name_key=Child.key_for(name))
    child.set_pin(_ask_pin())
    db.session.add(child)
    db.session.commit()
    click.echo(f"Added {name}.")


@bp.cli.command("set-pin")
@click.argument("name")
def set_pin(name):
    """Change NAME's PIN (also clears any lock)."""
    child = Child.find(name)
    if not child:
        raise click.ClickException(f"No login called {name}.")
    child.set_pin(_ask_pin())
    child.failed_attempts = 0
    child.locked_until = None
    db.session.commit()
    click.echo(f"PIN updated for {child.name}.")


@bp.cli.command("list-children")
def list_children():
    """Show everyone who can log in."""
    children = Child.query.order_by(Child.name).all()
    if not children:
        click.echo("No logins yet. Add one with: flask --app run add-child NAME")
    for c in children:
        lock = f"  (locked for {c.minutes_locked()} min)" if c.is_locked() else ""
        click.echo(f"- {c.name}{lock}")


@bp.cli.command("remove-child")
@click.argument("name")
@click.confirmation_option(prompt="This deletes the login AND all its progress. Continue?")
def remove_child(name):
    """Delete NAME's login and all their progress."""
    child = Child.find(name)
    if not child:
        raise click.ClickException(f"No login called {name}.")
    db.session.delete(child)
    db.session.commit()
    click.echo(f"Removed {child.name}.")
