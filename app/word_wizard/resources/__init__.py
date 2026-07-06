"""Word bank registry for Word Wizard.

Each resource module defines a dict called `quiz`, keyed by difficulty.
Normal imports replace the old importlib.util file loading: the banks are
loaded ONCE at startup instead of being re-executed on every request,
and paths can't break regardless of where the app is run from.
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