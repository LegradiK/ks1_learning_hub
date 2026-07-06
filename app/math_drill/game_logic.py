"""MathDrill question generation — pure logic, no Flask imports.

Digit ranges come in from app/core/difficulty.py via the routes,
so the shared difficulty picker controls question size.
"""

import random

CALC_TYPES = ("addition", "subtraction", "multiplication", "division")
STYLES = ("inline", "stacked")

ONE_DIGIT = (1, 9)

OP_SYMBOL = {
    "addition":       "+",
    "subtraction":    "−",
    "multiplication": "×",
    "division":       "÷",
}


def new_question(digit_pairs, calc_type="addition"):
    """Build one question dict: {"num1", "op", "num2", "answer"}.

    digit_pairs: list of ((a_min, a_max), (b_min, b_max)) tuples —
    one is chosen at random, so a level can mix sizes.
    """
    a_range, b_range = random.choice(digit_pairs)
    a = random.randint(*a_range)
    b = random.randint(*b_range)

    if calc_type == "subtraction":
        if a < b:
            a, b = b, a          # keep result positive
        op, answer = "−", a - b
    elif calc_type == "multiplication":
        # clamp to keep numbers sane regardless of difficulty ranges
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op, answer = "×", a * b
    elif calc_type == "division":
        b = random.randint(*ONE_DIGIT)
        answer = random.randint(*ONE_DIGIT)
        a = b * answer           # guarantee whole-number result
        op, answer = "÷", answer
    else:
        op, answer = "+", a + b

    return {"num1": a, "op": op, "num2": b, "answer": answer}