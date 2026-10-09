from flask import Blueprint

# cli_group=None → `flask import-bookshelf`, not `flask bookshelf import-bookshelf`
bp = Blueprint("bookshelf", __name__, cli_group=None)

from app.bookshelf import route, cli  # noqa: E402,F401
