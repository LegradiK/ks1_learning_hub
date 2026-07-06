from flask import Blueprint

bp = Blueprint(
    "math_drill",
    __name__,
    # templates stay in the central app/templates/math_drill/ folder,
    # so no template_folder override needed
)

from app.math_drill import route  # noqa: E402,F401  (register routes on bp)