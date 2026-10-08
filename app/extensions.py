"""Shared Flask extensions, created once and attached in create_app()."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
