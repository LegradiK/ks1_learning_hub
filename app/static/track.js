/* ============================================================
   Study tracking — feeds the 📊 My progress page.

   On a game page (body has data-game="math_drill" etc.) this counts
   seconds while the tab is visible AND the child has touched, typed
   or moved the mouse in the last 90 seconds, so a game left open on
   the sofa doesn't count as study. Time is sent every 30 seconds and
   when the page is left.

   Games call these when something happens:
     hubTrack.answer(true / false)   a question answered right / wrong
     hubTrack.win()                  a puzzle finished (crossword, sudoku…)
   ============================================================ */
(() => {
  const game = document.body.dataset.game;
  const IDLE_AFTER = 90;      // seconds without input before the clock pauses
  const SEND_EVERY = 30;

  function send(payload) {
    if (!game) return;
    try {
      fetch('/api/track', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.assign({ game }, payload)),
        keepalive: true,          // still delivered when the page is closing
        credentials: 'same-origin',
      }).catch(() => {});
    } catch (e) { /* tracking must never break a game */ }
  }

  window.hubTrack = {
    answer(correct) { send({ result: correct ? 'right' : 'wrong' }); },
    win()           { send({ result: 'win' }); },
  };

  if (!game) return;

  let lastInput = Date.now();
  let pending = 0;
  ['pointerdown', 'keydown', 'mousemove', 'touchstart', 'scroll', 'wheel']
    .forEach(ev => window.addEventListener(ev, () => { lastInput = Date.now(); },
                                           { passive: true, capture: true }));

  function flush() {
    if (pending > 0) { send({ seconds: pending }); pending = 0; }
  }

  setInterval(() => {
    const visible = document.visibilityState === 'visible';
    const awake = (Date.now() - lastInput) / 1000 < IDLE_AFTER;
    if (visible && awake) pending++;
    if (pending >= SEND_EVERY) flush();
  }, 1000);

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') flush();
  });
  window.addEventListener('pagehide', flush);
})();
