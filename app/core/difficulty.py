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
        "easy":   {"mode": "beginner"},
        "medium": {"mode": "advanced"},
        "hard":   {"mode": "advanced"},
    },
    "math_drill": {
        # digit_pairs feeds game_logic.new_question(); one pair is picked
        # at random per question, so a level can mix number sizes.
        "easy":   {"digit_pairs": [((1, 9),   (1, 9))]},
        "medium": {"digit_pairs": [((1, 9),   (10, 99)), ((10, 99), (1, 9))]},
        "hard":   {"digit_pairs": [((10, 99), (10, 99)), ((100, 999), (100, 999))]},
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