/* ============================================================
   MY BOOKSHELF — search & add, tidy (bulk remove), genre lookup.
   Each part only runs if its elements are on the page.
   ============================================================ */

const esc = s => String(s ?? "").replace(/[&<>"']/g,
  c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

function postForm(action, fields) {
  const form = document.createElement("form");
  form.method = "post";
  form.action = action;
  for (const [name, value] of fields) {
    const input = document.createElement("input");
    input.type = "hidden"; input.name = name; input.value = value ?? "";
    form.appendChild(input);
  }
  document.body.appendChild(form);
  form.submit();
}

/* ---------- Find a book (add page) ---------- */
function initFinder() {
  const finder = document.getElementById("finder");
  if (!finder) return;
  const input = document.getElementById("search-input");
  const msg = document.getElementById("search-message");
  const results = document.getElementById("search-results");
  const moreWrap = document.getElementById("load-more-wrap");
  const moreBtn = document.getElementById("load-more-btn");
  const bar = document.getElementById("bulk-add-bar");
  const barCount = document.getElementById("bulk-add-count");
  const ticked = new Set();
  const byId = new Map();
  let timer = null, controller = null, query = "", start = 0, total = 0;

  const status = () => document.querySelector("input[name=pick-status]:checked")?.value || "want_to_read";
  const plain = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "");

  input.addEventListener("input", () => {
    clearTimeout(timer);
    const q = plain(input.value.trim());
    if (q.length < 2) { results.innerHTML = ""; moreWrap.hidden = true; msg.textContent = ""; return; }
    msg.textContent = "Looking… 🔎";
    timer = setTimeout(() => run(q, true), 600);
  });

  moreBtn.addEventListener("click", () => {
    moreBtn.disabled = true; moreBtn.textContent = "Loading…";
    run(query, false);
  });

  async function run(q, fresh) {
    if (controller) controller.abort();
    controller = new AbortController();
    if (fresh) { query = q; start = 0; }
    try {
      const url = `${finder.dataset.searchUrl}?q=${encodeURIComponent(query)}&start=${start}`;
      const res = await fetch(url, { signal: controller.signal });
      const data = await res.json();
      if (data.error) { msg.textContent = data.error; return; }
      const items = data.items || [];
      total = data.total_items || 0;
      if (fresh) results.innerHTML = "";
      if (fresh && !items.length) {
        msg.textContent = "No books found — check the spelling and try again.";
        moreWrap.hidden = true;
        return;
      }
      items.forEach(b => byId.set(b.google_books_id, b));
      results.insertAdjacentHTML("beforeend", items.map(card).join(""));
      start += items.length;
      msg.textContent = `Found ${total} book${total === 1 ? "" : "s"} — tap ＋ Add, or tick a few and add them together.`;
      moreWrap.hidden = start >= total || !items.length;
    } catch (err) {
      if (err.name !== "AbortError") msg.textContent = "Something went wrong — try again.";
    } finally {
      moreBtn.disabled = false; moreBtn.textContent = "Show more books";
    }
  }

  function card(b) {
    const id = esc(b.google_books_id);
    const cover = (b.cover_url
      ? `<img src="${esc(b.cover_url)}" alt="" loading="lazy" referrerpolicy="no-referrer"
              onerror="this.parentElement.classList.add('no-img'); this.remove();">` : "")
      + `<span class="bk-cover-letter" aria-hidden="true">${esc((b.title || "?")[0])}</span>`;
    const action = b.on_shelf
      ? `<span class="bk-status bk-status-finished">On my shelf ✓</span>`
      : `<button type="button" class="jelly-btn bk-add-btn" data-add="${id}">＋ Add</button>`;
    return `
      <div class="bk-card ${b.on_shelf ? "is-mine" : ""}">
        ${b.on_shelf ? "" : `<label class="bk-select is-on" title="Tick to add">
          <input type="checkbox" class="result-select" data-id="${id}" ${ticked.has(b.google_books_id) ? "checked" : ""}
                 aria-label="Tick ${esc(b.title)}"></label>`}
        <div class="bk-cover ${b.cover_url ? "" : "no-img"}">${cover}</div>
        <p class="bk-title">${esc(b.title)}</p>
        <p class="bk-author">${esc(b.author)}${b.year ? ` · ${esc(b.year)}` : ""}</p>
        ${action}
      </div>`;
  }

  results.addEventListener("click", e => {
    const btn = e.target.closest("[data-add]");
    if (!btn) return;
    const b = byId.get(btn.dataset.add);
    btn.disabled = true; btn.textContent = "Adding…";
    postForm(finder.dataset.addUrl, [
      ["google_books_id", b.google_books_id], ["title", b.title], ["author", b.author],
      ["cover_url", b.cover_url], ["isbn", b.isbn], ["categories", b.categories], ["status", status()],
    ]);
  });

  results.addEventListener("change", e => {
    if (!e.target.classList.contains("result-select")) return;
    e.target.checked ? ticked.add(e.target.dataset.id) : ticked.delete(e.target.dataset.id);
    bar.hidden = ticked.size === 0;
    barCount.textContent = `${ticked.size} ticked`;
  });

  document.getElementById("bulk-add-btn").addEventListener("click", e => {
    e.target.disabled = true; e.target.textContent = "Adding…";
    postForm(finder.dataset.addManyUrl,
             [...[...ticked].map(id => ["google_books_id", id]), ["status", status()]]);
  });
}

/* ---------- Tidy my shelf (select + remove) ---------- */
function initTidy() {
  const toggle = document.getElementById("tidy-toggle");
  const grid = document.getElementById("book-grid");
  if (!toggle || !grid) return;
  const bar = document.getElementById("bulk-bar");
  const count = document.getElementById("bulk-count");
  const form = document.getElementById("bulk-delete-form");
  const chosen = new Set();

  toggle.addEventListener("click", () => {
    const on = grid.classList.toggle("is-tidying");
    toggle.setAttribute("aria-pressed", on);
    toggle.textContent = on ? "✓ Done tidying" : "🧹 Tidy my shelf";
    if (!on) {
      chosen.clear();
      grid.querySelectorAll(".book-select").forEach(cb => { cb.checked = false; });
      update();
    }
  });

  // While tidying, tapping a card ticks it instead of opening the book
  grid.addEventListener("click", e => {
    if (!grid.classList.contains("is-tidying")) return;
    const link = e.target.closest(".bk-card-link");
    if (!link) return;
    e.preventDefault();
    const cb = link.parentElement.querySelector(".book-select");
    cb.checked = !cb.checked;
    cb.dispatchEvent(new Event("change", { bubbles: true }));
  });

  grid.addEventListener("change", e => {
    if (!e.target.classList.contains("book-select")) return;
    e.target.checked ? chosen.add(e.target.dataset.id) : chosen.delete(e.target.dataset.id);
    e.target.closest(".bk-card").classList.toggle("is-picked", e.target.checked);
    update();
  });

  function update() {
    bar.hidden = chosen.size === 0;
    count.textContent = `${chosen.size} selected`;
    grid.querySelectorAll(".bk-card").forEach(c =>
      c.classList.toggle("is-picked", c.querySelector(".book-select")?.checked));
  }

  document.getElementById("bulk-delete-btn").addEventListener("click", () => {
    if (!chosen.size) return;
    if (!confirm(`Take ${chosen.size} book${chosen.size === 1 ? "" : "s"} off your shelf?`)) return;
    form.innerHTML = "";
    chosen.forEach(id => {
      const i = document.createElement("input");
      i.type = "hidden"; i.name = "book_id"; i.value = id;
      form.appendChild(i);
    });
    form.submit();
  });
}

/* ---------- Book page: edit / look up genres ---------- */
function toggleGenreEdit() {
  const view = document.getElementById("genre-view");
  const edit = document.getElementById("genre-edit");
  view.hidden = !view.hidden;
  edit.hidden = !edit.hidden;
  if (!edit.hidden) document.getElementById("genre-input").focus();
}

function initGenreLookup() {
  const btn = document.getElementById("fetch-genres-btn");
  if (!btn) return;
  const status = document.getElementById("genre-fetch-status");
  const input = document.getElementById("genre-input");
  const say = text => { status.textContent = text; setTimeout(() => { status.textContent = ""; }, 3000); };

  btn.addEventListener("click", async () => {
    btn.disabled = true;
    status.textContent = "Looking…";
    try {
      const params = new URLSearchParams({ isbn: btn.dataset.isbn, title: btn.dataset.title, author: btn.dataset.author });
      const res = await fetch(`${btn.dataset.url}?${params}`);
      if (!res.ok) throw new Error(res.status);
      const { genres = [] } = await res.json();
      const have = input.value.split(",").map(s => s.trim()).filter(Boolean);
      const seen = new Set(have.map(s => s.toLowerCase()));
      const fresh = genres.map(s => s.trim()).filter(s => s && !seen.has(s.toLowerCase()) && seen.add(s.toLowerCase()));
      if (!fresh.length) return say(genres.length ? "No new genres found." : "No genres found.");
      status.textContent = "";
      if (confirm(`Add these genres: ${fresh.join(", ")}?`)) {
        input.value = [...have, ...fresh].join(", ");
        input.form.submit();
      }
    } catch (e) {
      say("Couldn't look that up — try again.");
    } finally {
      btn.disabled = false;
    }
  });
}

initFinder();
initTidy();
initGenreLookup();
