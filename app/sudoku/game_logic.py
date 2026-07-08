"""Sudoku game logic — pure Python, no Flask imports.

Adapted from the standalone Pygame version's csv_reader.py.
Loads the 4x4 unique-solution dataset once at import time, then
serves random (quiz, solution) pairs on demand.

Expected data file (tab-separated, one header line):
    app/sudoku/data/4x4_sudoku_unique_solution.csv
Each line: 16-char board string \t 16-char solution string, 0 = empty.
"""

import csv  # noqa: F401  (kept for parity; parsing is simple splits)
import random
from pathlib import Path

GRID_SIZE = 4

# resolve relative to this file, not the current working directory —
# Flask apps are rarely launched from the blueprint folder
_DATA_FILE = Path(__file__).parent / "data" / "4x4_sudoku_unique_solution.csv"


def _parse_line(line):
    board_str, solution_str = line.strip().split("\t")
    board = [int(char) for char in board_str]
    solution = [int(char) for char in solution_str]
    return board, solution


def _to_grid(lst, size=GRID_SIZE):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def _load_all_puzzles():
    pairs = []
    with open(_DATA_FILE, encoding="utf-8") as sudoku_file:
        next(sudoku_file)  # skip header
        for line in sudoku_file:
            if not line.strip():
                continue
            board, solution = _parse_line(line)
            pairs.append((_to_grid(board), _to_grid(solution)))
    if not pairs:
        raise RuntimeError(f"No puzzles loaded from {_DATA_FILE}")
    return pairs


# loaded once when the blueprint imports this module
_PUZZLES = _load_all_puzzles()


def random_puzzle():
    """Return a dict ready for jsonify: a random quiz + its solution."""
    quiz, solution = random.choice(_PUZZLES)
    return {
        "size": GRID_SIZE,
        "grid": quiz,          # 0 = empty cell for the child to fill
        "solution": solution,  # used by the front-end Check
    }