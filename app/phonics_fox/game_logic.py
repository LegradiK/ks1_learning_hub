"""Phonics Fox game logic — pure Python, no Flask imports.

Phonics practice mapped to the UK Letters and Sounds progression:
  reception -> Phases 2-4 graphemes (sh, ch, ai, ee, igh, oa ...)
  year1     -> Phase 5 alternative spellings (ay, ea, ou, split digraphs ...)
  year2     -> trickier spellings (kn, wr, dge, tion ...)

Three modes:
  insert -> the word is shown with its sound gapped (r__n); the child
            picks the right grapheme from 4 options
  choose -> the child hears the word and picks the real spelling from
            4 options (the rest are pseudo-words made by swapping in
            confusable graphemes: rain / rayn / rane / rein)
  spell  -> the child hears the word and types the whole spelling

Split digraphs are written 'a-e', 'i-e', etc. (cake, kite).
"""

import random

# grapheme -> example words, per year group
SOUNDS = {
    "reception": {
        "ai":  ["rain", "tail", "snail", "paint", "train", "chain"],
        "ee":  ["feet", "seen", "tree", "green", "sleep", "sheep"],
        "igh": ["high", "light", "night", "right", "bright"],
        "oa":  ["boat", "coat", "road", "goat", "soap", "toast"],
        "oo":  ["moon", "food", "boot", "spoon", "roof"],
        "ow":  ["cow", "down", "town", "owl", "brown", "crown"],
        "oi":  ["coin", "soil", "boil", "point", "spoil"],
        "ar":  ["card", "park", "shark", "farm", "start"],
        "sh":  ["ship", "shop", "shell", "brush", "splash"],
        "ch":  ["chip", "chat", "lunch", "bench", "church"],
    },
    "year1": {
        "ay":  ["day", "play", "stay", "spray", "crayon"],
        "ea":  ["eat", "sea", "read", "beach", "dream"],
        "ou":  ["out", "cloud", "found", "shout", "proud"],
        "oy":  ["boy", "toy", "enjoy", "royal"],
        "ir":  ["girl", "bird", "shirt", "first", "third"],
        "aw":  ["saw", "paw", "draw", "yawn", "crawl"],
        "ew":  ["new", "flew", "grew", "chew", "threw"],
        "a-e": ["cake", "make", "snake", "gate", "plate"],
        "i-e": ["kite", "bike", "time", "smile", "slide"],
        "o-e": ["bone", "home", "note", "stone", "smoke"],
    },
    "year2": {
        "kn":   ["knee", "knock", "knife", "knot", "know"],
        "wr":   ["wrap", "wrist", "wrong", "wriggle"],
        "dge":  ["badge", "bridge", "hedge", "fridge", "edge"],
        "tion": ["station", "fiction", "motion", "action"],
        "ey":   ["key", "monkey", "donkey", "money", "valley"],
        "or":   ["fork", "storm", "sport", "corner", "morning"],
        "ur":   ["turn", "burn", "hurt", "nurse", "turnip"],
        "wh":   ["when", "which", "whisk", "whisper", "wheel"],
    },
}

# graphemes that make (roughly) the same sound — used to build wrong
# answers in insert mode and pseudo-words in choose mode
CONFUSABLE = {
    "ai":  ["ay", "a-e", "ei"],
    "ay":  ["ai", "a-e", "ei"],
    "a-e": ["ai", "ay", "ei"],
    "ee":  ["ea", "e-e", "ey"],
    "ea":  ["ee", "e-e", "ey"],
    "igh": ["ie", "i-e", "y"],
    "i-e": ["igh", "ie", "y"],
    "oa":  ["ow", "o-e", "oe"],
    "o-e": ["oa", "oe", "ow"],
    "oo":  ["ue", "ew", "u-e"],
    "ow":  ["ou", "au", "aw"],
    "ou":  ["ow", "au", "aw"],
    "oi":  ["oy", "oye", "oi e"],
    "oy":  ["oi", "oye", "oie"],
    "ar":  ["a", "al", "are"],
    "or":  ["aw", "au", "ore"],
    "ur":  ["ir", "er", "or"],
    "ir":  ["ur", "er", "or"],
    "aw":  ["or", "au", "ore"],
    "ew":  ["ue", "oo", "u-e"],
    "sh":  ["ch", "s", "ss"],
    "ch":  ["sh", "tch", "c"],
    "kn":  ["n", "gn", "nn"],
    "wr":  ["r", "rr", "w"],
    "dge": ["ge", "j", "dg"],
    "tion": ["shun", "sion", "tian"],
    "ey":  ["ee", "ea", "y"],
    "wh":  ["w", "we", "hw"],
}

MODES = ("insert", "choose", "spell")
YEARS = tuple(SOUNDS)
DEFAULT_MODE = "insert"
DEFAULT_YEAR = "reception"

# every real word we use, plus common words a grapheme swap might
# accidentally produce — pseudo-words are checked against this
_REAL_WORDS = {w for year in SOUNDS.values() for words in year.values() for w in words}
_REAL_WORDS |= {
    "tale", "sale", "male", "pale", "made", "mane", "pane", "plane", "may",
    "week", "weak", "meet", "meat", "see", "sea", "bee", "tea", "grown",
    "groan", "moan", "mane", "write", "right", "knight", "night", "no",
    "toe", "so", "sew", "new", "knew", "blue", "blew", "her", "fur", "fir",
    "saw", "sore", "soar", "paw", "pour", "poor", "boy", "buy", "by", "bye",
}


def _gap_word(word, grapheme):
    """Replace the grapheme with underscores: rain/ai -> r__n.

    Split digraphs gap the vowel letter and the final e: cake/a-e -> c_k_.
    """
    if "-" in grapheme:
        vowel = grapheme[0]
        i = word.find(vowel)
        chars = list(word)
        chars[i] = "_"
        chars[-1] = "_"       # the split digraph's final e
        return "".join(chars)
    return word.replace(grapheme, "_" * len(grapheme), 1)


def _apply_grapheme(word, old, new):
    """Swap one grapheme for another: rain + a-e -> rane, cake + ai -> caik."""
    if "-" in old:                       # word like 'cake' (a-e)
        vowel = old[0]
        base = word[:-1]                 # drop the final e
        if "-" in new:
            return base.replace(vowel, new[0], 1) + "e"
        return base.replace(vowel, new, 1)
    if "-" in new:                       # plain -> split: rain + a-e -> rane
        return word.replace(old, new[0], 1) + "e"
    return word.replace(old, new, 1)


def _pseudo_words(word, grapheme, count=3):
    """Wrong-but-plausible spellings of the word, never real words.

    Confusable graphemes first (same sound, different spelling); if a
    short word runs out of safe swaps, fall back to other vowel
    graphemes so there are always enough options.
    """
    fallback = [g for g in CONFUSABLE if g != grapheme and "-" not in g]
    random.shuffle(fallback)
    out = []
    for alt in CONFUSABLE.get(grapheme, []) + fallback:
        if " " in alt:
            continue
        fake = _apply_grapheme(word, grapheme, alt)
        if fake != word and fake not in _REAL_WORDS and fake not in out:
            out.append(fake)
        if len(out) == count:
            break
    return out


def _grapheme_options(grapheme, year, count=4):
    """The right grapheme plus confusable wrong ones, padded from the
    year's own grapheme set if a sound has few confusables."""
    options = [grapheme]
    for alt in CONFUSABLE.get(grapheme, []):
        if alt not in options and " " not in alt:
            options.append(alt)
        if len(options) == count:
            break
    pool = [g for g in SOUNDS[year] if g not in options]
    random.shuffle(pool)
    while len(options) < count and pool:
        options.append(pool.pop())
    random.shuffle(options)
    return options


def generate_question(mode=DEFAULT_MODE, year=DEFAULT_YEAR):
    """Return a dict ready for jsonify.

    insert -> {mode, year, word, grapheme, gapped, options: [graphemes]}
    choose -> {mode, year, word, grapheme, options: [spellings]}
    spell  -> {mode, year, word, grapheme}
    """
    if mode not in MODES:
        mode = DEFAULT_MODE
    if year not in SOUNDS:
        year = DEFAULT_YEAR

    grapheme = random.choice(list(SOUNDS[year]))
    word = random.choice(SOUNDS[year][grapheme])

    question = {"mode": mode, "year": year, "word": word, "grapheme": grapheme}

    if mode == "insert":
        question["gapped"] = _gap_word(word, grapheme)
        question["options"] = _grapheme_options(grapheme, year)
    elif mode == "choose":
        options = _pseudo_words(word, grapheme) + [word]
        random.shuffle(options)
        question["options"] = options

    return question