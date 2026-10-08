from flask import Blueprint

bp = Blueprint("spelling_master", __name__)

from app.spelling_master import route  # noqa: E402,F401  (register routes on bp)
