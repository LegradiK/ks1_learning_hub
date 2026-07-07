from flask import render_template

from app.hub import bp


@bp.route("/")
def index():
    return render_template("hub/index.html")