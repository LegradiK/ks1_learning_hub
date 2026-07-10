from flask import Blueprint

bp = Blueprint(
    "money_counter",
    __name__,
    # templates stay in the central app/templates/money_counter/ folder,
    # so no template_folder override needed
)

from app.money_counter import route  # noqa: E402,F401  (register routes on bp)