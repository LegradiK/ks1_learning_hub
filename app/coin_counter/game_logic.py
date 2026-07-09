"""Coin Counter game logic — pure Python, no Flask imports.

Two modes:
  count  -> show a handful of coins/notes, the child types the total
  make   -> show a target amount, the child taps money to build it
            (validation is client-side: any combination that sums to
             the target is correct; this module just picks fair targets)

Difficulties gate which money appears and how big totals get:
  easy   -> 1p, 2p, 5p, 10p                  small totals, few coins
  medium -> + 20p, 50p                        totals up to £1
  hard   -> + £1, £2                          totals past £1
  expert -> + £5, £10, £20, £50 notes         big totals, notes + coins

Values are in pence throughout; the front-end maps a value to its
artwork (coin-1 ... coin-200, note-500 ... note-5000).
"""

import random

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
NOTES = [500, 1000, 2000, 5000]
ALL_MONEY = COINS + NOTES

DIFFICULTY = {
    "easy":   {"money": [1, 2, 5, 10],                   "num": (2, 4), "max_total": 30},
    "medium": {"money": [1, 2, 5, 10, 20, 50],           "num": (3, 5), "max_total": 100},
    "hard":   {"money": [1, 2, 5, 10, 20, 50, 100, 200], "num": (4, 6), "max_total": 500},
    "expert": {"money": ALL_MONEY,                       "num": (4, 7), "max_total": 10000},
}
MODES = ("count", "make")
DEFAULT_MODE = "count"
DEFAULT_DIFFICULTY = "easy"


def format_pence(pence):
    """47 -> '47p', 100 -> '£1', 235 -> '£2.35', 5000 -> '£50'."""
    if pence < 100:
        return f"{pence}p"
    pounds, rest = divmod(pence, 100)
    return f"£{pounds}" if rest == 0 else f"£{pounds}.{rest:02d}"


def _pick_money(cfg):
    """Random handful of money within the difficulty's total budget."""
    lo, hi = cfg["num"]
    n = random.randint(lo, hi)
    picked = []
    total = 0
    for _ in range(n):
        affordable = [m for m in cfg["money"] if total + m <= cfg["max_total"]]
        if not affordable:
            break
        m = random.choice(affordable)
        picked.append(m)
        total += m
    picked.sort(reverse=True)   # notes first, then big coins: reads naturally
    return picked, total


def generate_question(mode=DEFAULT_MODE, difficulty=DEFAULT_DIFFICULTY):
    """Return a dict ready for jsonify.

    count -> {mode, difficulty, coins: [1000, 50, 2], total: 1052,
              total_label: '£10.52'}
    make  -> {mode, difficulty, target: 1052, target_label: '£10.52',
              coins: [...values available in the tray...]}
    """
    if mode not in MODES:
        mode = DEFAULT_MODE
    if difficulty not in DIFFICULTY:
        difficulty = DEFAULT_DIFFICULTY
    cfg = DIFFICULTY[difficulty]

    if mode == "count":
        money, total = _pick_money(cfg)
        return {
            "mode": mode,
            "difficulty": difficulty,
            "coins": money,
            "total": total,
            "total_label": format_pence(total),
        }

    # make mode: target is built from real money, so always achievable
    _, target = _pick_money(cfg)
    return {
        "mode": mode,
        "difficulty": difficulty,
        "target": target,
        "target_label": format_pence(target),
        "coins": cfg["money"],    # the tray the child can tap from
    }