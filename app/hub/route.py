from flask import abort, render_template

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
