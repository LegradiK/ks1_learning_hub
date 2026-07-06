"""Word Wizard word selection — pure logic, no Flask.

Session storage happens in routes.py; this module just picks a word
that hasn't been used yet, resetting the pool once everything's seen.
"""

import random


def pick_word(all_words, used):
    """Choose an unused word from all_words.

    Returns (chosen_word, updated_used_list). When every word has been
    used, the used list resets so the pool starts over.
    """
    remaining = [w for w in all_words if w not in used]

    if not remaining:
        used = []
        remaining = list(all_words)

    chosen = random.choice(remaining)
    used = used + [chosen]
    return chosen, used