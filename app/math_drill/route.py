from flask import render_template, request, jsonify
from app.math_drill import bp
from app.math_drill.game_logic import generate_puzzle
from app.core.difficulty import get_app_settings

@bp.route("/")
def game():
    settings = get_app_settings("math_drill")
    puzzle = generate_puzzle(**settings)
    return render_template("math_drill/game.html", puzzle=puzzle)