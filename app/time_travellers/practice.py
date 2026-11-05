"""Data for the two practice games in Time Travellers.

TIMELINE  — events from the lessons, for Timeline Challenge (put them in order).
SORT_SETS — sorting games for the shared sort page (see app/lesson_kit.py).
"""

TIMELINE = [
    {"year": 1476, "emoji": "🖨️", "label": "William Caxton prints books in England"},
    {"year": 1492, "emoji": "⛵", "label": "Columbus sails across the Atlantic"},
    {"year": 1558, "emoji": "👑", "label": "Elizabeth I becomes queen"},
    {"year": 1605, "emoji": "🎆", "label": "The Gunpowder Plot"},
    {"year": 1666, "emoji": "🔥", "label": "The Great Fire of London"},
    {"year": 1779, "emoji": "🧵", "label": "Samuel Crompton invents the spinning mule"},
    {"year": 1830, "emoji": "🚂", "label": "The first passenger railway opens"},
    {"year": 1837, "emoji": "👸", "label": "Victoria becomes queen"},
    {"year": 1854, "emoji": "🪔", "label": "Florence Nightingale helps soldiers"},
    {"year": 1903, "emoji": "✈️", "label": "The first aeroplane flight"},
    {"year": 1918, "emoji": "🌺", "label": "The First World War ends"},
    {"year": 1955, "emoji": "🚌", "label": "Rosa Parks keeps her bus seat"},
    {"year": 1969, "emoji": "🌕", "label": "Neil Armstrong walks on the Moon"},
    {"year": 1989, "emoji": "💻", "label": "Tim Berners-Lee invents the World Wide Web"},
]

# how many cards per round, and the smallest gap (in years) between any two,
# so Year 1 gets events that are easy to tell apart
TIMELINE_LEVELS = {
    "year1": {"cards": 3, "min_gap": 100},
    "year2": {"cards": 5, "min_gap": 0},
}

SORT_SETS = [
    {
        "id": "then-or-now",
        "title": "Then or Now?",
        "emoji": "🔄",
        "blurb": "Is it from long ago, or from today? You decide!",
        "question": "Is it from long ago, or something we do today?",
        "categories": [
            {"key": "then", "emoji": "📜", "label": "Long ago", "says": "That's from long ago"},
            {"key": "now", "emoji": "📱", "label": "Today", "says": "That's from today"},
        ],
        "items": [
            {"emoji": "🕯️", "text": "Lighting your house with candles", "category": "then"},
            {"emoji": "🪣", "text": "Fighting fires with leather buckets", "category": "then"},
            {"emoji": "🐴", "text": "Travelling to town by horse and cart", "category": "then"},
            {"emoji": "🪶", "text": "Writing with a feather pen", "category": "then"},
            {"emoji": "📜", "text": "Copying out books by hand", "category": "then"},
            {"emoji": "☎️", "text": "A phone with a dial, stuck to the wall", "category": "then"},
            {"emoji": "🧺", "text": "Washing clothes with a scrubbing board and mangle", "category": "then"},
            {"emoji": "⛵", "text": "Crossing the ocean in a wooden sailing ship", "category": "then"},
            {"emoji": "🚂", "text": "Riding a steam train to the seaside", "category": "then"},
            {"emoji": "👒", "text": "Changing in a bathing machine at the beach", "category": "then"},
            {"emoji": "🪀", "text": "Playing with a wooden hoop and stick", "category": "then"},
            {"emoji": "⏰", "text": "Being woken up by a knocker-upper", "category": "then"},
            {"emoji": "📱", "text": "Video calling Grandma on a phone", "category": "now"},
            {"emoji": "🚒", "text": "Fire engines with long hoses", "category": "now"},
            {"emoji": "🔌", "text": "Charging an electric car", "category": "now"},
            {"emoji": "🎮", "text": "Playing games on a tablet", "category": "now"},
            {"emoji": "🛒", "text": "Shopping online", "category": "now"},
            {"emoji": "📺", "text": "Watching a flat-screen TV in colour", "category": "now"},
            {"emoji": "🗣️", "text": "Asking a smart speaker to play a song", "category": "now"},
            {"emoji": "✈️", "text": "Flying abroad on a big jet plane", "category": "now"},
            {"emoji": "💻", "text": "Looking things up on a website", "category": "now"},
            {"emoji": "🧼", "text": "A washing machine doing the laundry", "category": "now"},
        ],
        "round": 8,
    },
]
