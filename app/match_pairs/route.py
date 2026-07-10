"""Match Pairs routes.

One page route renders the game shell; the JSON API deals a fresh
shuffled board at the requested difficulty. All dealing lives in
game_logic.py (pure Python, no Flask imports).
"""

from flask import render_template, request, jsonify

from app.match_pairs import bp
from app.match_pairs.game_logic import deal_board, PAIRS, DEFAULT_DIFFICULTY


@bp.route("/")
def game():
    return render_template("match_pairs/game.html")


@bp.route("/api/board")
def api_board():
    """Return a fresh board as JSON.

    Query params:
        difficulty: easy | medium | hard | extra_hard   (default easy)

    -> {difficulty, pairs, cards: [{pair, type, face}, ...]}
    """
    difficulty = request.args.get("difficulty", DEFAULT_DIFFICULTY)
    if difficulty not in PAIRS:
        difficulty = DEFAULT_DIFFICULTY
    return jsonify(deal_board(difficulty))