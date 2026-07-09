"""Coin Counter routes.

One page route renders the game shell; the JSON API deals a fresh
question at the requested mode and difficulty. All generation lives
in game_logic.py (pure Python, no Flask imports).
"""

from flask import render_template, request, jsonify

from app.coin_counter import bp
from app.coin_counter.game_logic import (
    generate_question, MODES, DIFFICULTY, DEFAULT_MODE, DEFAULT_DIFFICULTY,
)


@bp.route("/")
def game():
    return render_template("coin_counter/game.html")


@bp.route("/api/question")
def api_question():
    """Return a fresh question as JSON.

    Query params:
        mode: count | make                       (default count)
        difficulty: easy | medium | hard | expert (default easy)

    count -> {mode, difficulty, coins, total, total_label}
    make  -> {mode, difficulty, target, target_label, coins}
    """
    mode = request.args.get("mode", DEFAULT_MODE)
    if mode not in MODES:
        mode = DEFAULT_MODE

    difficulty = request.args.get("difficulty", DEFAULT_DIFFICULTY)
    if difficulty not in DIFFICULTY:
        difficulty = DEFAULT_DIFFICULTY

    return jsonify(generate_question(mode=mode, difficulty=difficulty))