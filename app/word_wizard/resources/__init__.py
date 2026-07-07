"""Word bank registry for Word Wizard.

Each resource module defines a dict called `quiz`, keyed by difficulty
(reception / year1 / year2 / all). Loaded once at startup via normal
imports and embedded into the page as JSON for the client-side game.
"""

from app.word_wizard.resources.tricky_words import quiz as _tricky_words
from app.word_wizard.resources.vocabulary import quiz as _vocabulary
from app.word_wizard.resources.top_frequent_word_100_200_300 import quiz as _frequent_words
from app.word_wizard.resources.fill_the_sentence import quiz as _fill_the_sentence

QUIZZES = {
    "stage1": _tricky_words,
    "stage2": _vocabulary,
    "stage3": _frequent_words,
    "stage4": _fill_the_sentence,
}