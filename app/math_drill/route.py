"""MathDrill routes — per-type difficulty.

Calc type is chosen first; the difficulty options shown depend on it
(levels_for). Switching type snaps the stored level back to that type's
default if the current one doesn't exist there (e.g. addition's
"extra_hard" -> multiplication has no such level).
"""

from flask import render_template, request, redirect, url_for, session, flash

from app.math_drill import bp
from app.math_drill.game_logic import (
    new_question, levels_for, default_level, CALC_TYPES, STYLES,
)


def _fresh_question():
    return new_question(
        session.get("md_calc_type", "addition"),
        session.get("md_difficulty"),
    )


def init_session():
    session.setdefault("md_correct", 0)
    session.setdefault("md_wrong", 0)
    session.setdefault("md_streak", 0)
    session.setdefault("md_total", 0)
    session.setdefault("md_calc_type", "addition")
    session.setdefault("md_difficulty", default_level(session["md_calc_type"]))
    session.setdefault("md_eq_style", "inline")
    if "md_question" not in session:
        session["md_question"] = _fresh_question()


@bp.route("/")
def index():
    init_session()
    q = session["md_question"]
    calc_type = session["md_calc_type"]
    return render_template(
        "math_drill/game.html",
        num1=q["num1"], op=q["op"], num2=q["num2"],
        correct=session["md_correct"],
        wrong=session["md_wrong"],
        streak=session["md_streak"],
        total=session["md_total"],
        difficulty=session["md_difficulty"],
        calc_type=calc_type,
        eq_style=session["md_eq_style"],
        calc_types=CALC_TYPES,
        levels=levels_for(calc_type),   # picker hidden when only 1
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
        # snap the level to this type's set if it doesn't carry over
        if session.get("md_difficulty") not in levels_for(calc_type):
            session["md_difficulty"] = default_level(calc_type)
        session["md_question"] = _fresh_question()
        session.modified = True
    return redirect(url_for("math_drill.index"))


@bp.route("/difficulty/<level>")
def set_difficulty(level):
    init_session()
    if level in levels_for(session["md_calc_type"]):
        session["md_difficulty"] = level
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