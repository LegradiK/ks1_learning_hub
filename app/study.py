"""Study tracking: time spent and answers given in each game, per day.

The browser sends a small update every 30 seconds while a game page is in
use (static/track.js), and each game calls hubTrack.answer(correct) or
hubTrack.win() when the child answers or finishes a puzzle. Math Drill
checks answers on the server, so it calls record() directly.

    from app.study import record
    record("math_drill", result="right")
"""

from datetime import date, datetime, timedelta

from flask import g
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.hub.activities import ACTIVITIES, GROUPS
from app.models import StudyLog

try:
    from zoneinfo import ZoneInfo
    UK = ZoneInfo("Europe/London")
except Exception:          # no tz database on the server: fall back to UTC
    UK = None

# "math_drill.index" -> "math_drill": the blueprint name is the game key
GAME_KEYS = {a["endpoint"].split(".")[0] for a in ACTIVITIES}

MAX_SECONDS_PER_UPDATE = 60   # the browser sends every 30s; anything bigger is ignored
RESULTS = {"right", "wrong", "win"}


def today_uk():
    return datetime.now(UK).date() if UK else date.today()


def _row(game, day):
    row = StudyLog.query.filter_by(child_id=g.child.id, game=game, day=day).first()
    if row is None:
        row = StudyLog(child_id=g.child.id, game=game, day=day,
                       seconds=0, right=0, wrong=0, wins=0)
        db.session.add(row)
        try:
            db.session.flush()
        except IntegrityError:          # two tabs created today's row at once
            db.session.rollback()
            row = StudyLog.query.filter_by(child_id=g.child.id, game=game, day=day).first()
    return row


def record(game, seconds=0, result=None):
    """Add time and/or one answer to today's row. Returns False if ignored."""
    if g.get("child") is None or game not in GAME_KEYS:
        return False
    seconds = max(0, min(int(seconds or 0), MAX_SECONDS_PER_UPDATE))
    if result not in RESULTS:
        result = None
    if not seconds and not result:
        return False

    row = _row(game, today_uk())
    row.seconds += seconds
    if result:
        column = "wins" if result == "win" else result     # right / wrong / wins
        setattr(row, column, getattr(row, column) + 1)
    db.session.commit()
    return True


# ── The report ────────────────────────────────────────────────────────────────
RANGES = {
    "week": ("Last 7 days", 7),
    "month": ("Last 30 days", 30),
    "all": ("All time", None),
}


def report(child, range_key="week"):
    """Everything the progress page shows, for one child."""
    label, days = RANGES.get(range_key, RANGES["week"])
    today = today_uk()

    q = StudyLog.query.filter_by(child_id=child.id)
    if days:
        q = q.filter(StudyLog.day > today - timedelta(days=days))
    rows = q.all()

    per_game = {}
    for r in rows:
        t = per_game.setdefault(r.game, {"seconds": 0, "right": 0, "wrong": 0,
                                         "wins": 0, "days": set(), "last": None})
        t["seconds"] += r.seconds
        t["right"] += r.right
        t["wrong"] += r.wrong
        t["wins"] += r.wins
        if r.seconds or r.right or r.wrong or r.wins:
            t["days"].add(r.day)
            t["last"] = max(t["last"], r.day) if t["last"] else r.day

    games = []
    for a in ACTIVITIES:
        key = a["endpoint"].split(".")[0]
        t = per_game.get(key, {"seconds": 0, "right": 0, "wrong": 0,
                               "wins": 0, "days": set(), "last": None})
        answered = t["right"] + t["wrong"]
        games.append(dict(
            activity=a, key=key,
            seconds=t["seconds"], right=t["right"], answered=answered,
            accuracy=round(100 * t["right"] / answered) if answered else None,
            wins=t["wins"], days=len(t["days"]), last=t["last"],
        ))
    top = max((gm["seconds"] for gm in games), default=0)
    for gm in games:
        gm["bar"] = round(100 * gm["seconds"] / top) if top else 0
        gm["last_label"] = _day_label(gm["last"], today)

    # Games grouped the same way as the menus (English, Maths, Brain Games...)
    groups = []
    for slug, grp in GROUPS.items():
        in_group = [gm for gm in games if gm["activity"]["group"] == slug]
        if in_group:
            groups.append(dict(grp, slug=slug, games=in_group,
                               seconds=sum(gm["seconds"] for gm in in_group)))

    # Minutes per day for the last 7 days (always, whatever the range)
    week = [today - timedelta(days=i) for i in range(6, -1, -1)]
    week_rows = StudyLog.query.filter(StudyLog.child_id == child.id,
                                      StudyLog.day >= week[0]).all()
    by_day = {d: 0 for d in week}
    for r in week_rows:
        by_day[r.day] = by_day.get(r.day, 0) + r.seconds
    day_top = max(by_day.values(), default=0)
    daily = [dict(day=d, label=d.strftime("%a"), seconds=by_day[d],
                  bar=round(100 * by_day[d] / day_top) if day_top else 0,
                  is_today=(d == today)) for d in week]

    right = sum(gm["right"] for gm in games)
    answered = sum(gm["answered"] for gm in games)
    return dict(
        range_key=range_key if range_key in RANGES else "week",
        range_label=label,
        ranges=RANGES,
        games=games,
        groups=groups,
        daily=daily,
        total_seconds=sum(gm["seconds"] for gm in games),
        total_days=len({d for t in per_game.values() for d in t["days"]}),
        right=right, answered=answered,
        accuracy=round(100 * right / answered) if answered else None,
        wins=sum(gm["wins"] for gm in games),
    )


def _day_label(day, today):
    if day is None:
        return None
    if day == today:
        return "today"
    if day == today - timedelta(days=1):
        return "yesterday"
    if day > today - timedelta(days=7):
        return day.strftime("%A")                       # "Tuesday"
    return f"{day.day} {day.strftime('%b')}"             # "6 Oct"


def nice_time(seconds):
    """95 -> '1 min', 3720 -> '1 hr 2 min', 20 -> 'under a minute'."""
    if not seconds:
        return "—"
    minutes = round(seconds / 60)
    if minutes < 1:
        return "under a minute"
    h, m = divmod(minutes, 60)
    if h and m:
        return f"{h} hr {m} min"
    if h:
        return f"{h} hr"
    return f"{m} min"
