"""Online safety lessons for Safe Surfers (ages 5–7).

Built from:
  * DfE "Teaching online safety in schools" — its five areas: evaluating what
    you see online, recognising persuasion, online behaviour, identifying
    risks, and how and when to seek support
  * the KS1 computing curriculum — use technology safely and respectfully,
    keep personal information private, and know where to go for help about
    content or contact online
  * Relationships Education — online relationships and being safe
  * UKCIS "Education for a Connected World" statements for ages 4–7

To add a lesson: add one dict to LESSONS (format in app/lesson_kit.py).
"""

AREAS = {
    "online-world": {
        "name": "Me and the Online World",
        "emoji": "🌐",
        "blurb": "What the internet is, and how to be kind and fair online.",
        "curriculum": "Online behaviour · online relationships · ownership",
    },
    "private": {
        "name": "Keeping Safe and Private",
        "emoji": "🔒",
        "blurb": "What to keep private, passwords, and people you don't know.",
        "curriculum": "Privacy and security · identifying risks · contact",
    },
    "think": {
        "name": "Think About What You See",
        "emoji": "🤔",
        "blurb": "Is it true? Is it an advert? What if something upsets you?",
        "curriculum": "Evaluating online content · recognising persuasion",
    },
    "healthy": {
        "name": "Healthy Screen Time",
        "emoji": "⏰",
        "blurb": "Balancing screens with play, sleep and family time.",
        "curriculum": "Health, wellbeing and lifestyle",
    },
    "help": {
        "name": "Getting Help",
        "emoji": "🙋",
        "blurb": "Who your trusted adults are, and what to do if you're worried.",
        "curriculum": "How and when to seek support",
    },
}


LESSONS = [
    # ------------------------------------------------------------ online world
    {
        "id": "what-is-the-internet",
        "area": "online-world",
        "emoji": "🌐",
        "title": "What Is the Internet?",
        "tag": "Getting started",
        "blurb": "How tablets, phones and computers talk to each other.",
        "pages": [
            {"emoji": "💻", "heading": "Devices",
             "text": "Tablets, phones, computers, games consoles and smart TVs are called "
                     "devices. Lots of them can go online."},
            {"emoji": "🌐", "heading": "Going online",
             "text": "The internet connects millions of devices all around the world. When you "
                     "watch a video, play a game with friends or video call Grandma, you are online."},
            {"emoji": "🎨", "heading": "Brilliant things online",
             "text": "We can learn, play, make art, listen to stories and talk to family far away. "
                     "The internet can be lots of fun!"},
            {"emoji": "🧑‍🤝‍🧑", "heading": "Real people",
             "text": "The messages, videos and games online are made by real people. Some people "
                     "online are kind — but not everyone is."},
            {"emoji": "🛡️", "heading": "Staying safe",
             "text": "Just like crossing the road, there are rules to keep us safe online. "
                     "In these lessons, you'll learn how to be a Safe Surfer!",
             "fact": "Always ask a grown-up before you go online."},
        ],
        "words": [
            ("internet", "connects devices all around the world"),
            ("online", "using the internet"),
            ("device", "a tablet, phone, computer or console"),
            ("app", "a program on a device, like a game"),
        ],
        "talk": "What do you like to do online? Who do you do it with?",
        "quiz": [
            {"q": "Which of these is a device?",
             "options": ["A tablet", "A banana", "A sock"], "answer": 0,
             "why": "Tablets, phones and computers are devices."},
            {"q": "Who makes the videos and messages we see online?",
             "options": ["Real people", "Nobody", "Robots only"], "answer": 0,
             "why": "Real people make what we see online."},
            {"q": "What should you do before going online?",
             "options": ["Ask a grown-up", "Hide", "Turn the volume up"], "answer": 0,
             "why": "Always ask a grown-up before going online."},
        ],
    },
    {
        "id": "being-kind-online",
        "area": "online-world",
        "emoji": "💛",
        "title": "Being Kind Online",
        "tag": "Online behaviour",
        "blurb": "Treat people online the way you would face to face.",
        "pages": [
            {"emoji": "🤝", "heading": "Same rules online",
             "text": "Be as kind online as you are in the playground. The people behind the "
                     "screen have feelings too."},
            {"emoji": "💬", "heading": "Kind messages",
             "text": "Kind words make people feel happy — like 'Great drawing!' or 'Thanks for "
                     "playing with me.'"},
            {"emoji": "😢", "heading": "Unkind messages",
             "text": "Sending mean messages, leaving someone out on purpose, or laughing at "
                     "someone online can really hurt. When it happens again and again, it is bullying."},
            {"emoji": "🛑", "heading": "Stop and think",
             "text": "Before you send something, ask: Is it kind? Would I say it to their face? "
                     "Would I like it if someone sent it to me?"},
            {"emoji": "🙋", "heading": "If someone is unkind",
             "text": "Don't reply with something mean. Tell a trusted grown-up. They can help "
                     "you block, report and sort it out.",
             "fact": "If a friend is upset by something online, you can help by telling a grown-up too."},
        ],
        "words": [
            ("kind", "being friendly and caring"),
            ("bullying", "being unkind to someone again and again on purpose"),
            ("block", "stop someone from contacting you"),
            ("report", "tell an adult or website about something wrong"),
        ],
        "talk": "Think of a kind message you could send to someone in your family.",
        "quiz": [
            {"q": "Should we be kind online?",
             "options": ["Yes, just like face to face", "No, it doesn't matter online"],
             "answer": 0, "why": "People online have feelings too."},
            {"q": "Someone sends you an unkind message. What should you do?",
             "options": ["Send a mean one back", "Tell a trusted grown-up", "Keep it secret"],
             "answer": 1, "why": "A trusted grown-up can help you sort it out."},
            {"q": "Which message is kind?",
             "options": ["'You're rubbish at this'", "'Great drawing!'", "'You can't play'"],
             "answer": 1, "why": "Kind words make people feel good."},
        ],
    },
    {
        "id": "asking-permission",
        "area": "online-world",
        "emoji": "📸",
        "title": "Asking Before You Share",
        "tag": "Sharing",
        "blurb": "Photos, pictures and work belong to the people who made them.",
        "pages": [
            {"emoji": "📸", "heading": "Photos of other people",
             "text": "Always ask before you take a photo of someone, and ask again before you "
                     "share it. They might not want other people to see it."},
            {"emoji": "🖼️", "heading": "Things people make",
             "text": "Pictures, songs and stories online belong to the people who made them. "
                     "Don't pretend someone else's work is yours."},
            {"emoji": "👣", "heading": "Online footprints",
             "text": "Things you put online can stay there for a long time, and lots of people "
                     "might see them. It's like leaving footprints in wet cement!"},
            {"emoji": "🙋", "heading": "Ask a grown-up first",
             "text": "Before you share a photo, video or drawing online, ask a trusted grown-up "
                     "if it's OK.",
             "fact": "It's OK to say 'No, please don't share that photo of me.'"},
        ],
        "words": [
            ("permission", "when someone says yes, you can"),
            ("share", "put something online for others to see"),
            ("belongs", "is owned by someone"),
            ("footprint", "the trail of things you leave online"),
        ],
        "talk": "How would you feel if someone shared a silly photo of you without asking?",
        "quiz": [
            {"q": "What should you do before sharing a photo of a friend?",
             "options": ["Ask them first", "Just share it", "Change their name"], "answer": 0,
             "why": "Always ask — they might not want it shared."},
            {"q": "Things you put online can…",
             "options": ["Stay there a long time", "Vanish after one minute", "Turn into sweets"],
             "answer": 0, "why": "Online posts can stay for a long time — like footprints."},
            {"q": "Is it OK to say 'please don't share that photo of me'?",
             "options": ["Yes", "No"], "answer": 0,
             "why": "You can always say no about photos of you."},
        ],
    },

    # ------------------------------------------------------------ private
    {
        "id": "private-information",
        "area": "private",
        "emoji": "🔒",
        "title": "Keep It Private",
        "tag": "Privacy",
        "blurb": "Some things about you are just for people you know in real life.",
        "pages": [
            {"emoji": "🗝️", "heading": "Private information",
             "text": "Private information is anything that tells people who you are or where to "
                     "find you."},
            {"emoji": "🏠", "heading": "Keep these private",
             "text": "Your full name, home address, phone number, school name, birthday, "
                     "passwords and photos of you in your school uniform."},
            {"emoji": "🎨", "heading": "OK to share (with a grown-up's OK)",
             "text": "Your favourite colour, animal or game is fine to talk about. A nickname "
                     "is safer than your real name in games."},
            {"emoji": "🕵️", "heading": "Why keep it private?",
             "text": "Not everyone online is who they say they are. Keeping your information "
                     "private keeps you and your family safe."},
            {"emoji": "❓", "heading": "If someone asks",
             "text": "If a person, game or website asks for private information, stop and ask "
                     "a trusted grown-up first.",
             "fact": "Real friends you know in person already know where you live — they don't need to ask online!"},
        ],
        "words": [
            ("private", "just for you and people you trust"),
            ("personal information", "things that tell people who you are or where you live"),
            ("nickname", "a made-up name you use instead of your real one"),
            ("trusted adult", "a grown-up who keeps you safe, like a parent or teacher"),
        ],
        "talk": "Which grown-ups would you ask before giving any information online?",
        "quiz": [
            {"q": "Which should you keep private?",
             "options": ["Your favourite colour", "Your home address", "Your favourite animal"],
             "answer": 1, "why": "Your address tells people where to find you."},
            {"q": "A game asks for your phone number. What do you do?",
             "options": ["Type it in", "Ask a trusted grown-up first", "Guess a number"],
             "answer": 1, "why": "Always check with a trusted grown-up first."},
            {"q": "In online games, it is safer to use…",
             "options": ["Your full real name", "A nickname"], "answer": 1,
             "why": "A nickname keeps your real name private."},
            {"q": "Is your school name private information?",
             "options": ["Yes", "No"], "answer": 0,
             "why": "Your school name tells people where to find you."},
        ],
    },
    {
        "id": "passwords",
        "area": "private",
        "emoji": "🔑",
        "title": "Passwords Are Secret",
        "tag": "Security",
        "blurb": "Passwords are like a key to your door.",
        "pages": [
            {"emoji": "🔑", "heading": "What is a password?",
             "text": "A password is a secret word or number that unlocks a device, game or "
                     "account. It's like the key to your front door."},
            {"emoji": "🤐", "heading": "Keep it secret",
             "text": "Never tell your password to friends — not even your best friend! Only "
                     "your trusted grown-ups should know it."},
            {"emoji": "💪", "heading": "Strong passwords",
             "text": "A strong password is hard to guess. Three random words, like "
                     "'DragonPizzaRocket', are much stronger than '1234' or your name.",
             "fact": "Grown-ups can help you make and remember your passwords."},
            {"emoji": "🚪", "heading": "Log out",
             "text": "When you finish on a shared device, log out — just like locking the door "
                     "when you leave."},
        ],
        "words": [
            ("password", "a secret word that unlocks something"),
            ("account", "your own space in an app or website"),
            ("log in", "use your password to get into your account"),
            ("log out", "leave your account so others can't use it"),
        ],
        "talk": "Why do you think '1234' is a bad password?",
        "quiz": [
            {"q": "Who should know your password?",
             "options": ["Your trusted grown-ups", "Everyone at school", "Anyone who asks"],
             "answer": 0, "why": "Only your trusted grown-ups should know it."},
            {"q": "Which password is strongest?",
             "options": ["1234", "Your name", "DragonPizzaRocket"], "answer": 2,
             "why": "Three random words are hard to guess."},
            {"q": "A password is like a…",
             "options": ["Key to your door", "Sticker", "Sandwich"], "answer": 0,
             "why": "It unlocks your account, like a key unlocks a door."},
        ],
    },
    {
        "id": "people-you-dont-know",
        "area": "private",
        "emoji": "🎭",
        "title": "People You Don't Know Online",
        "tag": "Contact",
        "blurb": "Not everyone online is who they say they are.",
        "pages": [
            {"emoji": "🎭", "heading": "Who are they really?",
             "text": "Online, you can't see who you're really talking to. Someone might say "
                     "they are a child, but really be a grown-up."},
            {"emoji": "👋", "heading": "Friend requests",
             "text": "If someone you don't know wants to be your friend or chat with you in a "
                     "game, don't say yes. Tell a trusted grown-up."},
            {"emoji": "🤫", "heading": "No secrets",
             "text": "If anyone online asks you to keep a secret, send a photo, or meet up, "
                     "that is NOT OK. Tell a trusted grown-up straight away."},
            {"emoji": "😟", "heading": "Trust your tummy",
             "text": "If something online makes you feel worried, scared or uncomfortable, "
                     "listen to that feeling. Stop and tell a grown-up.",
             "fact": "You will never be in trouble for telling a trusted grown-up."},
        ],
        "words": [
            ("stranger", "someone you don't know in real life"),
            ("friend request", "when someone asks to be your friend online"),
            ("uncomfortable", "a worried, wobbly feeling that something isn't right"),
            ("secret", "something you're asked not to tell — online secrets are never OK"),
        ],
        "talk": "Who are the people you know in real life that you chat to online?",
        "quiz": [
            {"q": "Someone you don't know sends a friend request. What do you do?",
             "options": ["Say yes", "Tell a trusted grown-up", "Send them a photo"], "answer": 1,
             "why": "Don't accept people you don't know — tell a grown-up."},
            {"q": "Someone online asks you to keep a secret. Is that OK?",
             "options": ["Yes", "No"], "answer": 1,
             "why": "Online secrets are never OK. Tell a trusted grown-up."},
            {"q": "Will you get into trouble for telling a grown-up?",
             "options": ["No — telling is always right", "Yes"], "answer": 0,
             "why": "Telling a trusted grown-up is always the right thing to do."},
        ],
    },

    # ------------------------------------------------------------ think about what you see
    {
        "id": "is-it-true",
        "area": "think",
        "emoji": "🧐",
        "title": "Is It True?",
        "tag": "Real or pretend",
        "blurb": "Not everything online is real or true.",
        "pages": [
            {"emoji": "🦄", "heading": "Real or pretend?",
             "text": "Some things online are real, and some are pretend — like cartoons, "
                     "stories and games. Some pictures are changed to look real when they're not."},
            {"emoji": "🐷", "heading": "Can pigs fly?",
             "text": "If you see a video of a flying pig, ask yourself: Could that really "
                     "happen? Does it make sense?"},
            {"emoji": "🗣️", "heading": "Facts and opinions",
             "text": "A fact is true for everyone: 'Dogs have four legs.' An opinion is what "
                     "someone thinks: 'Dogs are the best pets.' Both are found online."},
            {"emoji": "🔍", "heading": "Check it",
             "text": "If you're not sure something is true, ask a grown-up, or check in a book "
                     "or another trusted website.",
             "fact": "Computers can now make pictures and voices that look real but are made up."},
        ],
        "words": [
            ("true", "really happened or really is"),
            ("pretend", "made up, not real"),
            ("fact", "something that is true"),
            ("opinion", "what someone thinks or feels"),
        ],
        "talk": "Can you think of something you've seen on a screen that was pretend?",
        "quiz": [
            {"q": "Is everything online true?",
             "options": ["Yes", "No"], "answer": 1,
             "why": "Some things online are pretend or wrong."},
            {"q": "'Cats are the best animal.' Is this a fact or an opinion?",
             "options": ["Fact", "Opinion"], "answer": 1,
             "why": "It's what someone thinks — an opinion."},
            {"q": "You're not sure if something online is true. What can you do?",
             "options": ["Ask a grown-up or check a book", "Believe it anyway", "Share it with everyone"],
             "answer": 0, "why": "Check with a grown-up or another trusted source."},
        ],
    },
    {
        "id": "adverts-and-pop-ups",
        "area": "think",
        "emoji": "🎁",
        "title": "Adverts, Pop-ups and Buying Things",
        "tag": "Persuasion",
        "blurb": "'You've won a prize!' — or have you?",
        "pages": [
            {"emoji": "📢", "heading": "What is an advert?",
             "text": "An advert tries to make you want to buy something. Adverts pop up in "
                     "games, videos and websites."},
            {"emoji": "🎉", "heading": "Too good to be true",
             "text": "A pop-up that says 'You've won a free tablet! Click here!' is a trick. "
                     "Don't click it — show a grown-up."},
            {"emoji": "💎", "heading": "Buying in games",
             "text": "Some games ask you to buy gems, coins or extra levels with real money. "
                     "Always ask a grown-up first — never buy things by yourself."},
            {"emoji": "⬇️", "heading": "Downloads",
             "text": "Ask before you download a new app or game. Some can be unsafe or cost money.",
             "fact": "Games are sometimes designed to make you want to keep playing and spending."},
        ],
        "words": [
            ("advert", "something that tries to make you buy things"),
            ("pop-up", "a box that suddenly appears on the screen"),
            ("click", "press on something on a screen"),
            ("download", "put a new app or file onto a device"),
        ],
        "talk": "Have you seen an advert while playing a game? What was it selling?",
        "quiz": [
            {"q": "A pop-up says you've won a free tablet. What do you do?",
             "options": ["Click it quickly", "Don't click — show a grown-up", "Type your address"],
             "answer": 1, "why": "Prizes that pop up are usually tricks."},
            {"q": "What should you do before buying gems in a game?",
             "options": ["Ask a grown-up", "Just press buy", "Ask a friend"], "answer": 0,
             "why": "Gems cost real money — always ask a grown-up."},
            {"q": "What does an advert want you to do?",
             "options": ["Buy something", "Go to sleep", "Do your homework"], "answer": 0,
             "why": "Adverts try to make you want to buy things."},
        ],
    },
    {
        "id": "upsetting-things",
        "area": "think",
        "emoji": "😟",
        "title": "If Something Upsets You",
        "tag": "Content",
        "blurb": "What to do if you see something scary or worrying.",
        "pages": [
            {"emoji": "😨", "heading": "It can happen",
             "text": "Sometimes we see things online that make us feel scared, sad, worried or "
                     "confused. It is not your fault."},
            {"emoji": "🛑", "heading": "Stop",
             "text": "Turn the screen over, close the lid, or press the home button. You don't "
                     "have to keep looking."},
            {"emoji": "🙋", "heading": "Tell",
             "text": "Tell a trusted grown-up what you saw. They won't be cross — they want to "
                     "help you feel better and keep you safe."},
            {"emoji": "💬", "heading": "Talk about your feelings",
             "text": "Talking about how you feel helps. You can also draw it or write it down.",
             "fact": "Remember: Stop, close, tell."},
        ],
        "words": [
            ("upset", "feeling sad, scared or worried"),
            ("content", "what you see and hear online"),
            ("trusted adult", "a grown-up who keeps you safe"),
            ("feelings", "how you feel inside, like happy or worried"),
        ],
        "talk": "Who would you tell if something online upset you?",
        "quiz": [
            {"q": "You see something scary online. What do you do first?",
             "options": ["Keep watching", "Turn the screen over or close it", "Show your little brother"],
             "answer": 1, "why": "Stop looking — turn it over or close it."},
            {"q": "Then what should you do?",
             "options": ["Tell a trusted grown-up", "Keep it secret", "Pretend nothing happened"],
             "answer": 0, "why": "A trusted grown-up can help."},
            {"q": "Is it your fault if you see something upsetting?",
             "options": ["No", "Yes"], "answer": 0,
             "why": "It's never your fault — and you won't be in trouble for telling."},
        ],
    },

    # ------------------------------------------------------------ healthy
    {
        "id": "screen-time",
        "area": "healthy",
        "emoji": "⏰",
        "title": "Screen Time Balance",
        "tag": "Wellbeing",
        "blurb": "Screens are fun — and so are lots of other things!",
        "pages": [
            {"emoji": "📱", "heading": "Screens everywhere",
             "text": "Tablets, TVs, phones and games are fun. But too much screen time can make "
                     "your eyes tired and stop you doing other things."},
            {"emoji": "⚽", "heading": "Balance",
             "text": "A healthy day has a mix: playing outside, reading books, being with family, "
                     "drawing, building — and some screen time."},
            {"emoji": "😴", "heading": "Screens and sleep",
             "text": "Screens just before bed can make it harder to fall asleep. Switch off a "
                     "while before bedtime and read a book instead."},
            {"emoji": "⏲️", "heading": "Time to stop",
             "text": "It can be hard to stop playing. Use a timer, and finish at the end of a "
                     "level. Stopping when asked is a superpower!"},
            {"emoji": "🔞", "heading": "Age ratings",
             "text": "Games, apps and films have age ratings, like PEGI 3 or PEGI 7. They tell "
                     "grown-ups whether something is suitable for your age.",
             "fact": "Most social media apps are for people aged 13 and over."},
        ],
        "words": [
            ("screen time", "time spent on tablets, TVs, phones and games"),
            ("balance", "a healthy mix of different things"),
            ("age rating", "tells you the age something is suitable for"),
            ("wellbeing", "feeling healthy and happy"),
        ],
        "talk": "What are your favourite things to do that don't use a screen?",
        "quiz": [
            {"q": "What helps you sleep well?",
             "options": ["Switching off screens before bed", "Playing games in bed", "Watching scary videos"],
             "answer": 0, "why": "Screens before bed can keep your brain awake."},
            {"q": "What is a healthy day?",
             "options": ["A mix of play, books, family and some screens", "Screens all day",
                         "No fun at all"],
             "answer": 0, "why": "Balance is the key!"},
            {"q": "What does an age rating tell you?",
             "options": ["Whether something suits your age", "How long it lasts", "What colour it is"],
             "answer": 0, "why": "Age ratings help grown-ups choose safe games and apps."},
        ],
    },

    # ------------------------------------------------------------ help
    {
        "id": "trusted-adults",
        "area": "help",
        "emoji": "🙋",
        "title": "My Trusted Adults",
        "tag": "Getting help",
        "blurb": "Who can you tell when something worries you?",
        "pages": [
            {"emoji": "🧑‍🤝‍🧑", "heading": "What is a trusted adult?",
             "text": "A trusted adult is a grown-up who keeps you safe and listens to you — like "
                     "a parent, carer, teacher or grandparent."},
            {"emoji": "🖐️", "heading": "Your helping hand",
             "text": "Draw around your hand. On each finger, write the name of a trusted adult "
                     "you could talk to. Now you have five people who can help!"},
            {"emoji": "🗣️", "heading": "When to tell",
             "text": "Tell a trusted adult if something online makes you worried, scared, sad or "
                     "confused — or if someone asks for private information or secrets."},
            {"emoji": "🔁", "heading": "Keep telling",
             "text": "If the first grown-up you tell doesn't help, tell another one on your hand "
                     "until someone does."},
            {"emoji": "☎️", "heading": "Childline",
             "text": "Children can also talk to Childline, for free, about anything that worries "
                     "them. The number is 0800 1111.",
             "fact": "You will never be in trouble for asking for help."},
        ],
        "words": [
            ("trusted adult", "a grown-up who keeps you safe and listens"),
            ("worried", "a feeling that something might be wrong"),
            ("help", "when someone makes things better"),
            ("Childline", "a free helpline for children: 0800 1111"),
        ],
        "talk": "Who are the five trusted adults on your helping hand?",
        "quiz": [
            {"q": "Which of these is a trusted adult?",
             "options": ["Your teacher", "Someone you met in a game", "A pop-up"], "answer": 0,
             "why": "Teachers, parents and carers are trusted adults."},
            {"q": "If the first grown-up doesn't help, what do you do?",
             "options": ["Tell another trusted adult", "Give up", "Keep it secret"], "answer": 0,
             "why": "Keep telling until someone helps."},
            {"q": "What is Childline's number?",
             "options": ["0800 1111", "999", "1234"], "answer": 0,
             "why": "Childline is free on 0800 1111."},
        ],
    },
    {
        "id": "safe-surfer-rules",
        "area": "help",
        "emoji": "🏄",
        "title": "Safe Surfer Rules",
        "tag": "Review",
        "blurb": "Put it all together — the rules for staying safe online.",
        "pages": [
            {"emoji": "1️⃣", "heading": "Ask first",
             "text": "Ask a grown-up before going online, downloading, buying or sharing."},
            {"emoji": "2️⃣", "heading": "Keep it private",
             "text": "Keep your name, address, school, phone number and passwords private."},
            {"emoji": "3️⃣", "heading": "Be kind",
             "text": "Only send messages you'd be happy to say face to face."},
            {"emoji": "4️⃣", "heading": "Think about it",
             "text": "Not everything online is true. Not everyone is who they say they are."},
            {"emoji": "5️⃣", "heading": "Tell",
             "text": "If anything worries you: stop, close the screen, and tell a trusted adult.",
             "fact": "Make a poster of your Safe Surfer rules and put it near your device!"},
        ],
        "words": [
            ("rule", "something that helps keep us safe"),
            ("safe", "protected from harm"),
            ("online", "using the internet"),
        ],
        "talk": "Which Safe Surfer rule do you think is the most important? Why?",
        "quiz": [
            {"q": "What should you do before downloading a new game?",
             "options": ["Ask a grown-up", "Just download it"], "answer": 0,
             "why": "Rule 1: ask first."},
            {"q": "Which is private information?",
             "options": ["Your password", "Your favourite food"], "answer": 0,
             "why": "Rule 2: passwords are always private."},
            {"q": "Something online worries you. What do you do?",
             "options": ["Stop, close it, tell a trusted adult", "Keep watching", "Keep it to yourself"],
             "answer": 0, "why": "Rule 5: stop, close, tell."},
            {"q": "Is everyone online who they say they are?",
             "options": ["Not always", "Yes, always"], "answer": 0,
             "why": "Rule 4: think about it — people can pretend online."},
        ],
    },
]
