from datetime import timedelta
import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv("data.env")


def _database_url(app):
    """DATABASE_URL from the environment (Neon Postgres in production),
    or a local SQLite file when it isn't set, for working offline."""
    url = os.getenv("DATABASE_URL")
    if not url:
        os.makedirs(app.instance_path, exist_ok=True)
        return "sqlite:///" + os.path.join(app.instance_path, "ks1_hub.db")
    # Neon/Render give "postgres://" or "postgresql://"; SQLAlchemy needs the driver named
    for prefix in ("postgres://", "postgresql://"):
        if url.startswith(prefix):
            return "postgresql+psycopg://" + url[len(prefix):]
    return url


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_KEY")

    app.config.update(
        SQLALCHEMY_DATABASE_URI=_database_url(app),
        # Neon closes idle connections; check each one before use instead of erroring
        SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True, "pool_recycle": 280},
        PERMANENT_SESSION_LIFETIME=timedelta(days=30),   # stay logged in for a month
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=bool(os.getenv("RENDER")),  # https-only cookie on Render
    )
    if test_config:
        app.config.update(test_config)

    if not app.secret_key:
        raise RuntimeError("FLASK_KEY is not set — logins need it. Add it to data.env / Render.")

    from app.extensions import db
    db.init_app(app)

    from app.auth import bp as auth_bp
    from app.hub import bp as hub_bp
    from app.letter_quest import bp as letter_quest_bp
    from app.math_drill import bp as math_drill_bp
    from app.word_wizard import bp as word_wizard_bp
    from app.sudoku import bp as sudoku_bp
    from app.money_counter import bp as money_counter_bp
    from app.clock_master import bp as clock_master_bp
    from app.match_pairs import bp as match_pairs_bp
    from app.phonics_fox import bp as phonics_fox_bp
    from app.story_detective import bp as story_detective_bp
    from app.spelling_master import bp as spelling_master_bp
    from app.bookshelf import bp as bookshelf_bp

    app.register_blueprint(auth_bp)                                   # /login, /logout
    app.register_blueprint(hub_bp)                                    # "/"
    app.register_blueprint(letter_quest_bp, url_prefix="/letter-quest")
    app.register_blueprint(math_drill_bp,   url_prefix="/math-drill")
    app.register_blueprint(word_wizard_bp,  url_prefix="/word-wizard")
    app.register_blueprint(sudoku_bp, url_prefix="/sudoku")
    app.register_blueprint(money_counter_bp, url_prefix="/money-counter")
    app.register_blueprint(clock_master_bp, url_prefix="/clock-master")
    app.register_blueprint(match_pairs_bp, url_prefix="/match-pairs")
    app.register_blueprint(phonics_fox_bp, url_prefix="/phonics-fox")
    app.register_blueprint(story_detective_bp, url_prefix="/story-detective")
    app.register_blueprint(spelling_master_bp, url_prefix="/spelling-master")
    app.register_blueprint(bookshelf_bp, url_prefix="/bookshelf")

    with app.app_context():
        from app import models  # noqa: F401  (so create_all knows the tables)
        db.create_all()         # creates missing tables; never deletes data

    return app
