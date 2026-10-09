from flask import abort, g, render_template, request

from app.hub import bp
from app.hub.activities import (
    GROUPS, SECTIONS, activities_in, groups_in,
)


@bp.route("/")
def index():
    """Landing page: School Subjects or Brain Games."""
    return render_template("hub/index.html", sections=SECTIONS)


@bp.route("/subjects")
def subjects():
    """All school subjects (English, Maths, Science...)."""
    return render_template("hub/subjects.html", subjects=groups_in("subjects"))


@bp.route("/play/<slug>")
def group(slug):
    """The activities inside one subject, or the Brain Games list."""
    if slug not in GROUPS:
        abort(404)
    grp = GROUPS[slug]
    back = "hub.subjects" if grp["section"] == "subjects" else "hub.index"
    return render_template(
        "hub/group.html",
        group=grp,
        activities=activities_in(slug),
        back_endpoint=back,
    )


@bp.route("/about")
def about():
    return render_template("hub/about.html")


@bp.route("/progress")
def progress():
    """Progress report: how much the logged-in child played each game."""
    from app.study import report
    return render_template("hub/progress.html",
                           r=report(g.child, request.args.get("range", "week")))


@bp.route("/api/track", methods=["POST"])
def track():
    """Time and answers sent from static/track.js."""
    from app.study import record
    data = request.get_json(silent=True) or {}
    try:
        seconds = int(data.get("seconds") or 0)
    except (TypeError, ValueError):
        seconds = 0
    ok = record(str(data.get("game", "")), seconds, data.get("result"))
    return {"ok": ok}
