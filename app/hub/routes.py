from flask import render_template, redirect, url_for, request
from app.hub import bp
from app.core.difficulty import set_difficulty, LEVELS

@bp.route("/")
def index():
    return render_template("hub/index.html", levels=LEVELS)

@bp.route("/difficulty/<level>", methods=["POST"])
def change_difficulty(level):
    set_difficulty(level)
    return redirect(request.referrer or url_for("hub.index"))