from flask import Blueprint

bp = Blueprint(
    "story_detective",
    __name__,
    # templates stay in the central app/templates/story_detective/ folder,
    # so no template_folder override needed
)

from app.story_detective import route  # noqa: E402,F401  (register routes on bp)