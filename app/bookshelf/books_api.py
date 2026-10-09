"""Book lookups: Google Books for search and covers, Open Library for genres.

Moved over from the standalone bookshelf site. Nothing here touches the
database — routes call these and save what they return.
"""

import os
import unicodedata

import requests
from flask import current_app

GOOGLE_BOOKS_LINK = "https://www.googleapis.com/books/v1/volumes"


def _api_key():
    return current_app.config.get("GOOGLE_BOOKS_API_KEY") or os.getenv("GOOGLE_BOOKS_API_KEY")


def https_cover(url):
    """Google Books gives http:// cover links; the hub runs on https, so the
    browser would block them as mixed content."""
    if url and url.startswith("http://"):
        return "https://" + url[len("http://"):]
    return url or None


def normalize_text(s):
    """Lower-case and strip accents, so 'Zoe' finds 'Zoë'."""
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def search_google_books(q, start=0):
    """Returns (results, total_items) or raises requests.RequestException."""
    params = {"q": q, "maxResults": 40, "startIndex": start}
    if _api_key():
        params["key"] = _api_key()
    resp = requests.get(GOOGLE_BOOKS_LINK, params=params, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        published = info.get("publishedDate", "")
        results.append({
            "google_books_id": item.get("id"),
            "title": info.get("title", "Untitled"),
            "author": ", ".join(info.get("authors", [])) or "Unknown author",
            "year": published[:4] if published else None,
            "cover_url": https_cover(info.get("imageLinks", {}).get("thumbnail")),
            "isbn": _extract_isbn(info),
            "categories": ", ".join(info.get("categories", [])),
        })
    return results, data.get("totalItems", 0)


def _extract_isbn(volume_info):
    """Pull ISBN-13 (preferred) or ISBN-10 out of Google Books' industryIdentifiers list."""
    identifiers = volume_info.get("industryIdentifiers", [])
    isbn_13 = next((i["identifier"] for i in identifiers if i.get("type") == "ISBN_13"), None)
    isbn_10 = next((i["identifier"] for i in identifiers if i.get("type") == "ISBN_10"), None)
    return isbn_13 or isbn_10

def _fetch_volume_details(google_books_id):
    """Fetch a single volume by ID — used when bulk-adding from search results."""
    params = {}
    if _api_key():
        params["key"] = _api_key()

    resp = requests.get(f"{GOOGLE_BOOKS_LINK}/{google_books_id}", params=params, timeout=5)
    resp.raise_for_status()
    info = resp.json().get("volumeInfo", {})
    image_links = info.get("imageLinks", {})

    return {
        "google_books_id": google_books_id,
        "title": info.get("title", "Untitled"),
        "author": ", ".join(info.get("authors", [])) or "Unknown author",
        "cover_url": https_cover(image_links.get("thumbnail")),
        "isbn": _extract_isbn(info),
        "categories": ", ".join(info.get("categories", [])),
    }


# Subject strings that show up in Open Library data but aren't really genres.
_SUBJECT_NOISE = {"accelerated reader", "lexile", "large type books", "protected daisy"}

# Canonical genre whitelist, each mapped to keywords that might appear in
# Open Library's messier subject strings.
_GENRE_KEYWORDS = {
    "Fiction":                ["fiction"],
    "Military Fiction":       ["military fiction", "war stories", "military-fiction"],
    "Action":                 ["action"],
    "Nonfiction":              ["nonfiction", "non-fiction"],
    "Fantasy":                 ["fantasy"],
    "Science Fiction":         ["science fiction", "sci-fi", "sci fi"],
    "Mystery":                 ["mystery", "detective"],
    "Thriller":                ["thriller", "suspense"],
    "Horror":                  ["horror"],
    "Romance":                 ["romance", "love stories"],
    "Historical Fiction":      ["historical fiction", "historical"],
    "Young Adult":             ["young adult", "teen fiction", "juvenile fiction"],
    "Children's":              ["children's", "juvenile literature", "picture books"],
    "Biography":               ["biography", "biographical"],
    "Memoir":                  ["memoir", "autobiography"],
    "Poetry":                  ["poetry", "poems"],
    "Classics":                ["classic"],
    "Contemporary":            ["contemporary"],
    "Graphic Novels & Comics": ["graphic novel", "comic"],
    "Adventure":               ["adventure"],
    "Crime":                   ["crime"],
    "War":                     ["war"],
    "Self Help":               ["self-help", "self help"],
}

# More specific genres are checked before broad ones, so e.g. "Historical
# Fiction" is preferred over the generic "Fiction" match.
_GENRE_PRIORITY = [
    "Military Fiction", "Historical Fiction", 
    "Science Fiction", "Graphic Novels & Comics", "Self Help", "Mystery",
    "Thriller", "Horror", "Romance", "War", "Fantasy", "Adventure", "Action",
    "Crime", "Biography", "Memoir", "Poetry", "Classics", "Contemporary",
    "Young Adult", "Children's",
    "Nonfiction", "Fiction",
]


def map_to_known_genres(subjects, limit=5):
    """
    Match raw Open Library subject strings against the canonical genre
    whitelist using keyword matching. Returns only whitelisted genre names,
    deduplicated, most-specific first.
    """
    matched = set()

    for subject in subjects:
        subject_lower = subject.lower()
        for genre in _GENRE_PRIORITY:
            if genre in matched:
                continue
            if any(kw in subject_lower for kw in _GENRE_KEYWORDS[genre]):
                matched.add(genre)
                break

    ordered = [g for g in _GENRE_PRIORITY if g in matched]
    return ordered[:limit]


def get_genres_from_open_library(isbn, google_categories=None, limit=5):
    """
    Fetch genre tags for a book, preferring Open Library subjects, falling
    back to Google Books categories (also mapped through the same whitelist)
    if Open Library has nothing specific.
    """
    genres = []

    if isbn:
        headers = {"User-Agent": "KS1LearningHub/1.0 (github.com/LegradiK/ks1_learning_hub)"}
        try:
            edition_resp = requests.get(
                f"https://openlibrary.org/isbn/{isbn}.json", headers=headers, timeout=5
            )
            if edition_resp.status_code == 200:
                works = edition_resp.json().get("works", [])
                if works:
                    work_resp = requests.get(
                        f"https://openlibrary.org{works[0]['key']}.json",
                        headers=headers, timeout=5,
                    )
                    if work_resp.status_code == 200:
                        subjects = work_resp.json().get("subjects", [])
                        cleaned = [
                            s for s in subjects
                            if s.lower() not in _SUBJECT_NOISE
                            and ":" not in s and not any(c.isdigit() for c in s)
                        ]
                        genres = map_to_known_genres(cleaned, limit=limit)
        except requests.RequestException:
            pass

    # If Open Library gave nothing (or only the generic "Fiction"/"Nonfiction"),
    # try mapping Google Books' categories through the same whitelist.
    if (not genres or genres == ["Fiction"] or genres == ["Nonfiction"]) and google_categories:
        google_matches = map_to_known_genres([google_categories], limit=limit)
        if google_matches:
            genres = google_matches

    return genres


OL = "https://openlibrary.org"

# Generic labels that don't help as genres
SKIP_SUBJECTS = {"readers", "media tie-in"}


def get_ol_subjects(isbn):
    """Edition subjects, falling back to the work's subjects via the 'works' key."""
    try:
        resp = requests.get(f"{OL}/isbn/{isbn}.json", timeout=5)
        if not resp.ok:
            return []
        edition = resp.json()
    except (requests.RequestException, ValueError):
        return []

    subjects = edition.get("subjects", [])
    if subjects:
        return subjects

    works = edition.get("works", [])
    work_key = works[0].get("key") if works else None  # e.g. "/works/OL20848685W"
    if not work_key:
        return []

    try:
        resp = requests.get(f"{OL}{work_key}.json", timeout=5)
        if resp.ok:
            return resp.json().get("subjects", [])
    except (requests.RequestException, ValueError):
        pass
    return []


def _ol_subjects_by_title(title, author):
    params = {"title": title, "fields": "subject", "limit": 1}
    if author:
        params["author"] = author
    try:
        resp = requests.get(f"{OL}/search.json", params=params, timeout=5)
        if resp.ok:
            docs = resp.json().get("docs", [])
            return docs[0].get("subject", []) if docs else []
    except (requests.RequestException, ValueError):
        pass
    return []


def _clean_subjects(subjects, cap=8):
    cleaned, seen = [], set()
    for s in subjects:
        s = s.strip()
        if not s or ":" in s:  # drops "collectionID:swOTyr" etc.
            continue
        if " / " in s:  # "JUVENILE FICTION / Action & Adventure" -> "Action & Adventure"
            s = s.split(" / ")[-1]
        s = s.removesuffix(", fiction").strip()
        if s.isupper():
            s = s.title()
        key = s.lower()
        if key in SKIP_SUBJECTS or key in seen or len(s) >= 40:
            continue
        seen.add(key)
        cleaned.append(s)
        if len(cleaned) >= cap:
            break
    return cleaned




def lookup_genres(isbn, title, author):
    """Subjects for the "look up genres" button on a book page."""
    isbn = (isbn or "").strip().replace("-", "")
    subjects = get_ol_subjects(isbn) if isbn else []
    if not subjects and title:
        subjects = _ol_subjects_by_title(title, author)
    return _clean_subjects(subjects)
