"""Story Detective - game logic.

Stories are stored as ordered segments in /resources. A segment is either:
    {"text": "..."}                                      plain story text
    {"gap": {"answer": "...", "options": ["...", ...]}}  a missing word

Distractor rules (per gap):
    - one distractor is the same word class but the wrong meaning
    - one is plausible but contradicted by the story itself

Level differences:
    Year 1 -> 3 options per gap, played one gap at a time (client uses
              each gap's own "options" list, instant feedback per gap)
    Year 2 -> pooled clue bank across all gaps (client uses "bank")

Answers never leave the server until a story is solved: the client
payload strips them out, and checking happens via check_answers().
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
    """Story for the client: answers stripped, options shuffled.

    Includes both per-gap options (used by Year 1's one-gap-at-a-time
    mode) and a pooled, de-duplicated clue bank (used by Year 2).
    """
    story = _find(story_id)
    if story is None:
        return None

    segments = []
    bank, seen = [], set()
    for seg in story["segments"]:
        if "text" in seg:
            segments.append({"text": seg["text"]})
            continue
        options = seg["gap"]["options"][:]
        random.shuffle(options)
        segments.append({"gap": {"options": options}})
        for word in options:
            key = word.lower()
            if key not in seen:
                seen.add(key)
                bank.append(word)
    random.shuffle(bank)

    return {
        "id": story["id"],
        "title": story["title"],
        "emoji": story["emoji"],
        "level": story["level"],
        "segments": segments,
        "bank": bank,
    }


def check_answers(story_id, answers):
    """Check a (possibly partial) answer sheet.

    ``answers`` must be a list the same length as the story's gap count.
    Entries may be None for gaps not yet attempted (Year 1 checks one
    gap at a time). Returns None for a malformed request, otherwise:

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