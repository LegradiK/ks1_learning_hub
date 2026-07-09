"""Sudoku game logic — pure Python, no Flask imports, no data files.

Generates 4x4, 6x6 and 9x9 puzzles on demand:
  1. build a full valid solution with randomised backtracking
  2. remove clues one by one, keeping only removals that leave the
     puzzle with exactly ONE solution (so every puzzle is fair)
  3. stop when the difficulty's clue target is reached

Box shapes: 4x4 -> 2x2 boxes, 6x6 -> 2 rows x 3 cols, 9x9 -> 3x3.
"""

import random

# size -> (box_rows, box_cols)
BOX_DIMS = {4: (2, 2), 6: (2, 3), 9: (3, 3)}
SIZES = sorted(BOX_DIMS)
DEFAULT_SIZE = 4

# how many givens to leave on the board, per size and difficulty
CLUE_TARGETS = {
    4: {"easy": 8,  "medium": 7,  "hard": 6},
    6: {"easy": 20, "medium": 17, "hard": 14},
    9: {"easy": 40, "medium": 34, "hard": 28},
}
DEFAULT_DIFFICULTY = "easy"


def _candidates(grid, size, box_rows, box_cols, r, c):
    """Values that can legally go in (r, c) right now."""
    used = set(grid[r])                                   # row
    used.update(grid[i][c] for i in range(size))          # column
    br, bc = (r // box_rows) * box_rows, (c // box_cols) * box_cols
    for i in range(br, br + box_rows):                    # box
        for j in range(bc, bc + box_cols):
            used.add(grid[i][j])
    return [v for v in range(1, size + 1) if v not in used]


def _find_best_empty(grid, size, box_rows, box_cols):
    """Most-constrained empty cell (fewest candidates) — keeps 9x9 fast."""
    best = None
    best_cands = None
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 0:
                cands = _candidates(grid, size, box_rows, box_cols, r, c)
                if best is None or len(cands) < len(best_cands):
                    best, best_cands = (r, c), cands
                    if len(cands) <= 1:
                        return best, best_cands
    return best, best_cands


def _fill(grid, size, box_rows, box_cols):
    """Complete the grid in place with a random valid solution."""
    cell, cands = _find_best_empty(grid, size, box_rows, box_cols)
    if cell is None:
        return True
    r, c = cell
    random.shuffle(cands)
    for v in cands:
        grid[r][c] = v
        if _fill(grid, size, box_rows, box_cols):
            return True
    grid[r][c] = 0
    return False


def _count_solutions(grid, size, box_rows, box_cols, limit=2):
    """Count solutions, stopping early once `limit` is reached."""
    cell, cands = _find_best_empty(grid, size, box_rows, box_cols)
    if cell is None:
        return 1
    r, c = cell
    count = 0
    for v in cands:
        grid[r][c] = v
        count += _count_solutions(grid, size, box_rows, box_cols, limit - count)
        grid[r][c] = 0
        if count >= limit:
            break
    return count


def generate_puzzle(size=DEFAULT_SIZE, difficulty=DEFAULT_DIFFICULTY):
    """Return a dict ready for jsonify: puzzle grid + its unique solution."""
    if size not in BOX_DIMS:
        size = DEFAULT_SIZE
    if difficulty not in CLUE_TARGETS[size]:
        difficulty = DEFAULT_DIFFICULTY

    box_rows, box_cols = BOX_DIMS[size]

    # 1. full solution
    solution = [[0] * size for _ in range(size)]
    _fill(solution, size, box_rows, box_cols)

    # 2. dig holes while the puzzle stays uniquely solvable
    puzzle = [row[:] for row in solution]
    target = CLUE_TARGETS[size][difficulty]
    clues = size * size

    cells = [(r, c) for r in range(size) for c in range(size)]
    random.shuffle(cells)
    for r, c in cells:
        if clues <= target:
            break
        backup = puzzle[r][c]
        puzzle[r][c] = 0
        if _count_solutions(puzzle, size, box_rows, box_cols) == 1:
            clues -= 1
        else:
            puzzle[r][c] = backup   # removal broke uniqueness — put it back

    return {
        "size": size,
        "boxRows": box_rows,
        "boxCols": box_cols,
        "difficulty": difficulty,
        "grid": puzzle,        # 0 = empty cell for the child to fill
        "solution": solution,
    }