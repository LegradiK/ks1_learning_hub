"""Letter Quest routes — was main.py.

What changed from the standalone version:
- @app.route -> @bp.route; endpoints namespaced letter_quest.*
- app creation, load_dotenv, secret_key, port config: gone — factory's job
- Word banks now load from app/letter_quest/data/ by default, with env
  vars (WORDS_FILE / PICTURES_FILE) still honoured as overrides. Paths are
  anchored to this module, not the cwd, so they survive the move.
- Initial mode comes from the GLOBAL difficulty: easy -> beginner
  (picture clues), medium/hard -> advanced. The explicit /beginner and
  /advanced routes and the ?mode= query param still override it, so the
  existing front-end JS keeps working.
- game_logic.py (build_puzzle) moves over completely unchanged.
"""

import json
import os
from pathlib import Path

from flask import render_template, jsonify, request

from app.letter_quest import bp
from app.letter_quest.game_logic import build_puzzle
from app.core.difficulty import get_app_settings

_DATA_DIR = Path(__file__).parent / "data"


# ── Word-bank loader ──────────────────────────────────────────────────────────

def _load_bank(env_var, default_name, clue_key):
    path = Path(os.getenv(env_var) or (_DATA_DIR / default_name))
    if not path.is_absolute():
        path = _DATA_DIR / path
    try:
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)
        return {
            cat["label"]: [(w["word"], w[clue_key]) for w in cat["words"]]
            for cat in raw["categories"].values()
        }
    except FileNotFoundError:
        return {}


WORD_BANK    = _load_bank("WORDS_FILE",    "words.json",    "clue")
PICTURE_BANK = _load_bank("PICTURES_FILE", "pictures.json", "clue")


# ── Routes ────────────────────────────────────────────────────────────────────

def _render_game(initial_mode=None):
    if initial_mode is None:
        initial_mode = get_app_settings("letter_quest")["mode"]
    return render_template(
        "letter_quest/game.html",
        topics=list(WORD_BANK.keys()),
        beginner_topics=list(PICTURE_BANK.keys()),
        initial_mode=initial_mode,
    )


@bp.route("/")
def game():
    return _render_game()          # mode follows the global difficulty


@bp.route("/beginner")
def beginner():
    return _render_game("beginner")


@bp.route("/advanced")
def advanced():
    return _render_game("advanced")


@bp.route("/api/puzzle")
def api_puzzle():
    default_mode = get_app_settings("letter_quest")["mode"]
    mode  = request.args.get("mode", default_mode)
    bank  = PICTURE_BANK if mode == "beginner" else WORD_BANK
    topic = request.args.get("topic", "")

    if topic not in bank:
        topic = next(iter(bank), None)
    if not topic:
        return jsonify({"error": "no topics available for this mode"}), 404

    puzzle = build_puzzle(bank[topic])
    puzzle["mode"]  = mode
    puzzle["topic"] = topic
    return jsonify(puzzle)


@bp.route("/api/check", methods=["POST"])
def api_check():
    data    = request.get_json()
    answers = data.get("answers", {})
    correct = data.get("words",   {})

    result = {}
    for key, guess in answers.items():
        right = correct.get(key, "")
        if guess.upper() == right.upper():
            result[key] = "correct"
        elif guess.strip() == "":
            result[key] = "empty"
        else:
            result[key] = "wrong"
    return jsonify(result)