"""Shared difficulty system for the KS1 Learning Hub.

One global level (easy / medium / hard) stored in the Flask session,
translated into per-game parameters via the SETTINGS table.

Usage in a game's routes.py:

    from app.core.difficulty import get_app_settings

    settings = get_app_settings("letter_quest")
    puzzle = generate_puzzle(**settings)

The hub blueprint calls set_difficulty(); the context processor in
app/__init__.py exposes get_difficulty() to every template as `difficulty`.
"""

from flask import session

LEVELS = ("easy", "medium", "hard")
DEFAULT = "easy"

# One global level -> concrete settings per game.
# Keys inside each level dict should match the keyword arguments
# your game_logic functions accept.
SETTINGS = {
    "letter_quest": {
        "easy":   {"grid_size": 8,  "max_word_len": 4, "picture_clues": True},
        "medium": {"grid_size": 10, "max_word_len": 6, "picture_clues": True},
        "hard":   {"grid_size": 12, "max_word_len": 8, "picture_clues": False},
    },
    "math_drill": {
        "easy":   {"max_number": 10,  "operations": ["+"],           "num_questions": 6,  "time_limit": None},
        "medium": {"max_number": 20,  "operations": ["+", "-"],      "num_questions": 8,  "time_limit": 60},
        "hard":   {"max_number": 100, "operations": ["+", "-", "x"], "num_questions": 10, "time_limit": 45},
    },
    "word_wizard": {
        # `bank` names which word bank game_logic should draw from
        # (see app/word_wizard/word_banks/); `hints` feeds the template.
        "easy":   {"bank": "easy", "word_length": (3, 4), "hints": 3},
        "medium": {"bank": "mixed", "word_length": (4, 6), "hints": 2},
        "hard":   {"bank": "hard", "word_length": (5, 8), "hints": 1},
    },
}


def get_difficulty() -> str:
    """Current global difficulty level, defaulting to easy."""
    return session.get("difficulty", DEFAULT)


def set_difficulty(level: str) -> None:
    """Store a new global level in the session. Ignores unknown levels."""
    if level in LEVELS:
        session["difficulty"] = level


def get_app_settings(app_name: str) -> dict:
    """Settings dict for one game at the current difficulty.

    Raises KeyError if app_name isn't in SETTINGS — deliberate, so a
    typo in a blueprint fails loudly rather than silently defaulting.
    """
    return SETTINGS[app_name][get_difficulty()]