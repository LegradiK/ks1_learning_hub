"""Single source of truth for what appears on the hub menus.

To add a game: add one dict to ACTIVITIES with the group it belongs to.
To add a subject: add it to GROUPS with section="subjects".
Templates loop over these, so nothing needs changing in the HTML.
"""

# Top-level sections shown on the landing page.
SECTIONS = {
    "subjects": {
        "name": "School Subjects",
        "badge": "📚",
        "theme": "theme-words",
        "blurb": "Learn English, maths, science, history and online safety — "
                 "just like at school!",
    },
    "brain-games": {
        "name": "Brain Games",
        "badge": "🎲",
        "theme": "theme-detective",
        "blurb": "Puzzles and memory games to stretch your thinking — "
                 "just for fun!",
    },
}

# Groups of activities. Each belongs to one section.
# Order here is the order cards appear in.
GROUPS = {
    "english": {
        "name": "English",
        "section": "subjects",
        "badge": "📖",
        "theme": "theme-words",
        "blurb": "Phonics, spelling, reading and word puzzles.",
    },
    "maths": {
        "name": "Maths",
        "section": "subjects",
        "badge": "🔢",
        "theme": "theme-maths",
        "blurb": "Numbers, sums, money and telling the time.",
    },
    "science": {
        "name": "Science",
        "section": "subjects",
        "badge": "🔬",
        "theme": "theme-letters",
        "blurb": "Explore plants, animals, materials and seasons, "
                 "and find out how the world works!",
    },
    "history": {
        "name": "History",
        "section": "subjects",
        "badge": "🏰",
        "theme": "theme-sudoku",
        "blurb": "Travel back in time to meet famous people and discover "
                 "how life used to be!",
    },
    "online-safety": {
        "name": "Online Safety",
        "section": "subjects",
        "badge": "🛡️",
        "theme": "theme-money",
        "blurb": "Learn how to stay safe and kind online, and know when "
                 "to ask a grown-up for help!",
    },
    "brain-games": {
        "name": "Brain Games",
        "section": "brain-games",
        "badge": "🎲",
        "theme": "theme-detective",
        "blurb": "Puzzles and memory games — just for fun!",
    },
}

# Every playable activity. `endpoint` is passed to url_for().
# Use `badge_img` (a file in /static) instead of `badge` for image badges.
ACTIVITIES = [
    # --- English ---
    {"name": "Word Wizard", "group": "english", "endpoint": "word_wizard.game",
     "badge_img": "wizard.png", "theme": "theme-words",
     "blurb": "Put on your wizard hat — listen closely and spell the magic words!"},
    {"name": "Phonics Fox", "group": "english", "endpoint": "phonics_fox.game",
     "badge": "🦊", "theme": "theme-sound",
     "blurb": "Hear the word, spot the sound, spell it right!"},
    {"name": "Letter Quest", "group": "english", "endpoint": "letter_quest.game",
     "badge": "🔤", "theme": "theme-letters",
     "blurb": "Crack the crossword with pictures or clues."},
    {"name": "Story Detective", "group": "english", "endpoint": "story_detective.game",
     "badge": "🔍", "theme": "theme-detective",
     "blurb": "Some words have gone missing — can you crack the case?"},
    {"name": "Spelling Master", "group": "english", "endpoint": "spelling_master.game",
     "badge": "🏆", "theme": "theme-words",
     "blurb": "Practise your weekly spellings and beat your tricky words!"},

    # --- Maths ---
    {"name": "Math Drill", "group": "maths", "endpoint": "math_drill.index",
     "badge": "➕", "theme": "theme-maths",
     "blurb": "Quick-fire sums to sharpen your brain."},
    {"name": "Money Counter", "group": "maths", "endpoint": "money_counter.game",
     "badge": "💰", "theme": "theme-money",
     "blurb": "Count coins and notes and become a money expert!"},
    {"name": "Clock Master", "group": "maths", "endpoint": "clock_master.game",
     "badge": "⏰", "theme": "theme-clock",
     "blurb": "Tick tock — can you read the clock?"},

    # --- Brain games ---
    {"name": "Sudoku", "group": "brain-games", "endpoint": "sudoku.game",
     "badge": "🧩", "theme": "theme-sudoku",
     "blurb": "Fill every row, column and box — with numbers or animals!"},
    {"name": "Match Pairs", "group": "brain-games", "endpoint": "match_pairs.game",
     "badge": "🃏", "theme": "theme-pairs",
     "blurb": "Flip, remember, match — pair every picture with its word!"},
]


def groups_in(section):
    """Groups belonging to a section, each with its activity count."""
    return [
        dict(group, slug=slug,
             count=sum(1 for a in ACTIVITIES if a["group"] == slug))
        for slug, group in GROUPS.items()
        if group["section"] == section
    ]


def activities_in(group_slug):
    return [a for a in ACTIVITIES if a["group"] == group_slug]
