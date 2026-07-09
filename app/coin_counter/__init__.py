from flask import Blueprint

bp = Blueprint(
    "coin_counter",
    __name__,
    # templates stay in the central app/templates/coin_counter/ folder,
    # so no template_folder override needed
)

from app.coin_counter import route  # noqa: E402,F401  (register routes on bp)