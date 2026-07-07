"""Word Wizard routes.

This game is CLIENT-SIDE: all four stages render as tab panels in one
page, and stage/difficulty switching, word picking, no-repeat tracking,
progress, and speech all happen in the browser JS. The server's only
job is to render the page with the full quiz data embedded.

(The old standalone /stage/<id>/<difficulty> route was dead code — it
rendered "main.py" and was never linked from the template — so it has
no equivalent here.)
"""

from flask import render_template

from app.word_wizard import bp
from app.word_wizard.resources import QUIZZES


@bp.route("/")
def game():
    return render_template("word_wizard/game.html", quizzes=QUIZZES)