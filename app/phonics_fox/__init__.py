from flask import Blueprint

bp = Blueprint(
    "phonics_fox",
    __name__,
    # templates stay in the central app/templates/phonics_fox/ folder,
    # so no template_folder override needed
)

from app.phonics_fox import route  # noqa: E402,F401  (register routes on bp)