"""Word bank registry for Word Wizard.

Each resource module defines a dict called `quiz`, keyed by difficulty
(reception / year1 / year2 / all). Loaded once at startup via normal
imports and embedded into the page as JSON for the client-side game.
"""

"""Story registry for Story Detective.

Each resource module defines a list of story dicts (segments format).
To add stories: append to year1_stories.py / year2_stories.py, or add a
new module and include its list in QUIZZES below. Nothing in
game_logic.py or route.py needs to change.
"""

from app.story_detective.resources.year1_stories import YEAR1_STORIES
from app.story_detective.resources.year2_stories import YEAR2_STORIES

# game_logic expects one flat list; each story carries its own "level".
QUIZZES = YEAR1_STORIES + YEAR2_STORIES


def _validate(stories):
    """Catch authoring mistakes at startup instead of mid-game."""
    seen_ids = set()
    for story in stories:
        sid = story.get("id", "<missing id>")
        if sid in seen_ids:
            raise ValueError(f"Duplicate story id: {sid!r}")
        seen_ids.add(sid)

        for key in ("id", "title", "emoji", "level", "segments"):
            if key not in story:
                raise ValueError(f"Story {sid!r} is missing {key!r}")

        gap_count = 0
        for seg in story["segments"]:
            if "text" in seg:
                continue
            gap = seg.get("gap")
            if not gap:
                raise ValueError(f"Story {sid!r} has a segment with neither text nor gap")
            gap_count += 1
            answer, options = gap.get("answer"), gap.get("options", [])
            if answer not in options:
                raise ValueError(
                    f"Story {sid!r}: answer {answer!r} is not in its options {options}"
                )
            if len(options) != len({o.lower() for o in options}):
                raise ValueError(f"Story {sid!r}: duplicate options for answer {answer!r}")
        if gap_count == 0:
            raise ValueError(f"Story {sid!r} has no gaps")


_validate(QUIZZES)