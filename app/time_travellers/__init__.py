from flask import Blueprint

bp = Blueprint(
    "time_travellers",
    __name__,
    # templates live in the central app/templates/time_travellers/ folder
)

from app.time_travellers import route  # noqa: E402,F401  (register routes on bp)
