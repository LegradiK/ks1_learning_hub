"""MathDrill question generation — pure logic, no Flask.

Difficulty levels are PER CALC TYPE now:
- addition:       easy / medium / hard / extra_hard / random
- subtraction:    same five levels as addition
- multiplication: easy (1-digit × 1-digit) / hard (1-digit × 2-digit)
- division:       one fixed level (1-digit divisor, whole answers)
"""

import random

CALC_TYPES = ("addition", "subtraction", "multiplication", "division")
STYLES = ("inline", "stacked")

ONE_DIGIT   = (1, 9)
TWO_DIGIT   = (10, 99)
THREE_DIGIT = (100, 999)

# Which levels each calc type offers, in display order.
# A single-entry tuple means the difficulty picker is hidden for that type.
_FIVE_LEVELS = ("easy", "medium", "hard", "extra_hard", "random")

LEVELS_FOR = {
    "addition":       _FIVE_LEVELS,
    "subtraction":    _FIVE_LEVELS,
    "multiplication": ("easy", "hard"),
    "division":       ("standard",),
}

_ADDSUB_CONFIGS = {
    "easy":       [(ONE_DIGIT, ONE_DIGIT)],
    "medium":     [(ONE_DIGIT, TWO_DIGIT), (TWO_DIGIT, ONE_DIGIT)],
    "hard":       [(TWO_DIGIT, TWO_DIGIT)],
    "extra_hard": [(THREE_DIGIT, THREE_DIGIT)],
    "random": [
        (ONE_DIGIT,  ONE_DIGIT),
        (ONE_DIGIT,  TWO_DIGIT),
        (TWO_DIGIT,  ONE_DIGIT),
        (TWO_DIGIT,  TWO_DIGIT),
        (THREE_DIGIT, THREE_DIGIT),
    ],
}

# (calc_type, level) -> list of ((a_min, a_max), (b_min, b_max))
CONFIGS = {
    **{("addition", lv): pairs for lv, pairs in _ADDSUB_CONFIGS.items()},
    **{("subtraction", lv): pairs for lv, pairs in _ADDSUB_CONFIGS.items()},

    ("multiplication", "easy"): [(ONE_DIGIT, ONE_DIGIT)],
    ("multiplication", "hard"): [(ONE_DIGIT, TWO_DIGIT)],
    # division handled specially in new_question (no ranges needed)
}


def levels_for(calc_type):
    """Levels available for a calc type (1 entry = no picker shown)."""
    return LEVELS_FOR[calc_type]


def default_level(calc_type):
    return LEVELS_FOR[calc_type][0]


def new_question(calc_type="addition", difficulty=None):
    """Build one question dict: {"num1", "op", "num2", "answer"}.

    Falls back to the type's default level if difficulty is None or
    not valid for this calc type (e.g. after switching type).
    """
    if difficulty not in LEVELS_FOR[calc_type]:
        difficulty = default_level(calc_type)

    if calc_type == "division":
        b = random.randint(*ONE_DIGIT)
        answer = random.randint(*ONE_DIGIT)
        a = b * answer           # guarantee whole-number result
        return {"num1": a, "op": "÷", "num2": b, "answer": answer}

    a_range, b_range = random.choice(CONFIGS[(calc_type, difficulty)])
    a = random.randint(*a_range)
    b = random.randint(*b_range)

    if calc_type == "subtraction":
        if a < b:
            a, b = b, a          # keep result positive
        return {"num1": a, "op": "−", "num2": b, "answer": a - b}

    if calc_type == "multiplication":
        return {"num1": a, "op": "×", "num2": b, "answer": a * b}

    return {"num1": a, "op": "+", "num2": b, "answer": a + b}