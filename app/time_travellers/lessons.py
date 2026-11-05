"""History lessons for Time Travellers — the KS1 history programme of study.

The lessons follow the national curriculum for England (history, key stage 1):

  * skills            — words about time, putting things in order, and how
                        we find out about the past (sources)
  * living-memory     — changes within living memory
  * big-events        — events beyond living memory that matter nationally
                        or globally (Great Fire of London, first flight...)
  * famous-people     — significant individuals, compared across periods
  * local             — significant events, people and places in our locality
                        (Bolton and Greater Manchester)

To add a lesson: add one dict to LESSONS. Nothing else needs changing.
The pages themselves come from the shared lesson engine (app/lesson_kit.py).

Each lesson:
    id, area, emoji, title, tag (short label, e.g. "1666"), blurb
    pages  — list of {"emoji", "heading", "text", "fact" (optional)}
    words  — list of (word, meaning)          key vocabulary
    talk   — a question to talk about with a grown-up
    quiz   — list of {"q", "options", "answer" (index), "why"}
"""

AREAS = {
    "skills": {
        "name": "Be a History Detective",
        "emoji": "🔎",
        "blurb": "Learn the words for time, and how we find out about the past.",
        "curriculum": "Chronology, vocabulary and sources",
    },
    "living-memory": {
        "name": "When Grown-ups Were Little",
        "emoji": "👵",
        "blurb": "How life has changed since your grandparents were children.",
        "curriculum": "Changes within living memory",
    },
    "big-events": {
        "name": "Big Events Long Ago",
        "emoji": "🔥",
        "blurb": "Amazing things that happened long before anyone alive today was born.",
        "curriculum": "Events beyond living memory",
    },
    "famous-people": {
        "name": "Famous People",
        "emoji": "⭐",
        "blurb": "Meet people who changed the world — and compare them!",
        "curriculum": "Lives of significant individuals",
    },
    "local": {
        "name": "History Near Me",
        "emoji": "🏡",
        "blurb": "Discover the history of Bolton and Greater Manchester.",
        "curriculum": "Significant events, people and places in the locality",
    },
}


LESSONS = [
    # ------------------------------------------------------------------ skills
    {
        "id": "past-present-future",
        "area": "skills",
        "emoji": "⏳",
        "title": "Past, Present and Future",
        "tag": "Time words",
        "blurb": "Yesterday, today, long ago — learn the words for time.",
        "pages": [
            {"emoji": "🕰️", "heading": "What is history?",
             "text": "History is the story of the past. The past is everything that has "
                     "already happened — even this morning's breakfast!"},
            {"emoji": "📅", "heading": "Past, present and future",
             "text": "The past is what has already happened. The present is now. "
                     "The future is what has not happened yet."},
            {"emoji": "🧒", "heading": "Your own history",
             "text": "You have a history too! First you were a baby. Then you learned to "
                     "walk and talk. Now you go to school.",
             "fact": "You can make a timeline of your life with baby photos!"},
            {"emoji": "🔢", "heading": "Long, long ago",
             "text": "A decade is 10 years. A century is 100 years. Things that happened "
                     "hundreds of years ago happened long, long ago."},
            {"emoji": "➡️", "heading": "Timelines",
             "text": "A timeline puts things in order. The oldest things go at the start. "
                     "The newest things go at the end."},
        ],
        "words": [
            ("past", "the time that has already happened"),
            ("present", "now"),
            ("future", "the time that has not happened yet"),
            ("decade", "10 years"),
            ("century", "100 years"),
            ("timeline", "a line that shows things in the order they happened"),
        ],
        "talk": "What did you do yesterday? What will you do tomorrow?",
        "quiz": [
            {"q": "Which word means NOW?",
             "options": ["Past", "Present", "Future"], "answer": 1,
             "why": "The present is now. The past has gone, and the future is still to come."},
            {"q": "How many years are in a century?",
             "options": ["10", "100", "1000"], "answer": 1,
             "why": "A century is 100 years. A decade is 10 years."},
            {"q": "On a timeline, where do the oldest things go?",
             "options": ["At the start", "In the middle", "At the end"], "answer": 0,
             "why": "Timelines start with the oldest things and end with the newest."},
            {"q": "Tomorrow is in the…",
             "options": ["Past", "Present", "Future"], "answer": 2,
             "why": "Tomorrow hasn't happened yet, so it is in the future."},
        ],
    },
    {
        "id": "how-do-we-know",
        "area": "skills",
        "emoji": "🔍",
        "title": "How Do We Know About the Past?",
        "tag": "Sources",
        "blurb": "Photos, diaries and old objects are clues from long ago.",
        "pages": [
            {"emoji": "🕵️", "heading": "Clues from the past",
             "text": "Nobody alive today saw the Great Fire of London. So how do we know "
                     "about it? We look for clues! History detectives call clues sources."},
            {"emoji": "📷", "heading": "Photographs",
             "text": "Old photos show us what people wore and what their homes looked like. "
                     "Very old photos are black and white.",
             "fact": "Cameras were invented less than 200 years ago — so there are no photos "
                     "of Queen Elizabeth I!"},
            {"emoji": "📔", "heading": "Diaries and letters",
             "text": "People wrote about their lives in diaries and letters. A man called "
                     "Samuel Pepys wrote a diary about the Great Fire of London."},
            {"emoji": "🏺", "heading": "Old objects",
             "text": "Old objects are called artefacts. Toys, pots and coins dug up from the "
                     "ground tell us how people lived. You can see them in museums."},
            {"emoji": "👴", "heading": "Asking people",
             "text": "We can ask older people what life was like when they were young. "
                     "Their memories are history too!"},
            {"emoji": "🖼️", "heading": "Paintings",
             "text": "Paintings show us the past, but be careful! A painter might make "
                     "a king or queen look grander than they really were."},
        ],
        "words": [
            ("source", "something that tells us about the past"),
            ("artefact", "an old object made by people"),
            ("diary", "a book where someone writes about their day"),
            ("museum", "a building where old and special things are kept for us to see"),
            ("evidence", "clues that show something is true"),
        ],
        "talk": "Ask a grown-up: what is the oldest thing in our house? How old is it?",
        "quiz": [
            {"q": "What do history detectives call clues about the past?",
             "options": ["Sources", "Stickers", "Spells"], "answer": 0,
             "why": "Clues about the past are called sources."},
            {"q": "Who wrote a diary about the Great Fire of London?",
             "options": ["Neil Armstrong", "Samuel Pepys", "Queen Victoria"], "answer": 1,
             "why": "Samuel Pepys wrote about the fire in his diary in 1666."},
            {"q": "What is an artefact?",
             "options": ["A kind of animal", "An old object made by people", "A painting of the sea"],
             "answer": 1, "why": "An artefact is an object people made long ago, like a pot or a coin."},
            {"q": "Why might a painting not show exactly how someone looked?",
             "options": ["Paint goes mouldy", "The painter might make them look grander",
                         "Paintings are always upside down"],
             "answer": 1, "why": "Painters sometimes made important people look better than they really were."},
        ],
    },

    # ------------------------------------------------------- changes in living memory
    {
        "id": "toys-then-and-now",
        "area": "living-memory",
        "emoji": "🧸",
        "title": "Toys Then and Now",
        "tag": "Then and now",
        "blurb": "What did children play with before tablets and video games?",
        "pages": [
            {"emoji": "🪀", "heading": "Toys long ago",
             "text": "About 150 years ago, in Victorian times, children played with wooden "
                     "toys. They had spinning tops, wooden dolls, hoops and rocking horses."},
            {"emoji": "🧸", "heading": "The first teddy bears",
             "text": "Teddy bears were first made about 120 years ago. They were named after "
                     "an American president called Teddy Roosevelt."},
            {"emoji": "🧩", "heading": "When Grandma and Grandpa were little",
             "text": "About 50 years ago, children played with marbles, skipping ropes, "
                     "yo-yos, building bricks and board games. They played outside a lot!",
             "fact": "Lots of children collected conkers in autumn and played conkers in the playground."},
            {"emoji": "🎮", "heading": "Toys today",
             "text": "Today many toys use batteries or electricity. Children play video games, "
                     "use tablets and have toys that talk or move by themselves."},
            {"emoji": "⚽", "heading": "Still the same!",
             "text": "Some toys have not changed much at all. Children long ago played with "
                     "balls, dolls and teddies — just like you!"},
        ],
        "words": [
            ("Victorian", "the time when Queen Victoria was queen, about 150 years ago"),
            ("old", "made a long time ago"),
            ("modern", "new, from today"),
            ("similar", "nearly the same"),
            ("different", "not the same"),
        ],
        "talk": "Ask a grown-up: what was your favourite toy when you were little?",
        "quiz": [
            {"q": "What were most Victorian toys made from?",
             "options": ["Plastic", "Wood", "Glass"], "answer": 1,
             "why": "Victorian toys were mostly made of wood, metal and cloth. Plastic toys came much later."},
            {"q": "Which toy is a MODERN toy?",
             "options": ["A spinning top", "A rocking horse", "A tablet game"], "answer": 2,
             "why": "Tablets are new. Spinning tops and rocking horses are very old toys."},
            {"q": "Which toy did children play with long ago AND today?",
             "options": ["A ball", "A video game", "A talking robot"], "answer": 0,
             "why": "Children have played with balls for thousands of years!"},
            {"q": "Teddy bears were named after…",
             "options": ["A zookeeper", "An American president", "A queen"], "answer": 1,
             "why": "They were named after President Teddy Roosevelt."},
        ],
    },
    {
        "id": "homes-then-and-now",
        "area": "living-memory",
        "emoji": "🏠",
        "title": "Homes and Gadgets Then and Now",
        "tag": "Then and now",
        "blurb": "Phones, TVs and washing — how homes have changed.",
        "pages": [
            {"emoji": "☎️", "heading": "Telephones",
             "text": "When your grandparents were little, the phone was stuck to the wall "
                     "with a wire. You turned a dial to ring a number. Today we carry "
                     "phones in our pockets!"},
            {"emoji": "📺", "heading": "Television",
             "text": "Long ago, TVs were big boxes with black and white pictures. There were "
                     "only a few channels. Now TVs are flat, in colour, with lots of programmes.",
             "fact": "Colour TV first came to Britain in 1967."},
            {"emoji": "🧺", "heading": "Wash day",
             "text": "Long ago, washing clothes took all day. People scrubbed them by hand and "
                     "squeezed out the water with a mangle. Now a washing machine does it for us."},
            {"emoji": "🎵", "heading": "Music",
             "text": "People used to play music on records and cassette tapes. Today we can "
                     "listen to almost any song on a phone or a smart speaker."},
            {"emoji": "💻", "heading": "Computers and the internet",
             "text": "When your grown-ups were little, most homes had no computer and no "
                     "internet. Now we can video call family far away!"},
        ],
        "words": [
            ("gadget", "a clever machine or tool"),
            ("living memory", "a time that people alive today can remember"),
            ("invention", "something new that someone made for the first time"),
            ("change", "when something becomes different"),
        ],
        "talk": "Ask a grown-up: what did your home have when you were little that ours doesn't?",
        "quiz": [
            {"q": "Long ago, how did people ring a number on a phone?",
             "options": ["Turned a dial", "Tapped a screen", "Said the name out loud"], "answer": 0,
             "why": "Old phones had a round dial you turned with your finger for each number."},
            {"q": "What colour were the pictures on very old TVs?",
             "options": ["Rainbow colours", "Black and white", "Only blue"], "answer": 1,
             "why": "The first TVs showed black and white pictures."},
            {"q": "What did people use before washing machines?",
             "options": ["A dishwasher", "A mangle and scrubbing by hand", "A hairdryer"], "answer": 1,
             "why": "People scrubbed clothes by hand and squeezed them through a mangle."},
            {"q": "'Living memory' means a time that…",
             "options": ["Nobody remembers", "Only dinosaurs remember", "People alive today can remember"],
             "answer": 2, "why": "If someone alive today remembers it, it is within living memory."},
        ],
    },
    {
        "id": "seaside-holidays",
        "area": "living-memory",
        "emoji": "🏖️",
        "title": "Seaside Holidays Long Ago",
        "tag": "Then and now",
        "blurb": "Bathing machines, donkey rides and Punch and Judy!",
        "pages": [
            {"emoji": "🚂", "heading": "Off to the seaside!",
             "text": "In Victorian times, new railways meant families could take the train to "
                     "the seaside. Towns like Blackpool became very busy."},
            {"emoji": "👒", "heading": "Victorian swimming",
             "text": "Victorians wore swimming costumes that covered nearly all their body. "
                     "They changed inside little huts on wheels called bathing machines, "
                     "which were pulled into the sea."},
            {"emoji": "🎭", "heading": "Fun on the beach",
             "text": "Families watched Punch and Judy puppet shows, rode donkeys and walked "
                     "along the pier. People still do these things today!",
             "fact": "Blackpool Tower opened in 1894 — over 130 years ago."},
            {"emoji": "🚌", "heading": "When Grandma was little",
             "text": "About 50 years ago, lots of families went to British seaside towns by car "
                     "or coach. They stayed in holiday camps or guest houses."},
            {"emoji": "✈️", "heading": "Holidays today",
             "text": "Today some families still go to the British seaside. Others fly in a "
                     "plane to beaches in other countries."},
        ],
        "words": [
            ("seaside", "a place by the sea where people go on holiday"),
            ("pier", "a long walkway built out over the sea"),
            ("bathing machine", "a hut on wheels for changing in, pulled into the sea"),
            ("holiday", "time off for rest and fun"),
        ],
        "talk": "What would you pack for a seaside trip? Would a Victorian child pack the same things?",
        "quiz": [
            {"q": "How did Victorian families get to the seaside?",
             "options": ["By plane", "By train", "By rocket"], "answer": 1,
             "why": "New railways took Victorian families to the seaside."},
            {"q": "What was a bathing machine?",
             "options": ["A washing machine", "A hut on wheels for changing in", "A boat"], "answer": 1,
             "why": "It was a hut on wheels that was pulled into the sea."},
            {"q": "Which seaside fun do people STILL enjoy today?",
             "options": ["Punch and Judy shows", "Bathing machines", "Riding a penny-farthing"], "answer": 0,
             "why": "You can still watch Punch and Judy at some beaches today."},
            {"q": "Which seaside town in the North West has a famous tower?",
             "options": ["Blackpool", "Bolton", "Brighton"], "answer": 0,
             "why": "Blackpool Tower opened in 1894."},
        ],
    },

    # ------------------------------------------------------- events beyond living memory
    {
        "id": "great-fire-of-london",
        "area": "big-events",
        "emoji": "🔥",
        "title": "The Great Fire of London",
        "tag": "1666",
        "blurb": "A bakery fire that burned for four days and changed London forever.",
        "pages": [
            {"emoji": "🏘️", "heading": "London in 1666",
             "text": "Over 350 years ago, London looked very different. The houses were made "
                     "of wood and straw. They were built very close together on narrow streets."},
            {"emoji": "🍞", "heading": "A fire in the bakery",
             "text": "Early on Sunday 2nd September 1666, a fire started in Thomas Farriner's "
                     "bakery on Pudding Lane. He was the king's baker."},
            {"emoji": "💨", "heading": "Why did it spread so fast?",
             "text": "The summer had been hot and dry. A strong wind blew the flames from house "
                     "to house. Shops by the river were full of things that burn easily, "
                     "like oil, wood and coal."},
            {"emoji": "🪣", "heading": "Fighting the fire",
             "text": "There were no fire engines. People passed leather buckets of water and used "
                     "squirts. They pulled houses down with long fire hooks to stop the flames."},
            {"emoji": "⛵", "heading": "Escaping",
             "text": "People ran away with whatever they could carry. Many escaped in boats on "
                     "the River Thames. Others camped in the fields outside the city."},
            {"emoji": "🧀", "heading": "Samuel Pepys's diary",
             "text": "Samuel Pepys wrote about the fire in his diary. He buried his wine and "
                     "his Parmesan cheese in the garden to keep them safe!",
             "fact": "His diary is one of the main ways we know what happened."},
            {"emoji": "🏚️", "heading": "Four days of fire",
             "text": "The fire burned for four days. More than 13,000 houses burned down, "
                     "and the old St Paul's Cathedral was destroyed."},
            {"emoji": "⛪", "heading": "Building London again",
             "text": "New houses were built with brick and stone, which don't burn as easily. "
                     "Sir Christopher Wren designed a new St Paul's Cathedral, which you can "
                     "still visit today."},
            {"emoji": "🗼", "heading": "The Monument",
             "text": "A tall stone tower called the Monument was built to remember the fire. "
                     "It is 202 feet tall — and it stands 202 feet from where the bakery was!"},
        ],
        "words": [
            ("bakery", "a place where bread is baked"),
            ("Pudding Lane", "the street where the fire started"),
            ("diary", "a book where someone writes about each day"),
            ("cathedral", "a very big, important church"),
            ("fire hook", "a long pole with a hook for pulling houses down"),
        ],
        "talk": "How are fires put out today? What is different from 1666?",
        "quiz": [
            {"q": "Where did the Great Fire of London start?",
             "options": ["In a bakery on Pudding Lane", "In a castle", "On a ship"], "answer": 0,
             "why": "It started in Thomas Farriner's bakery on Pudding Lane."},
            {"q": "In which year was the Great Fire?",
             "options": ["1066", "1666", "1966"], "answer": 1,
             "why": "The Great Fire of London was in 1666."},
            {"q": "Why did the fire spread so quickly?",
             "options": ["The houses were made of wood and close together",
                         "It was snowing", "The houses were made of stone"],
             "answer": 0, "why": "Wooden houses, close together, a dry summer and a strong wind helped it spread."},
            {"q": "What did Samuel Pepys bury in his garden?",
             "options": ["His cat", "His cheese", "His shoes"], "answer": 1,
             "why": "He buried his Parmesan cheese (and his wine) to keep them safe!"},
            {"q": "What were new houses built from after the fire?",
             "options": ["Wood and straw", "Paper", "Brick and stone"], "answer": 2,
             "why": "Brick and stone don't burn as easily as wood."},
            {"q": "Who designed the new St Paul's Cathedral?",
             "options": ["Sir Christopher Wren", "King Henry VIII", "Thomas Farriner"], "answer": 0,
             "why": "Sir Christopher Wren designed it, and it still stands today."},
        ],
    },
    {
        "id": "bonfire-night",
        "area": "big-events",
        "emoji": "🎆",
        "title": "The Gunpowder Plot and Bonfire Night",
        "tag": "1605",
        "blurb": "Why do we have fireworks on the 5th of November?",
        "pages": [
            {"emoji": "👑", "heading": "King James",
             "text": "Over 400 years ago, in 1605, James the First was king. Some men were very "
                     "unhappy with the king and the rules he made."},
            {"emoji": "🛢️", "heading": "A secret plan",
             "text": "The men made a secret plan to blow up the Houses of Parliament while the "
                     "king was inside. They hid 36 barrels of gunpowder in a cellar underneath."},
            {"emoji": "✉️", "heading": "A warning letter",
             "text": "Someone sent a letter warning a lord to stay away from Parliament. "
                     "The king's men searched the cellars."},
            {"emoji": "🔦", "heading": "Guy Fawkes is caught",
             "text": "On the night of 4th November, they found Guy Fawkes guarding the "
                     "gunpowder. The plan had failed, and the king was safe."},
            {"emoji": "🔥", "heading": "Bonfires to celebrate",
             "text": "People lit bonfires to celebrate that the king was safe. We still "
                     "remember it every year on the 5th of November with bonfires and fireworks.",
             "fact": "This is an anniversary — we remember the same event on the same date every year."},
            {"emoji": "🧤", "heading": "Firework safety",
             "text": "Fireworks are beautiful but dangerous. Always stand back, let a grown-up "
                     "light them, and wear gloves if you hold a sparkler."},
        ],
        "words": [
            ("plot", "a secret plan to do something bad"),
            ("Parliament", "where people meet to make the country's laws"),
            ("gunpowder", "a powder that explodes"),
            ("anniversary", "the same date each year when we remember something"),
        ],
        "talk": "Why do you think people still remember the Gunpowder Plot after 400 years?",
        "quiz": [
            {"q": "What did the plotters want to blow up?",
             "options": ["A bakery", "The Houses of Parliament", "A ship"], "answer": 1,
             "why": "They wanted to blow up the Houses of Parliament with the king inside."},
            {"q": "Who was caught guarding the gunpowder?",
             "options": ["Guy Fawkes", "Samuel Pepys", "William Caxton"], "answer": 0,
             "why": "Guy Fawkes was caught in the cellar."},
            {"q": "On which date is Bonfire Night?",
             "options": ["25th December", "5th November", "1st January"], "answer": 1,
             "why": "We remember the Gunpowder Plot on the 5th of November."},
            {"q": "Who should light fireworks?",
             "options": ["Children", "A grown-up", "Nobody ever"], "answer": 1,
             "why": "Fireworks are dangerous — only grown-ups should light them."},
        ],
    },
    {
        "id": "first-flight",
        "area": "big-events",
        "emoji": "✈️",
        "title": "The First Aeroplane Flight",
        "tag": "1903",
        "blurb": "Two brothers who taught the world to fly.",
        "pages": [
            {"emoji": "🐦", "heading": "Dreaming of flying",
             "text": "For thousands of years, people watched birds and wished they could fly too. "
                     "Some tried with wings made of feathers — but they couldn't fly!"},
            {"emoji": "🚲", "heading": "The Wright brothers",
             "text": "Orville and Wilbur Wright were brothers from America. They ran a bicycle "
                     "shop, and they loved building machines."},
            {"emoji": "🪁", "heading": "Gliders and kites",
             "text": "The brothers tested kites and gliders for years. They learned how to "
                     "steer and balance a flying machine."},
            {"emoji": "🛫", "heading": "17th December 1903",
             "text": "On a windy beach near Kitty Hawk, Orville flew their plane, the Flyer. "
                     "It stayed in the air for 12 seconds. It was the first proper aeroplane flight!",
             "fact": "That first flight was shorter than the wingspan of a jumbo jet!"},
            {"emoji": "🌍", "heading": "Flying today",
             "text": "Planes got faster and bigger. Now huge jets carry hundreds of people "
                     "around the world every day."},
        ],
        "words": [
            ("aeroplane", "a machine with wings and an engine that flies"),
            ("glider", "a plane with no engine that floats on the wind"),
            ("inventor", "someone who makes something new for the first time"),
            ("engine", "a machine that makes something move"),
        ],
        "talk": "How did people travel to other countries before there were aeroplanes?",
        "quiz": [
            {"q": "Who made the first aeroplane flight?",
             "options": ["The Wright brothers", "Neil Armstrong", "Queen Victoria"], "answer": 0,
             "why": "Orville and Wilbur Wright made the first flight in 1903."},
            {"q": "What kind of shop did the brothers run?",
             "options": ["A sweet shop", "A bicycle shop", "A bakery"], "answer": 1,
             "why": "They ran a bicycle shop in America."},
            {"q": "How long did the very first flight last?",
             "options": ["12 seconds", "12 hours", "12 days"], "answer": 0,
             "why": "It lasted just 12 seconds — but it changed the world!"},
            {"q": "In which year was the first aeroplane flight?",
             "options": ["1666", "1903", "2003"], "answer": 1,
             "why": "It was on 17th December 1903."},
        ],
    },
    {
        "id": "remembrance-day",
        "area": "big-events",
        "emoji": "🌺",
        "title": "Remembrance Day",
        "tag": "1918",
        "blurb": "Why we wear poppies and keep a two-minute silence.",
        "pages": [
            {"emoji": "🌍", "heading": "A big war",
             "text": "More than 100 years ago, many countries fought in the First World War. "
                     "It lasted from 1914 to 1918. Lots of soldiers, nurses and helpers went "
                     "far from home."},
            {"emoji": "🕚", "heading": "The war ends",
             "text": "The fighting stopped at 11 o'clock on the 11th day of the 11th month — "
                     "11th November 1918."},
            {"emoji": "🌺", "heading": "Red poppies",
             "text": "Red poppy flowers grew in the fields where the soldiers had fought. "
                     "Now people wear poppies to remember them."},
            {"emoji": "🤫", "heading": "Two minutes of quiet",
             "text": "Every year on 11th November, at 11 o'clock, many people stop and stay "
                     "quiet for two minutes. This is called the two-minute silence.",
             "fact": "On Remembrance Sunday, people lay poppy wreaths at war memorials."},
            {"emoji": "🕊️", "heading": "Remembering",
             "text": "We remember all the people who helped in wars, and we hope for peace. "
                     "You might find a war memorial near your home or school."},
        ],
        "words": [
            ("remember", "to think about something from the past"),
            ("poppy", "a red flower we wear to remember"),
            ("memorial", "something built so we remember people or events"),
            ("peace", "when there is no fighting"),
        ],
        "talk": "Have you seen a war memorial? Where was it?",
        "quiz": [
            {"q": "Which flower do people wear on Remembrance Day?",
             "options": ["A daisy", "A red poppy", "A sunflower"], "answer": 1,
             "why": "Red poppies grew where the soldiers fought, so we wear them to remember."},
            {"q": "What time does the two-minute silence start?",
             "options": ["11 o'clock", "3 o'clock", "Midnight"], "answer": 0,
             "why": "The fighting stopped at 11 o'clock on 11th November 1918."},
            {"q": "When did the First World War end?",
             "options": ["1666", "1918", "2018"], "answer": 1,
             "why": "It ended on 11th November 1918."},
        ],
    },

    # ------------------------------------------------------- significant individuals
    {
        "id": "two-queens",
        "area": "famous-people",
        "emoji": "👑",
        "title": "Elizabeth I and Queen Victoria",
        "tag": "Compare two queens",
        "blurb": "Two famous queens who lived nearly 300 years apart.",
        "pages": [
            {"emoji": "👑", "heading": "Queen Elizabeth I",
             "text": "Elizabeth the First became queen in 1558, when she was 25. She was a "
                     "Tudor queen and ruled for 44 years."},
            {"emoji": "⛵", "heading": "Elizabeth's England",
             "text": "In her time, sailors explored the world in wooden ships. William "
                     "Shakespeare wrote his famous plays. In 1588 her navy beat the Spanish Armada."},
            {"emoji": "👸", "heading": "Queen Victoria",
             "text": "Victoria became queen in 1837, when she was only 18. She ruled for 63 years. "
                     "She married Prince Albert and they had nine children."},
            {"emoji": "🚂", "heading": "Victoria's Britain",
             "text": "In her time there were new railways, factories and inventions like the "
                     "telephone. She was one of the first royals to travel by train."},
            {"emoji": "⚖️", "heading": "Same and different",
             "text": "Both were powerful queens who ruled for a long time. Elizabeth never "
                     "married. Victoria had a big family. Elizabeth rode horses and carriages. "
                     "Victoria could take a train!",
             "fact": "There are photographs of Queen Victoria, but only paintings of Elizabeth I — "
                     "cameras hadn't been invented in her time."},
        ],
        "words": [
            ("reign", "the time a king or queen rules"),
            ("Tudor", "the royal family of Henry VIII and Elizabeth I"),
            ("Victorian", "from the time of Queen Victoria"),
            ("monarch", "a king or queen"),
            ("compare", "look at how things are the same and different"),
        ],
        "talk": "If you were a king or queen, what would you change?",
        "quiz": [
            {"q": "Which queen ruled first?",
             "options": ["Elizabeth I", "Queen Victoria"], "answer": 0,
             "why": "Elizabeth I became queen in 1558. Victoria became queen in 1837."},
            {"q": "How old was Victoria when she became queen?",
             "options": ["8", "18", "80"], "answer": 1,
             "why": "She was just 18 years old."},
            {"q": "Which queen could travel by train?",
             "options": ["Elizabeth I", "Queen Victoria"], "answer": 1,
             "why": "Railways were built in Victoria's time. There were no trains when Elizabeth was queen."},
            {"q": "Why are there no photographs of Elizabeth I?",
             "options": ["She was shy", "Cameras hadn't been invented", "They were all lost"], "answer": 1,
             "why": "Cameras were invented over 200 years after she died, so we only have paintings."},
        ],
    },
    {
        "id": "explorers",
        "area": "famous-people",
        "emoji": "🧭",
        "title": "Christopher Columbus and Neil Armstrong",
        "tag": "Compare two explorers",
        "blurb": "One sailed across an ocean, one walked on the Moon.",
        "pages": [
            {"emoji": "⛵", "heading": "Christopher Columbus",
             "text": "In 1492, Columbus sailed from Spain with three wooden ships. He wanted to "
                     "find a new way to Asia by sailing west across the Atlantic Ocean."},
            {"emoji": "🏝️", "heading": "Land ahoy!",
             "text": "After about ten weeks, his sailors saw land. It wasn't Asia — it was islands "
                     "in the Caribbean. People already lived there, but Europeans didn't know about them."},
            {"emoji": "🚀", "heading": "Neil Armstrong",
             "text": "In July 1969, Neil Armstrong flew to the Moon in a rocket called Apollo 11, "
                     "with Buzz Aldrin and Michael Collins. The journey took four days."},
            {"emoji": "👣", "heading": "Walking on the Moon",
             "text": "Neil Armstrong was the first person to step onto the Moon. Millions of "
                     "people watched on TV. His footprints are still there today!",
             "fact": "There is no wind on the Moon, so nothing blows the footprints away."},
            {"emoji": "⚖️", "heading": "Same and different",
             "text": "Both were brave explorers who went somewhere new. Columbus used the wind "
                     "and the stars to find his way. Armstrong used a rocket and computers."},
        ],
        "words": [
            ("explorer", "someone who travels to find new places"),
            ("voyage", "a long journey by sea or in space"),
            ("astronaut", "someone who travels into space"),
            ("rocket", "a machine that blasts into space"),
        ],
        "talk": "Where would you most like to explore? How would you get there?",
        "quiz": [
            {"q": "How did Columbus travel?",
             "options": ["In a rocket", "In wooden sailing ships", "In a plane"], "answer": 1,
             "why": "He sailed in three wooden ships in 1492."},
            {"q": "Who was the first person to walk on the Moon?",
             "options": ["Neil Armstrong", "Christopher Columbus", "Orville Wright"], "answer": 0,
             "why": "Neil Armstrong stepped onto the Moon in 1969."},
            {"q": "Who explored first?",
             "options": ["Columbus", "Armstrong"], "answer": 0,
             "why": "Columbus sailed in 1492, nearly 500 years before the Moon landing in 1969."},
            {"q": "Why are Armstrong's footprints still on the Moon?",
             "options": ["Someone guards them", "There is no wind to blow them away", "They are painted on"],
             "answer": 1, "why": "With no wind or rain on the Moon, the footprints stay."},
        ],
    },
    {
        "id": "caxton-and-berners-lee",
        "area": "famous-people",
        "emoji": "📖",
        "title": "William Caxton and Tim Berners-Lee",
        "tag": "Compare two inventors",
        "blurb": "The printing press and the World Wide Web — sharing words with everyone.",
        "pages": [
            {"emoji": "🪶", "heading": "Books by hand",
             "text": "Long ago, every book was copied out by hand with a feather pen. One book "
                     "could take months to make, so books were rare and very expensive."},
            {"emoji": "🖨️", "heading": "William Caxton",
             "text": "In 1476, William Caxton set up the first printing press in England, in "
                     "London. It could print many copies of a page quickly."},
            {"emoji": "📚", "heading": "Books for more people",
             "text": "Caxton printed stories, poems and books about history. More people could "
                     "buy books and learn to read."},
            {"emoji": "💻", "heading": "Tim Berners-Lee",
             "text": "Tim Berners-Lee was born in London. In 1989 he invented the World Wide Web "
                     "— the websites we visit on the internet."},
            {"emoji": "🎁", "heading": "A gift to the world",
             "text": "He chose not to charge money for his invention, so everyone could use it "
                     "for free.",
             "fact": "Caxton and Berners-Lee lived over 500 years apart, but both helped people share words and ideas."},
        ],
        "words": [
            ("printing press", "a machine that prints words onto paper"),
            ("World Wide Web", "all the websites on the internet"),
            ("website", "pages you can visit on a computer, tablet or phone"),
            ("invent", "make something new for the first time"),
        ],
        "talk": "How do you find out new things — from books, websites or people?",
        "quiz": [
            {"q": "How were books made before printing presses?",
             "options": ["Copied out by hand", "On a computer", "With a photocopier"], "answer": 0,
             "why": "People copied every word by hand, which took a very long time."},
            {"q": "Who brought the printing press to England?",
             "options": ["William Caxton", "Tim Berners-Lee", "Guy Fawkes"], "answer": 0,
             "why": "William Caxton set up England's first printing press in 1476."},
            {"q": "What did Tim Berners-Lee invent?",
             "options": ["The aeroplane", "The World Wide Web", "The teddy bear"], "answer": 1,
             "why": "He invented the World Wide Web in 1989."},
            {"q": "What did both inventions help people do?",
             "options": ["Share words and ideas", "Fly", "Cook food"], "answer": 0,
             "why": "Printed books and websites both help people share words and ideas."},
        ],
    },
    {
        "id": "brave-nurses",
        "area": "famous-people",
        "emoji": "🏥",
        "title": "Florence Nightingale, Mary Seacole and Edith Cavell",
        "tag": "Compare three nurses",
        "blurb": "Three brave nurses who cared for soldiers.",
        "pages": [
            {"emoji": "🪔", "heading": "Florence Nightingale",
             "text": "In 1854, Florence Nightingale went to help soldiers hurt in the Crimean War. "
                     "The hospital was dirty and many soldiers were very ill."},
            {"emoji": "🧼", "heading": "The Lady with the Lamp",
             "text": "Florence made the hospital clean, with fresh air, soap and good food. "
                     "She checked on soldiers at night with her lamp. Later she started a school "
                     "to train nurses."},
            {"emoji": "🌿", "heading": "Mary Seacole",
             "text": "Mary Seacole was born in Jamaica. She learned how to use herbs to make "
                     "medicines. She wanted to help the soldiers in the Crimean War too."},
            {"emoji": "☕", "heading": "Mary's British Hotel",
             "text": "When she was not allowed to join the nurses, Mary paid for the journey "
                     "herself! She built the British Hotel near the fighting, where soldiers "
                     "could get food, rest and medicine."},
            {"emoji": "🎖️", "heading": "Edith Cavell",
             "text": "Edith Cavell was a nurse from Norfolk. In the First World War she worked "
                     "in Belgium and cared for soldiers from both sides. She bravely helped "
                     "about 200 soldiers escape to safety."},
            {"emoji": "⚖️", "heading": "Same and different",
             "text": "All three were brave and kind, and cared for soldiers in wartime. "
                     "Florence and Mary lived at the same time. Edith lived about 60 years later.",
             "fact": "Hospitals today still follow Florence's idea: keep everything clean!"},
        ],
        "words": [
            ("nurse", "someone who looks after people who are ill or hurt"),
            ("hospital", "a place where ill people are cared for"),
            ("herbs", "plants used in medicine or cooking"),
            ("brave", "doing something even when it is hard or scary"),
        ],
        "talk": "How do nurses and doctors help us today? What do they use that Florence didn't have?",
        "quiz": [
            {"q": "Who was called 'the Lady with the Lamp'?",
             "options": ["Mary Seacole", "Florence Nightingale", "Edith Cavell"], "answer": 1,
             "why": "Florence checked on the soldiers at night carrying a lamp."},
            {"q": "Where was Mary Seacole born?",
             "options": ["Jamaica", "London", "Belgium"], "answer": 0,
             "why": "Mary Seacole was born in Jamaica."},
            {"q": "What did Florence Nightingale make sure the hospital was?",
             "options": ["Clean", "Noisy", "Dark"], "answer": 0,
             "why": "Keeping things clean stopped many soldiers getting more ill."},
            {"q": "Edith Cavell helped soldiers in which war?",
             "options": ["The Crimean War", "The First World War"], "answer": 1,
             "why": "Edith Cavell worked in Belgium during the First World War."},
        ],
    },
    {
        "id": "standing-up-for-fairness",
        "area": "famous-people",
        "emoji": "✊",
        "title": "Rosa Parks and Emily Davison",
        "tag": "Compare two campaigners",
        "blurb": "Two women who stood up against unfair rules.",
        "pages": [
            {"emoji": "🗳️", "heading": "Women couldn't vote",
             "text": "Over 100 years ago in Britain, women were not allowed to vote for the "
                     "people who made the laws. Lots of people thought this was unfair."},
            {"emoji": "📣", "heading": "Emily Davison",
             "text": "Emily Davison was a suffragette. Suffragettes campaigned for women to get "
                     "the vote. They marched, made speeches and protested."},
            {"emoji": "🏇", "heading": "The horse race",
             "text": "In 1913, Emily ran onto the track at a big horse race. She was badly hurt "
                     "and died. Her bravery made many more people think about votes for women.",
             "fact": "In 1918 some women could vote, and from 1928 women could vote just like men."},
            {"emoji": "🚌", "heading": "Rosa Parks",
             "text": "In America in 1955, there was an unfair rule on buses. Black people had to "
                     "give up their seats for white people. Rosa Parks was asked to give up her "
                     "seat — and she said no."},
            {"emoji": "🚶", "heading": "Walking instead",
             "text": "Rosa was arrested. In protest, people refused to ride the buses for over a "
                     "year! In the end, the unfair bus rule was changed."},
            {"emoji": "⚖️", "heading": "Same and different",
             "text": "Both women stood up against rules that were unfair. Emily lived in Britain "
                     "over 100 years ago. Rosa lived in America about 70 years ago."},
        ],
        "words": [
            ("vote", "choose someone or something, like choosing who runs the country"),
            ("suffragette", "a woman who campaigned for women to vote"),
            ("protest", "show you think something is wrong"),
            ("fair", "treating everyone the same way"),
        ],
        "talk": "Have you ever seen something unfair? What could you do to help?",
        "quiz": [
            {"q": "What did suffragettes want?",
             "options": ["Free sweets", "Votes for women", "More horses"], "answer": 1,
             "why": "Suffragettes campaigned so women could vote."},
            {"q": "What did Rosa Parks refuse to give up?",
             "options": ["Her bus seat", "Her hat", "Her dog"], "answer": 0,
             "why": "She refused to give up her bus seat because the rule was unfair."},
            {"q": "Which country did Rosa Parks live in?",
             "options": ["Britain", "America", "Jamaica"], "answer": 1,
             "why": "Rosa Parks lived in Montgomery, in America."},
            {"q": "What was the same about Emily and Rosa?",
             "options": ["They were sisters", "They stood up against unfair rules",
                         "They were both queens"],
             "answer": 1, "why": "Both women were brave and stood up against unfair rules."},
        ],
    },
    {
        "id": "painters",
        "area": "famous-people",
        "emoji": "🎨",
        "title": "Pieter Bruegel and L.S. Lowry",
        "tag": "Compare two painters",
        "blurb": "Two artists who loved painting busy crowds of people.",
        "pages": [
            {"emoji": "🖌️", "heading": "Pieter Bruegel",
             "text": "Pieter Bruegel was a painter who lived nearly 500 years ago, in the "
                     "country we now call Belgium."},
            {"emoji": "👨‍🌾", "heading": "Busy village life",
             "text": "Bruegel painted ordinary people — farmers working, families at weddings, "
                     "and hunters walking through the snow."},
            {"emoji": "🤸", "heading": "Children's Games",
             "text": "One of his paintings is called Children's Games. It shows over 80 games, "
                     "like leapfrog, hoops and blind man's buff!"},
            {"emoji": "🏭", "heading": "L.S. Lowry",
             "text": "L.S. Lowry lived much later and painted near us, in Salford and "
                     "Manchester. He painted mills, chimneys and busy streets."},
            {"emoji": "🧍", "heading": "Matchstick people",
             "text": "Lowry's people are thin, like matchsticks. He worked as a rent collector "
                     "in the day and painted at night.",
             "fact": "You can see his paintings at The Lowry in Salford Quays."},
            {"emoji": "⚖️", "heading": "Same and different",
             "text": "Both painted crowds of everyday people. Bruegel's people are in villages "
                     "and fields. Lowry's people are in towns, going to work in factories."},
        ],
        "words": [
            ("artist", "someone who makes art, like paintings"),
            ("painting", "a picture made with paint"),
            ("mill", "a big factory where cotton was made into thread and cloth"),
            ("crowd", "lots of people together"),
        ],
        "talk": "If you painted a busy picture of your town, what would you put in it?",
        "quiz": [
            {"q": "Which painter lived first?",
             "options": ["Pieter Bruegel", "L.S. Lowry"], "answer": 0,
             "why": "Bruegel lived nearly 500 years ago. Lowry lived in the last century."},
            {"q": "What do Lowry's people look like?",
             "options": ["Matchsticks", "Robots", "Giants"], "answer": 0,
             "why": "People call them 'matchstick men' because they are so thin."},
            {"q": "Where did Lowry paint?",
             "options": ["Salford and Manchester", "The Moon", "Jamaica"], "answer": 0,
             "why": "Lowry painted mills and streets in Salford and Manchester."},
            {"q": "What did both painters like to paint?",
             "options": ["Only flowers", "Crowds of everyday people", "Only the sea"], "answer": 1,
             "why": "They both painted busy crowds of ordinary people."},
        ],
    },

    # ------------------------------------------------------------------ local
    {
        "id": "crompton-and-the-mills",
        "area": "local",
        "emoji": "🧵",
        "title": "Samuel Crompton and Bolton's Cotton Mills",
        "tag": "Bolton",
        "blurb": "A Bolton inventor and the mills that made our town busy.",
        "pages": [
            {"emoji": "🐑", "heading": "Spinning thread",
             "text": "To make cloth, you first spin cotton into thread. Long ago, people spun "
                     "thread at home on a spinning wheel, one thread at a time."},
            {"emoji": "🏡", "heading": "Samuel Crompton",
             "text": "Samuel Crompton was born in Bolton in 1753. He lived in an old house "
                     "called Hall i' th' Wood. You can visit it today — it is a museum!"},
            {"emoji": "⚙️", "heading": "The spinning mule",
             "text": "In 1779, Samuel invented a machine called the spinning mule. It could spin "
                     "lots of fine, strong threads at the same time."},
            {"emoji": "🏭", "heading": "The cotton mills",
             "text": "Soon Bolton was full of huge cotton mills with tall chimneys. Thousands of "
                     "people worked there — and in Victorian times, even children worked in the mills."},
            {"emoji": "⏰", "heading": "The knocker-upper",
             "text": "Most workers had no alarm clocks. A knocker-upper walked the streets early "
                     "in the morning, tapping on bedroom windows with a long stick to wake them up!",
             "fact": "Many workers wore wooden-soled clogs, which clattered on the cobbled streets."},
            {"emoji": "🔎", "heading": "Be a local detective",
             "text": "Look around your town. Can you spot old mill buildings, tall chimneys, or "
                     "street names that give clues about the past?"},
        ],
        "words": [
            ("cotton", "soft fibre from a plant, made into thread and cloth"),
            ("spinning mule", "Samuel Crompton's machine for spinning thread"),
            ("mill", "a big factory with machines"),
            ("local", "near where you live"),
            ("knocker-upper", "a person who woke workers up by tapping on windows"),
        ],
        "talk": "Do you know any old buildings near you? What do you think they were used for?",
        "quiz": [
            {"q": "What did Samuel Crompton invent?",
             "options": ["The spinning mule", "The aeroplane", "The teddy bear"], "answer": 0,
             "why": "He invented the spinning mule in 1779."},
            {"q": "Which town was Samuel Crompton from?",
             "options": ["Bolton", "London", "Blackpool"], "answer": 0,
             "why": "He was born in Bolton and lived at Hall i' th' Wood."},
            {"q": "What did a knocker-upper do?",
             "options": ["Built houses", "Woke people up for work", "Baked bread"], "answer": 1,
             "why": "They tapped on windows with a long stick to wake mill workers."},
            {"q": "What was made in a cotton mill?",
             "options": ["Thread and cloth", "Cars", "Ice cream"], "answer": 0,
             "why": "Mills spun cotton into thread and wove it into cloth."},
        ],
    },
    {
        "id": "greater-manchester-firsts",
        "area": "local",
        "emoji": "🚂",
        "title": "Greater Manchester Firsts",
        "tag": "Greater Manchester",
        "blurb": "The first passenger railway, and a famous suffragette from Manchester.",
        "pages": [
            {"emoji": "🐴", "heading": "Before trains",
             "text": "Long ago, people travelled by horse, by cart or on foot. A journey from "
                     "Manchester to Liverpool took many hours."},
            {"emoji": "🚂", "heading": "The Rocket",
             "text": "George and Robert Stephenson built a steam train called the Rocket. "
                     "In 1829 it won a race to find the best engine."},
            {"emoji": "🛤️", "heading": "The first passenger railway",
             "text": "In 1830, the Liverpool and Manchester Railway opened. It was the first "
                     "railway in the world to carry passengers between two cities by steam train.",
             "fact": "The old Manchester station is now part of the Science and Industry Museum."},
            {"emoji": "🗳️", "heading": "Emmeline Pankhurst",
             "text": "Emmeline Pankhurst was born in Manchester. In 1903 she started a group of "
                     "suffragettes in Manchester, who campaigned for women to get the vote."},
            {"emoji": "🗽", "heading": "Remembered today",
             "text": "Today there is a statue of Emmeline Pankhurst in Manchester, in St Peter's "
                     "Square. People remember her for helping women get the vote."},
        ],
        "words": [
            ("steam train", "a train pushed along by steam from boiling water"),
            ("passenger", "someone travelling on a train, bus or plane"),
            ("railway", "the tracks that trains run on"),
            ("statue", "a model of a person, made of stone or metal"),
        ],
        "talk": "How do you travel to school? How would a child 200 years ago have travelled?",
        "quiz": [
            {"q": "What was the Rocket?",
             "options": ["A space rocket", "A steam train", "A firework"], "answer": 1,
             "why": "The Rocket was the Stephensons' famous steam train."},
            {"q": "Which railway was the world's first passenger railway between two cities?",
             "options": ["Liverpool and Manchester", "London and Paris", "Bolton and Blackpool"],
             "answer": 0, "why": "The Liverpool and Manchester Railway opened in 1830."},
            {"q": "What did Emmeline Pankhurst campaign for?",
             "options": ["Votes for women", "More trains", "Longer holidays"], "answer": 0,
             "why": "She led the suffragettes, who campaigned for votes for women."},
            {"q": "How did people travel before trains?",
             "options": ["By horse, cart or on foot", "By plane", "By electric car"], "answer": 0,
             "why": "Before trains, people walked or used horses and carts."},
        ],
    },
]

