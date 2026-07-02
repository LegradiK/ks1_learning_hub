from flask import Blueprint

bp = Blueprint("hub", __name__)

from app.hub import routes  # noqa: E402,F401