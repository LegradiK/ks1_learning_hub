from flask import Blueprint

bp = Blueprint(
    "word_wizard",
    __name__,
    # templates stay in the central app/templates/word_wizard/ folder,
    # so no template_folder override needed
)

from app.word_wizard import route  # noqa: E402,F401  (register routes on bp)