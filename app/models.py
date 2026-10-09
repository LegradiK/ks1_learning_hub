"""Database tables: the children who can log in, and their saved progress."""

from datetime import datetime, timedelta, timezone

from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db

MAX_PIN_ATTEMPTS = 5            # wrong PINs in a row before a short lock
LOCK_MINUTES = 5


def _now():
    return datetime.now(timezone.utc).replace(tzinfo=None)   # stored as naive UTC


class Child(db.Model):
    __tablename__ = "children"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)               # as shown: "Leo"
    name_key = db.Column(db.String(40), unique=True, nullable=False)  # for lookup: "leo"
    pin_hash = db.Column(db.String(255), nullable=False)
    failed_attempts = db.Column(db.Integer, default=0, nullable=False)
    locked_until = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=_now, nullable=False)

    progress = db.relationship("GameProgress", backref="child",
                               cascade="all, delete-orphan", lazy=True)

    @staticmethod
    def key_for(name):
        return " ".join(name.split()).lower()

    @classmethod
    def find(cls, name):
        return cls.query.filter_by(name_key=cls.key_for(name)).first()

    def set_pin(self, pin):
        self.pin_hash = generate_password_hash(pin)

    # ── PIN checking with a short lock after too many wrong tries ──
    def is_locked(self):
        return self.locked_until is not None and self.locked_until > _now()

    def minutes_locked(self):
        if not self.is_locked():
            return 0
        return max(1, round((self.locked_until - _now()).total_seconds() / 60))

    def try_pin(self, pin):
        """True if the PIN is right. Wrong tries count towards a lock."""
        if self.is_locked():
            return False
        if check_password_hash(self.pin_hash, pin):
            self.failed_attempts = 0
            self.locked_until = None
            return True
        self.failed_attempts += 1
        if self.failed_attempts >= MAX_PIN_ATTEMPTS:
            self.failed_attempts = 0
            self.locked_until = _now() + timedelta(minutes=LOCK_MINUTES)
        return False


class GameProgress(db.Model):
    """One row per child per game; `data` is whatever that game wants to keep."""
    __tablename__ = "game_progress"
    __table_args__ = (db.UniqueConstraint("child_id", "game"),)

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("children.id"), nullable=False)
    game = db.Column(db.String(40), nullable=False)
    data = db.Column(db.JSON, nullable=False, default=dict)
    updated_at = db.Column(db.DateTime, default=_now, onupdate=_now, nullable=False)


class StudyLog(db.Model):
    """How much a child played each game on each day (UK date).

    One row per child, per game, per day. `seconds` is active time on the
    game page (tab visible and touched in the last 90s); right/wrong count
    answered questions; wins counts finished puzzles (crossword, sudoku...).
    """
    __tablename__ = "study_log"
    __table_args__ = (db.UniqueConstraint("child_id", "game", "day"),)

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("children.id"), nullable=False, index=True)
    game = db.Column(db.String(40), nullable=False)       # blueprint name, e.g. "math_drill"
    day = db.Column(db.Date, nullable=False)
    seconds = db.Column(db.Integer, default=0, nullable=False)
    right = db.Column(db.Integer, default=0, nullable=False)
    wrong = db.Column(db.Integer, default=0, nullable=False)
    wins = db.Column(db.Integer, default=0, nullable=False)

    child = db.relationship("Child", backref=db.backref(
        "study_logs", cascade="all, delete-orphan", lazy=True))
