"""Shared lesson engine for the School Subjects (History, Science, Online Safety).

Each subject is a blueprint with its own data module:

    AREAS      — {slug: {"name", "emoji", "blurb", "curriculum"}}   menu sections
    LESSONS    — list of lesson dicts (see below)
    SORT_SETS  — optional sorting games (see below)

and calls add_lesson_routes() to get these pages:

    /                     the subject menu: practice games + lessons by area
    /lesson/<lesson_id>   one lesson: story pages, key words, talk time, quiz
    /sort/<set_id>        a sorting game ("Is it a mammal or a bird?")

A lesson:
    id, area, emoji, title, tag (short label, e.g. "1666" or "Year 1"), blurb
    pages  — [{"emoji", "heading", "text", "fact" (optional)}]
    words  — [(word, meaning)]
    talk   — a question to talk about with a grown-up
    quiz   — [{"q", "options", "answer" (index), "why"}]

A sort set:
    {"id", "title", "emoji", "blurb", "question",
     "categories": [{"key", "emoji", "label", "says"}],   # says: "from long ago"
     "items": [{"emoji", "text", "category", "why" (optional)}],
     "round": 8}                                          # cards per round

Templates live in app/templates/lessons/ and are shared by every subject.
"""

from flask import abort, render_template


def lessons_by_area(areas, lessons):
    """[(area_slug, area, [lessons...]), ...] in AREAS order, skipping empty areas."""
    out = []
    for slug, area in areas.items():
        in_area = [l for l in lessons if l["area"] == slug]
        if in_area:
            out.append((slug, area, in_area))
    return out


def lesson_payload(areas, lessons, lesson_id):
    """One lesson ready for the page, with the next lesson to link to."""
    by_id = {l["id"]: l for l in lessons}
    lesson = by_id.get(lesson_id)
    if lesson is None:
        return None
    i = lessons.index(lesson)
    nxt = lessons[i + 1] if i + 1 < len(lessons) else None
    return dict(
        lesson,
        words=[{"word": w, "meaning": m} for w, m in lesson["words"]],
        area_name=areas[lesson["area"]]["name"],
        next_id=nxt["id"] if nxt else None,
        next_title=nxt["title"] if nxt else None,
    )


def add_lesson_routes(bp, *, subject, areas, lessons, sort_sets=(), extra_games=()):
    """Register the shared lesson pages on a subject blueprint.

    subject:      {"name", "badge", "theme", "tagline", "group"}
                  group = the hub group slug the Back button returns to
    extra_games:  subject-only games for the Practice Games row:
                  [{"endpoint", "emoji", "title", "blurb"}]
    """
    sets_by_id = {s["id"]: s for s in sort_sets}
    games = [
        {"endpoint": f"{bp.name}.sort", "args": {"set_id": s["id"]},
         "emoji": s["emoji"], "title": s["title"], "blurb": s["blurb"]}
        for s in sort_sets
    ] + [dict(g, args={}) for g in extra_games]

    def context(**kw):
        return dict(subject=subject, bp=bp.name, **kw)

    @bp.route("/")
    def index():
        return render_template(
            "lessons/index.html",
            **context(areas=lessons_by_area(areas, lessons),
                      total=len(lessons), games=games),
        )

    @bp.route("/lesson/<lesson_id>")
    def lesson(lesson_id):
        data = lesson_payload(areas, lessons, lesson_id)
        if data is None:
            abort(404)
        return render_template("lessons/lesson.html", **context(lesson=data))

    @bp.route("/sort/<set_id>")
    def sort(set_id):
        sort_set = sets_by_id.get(set_id)
        if sort_set is None:
            abort(404)
        return render_template("lessons/sort.html", **context(sort_set=sort_set))
