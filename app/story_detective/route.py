from flask import jsonify, render_template, request

from app.story_detective import bp
from app.story_detective.game_logic import (
    check_answers,
    get_story_payload,
    list_stories,
    stars_for,
)


@bp.route("/")
def game():
    return render_template(
        "story_detective/game.html",
        quizzes=list_stories(),
    )


@bp.get("/api/story/<story_id>")
def api_story(story_id):
    story = get_story_payload(story_id)
    if story is None:
        return jsonify({"error": "Story not found"}), 404
    return jsonify(story)


@bp.post("/api/check")
def api_check():
    # silent=True + .get() -> a malformed body gives a clean 400,
    # not a KeyError 500 like data["story_id"] did.
    data = request.get_json(silent=True) or {}

    result = check_answers(data.get("story_id"), data.get("answers"))
    if result is None:
        return jsonify({"error": "Invalid request"}), 400

    if result["solved"]:
        result["stars"] = stars_for(data.get("attempts", 1))
    return jsonify(result)