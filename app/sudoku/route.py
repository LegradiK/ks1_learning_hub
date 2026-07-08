"""Sudoku routes.

One page route renders the game shell; the JSON API hands the
front-end a random puzzle from the 4x4 unique-solution dataset.
All data loading lives in game_logic.py (pure Python, no Flask).
"""

from flask import render_template, jsonify

from app.sudoku import bp
from app.sudoku.game_logic import random_puzzle


@bp.route("/")
def game():
    return render_template("sudoku/game.html")


@bp.route("/api/puzzle")
def api_puzzle():
    """Return a fresh random puzzle: {size, grid, solution}, 0 = empty."""
    return jsonify(random_puzzle())