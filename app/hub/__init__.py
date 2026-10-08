from flask import Blueprint

bp = Blueprint("hub", __name__)


@bp.app_context_processor
def inject_nav():
    """Make the menu data available to base.html on every page."""
    from app.hub.activities import ACTIVITIES, groups_in
    return {
        "nav_subjects": groups_in("subjects"),
        "nav_activities": ACTIVITIES,
    }


from app.hub import route  # noqa: E402,F401
