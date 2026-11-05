from app.lesson_kit import add_lesson_routes
from app.science_lab import bp
from app.science_lab.lessons import AREAS, LESSONS
from app.science_lab.sorts import SORT_SETS

add_lesson_routes(
    bp,
    subject={
        "name": "Science Explorers",
        "badge": "🔬",
        "theme": "theme-science",
        "tagline": "Put on your lab goggles — pick a lesson, then try the quiz!",
        "group": "science",
        "done_title": "Super scientist, you did it!",
    },
    areas=AREAS,
    lessons=LESSONS,
    sort_sets=SORT_SETS,
)
