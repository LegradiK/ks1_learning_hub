"""Spelling Master game logic — no Flask in here, so it's easy to test.

Progress ("history") is saved per child in the database (see route.py and
app/progress.py); the functions here just take it in and hand it back.

History shape (one entry per word the child has tried):

    {
        "because": {"right": 2, "wrong": 3, "last": "wrong",
                    "misspellings": ["becos", "becuase"]},
        ...
    }
"""

import json
import random
import re
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "words.json"

ROUND_SIZE = 10
MAX_MISSPELLINGS = 3     # remember the last few wrong attempts per word
MAX_HISTORY_WORDS = 500  # guard against oversized / tampered client data


# ── Word lists ────────────────────────────────────────────────────────────────
#
# words.json:
#     {"weeks": [
#         {"week": 1, "words": [{"word": "bright", "sentence": "The sun is bright."}, ...]},
#         ...
#     ]}
# A word can also be a plain string ("bright") if you don't want a sentence.

@lru_cache(maxsize=1)
def load_weeks():
    """{week number: [{"word", "sentence"}, ...]} from words.json, tidied up.

    Blank words and stray spaces are ignored, and weeks with no words are
    skipped. Two weeks with the same number is almost always a copy-paste
    slip, so that stops with a clear error instead of silently merging.
    """
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)
    weeks = {}
    for block in data.get("weeks", []):
        number = int(block["week"])
        if number in weeks:
            raise ValueError(
                f"words.json: week {number} appears more than once — "
                "give each week its own number."
            )
        words = [_clean_entry(e) for e in block.get("words", [])]
        words = [w for w in words if w["word"]]
        if words:
            weeks[number] = words
    return dict(sorted(weeks.items()))


def _clean_entry(entry):
    if isinstance(entry, str):
        return {"word": entry.strip(), "sentence": ""}
    return {"word": str(entry.get("word", "")).strip(),
            "sentence": str(entry.get("sentence", "")).strip()}


def list_weeks():
    """[{"week": 1, "count": 10}, ...] for the week buttons."""
    return [{"week": n, "count": len(words)} for n, words in load_weeks().items()]


def all_words():
    """Every word across all weeks as {"word", "sentence", "week"}.

    If the school repeats a word in a later week, it only appears once
    here (under its first week), so a random round never asks it twice.
    """
    seen = set()
    result = []
    for week, words in load_weeks().items():
        for entry in words:
            if entry["word"].lower() not in seen:
                seen.add(entry["word"].lower())
                result.append(dict(entry, week=week))
    return result


# ── History (progress) ────────────────────────────────────────────────────────

def clean_history(raw):
    """Keep only well-formed entries for words we actually have.

    The history comes from the browser, so never trust its shape.
    """
    if not isinstance(raw, dict):
        return {}
    known = {w["word"] for w in all_words()}
    clean = {}
    for word, stats in list(raw.items())[:MAX_HISTORY_WORDS]:
        if word not in known or not isinstance(stats, dict):
            continue
        misspellings = stats.get("misspellings", [])
        clean[word] = {
            "right": _non_negative_int(stats.get("right")),
            "wrong": _non_negative_int(stats.get("wrong")),
            "last": stats.get("last") if stats.get("last") in ("right", "wrong") else None,
            "misspellings": [str(m)[:30] for m in misspellings][-MAX_MISSPELLINGS:]
            if isinstance(misspellings, list) else [],
        }
    return clean


def _non_negative_int(value):
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def record_result(history, word, attempt, correct):
    """Return a NEW history with this attempt added."""
    history = {k: dict(v) for k, v in history.items()}
    stats = history.get(word, {"right": 0, "wrong": 0, "last": None, "misspellings": []})
    stats["misspellings"] = list(stats.get("misspellings", []))
    if correct:
        stats["right"] += 1
        stats["last"] = "right"
    else:
        stats["wrong"] += 1
        stats["last"] = "wrong"
        attempt = attempt.strip()
        if attempt:
            stats["misspellings"] = (stats["misspellings"] + [attempt])[-MAX_MISSPELLINGS:]
    history[word] = stats
    return history


def mistake_score(stats):
    """How much a word needs practice: higher = more trouble.

    Mostly the share of attempts that were wrong, with a bump if the most
    recent attempt was wrong (a fresh mistake matters more than an old one).
    Getting it right a few times in a row brings the score back down.
    """
    if not stats:
        return 0.0
    attempts = stats["right"] + stats["wrong"]
    if stats["wrong"] == 0 or attempts == 0:
        return 0.0
    score = stats["wrong"] / attempts
    if stats.get("last") == "wrong":
        score += 0.5
    return round(score, 3)


def tricky_words(history, limit=10):
    """Words the child gets wrong most, worst first."""
    lookup = {w["word"]: w for w in all_words()}
    scored = [
        {"word": word, "week": lookup[word]["week"], "score": mistake_score(stats),
         "right": stats["right"], "wrong": stats["wrong"],
         "misspellings": stats["misspellings"]}
        for word, stats in history.items()
        if word in lookup and mistake_score(stats) > 0
    ]
    scored.sort(key=lambda w: (-w["score"], -w["wrong"], w["word"]))
    return scored[:limit]


# ── Building a round ──────────────────────────────────────────────────────────

def build_round(mode, week=None, history=None, size=ROUND_SIZE, rng=random):
    """Pick the words for one round.

    mode="week":   all words from one week, shuffled
    mode="random": words from every week; ones the child struggles with,
                   and ones never tried, come up more often
    mode="tricky": the words the child gets wrong most, shuffled

    Returns (title, words). Raises ValueError for a bad mode/week.
    """
    history = history or {}

    if mode == "week":
        weeks = load_weeks()
        if week not in weeks:
            raise ValueError(f"No such week: {week}")
        words = [dict(w, week=week) for w in weeks[week]]
        rng.shuffle(words)
        return f"Week {week}", words

    if mode == "random":
        pool = all_words()
        weights = [_random_weight(history.get(w["word"])) for w in pool]
        return "Random mix", _weighted_sample(pool, weights, min(size, len(pool)), rng)

    if mode == "tricky":
        lookup = {w["word"]: w for w in all_words()}
        # take the words he struggles with most, then ask them in a random order
        words = [dict(lookup[t["word"]]) for t in tricky_words(history, limit=size)]
        rng.shuffle(words)
        return "Tricky words", words

    raise ValueError(f"Unknown mode: {mode}")


def _random_weight(stats):
    """Chance of a word appearing in a random round."""
    if not stats:
        return 2.0                       # never tried: worth a look
    return 1.0 + 4.0 * mistake_score(stats)   # 1.0 (always right) .. 7.0 (keeps slipping)


def _weighted_sample(items, weights, k, rng):
    """Pick k different items, favouring higher weights."""
    items, weights = list(items), list(weights)
    chosen = []
    for _ in range(k):
        pick = rng.choices(range(len(items)), weights=weights)[0]
        chosen.append(items.pop(pick))
        weights.pop(pick)
    return chosen


# ── Checking an answer ────────────────────────────────────────────────────────

def check_spelling(target, attempt):
    """Compare the child's attempt with the right spelling.

    Capital letters don't count against the child. Returns:
        correct  – True / False
        letters  – the RIGHT spelling, letter by letter, each marked
                   "ok" (they got it) or "fix" (missed or wrong), so the
                   page can show exactly which bit to practise
    """
    target_clean = target.strip()
    attempt_clean = " ".join(attempt.strip().split())
    correct = attempt_clean.lower() == target_clean.lower()

    status = ["fix"] * len(target_clean)
    matcher = SequenceMatcher(None, target_clean.lower(), attempt_clean.lower())
    for block in matcher.get_matching_blocks():
        for i in range(block.a, block.a + block.size):
            status[i] = "ok"

    letters = [{"letter": ch, "status": st} for ch, st in zip(target_clean, status)]
    return {"correct": correct, "letters": letters}


# ── Sentence mode ─────────────────────────────────────────────────────────────

def split_sentence(sentence, word):
    """Cut the spelling word out of its sentence, for the fill-the-gap test.

    "The sun is very bright today." + "bright"
        → {"before": "The sun is very ", "after": " today."}

    Matches whole words only and ignores capitals ("The" counts for "the"),
    so "are" is never found inside "share". Returns None when the sentence
    doesn't contain the word — that word is then tested on its own.
    """
    if not sentence:
        return None
    match = re.search(rf"(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])", sentence, re.IGNORECASE)
    if not match:
        return None
    return {"before": sentence[:match.start()], "after": sentence[match.end():]}


def add_gaps(words):
    """Attach the gapped sentence (or None) to each word in a round."""
    return [dict(w, gap=split_sentence(w.get("sentence", ""), w["word"])) for w in words]