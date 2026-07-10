"""Match Pairs game logic — pure Python, no Flask imports.

Deals a shuffled board of face-down cards. Each pair is one PICTURE
card (an emoji) and one WORD card (its name); the child must flip a
matching picture + word to take the pair.

Difficulty sets both the board size and the word complexity:
  easy       ->  4 pairs  (8 cards)   short Reception words
  medium     ->  6 pairs  (12 cards)  Year 1 words
  hard       -> 10 pairs  (20 cards)  Year 2 words
  extra_hard -> 16 pairs  (32 cards)  long tricky words
"""

import random

# (emoji, word) pools — each pool is larger than its pair count so
# every game deals a different selection
PAIRS = {
    "easy": [
        ("🐱", "cat"), ("🐶", "dog"), ("☀️", "sun"), ("🐟", "fish"),
        ("🐷", "pig"), ("🐮", "cow"), ("🚗", "car"), ("🚌", "bus"),
        ("🥚", "egg"), ("🎩", "hat"), ("🛏️", "bed"), ("🐝", "bee"),
    ],
    "medium": [
        ("🐑", "sheep"), ("🚂", "train"), ("🏠", "house"), ("🍎", "apple"),
        ("⭐", "star"), ("🌙", "moon"), ("🌳", "tree"), ("🐸", "frog"),
        ("⛵", "boat"), ("🌧️", "rain"), ("🐌", "snail"), ("🦆", "duck"),
        ("🐴", "horse"), ("🍰", "cake"),
    ],
    "hard": [
        ("🐘", "elephant"), ("🌈", "rainbow"), ("🐧", "penguin"),
        ("🚀", "rocket"), ("🏰", "castle"), ("🕷️", "spider"),
        ("🐬", "dolphin"), ("🍌", "banana"), ("🚜", "tractor"),
        ("🐉", "dragon"), ("🐵", "monkey"), ("🌸", "flower"),
        ("🦋", "butterfly"), ("☂️", "umbrella"), ("🥪", "sandwich"),
    ],
    "extra_hard": [
        ("🐊", "crocodile"), ("🚁", "helicopter"), ("🍓", "strawberry"),
        ("🦕", "dinosaur"), ("🦘", "kangaroo"), ("🐙", "octopus"),
        ("🐢", "tortoise"), ("🍄", "mushroom"), ("⛄", "snowman"),
        ("🦄", "unicorn"), ("🌋", "volcano"), ("🔭", "telescope"),
        ("✂️", "scissors"), ("🍍", "pineapple"), ("🦔", "hedgehog"),
        ("🐿️", "squirrel"), ("🦏", "rhinoceros"), ("🐛", "caterpillar"),
        ("🧸", "teddy bear"), ("🎠", "carousel"),
    ],
}

NUM_PAIRS = {"easy": 4, "medium": 6, "hard": 10, "extra_hard": 16}
DEFAULT_DIFFICULTY = "easy"


def deal_board(difficulty=DEFAULT_DIFFICULTY):
    """Return a dict ready for jsonify: shuffled cards for one game.

    {difficulty, pairs: 6, cards: [
        {"pair": 0, "type": "pic",  "face": "🐱"},
        {"pair": 0, "type": "word", "face": "cat"},
        ...shuffled...
    ]}
    """
    if difficulty not in PAIRS:
        difficulty = DEFAULT_DIFFICULTY

    chosen = random.sample(PAIRS[difficulty], NUM_PAIRS[difficulty])

    cards = []
    for i, (emoji, word) in enumerate(chosen):
        cards.append({"pair": i, "type": "pic",  "face": emoji})
        cards.append({"pair": i, "type": "word", "face": word})
    random.shuffle(cards)

    return {
        "difficulty": difficulty,
        "pairs": NUM_PAIRS[difficulty],
        "cards": cards,
    }