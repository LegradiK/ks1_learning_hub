"""Phonics Fox routes.

One page route renders the game shell; the JSON API deals a fresh
phonics question at the requested mode and year group. All generation
lives in game_logic.py (pure Python, no Flask imports).
"""

from flask import render_template, request, jsonify

from app.phonics_fox import bp
from app.phonics_fox.game_logic import (
    generate_question, MODES, YEARS, DEFAULT_MODE, DEFAULT_YEAR,
)


@bp.route("/")
def game():
    return render_template("phonics_fox/game.html")


@bp.route("/api/question")
def api_question():
    """Return a fresh question as JSON.

    Query params:
        mode: insert | choose | spell             (default insert)
        year: reception | year1 | year2           (default reception)

    insert -> {mode, year, word, grapheme, gapped, options}
    choose -> {mode, year, word, grapheme, options}
    spell  -> {mode, year, word, grapheme}
    """
    mode = request.args.get("mode", DEFAULT_MODE)
    if mode not in MODES:
        mode = DEFAULT_MODE

    year = request.args.get("year", DEFAULT_YEAR)
    if year not in YEARS:
        year = DEFAULT_YEAR

    return jsonify(generate_question(mode=mode, year=year))