"""MathDrill routes — was main.py.

What changed from the standalone version:
- @app.route -> @bp.route; url_for("index") -> url_for("math_drill.index")
- app creation, load_dotenv, secret_key: gone — handled by the app factory
- The local /difficulty/<level> route is REMOVED. Difficulty is now global
  (hub.change_difficulty) and digit ranges come from get_app_settings().
- Session keys are namespaced with "md_" so they can't collide with the
  global session["difficulty"] or other games' state.
"""

from flask import render_template, request, redirect, url_for, session, flash

from app.math_drill import bp
from app.math_drill.game_logic import new_question, CALC_TYPES, STYLES
from app.core.difficulty import get_app_settings, get_difficulty


def _fresh_question():
    settings = get_app_settings("math_drill")
    return new_question(settings["digit_pairs"], session.get("md_calc_type", "addition"))


def init_session():
    session.setdefault("md_correct", 0)
    session.setdefault("md_wrong", 0)
    session.setdefault("md_streak", 0)
    session.setdefault("md_total", 0)
    session.setdefault("md_calc_type", "addition")
    session.setdefault("md_eq_style", "inline")

    # Regenerate if there's no question yet, or if the global difficulty
    # changed since the current question was generated.
    if "md_question" not in session or session.get("md_level") != get_difficulty():
        session["md_question"] = _fresh_question()
        session["md_level"] = get_difficulty()


@bp.route("/")
def index():
    init_session()
    q = session["md_question"]
    return render_template(
        "math_drill/game.html",
        num1=q["num1"], op=q["op"], num2=q["num2"],
        correct=session["md_correct"],
        wrong=session["md_wrong"],
        streak=session["md_streak"],
        total=session["md_total"],
        calc_type=session["md_calc_type"],
        eq_style=session["md_eq_style"],
        calc_types=CALC_TYPES,
    )


@bp.route("/check", methods=["POST"])
def check_answer():
    init_session()
    q = session["md_question"]
    try:
        user_answer = int(request.form["answer"])
    except (ValueError, KeyError):
        flash("Please enter a whole number.", "info")
        return redirect(url_for("math_drill.index"))

    session["md_total"] += 1
    if user_answer == q["answer"]:
        session["md_correct"] += 1
        session["md_streak"] += 1
        flash(f"✓ Correct!  {q['num1']} {q['op']} {q['num2']} = {q['answer']}", "success")
    else:
        session["md_wrong"] += 1
        session["md_streak"] = 0
        flash(f"✗ Not quite: {q['num1']} {q['op']} {q['num2']} = {q['answer']}, you answered {user_answer}.", "error")

    session["md_question"] = _fresh_question()
    session.modified = True
    return redirect(url_for("math_drill.index"))


@bp.route("/new")
def new_question_route():
    init_session()
    session["md_question"] = _fresh_question()
    session.modified = True
    return redirect(url_for("math_drill.index"))


@bp.route("/type/<calc_type>")
def set_type(calc_type):
    if calc_type in CALC_TYPES:
        session["md_calc_type"] = calc_type
        session["md_question"] = _fresh_question()
        session.modified = True
    return redirect(url_for("math_drill.index"))


@bp.route("/style/<style>")
def set_style(style):
    if style in STYLES:
        session["md_eq_style"] = style
        session.modified = True
    return redirect(url_for("math_drill.index"))


@bp.route("/reset")
def reset():
    for key in ("md_correct", "md_wrong", "md_streak", "md_total", "md_question"):
        session.pop(key, None)
    return redirect(url_for("math_drill.index"))