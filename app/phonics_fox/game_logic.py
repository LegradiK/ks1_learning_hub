"""Phonics Fox game logic — pure Python, no Flask imports.

Grapheme sets mapped to the UK Letters and Sounds / spelling curriculum:

  reception -> Phases 2-4: ck, qu, ll/ss/ff, the consonant digraphs
               (ch, sh, th, ng), vowel digraphs (ai, ee, igh, oa, oo),
               and more vowel sounds (ar, or, ur, ow, oi, ear, air, er).
               Phase 4 adds no new sounds, so blends appear inside the
               word choices instead (train, string, crown, splash...).

  year1     -> Phase 5 alternative graphemes: ay, ou, ie, ea, oy, ir,
               ue, aw, wh, ph, ew, oe, au, ey, and the split digraphs
               a-e, e-e, i-e, o-e, u-e.

  year2     -> Year 2 spelling curriculum: silent letters (kn, wr, gn),
               dge/ge, soft c, tion, and -le endings.

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
    # ---- Phases 2-4 (Phase 4 blends live inside the words) ----
    "reception": {
        "ck":  ["kick", "duck", "sock", "rock", "clock", "truck"],
        "qu":  ["quick", "quiz", "queen", "quack"],
        "ll":  ["bell", "doll", "hill", "smell", "spill"],
        "ss":  ["miss", "hiss", "dress", "cross", "press"],
        "ff":  ["puff", "cliff", "sniff", "fluff"],
        "ch":  ["chip", "chat", "lunch", "bench", "crunch"],
        "sh":  ["ship", "shop", "shell", "brush", "splash"],
        "th":  ["thin", "thick", "moth", "bath", "cloth"],
        "ng":  ["ring", "king", "song", "long", "string"],
        "ai":  ["rain", "tail", "snail", "paint", "train", "chain"],
        "ee":  ["feet", "seen", "tree", "green", "sleep", "sheep"],
        "igh": ["high", "light", "night", "right", "bright"],
        "oa":  ["boat", "coat", "road", "goat", "soap", "toast"],
        "oo":  ["moon", "food", "boot", "spoon", "roof"],
        "ar":  ["card", "park", "shark", "farm", "start", "sharp"],
        "or":  ["fork", "corn", "storm", "sport", "torch"],
        "ur":  ["turn", "burn", "hurt", "curl", "burst"],
        "ow":  ["cow", "down", "town", "owl", "brown", "crown"],
        "oi":  ["coin", "soil", "boil", "point", "spoil"],
        "ear": ["ear", "hear", "near", "year", "beard"],
        "air": ["air", "hair", "fair", "chair", "stairs"],
        "er":  ["hammer", "ladder", "dinner", "summer", "winter"],
    },
    # ---- Phase 5: alternative graphemes + split digraphs ----
    "year1": {
        "ay":  ["day", "play", "stay", "spray", "crayon"],
        "ou":  ["out", "cloud", "found", "shout", "proud"],
        "ie":  ["tie", "pie", "lie", "dried"],
        "ea":  ["eat", "sea", "read", "beach", "dream", "treat"],
        "oy":  ["boy", "toy", "enjoy", "royal", "oyster"],
        "ir":  ["girl", "bird", "shirt", "first", "third", "dirty"],
        "ue":  ["blue", "clue", "glue", "true", "rescue"],
        "aw":  ["saw", "paw", "draw", "yawn", "crawl", "straw"],
        "wh":  ["when", "which", "whisk", "wheel", "white"],
        "ph":  ["photo", "phone", "dolphin", "elephant", "alphabet"],
        "ew":  ["flew", "grew", "chew", "threw", "stew"],
        "oe":  ["toe", "goes", "tiptoe", "heroes"],
        "au":  ["autumn", "launch", "sauce", "astronaut", "haunted"],
        "ey":  ["key", "monkey", "donkey", "money", "valley", "honey"],
        "a-e": ["cake", "make", "snake", "gate", "plate"],
        "e-e": ["these", "theme", "complete"],
        "i-e": ["kite", "bike", "time", "smile", "slide", "shine"],
        "o-e": ["bone", "home", "note", "stone", "smoke"],
        "u-e": ["cube", "tune", "flute", "cute", "huge"],
    },
    # ---- Year 2 spelling curriculum ----
    "year2": {
        "kn":   ["knee", "knock", "knife", "knot", "know", "knight"],
        "wr":   ["wrap", "wrist", "wrong", "write", "wriggle"],
        "gn":   ["gnat", "gnaw", "gnome", "sign"],
        "dge":  ["badge", "bridge", "hedge", "fridge", "edge", "dodge"],
        "ge":   ["cage", "stage", "change", "large", "orange"],
        "c":    ["city", "race", "ice", "space", "pencil"],   # soft c
        "tion": ["station", "fiction", "motion", "action", "section"],
        "le":   ["table", "apple", "little", "bottle", "middle", "candle"],
    },
}

# graphemes that make (roughly) the same sound — used to build wrong
# answers in insert mode and pseudo-words in choose mode
CONFUSABLE = {
    # reception
    "ck":  ["k", "c", "ch"],
    "qu":  ["kw", "q", "cw"],
    "ll":  ["l", "le", "el"],
    "ss":  ["s", "se", "ce"],
    "ff":  ["f", "ph", "gh"],
    "ch":  ["sh", "tch", "c"],
    "sh":  ["ch", "s", "ss"],
    "th":  ["f", "v", "ff"],
    "ng":  ["n", "nk", "gn"],
    "ai":  ["ay", "a-e", "ei"],
    "ee":  ["ea", "e-e", "ey"],
    "igh": ["ie", "i-e", "y"],
    "oa":  ["ow", "o-e", "oe"],
    "oo":  ["ue", "ew", "u-e"],
    "ar":  ["a", "al", "are"],
    "or":  ["aw", "au", "ore"],
    "ur":  ["ir", "er", "or"],
    "ow":  ["ou", "au", "aw"],
    "oi":  ["oy", "oye", "oie"],
    "ear": ["eer", "ere", "ier"],
    "air": ["are", "ere", "air"],
    "er":  ["ur", "ir", "or"],
    # year 1
    "ay":  ["ai", "a-e", "ei"],
    "ou":  ["ow", "au", "aw"],
    "ie":  ["igh", "i-e", "y"],
    "ea":  ["ee", "e-e", "ey"],
    "oy":  ["oi", "oye", "oie"],
    "ir":  ["ur", "er", "or"],
    "ue":  ["ew", "oo", "u-e"],
    "aw":  ["or", "au", "ore"],
    "wh":  ["w", "we", "hw"],
    "ph":  ["f", "ff", "v"],
    "ew":  ["ue", "oo", "u-e"],
    "oe":  ["oa", "ow", "o-e"],
    "au":  ["aw", "or", "ore"],
    "ey":  ["ee", "ea", "y"],
    "a-e": ["ai", "ay", "ei"],
    "e-e": ["ee", "ea", "ey"],
    "i-e": ["igh", "ie", "y"],
    "o-e": ["oa", "oe", "ow"],
    "u-e": ["ue", "ew", "oo"],
    # year 2
    "kn":   ["n", "gn", "nn"],
    "wr":   ["r", "rr", "w"],
    "gn":   ["n", "kn", "nn"],
    "dge":  ["ge", "j", "dg"],
    "ge":   ["j", "dge", "g"],
    "c":    ["s", "k", "ss"],
    "tion": ["shun", "sion", "tian"],
    "le":   ["el", "al", "il"],
}

MODES = ("insert", "choose", "spell")
YEARS = tuple(SOUNDS)
DEFAULT_MODE = "insert"
DEFAULT_YEAR = "reception"

# every real word we use, plus common words a grapheme swap might
# accidentally produce — pseudo-words are checked against this
_REAL_WORDS = {w for year in SOUNDS.values() for words in year.values() for w in words}
_REAL_WORDS |= {
    # homophones / near-misses that swaps can generate
    "tale", "sale", "male", "pale", "made", "mane", "pane", "plane", "may",
    "plait", "gait", "week", "weak", "meet", "meat", "reed", "beech",
    "see", "sea", "bee", "tea", "flue", "tow", "grown", "groan", "moan",
    "rite", "right", "write", "knight", "night", "sin", "rap", "rake",
    "cadge", "fin", "kin", "son", "his", "tern", "spake", "now", "not",
    "no", "know", "knew", "new", "toe", "so", "sew", "blue", "blew",
    "her", "fur", "fir", "sore", "soar", "saw", "poor", "pour", "paw",
    "boy", "buy", "by", "bye", "here", "hear", "there", "their",
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
        if " " in alt or alt == grapheme:
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