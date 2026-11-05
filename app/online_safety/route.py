from app.lesson_kit import add_lesson_routes
from app.online_safety import bp
from app.online_safety.lessons import AREAS, LESSONS
from app.online_safety.sorts import SORT_SETS

add_lesson_routes(
    bp,
    subject={
        "name": "Safe Surfers",
        "badge": "🏄",
        "theme": "theme-safety",
        "tagline": "Learn to surf the internet safely — pick a lesson, then try the quiz!",
        "group": "online-safety",
        "done_title": "Safe Surfer, you did it!",
    },
    areas=AREAS,
    lessons=LESSONS,
    sort_sets=SORT_SETS,
)
