from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv("data.env")


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_KEY")

    from app.hub import bp as hub_bp
    from app.letter_quest import bp as letter_quest_bp
    from app.math_drill import bp as math_drill_bp
    from app.word_wizard import bp as word_wizard_bp
    from app.sudoku import bp as sudoku_bp
    from app.money_counter import bp as money_counter_bp
    from app.clock_master import bp as clock_master_bp

    app.register_blueprint(hub_bp)                                    # "/"
    app.register_blueprint(letter_quest_bp, url_prefix="/letter-quest")
    app.register_blueprint(math_drill_bp,   url_prefix="/math-drill")
    app.register_blueprint(word_wizard_bp,  url_prefix="/word-wizard")
    app.register_blueprint(sudoku_bp, url_prefix="/sudoku")
    app.register_blueprint(money_counter_bp, url_prefix="/money-counter")
    app.register_blueprint(clock_master_bp, url_prefix="/clock-master")

    return app