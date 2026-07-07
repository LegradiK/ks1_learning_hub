"""Word Wizard routes — difficulty is game-local, back in the URL per stage
(each stage's quiz dict is keyed by its own difficulty levels)."""

from flask import render_template, session, abort

from app.word_wizard import bp
from app.word_wizard.game_logic import pick_word
from app.word_wizard.resources import QUIZZES


@bp.route("/")
def game():
    """Stage chooser — no active question yet."""
    return render_template(
        "word_wizard/game.html",
        quizzes=QUIZZES,
        question=None,
        active_id=None,
        active_difficulty=None,
    )


@bp.route("/stage/<stage_id>/<difficulty>")
def stage(stage_id, difficulty):
    quiz = QUIZZES.get(stage_id)
    if quiz is None or difficulty not in quiz:
        abort(404)

    all_words = quiz[difficulty]

    # Per-user used-word tracking, keyed by stage + difficulty
    used_map = session.get("ww_used", {})
    key = f"{stage_id}_{difficulty}"
    question, used = pick_word(all_words, used_map.get(key, []))
    used_map[key] = used
    session["ww_used"] = used_map
    session.modified = True

    return render_template(
        "word_wizard/game.html",
        quizzes=QUIZZES,
        question=question,
        active_id=stage_id,
        active_difficulty=difficulty,
        resource=quiz,
    )


@bp.route("/reset")
def reset():
    """Forget which words have been seen."""
    session.pop("ww_used", None)
    return render_template(
        "word_wizard/game.html",
        quizzes=QUIZZES,
        question=None,
        active_id=None,
        active_difficulty=None,
    )