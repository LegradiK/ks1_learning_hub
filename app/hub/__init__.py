from flask import Blueprint

bp = Blueprint("hub", __name__)


@bp.app_context_processor
def inject_nav():
    """Make the menu data available to base.html on every page."""
    from flask import request
    from app.hub.activities import ACTIVITIES, groups_in
    from app.study import GAME_KEYS, nice_time
    return {
        "nav_subjects": groups_in("subjects"),
        "nav_activities": ACTIVITIES,
        # set on game pages so static/track.js knows what to time
        "current_game": request.blueprint if request.blueprint in GAME_KEYS else None,
        "nice_time": nice_time,
    }


from app.hub import route  # noqa: E402,F401
