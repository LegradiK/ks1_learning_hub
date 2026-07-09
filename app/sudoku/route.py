"""Sudoku routes.

One page route renders the game shell; the JSON API generates a fresh
puzzle at the requested size. All generation lives in game_logic.py
(pure Python, no Flask imports, no data files).
"""

from flask import render_template, request, jsonify

from app.sudoku import bp
from app.sudoku.game_logic import generate_puzzle, SIZES, DEFAULT_SIZE


@bp.route("/")
def game():
    return render_template("sudoku/game.html")


@bp.route("/api/puzzle")
def api_puzzle():
    """Return {size, boxRows, boxCols, difficulty, grid, solution}.

    Query params:
        size: 4 | 6 | 9        (default 4)
        difficulty: easy | medium | hard   (default easy)
    """
    try:
        size = int(request.args.get("size", DEFAULT_SIZE))
    except ValueError:
        size = DEFAULT_SIZE
    if size not in SIZES:
        size = DEFAULT_SIZE

    difficulty = request.args.get("difficulty", "easy")
    return jsonify(generate_puzzle(size=size, difficulty=difficulty))