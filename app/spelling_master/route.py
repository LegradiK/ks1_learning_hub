"""Spelling Master routes.

The page asks the server for a round of words, then checks each answer
through the API. Progress (which words the child gets wrong) is saved to
the logged-in child's account, so it follows them to any device.
"""

from flask import abort, jsonify, render_template, request

from app.progress import load_progress, save_progress
from app.spelling_master import bp
from app.spelling_master.game_logic import (
    add_gaps, all_words, build_round, check_spelling, clean_history, list_weeks,
    record_result, tricky_words,
)

GAME = "spelling_master"


def _history():
    # clean_history drops words that are no longer in words.json
    return clean_history(load_progress(GAME))


@bp.route("/")
def game():
    return render_template("spelling_master/game.html", weeks=list_weeks())


@bp.route("/api/round", methods=["POST"])
def new_round():
    """Body: {"mode": "week"|"random"|"tricky", "week": 1}"""
    data = request.get_json(silent=True) or {}
    week = data.get("week")
    try:
        week = int(week) if week is not None else None
        title, words = build_round(data.get("mode"), week=week, history=_history())
    except (TypeError, ValueError) as err:
        abort(400, description=str(err))
    return jsonify(title=title, words=add_gaps(words))


@bp.route("/api/check", methods=["POST"])
def check():
    """Body: {"word": "because", "attempt": "becos"} → verdict + letter feedback."""
    data = request.get_json(silent=True) or {}
    word = str(data.get("word", ""))
    attempt = str(data.get("attempt", ""))[:40]
    if word not in {w["word"] for w in all_words()}:
        abort(400, description="Unknown word")

    result = check_spelling(word, attempt)
    save_progress(GAME, record_result(_history(), word, attempt, result["correct"]))
    return jsonify(**result, answer=word)


@bp.route("/api/tricky", methods=["POST"])
def tricky():
    """The words to practise, worst first."""
    return jsonify(words=tricky_words(_history()))


@bp.route("/api/reset", methods=["POST"])
def reset():
    """Grown-ups' "reset progress" button."""
    save_progress(GAME, {})
    return jsonify(ok=True)
