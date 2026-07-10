from flask import Blueprint

bp = Blueprint(
    "clock_master",
    __name__,
    # templates stay in the central app/templates/clock_master/ folder,
    # so no template_folder override needed
)

from app.clock_master import route  # noqa: E402,F401  (register routes on bp)