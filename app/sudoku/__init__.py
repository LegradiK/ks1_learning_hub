"""Sudoku blueprint — number puzzles sized for KS1 (4x4, 6x6, 9x9)."""

from flask import Blueprint

bp = Blueprint(
    "sudoku", 
    __name__
    )

# imported at the bottom to avoid circular imports (bp must exist first)
from app.sudoku import route  # noqa: E402,F401