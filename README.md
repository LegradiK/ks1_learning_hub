# 🎈 KS1 Learning Hub

**Little games for big learning** — a collection of free, curriculum-inspired learning games for children aged 4–7 (Reception to Year 2), built with Flask.

🔗 **Live demo:** [kidslearninggames.pythonanywhere.com](https://kidslearninggames.pythonanywhere.com/)

<!-- TODO: add a screenshot or short GIF of the hub home page here -->

<!-- ![KS1 Learning Hub home page](docs/screenshot-home.png) -->

---

## ✨ What's inside

Ten games, a reading log and a progress report, grouped into three sections on the home page: **School Subjects**, **Brain Games** and **My Bookshelf**. Most games have level switches (from Reception up to Year 2), chunky tap-friendly buttons, instant feedback and stars or streaks to earn.

### 📚 School Subjects — English


| Game                   | What children practise                                                                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧙 **Word Wizard**     | Listen-and-spell — hear a word read aloud, then spell it, stage by stage (Reception, Year 1 and Year 2 word banks)                                                      |
| 🦊 **Phonics Fox**     | Phonics — find the missing sound, pick the right spelling, or spell the whole word (Reception Phases 2–4, Year 1 Phase 5, Year 2 spelling rules)                       |
| 🔤 **Letter Quest**    | A child-sized crossword with picture clues (Beginner) or written clues (Advanced)                                                                                        |
| 🔍 **Story Detective** | Reading comprehension — fill the gaps in a short story using clues in the text. 44 stories, including retellings of well-known fairy tales, fables and folk tales       |
| 🏆 **Spelling Master** | The weekly spelling list from school — test by week, mixed at random, or just the "tricky words" the child keeps getting wrong. Words on their own or inside a sentence |

### 🔢 School Subjects — Maths


| Game                 | What children practise                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| ➕ **Math Drill**    | Quick-fire addition, subtraction, multiplication and division, with difficulty levels and a streak counter |
| 💰 **Money Counter** | Counting UK coins and notes, and making amounts from a tray of money                                       |
| ⏰ **Clock Master**  | Reading an analogue clock, and setting the time by dragging the hands                                      |

Science, History and Online Safety are on the way and show as "coming soon".

### 🎲 Brain Games


| Game               | What children practise                                              |
| -------------------- | --------------------------------------------------------------------- |
| 🧩 **Sudoku**      | 4×4, 6×6 and 9×9 puzzles, with numbers or animals                |
| 🃏 **Match Pairs** | A memory game pairing pictures with their words, from 4 to 16 pairs |

### 📕 My Bookshelf

A reading log for the child: search for books (Google Books, with genres from Open Library), sort them into *Reading now*, *Finished* and *Want to read*, give stars and short reviews, and track how many times a book has been read. Reading awards unlock at 1, 5, 10… up to 1,000 books, each with a printable PDF certificate.

### 📊 My progress

A report for each child showing time spent and answers given in every game, over the last 7 days, the last 30 days or all time — plus their reading.

---

## 🧠 Design principles

- **Practice should feel like play.** Short games, no timers, no pressure — wrong answers just hop back out for another go, and solving on the first try earns three stars.
- **Built for small hands, on any screen.** Every tappable target is at least 44–52 px, with visible focus rings for keyboard users and `prefers-reduced-motion` support. On phones the top bar folds into a ☰ Menu, cards and settings stack neatly, and puzzles such as the crossword and Sudoku resize to fit the screen.
- **Answers live on the server.** Games like Story Detective and Spelling Master never send the correct answers to the browser — the client submits its answers to a checking API, so peeking at DevTools spoils nothing.
- **One design system, many themes.** A single stylesheet drives every game through CSS custom properties: each game swaps `--accent` / `--accent-soft` via a `theme-*` body class, and shared components (jelly buttons, panels, progress bars, score cards) restyle themselves automatically.
- **Voices through Puter.** Words and sentences are read aloud with [Puter](https://puter.com)'s text-to-speech, with a man or woman voice to choose from. A speaker button in the top bar shows whether voices are on.

---

## 🏗️ Architecture

```
ks1_learning_hub/
├── run.py                       # entry point (Render / local)
├── pythonanywhere_run.py        # entry point for PythonAnywhere
├── requirements.txt
├── app/
│   ├── __init__.py              # app factory + blueprint registration
│   ├── extensions.py            # SQLAlchemy
│   ├── models.py                # children, game progress, study log, books
│   ├── progress.py              # save/load each child's progress per game
│   ├── study.py                 # time + answers per game, and the progress report
│   ├── templates/
│   │   ├── base.html            # shared shell: top bar, Learning menu, footer
│   │   ├── hub/                 # home, subjects, game lists, about, progress
│   │   └── <game>/              # one template folder per game
│   ├── static/
│   │   ├── style.css            # the shared design system (incl. phone layouts)
│   │   ├── speech.js            # text-to-speech via Puter
│   │   ├── track.js             # sends time spent / answers to the server
│   │   └── bookshelf.js, script.js, images
│   ├── hub/
│   │   └── activities.py        # one list of every section, subject and game
│   ├── auth/                    # name + PIN login, and grown-up CLI commands
│   ├── bookshelf/               # reading log, book search, awards, certificates
│   └── story_detective/         # each game is a self-contained blueprint:
│       ├── __init__.py          #   blueprint object
│       ├── route.py             #   page + JSON API routes
│       ├── game_logic.py        #   pure-Python game rules (no Flask imports)
│       └── resources/           #   content as data modules
│           ├── year1_stories.py
│           └── year2_stories.py
```

**Key decisions:**

- **App factory + blueprints.** The hub started life as three standalone Flask apps (Letter Quest, Math Drill, Word Wizard) that were consolidated into one application, and a standalone reading tracker was later merged in as My Bookshelf. Each game is an isolated blueprint with its own routes, logic and content — adding a game never touches another game's code.
- **One list drives the menus.** `app/hub/activities.py` lists every section, subject and game. The home page, subject pages, the Learning menu and the How to play list are all built from it, so adding a game there puts it everywhere.
- **Content as data, separate from logic.** Game content (stories, word lists, spelling weeks) lives in data files validated at startup. Adding a Story Detective story or a week of spellings means editing a data file — no changes to routes or game logic.
- **Server-side checking.** Game rules live in `game_logic.py` modules that know nothing about Flask, exposed through small JSON APIs. The front end is vanilla JavaScript — no framework, no build step.
- **Simple, private logins.** Children log in with their name and a 4-digit PIN (five wrong tries in a row locks the login for five minutes). There's no sign-up page: a grown-up creates logins from the command line. Each child's progress, study time and bookshelf are saved to their own account, so they follow them to any device. Nothing is shared with third parties apart from book searches (Google Books / Open Library) and voices (Puter).
- **Same code, any database.** Locally the app uses a SQLite file; in production it uses Postgres (Neon) via `DATABASE_URL`. Tables are created automatically on startup.

---

## 🚀 Running locally

Requires **Python 3.12+**.

```bash
git clone https://github.com/LegradiK/ks1_learning_hub.git
cd ks1_learning_hub

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Create a `data.env` file in the project folder:

```
FLASK_KEY=any-long-random-string
# DATABASE_URL=postgresql://...   # optional — leave out to use a local SQLite file
```

Create a login, then start the server:

```bash
flask --app run add-child <child name>   # asks for a 4-digit PIN
python3 run.py
```

Open http://127.0.0.1:5000 and log in.

Other grown-up commands:

```bash
flask --app run set-pin <child name>          # change a PIN
flask --app run list-children
flask --app run remove-child <child name> 
flask --app run import-bookshelf path/to/reading_tracker.db <child name>    # bring books across from the old bookshelf site
```

To test on a tablet or phone on the same Wi-Fi, `run.py` already listens on all interfaces — visit `http://<your-computer-ip>:5000` from the device.

---

## ☁️ Deployment

The app runs in two places:

**PythonAnywhere** — [kidslearninggames.pythonanywhere.com](https://kidslearninggames.pythonanywhere.com/)

- WSGI entry point: `pythonanywhere_run.py` (`app`)
- Update by pushing to GitHub, then `git pull` in a PythonAnywhere console and **Reload** on the Web tab

---

## ➕ Adding content

### A week of spellings (Spelling Master)

Add a block to `app/spelling_master/data/words.json` with the next week number. The `sentence` is read aloud for the "words in sentences" test, and the word inside it becomes the gap:

```json
{
  "week": 8,
  "words": [
    {"word": "train", "sentence": "We went to the seaside by train."},
    {"word": "said",  "sentence": "Mum said it was time for bed."}
  ]
}
```

The new week appears in the week dropdown as soon as the updated file is on the server — no restart needed. Weeks are listed ten to a column (weeks 11–20 in the second column, and so on).

### A Story Detective story

Stories are plain dicts in `app/story_detective/resources/`. Append one to the right year file and restart — a startup validator catches authoring mistakes (duplicate ids, missing fields, an answer missing from its own options) before they reach a child:

```python
{
    "id": "my-new-story",
    "level": 1,
    "emoji": "🌟",
    "title": "My New Story",
    "segments": [
        {"text": "The sun was "},
        {"gap": {"answer": "bright", "options": ["bright", "green", "sleepy"]}},
        {"text": " in the sky."},
    ],
}
```

In Year 1 the word bank shows only the right answers; in Year 2 it mixes in every gap's wrong options too. Distractor guidelines used across the stories: one option is the same word class with the wrong meaning; one is plausible but contradicted by the story — so a right answer always proves the child read and understood the text. In Year 2, check that no wrong option also fits a different gap in the same story.

### A new game

Create a blueprint (`__init__.py`, `route.py`, `game_logic.py`) and a template folder, register it in `app/__init__.py`, then add one entry to `ACTIVITIES` in `app/hub/activities.py` — it then shows up on the home page, in the Learning menu and in the progress report.

---

## 🗺️ Roadmap — ideas for the future

- [ ]  Science, History and Online Safety games
- [ ]  Drag-and-drop word placement in Story Detective (it was tried, then replaced with tap-to-place because it wasn't reliable)
- [ ]  More word banks per level
- [ ]  Automated tests for game logic and API routes
- [ ]  Sound effects and celebration animations
- [ ]  Printable activity sheets to pair with the games

---

## 👋 About

Built by **Kaho** ([@LegradiK](https://github.com/LegradiK)) — a Python developer
based in Greater Manchester. Spotted a bug or have an idea for a new game?
[Open an issue](https://github.com/LegradiK/ks1_learning_hub/issues) — I'd love to hear it.
