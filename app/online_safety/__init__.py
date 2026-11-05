from flask import Blueprint

bp = Blueprint("online_safety", __name__)   # templates: app/templates/lessons/ (shared)

from app.online_safety import route  # noqa: E402,F401  (register routes on bp)
