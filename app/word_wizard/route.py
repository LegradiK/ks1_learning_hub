from flask import render_template, request, jsonify
from app.word_wizard import bp
from app.word_wizard.game_logic import generate_puzzle
from app.core.difficulty import get_app_settings

@bp.route("/")
def game():
    settings = get_app_settings("word_wizard")
    puzzle = generate_puzzle(**settings)
    return render_template("word_wizard/game.html", puzzle=puzzle)