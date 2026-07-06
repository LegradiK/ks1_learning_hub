"""Word Wizard routes — was main.py.

What changed from the standalone version:
- @app.route -> @bp.route; endpoints now word_wizard.game / word_wizard.stage
- importlib file loading -> normal imports via resources/__init__.py (QUIZZES)
- Difficulty is REMOVED from the URL. The global picker in base.html sets it;
  routes read it with get_difficulty(). NOTE: your quiz dicts must be keyed
  "easy" / "medium" / "hard" to match — rename keys if they differ.
- used_words module-level dict -> session["ww_used"]. The old global was
  shared between ALL users (one child's used words hid words from another)
  and vanished on every server restart. Session storage is per-user.
- Fixed two bugs: word_quiz() was called with 2 args but defined with 3,
  and the stage route rendered "main.py" instead of the template.
"""

from flask import render_template, session, abort

from app.word_wizard import bp
from app.word_wizard.game_logic import pick_word
from app.word_wizard.resources import QUIZZES
from app.core.difficulty import get_difficulty


@bp.route("/")
def game():
    """Stage chooser — no active question yet."""
    return render_template(
        "word_wizard/game.html",
        quizzes=QUIZZES,
        question=None,
        active_id=None,
    )


@bp.route("/stage/<stage_id>")
def stage(stage_id):
    if stage_id not in QUIZZES:
        abort(404)

    level = get_difficulty()
    quiz = QUIZZES[stage_id]
    all_words = quiz[level]

    # Per-user used-word tracking, keyed by stage + difficulty
    used_map = session.get("ww_used", {})
    key = f"{stage_id}_{level}"
    question, used = pick_word(all_words, used_map.get(key, []))
    used_map[key] = used
    session["ww_used"] = used_map
    session.modified = True

    return render_template(
        "word_wizard/game.html",
        quizzes=QUIZZES,
        question=question,
        active_id=stage_id,
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
    )