"""Match Pairs blueprint — flip cards to match pictures with words."""

from flask import Blueprint

bp = Blueprint("match_pairs", __name__)

# imported at the bottom to avoid circular imports (bp must exist first)
from app.match_pairs import route  # noqa: E402,F401