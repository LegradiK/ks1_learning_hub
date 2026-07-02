from flask import render_template, request, jsonify
from app.letter_quest import bp
from app.letter_quest.game_logic import generate_puzzle
from app.core.difficulty import get_app_settings

@bp.route("/")
def game():
    settings = get_app_settings("letter_quest")
    puzzle = generate_puzzle(**settings)
    return render_template("letter_quest/game.html", puzzle=puzzle)