"""Clock Master game logic — pure Python, no Flask imports.

Two modes:
  read -> the clock shows a time, the child picks the right phrase
          from multiple-choice options
  set  -> the child is given a phrase ("half past 3") and drags the
          clock hands to match (validation is client-side: compare
          the set hands against hour/minute)

Difficulties follow the KS1 progression:
  oclock  -> o'clock only                       (Year 1, first steps)
  half    -> o'clock and half past              (Year 1)
  quarter -> + quarter past and quarter to      (Year 2)
  five    -> any five-minute time               (Year 2, confident)
"""

import random

DIFFICULTY = {
    "oclock":  [0],
    "half":    [0, 30],
    "quarter": [0, 15, 30, 45],
    "five":    list(range(0, 60, 5)),
}
MODES = ("read", "set")
DEFAULT_MODE = "read"
DEFAULT_DIFFICULTY = "oclock"

NUM_WORDS = {5: "five", 10: "ten", 20: "twenty", 25: "twenty-five"}


def time_phrase(hour, minute):
    """Child-friendly phrase: '3 o'clock', 'half past 3', 'quarter to 4'."""
    next_hour = hour % 12 + 1
    if minute == 0:
        return f"{hour} o'clock"
    if minute == 30:
        return f"half past {hour}"
    if minute == 15:
        return f"quarter past {hour}"
    if minute == 45:
        return f"quarter to {next_hour}"
    if minute < 30:
        return f"{NUM_WORDS[minute]} past {hour}"
    return f"{NUM_WORDS[60 - minute]} to {next_hour}"


def digital_label(hour, minute):
    """'3:05' — shown alongside the phrase at higher difficulties."""
    return f"{hour}:{minute:02d}"


def _random_time(minutes_pool):
    return random.randint(1, 12), random.choice(minutes_pool)


def _distractors(hour, minute, minutes_pool, count=3):
    """Plausible wrong answers: same difficulty pool, near-miss biased.

    Mixes two classic confusions: same hands different hour, and the
    hour/minute swap ('quarter past 3' vs 'quarter to 3' vs '3 o'clock').
    """
    correct = time_phrase(hour, minute)
    options = set()
    attempts = 0
    while len(options) < count and attempts < 100:
        attempts += 1
        if random.random() < 0.5:
            # nudge the hour, keep the minute — classic near-miss
            h = (hour - 1 + random.choice([1, 2, 11])) % 12 + 1
            m = minute
        else:
            h, m = _random_time(minutes_pool)
        phrase = time_phrase(h, m)
        if phrase != correct:
            options.add(phrase)
    return list(options)


def generate_question(mode=DEFAULT_MODE, difficulty=DEFAULT_DIFFICULTY):
    """Return a dict ready for jsonify.

    read -> {mode, difficulty, hour, minute, phrase, digital,
             options: [4 shuffled phrases including the answer]}
    set  -> {mode, difficulty, hour, minute, phrase, digital}
    """
    if mode not in MODES:
        mode = DEFAULT_MODE
    if difficulty not in DIFFICULTY:
        difficulty = DEFAULT_DIFFICULTY

    pool = DIFFICULTY[difficulty]
    hour, minute = _random_time(pool)
    phrase = time_phrase(hour, minute)

    question = {
        "mode": mode,
        "difficulty": difficulty,
        "hour": hour,
        "minute": minute,
        "phrase": phrase,
        "digital": digital_label(hour, minute),
    }

    if mode == "read":
        options = _distractors(hour, minute, pool) + [phrase]
        random.shuffle(options)
        question["options"] = options

    return question