from flask import render_template

from app.lesson_kit import add_lesson_routes
from app.time_travellers import bp
from app.time_travellers.lessons import AREAS, LESSONS
from app.time_travellers.practice import SORT_SETS, TIMELINE, TIMELINE_LEVELS

# Menu, lessons and the Then or Now? sort game come from the shared engine
add_lesson_routes(
    bp,
    subject={
        "name": "Time Travellers",
        "badge": "🕰️",
        "theme": "theme-history",
        "tagline": "Jump into the time machine — pick a lesson, then try the quiz!",
        "group": "history",
        "done_title": "Time traveller, you did it!",
    },
    areas=AREAS,
    lessons=LESSONS,
    sort_sets=SORT_SETS,
    extra_games=[{
        "endpoint": "time_travellers.timeline", "emoji": "📏",
        "title": "Timeline Challenge",
        "blurb": "Put famous events in order, from oldest to newest.",
    }],
)


@bp.route("/timeline")
def timeline():
    return render_template("time_travellers/timeline.html",
                           events=TIMELINE, levels=TIMELINE_LEVELS)
