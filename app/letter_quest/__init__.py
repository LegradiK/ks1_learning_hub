from flask import Blueprint

bp = Blueprint(
    "letter_quest",
    __name__,
    # templates stay in the central app/templates/letter_quest/ folder,
    # so no template_folder override needed
)

from app.letter_quest import route  # noqa: E402,F401  (register routes on bp)