from flask import Blueprint

bp = Blueprint("science_lab", __name__)   # templates: app/templates/lessons/ (shared)

from app.science_lab import route  # noqa: E402,F401  (register routes on bp)
