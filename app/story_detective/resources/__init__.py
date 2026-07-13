"""Word bank registry for Word Wizard.

Each resource module defines a dict called `quiz`, keyed by difficulty
(reception / year1 / year2 / all). Loaded once at startup via normal
imports and embedded into the page as JSON for the client-side game.
"""

from app.story_detective.resources.year1_stories import quiz as __year1_stories
from app.story_detective.resources.year2_stories import quiz as __year2_stories


QUIZZES = {
    "stage1": __year1_stories,
    "stage2": __year2_stories
}