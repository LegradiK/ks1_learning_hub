"""Clock Master routes.

One page route renders the game shell; the JSON API deals a fresh
time question at the requested mode and difficulty. All generation
lives in game_logic.py (pure Python, no Flask imports).
"""

from flask import render_template, request, jsonify

from app.clock_master import bp
from app.clock_master.game_logic import (
    generate_question, MODES, DIFFICULTY, DEFAULT_MODE, DEFAULT_DIFFICULTY,
)


@bp.route("/")
def game():
    return render_template("clock_master/game.html")


@bp.route("/api/question")
def api_question():
    """Return a fresh question as JSON.

    Query params:
        mode: read | set                              (default read)
        difficulty: oclock | half | quarter | five    (default oclock)

    read -> {mode, difficulty, hour, minute, phrase, digital, options}
    set  -> {mode, difficulty, hour, minute, phrase, digital}
    """
    mode = request.args.get("mode", DEFAULT_MODE)
    if mode not in MODES:
        mode = DEFAULT_MODE

    difficulty = request.args.get("difficulty", DEFAULT_DIFFICULTY)
    if difficulty not in DIFFICULTY:
        difficulty = DEFAULT_DIFFICULTY

    return jsonify(generate_question(mode=mode, difficulty=difficulty))