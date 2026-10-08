"""Load and save a game's progress for whoever is logged in.

    from app.progress import load_progress, save_progress

    history = load_progress("spelling_master")      # {} the first time
    save_progress("spelling_master", history)
"""

from flask import g

from app.extensions import db
from app.models import GameProgress


def _row(game):
    return GameProgress.query.filter_by(child_id=g.child.id, game=game).first()


def load_progress(game):
    row = _row(game)
    return dict(row.data) if row else {}


def save_progress(game, data):
    row = _row(game)
    if row is None:
        row = GameProgress(child_id=g.child.id, game=game, data=data)
        db.session.add(row)
    else:
        row.data = data          # assign a new dict so the JSON change is saved
    db.session.commit()
