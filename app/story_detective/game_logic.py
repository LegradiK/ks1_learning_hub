"""Story Detective - game logic.

Stories are stored as ordered segments in /resources. A segment is either:
    {"text": "..."}                                      plain story text
    {"gap": {"answer": "...", "options": ["...", ...]}}  a missing word

Distractor rules (per gap):
    - one distractor is the same word class but the wrong meaning
    - one is plausible but contradicted by the story itself

Level differences (both levels play the same fill-then-check flow):
    Year 1 -> the word bank contains ONLY the correct answers, shuffled.
              Every word belongs somewhere; the child just matches them.
    Year 2 -> the bank pools all gap options (answers + distractors),
              de-duplicated and shuffled.

Answers are checked server-side via check_answers(); the payload never
labels which bank words are correct.
"""

import random
from app.story_detective.resources import QUIZZES as STORIES

STARS_BY_ATTEMPT = {1: 3, 2: 2}  # three or more attempts -> 1 star

# ---------------------------------------------------------------- helpers

def _find(story_id):
    """Return the raw story dict, or None."""
    return next((s for s in STORIES if s["id"] == story_id), None)


def _gap_answers(story):
    """Ordered list of correct answers for a story."""
    return [seg["gap"]["answer"] for seg in story["segments"] if "gap" in seg]


def _full_text(story):
    """The complete story with all answers filled in."""
    return "".join(
        seg["text"] if "text" in seg else seg["gap"]["answer"]
        for seg in story["segments"]
    )


def _build_bank(story):
    """The word bank for the client, depending on the story's level.

    Year 1: the answers only — no distractors, nothing confusing.
    Year 2: every gap's options, de-duplicated (case-insensitive).
    """
    if story["level"] == 1:
        bank = _gap_answers(story)[:]
    else:
        bank, seen = [], set()
        for seg in story["segments"]:
            if "gap" not in seg:
                continue
            for word in seg["gap"]["options"]:
                key = word.lower()
                if key not in seen:
                    seen.add(key)
                    bank.append(word)
    random.shuffle(bank)
    return bank


# ------------------------------------------------------------- public API

def list_stories():
    """Metadata for the menu screen (no answers, no segments)."""
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "emoji": s["emoji"],
            "level": s["level"],
            "gap_count": len(_gap_answers(s)),
        }
        for s in STORIES
    ]


def get_story_payload(story_id):
    """Story for the client: answers stripped from segments, bank built
    per level (see _build_bank)."""
    story = _find(story_id)
    if story is None:
        return None

    segments = [
        {"text": seg["text"]} if "text" in seg else {"gap": {}}
        for seg in story["segments"]
    ]

    return {
        "id": story["id"],
        "title": story["title"],
        "emoji": story["emoji"],
        "level": story["level"],
        "segments": segments,
        "bank": _build_bank(story),
    }


def check_answers(story_id, answers):
    """Check a (possibly partial) answer sheet.

    ``answers`` must be a list the same length as the story's gap count.
    Entries may be None for gaps not yet attempted. Returns None for a
    malformed request, otherwise:

        {
          "results": [True | False | None, ...],   one per gap
          "solved":  bool,                          every gap correct
          "full_text": "..."                        only when solved
        }
    """
    story = _find(story_id)
    if story is None:
        return None

    correct = _gap_answers(story)
    if not isinstance(answers, list) or len(answers) != len(correct):
        return None

    results = [
        None if given is None
        else str(given).strip().lower() == answer.lower()
        for given, answer in zip(answers, correct)
    ]
    solved = all(r is True for r in results)

    payload = {"results": results, "solved": solved}
    if solved:
        payload["full_text"] = _full_text(story)
    return payload


def stars_for(attempts):
    """Stars earned: solved on attempt 1 -> 3, attempt 2 -> 2, else 1."""
    try:
        attempts = max(1, int(attempts))
    except (TypeError, ValueError):
        attempts = 1
    return STARS_BY_ATTEMPT.get(attempts, 1)