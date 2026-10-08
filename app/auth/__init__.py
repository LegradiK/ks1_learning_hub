from flask import Blueprint

# cli_group=None → commands are `flask add-child`, not `flask auth add-child`
bp = Blueprint("auth", __name__, cli_group=None)

from app.auth import route, cli  # noqa: E402,F401
