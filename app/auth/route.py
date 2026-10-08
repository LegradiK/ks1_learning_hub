"""Name + PIN login.

Every page except the login page needs a logged-in child; the check runs
before each request (require_login). The Puter sign-in happens in the
browser on the same click as "Let's go" — see templates/auth/login.html.
"""

from flask import (
    flash, g, redirect, render_template, request, session, url_for,
)

from app.auth import bp
from app.extensions import db
from app.models import Child

# Pages anyone can open without logging in.
PUBLIC_ENDPOINTS = {"auth.login", "static"}


@bp.before_app_request
def require_login():
    child_id = session.get("child_id")
    g.child = db.session.get(Child, child_id) if child_id else None

    if g.child is None and request.endpoint not in PUBLIC_ENDPOINTS:
        if "/api/" in request.path or request.is_json:     # game API calls get JSON, not a page
            return {"error": "Please log in again."}, 401
        return redirect(url_for("auth.login", next=request.full_path.rstrip("?")))


def _safe_next(target):
    """Only redirect back within this site."""
    if target and target.startswith("/") and not target.startswith("//"):
        return target
    return url_for("hub.index")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if g.child and request.method == "GET":
        return redirect(_safe_next(request.args.get("next")))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        pin = request.form.get("pin", "").strip()
        next_url = request.form.get("next")

        child = Child.find(name) if name else None
        if child and child.is_locked():
            flash(f"Too many tries — wait {child.minutes_locked()} minutes, then try again.", "error")
        elif child and len(pin) == 4 and pin.isdigit() and child.try_pin(pin):
            db.session.commit()
            session.clear()
            session["child_id"] = child.id
            session.permanent = True               # stay logged in (see PERMANENT_SESSION_LIFETIME)
            return redirect(_safe_next(next_url))
        else:
            if child:
                db.session.commit()                # save the failed-attempt count
            flash("That name and PIN don't match. Try again!", "error")
        return render_template("auth/login.html", name=name, next=next_url), 401

    return render_template("auth/login.html", name="", next=request.args.get("next", ""))


@bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
