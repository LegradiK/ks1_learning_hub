/* ============================================================
   Shared speech for every game: Puter neural voice (Amy / Brian),
   falling back to the browser's built-in voice.
   Same code as the SPEECH section of script.js — pages that don't
   load script.js (it starts Word Wizard on load) include this instead.

   Needs <script src="https://js.puter.com/v2/"> (already in base.html).
   ============================================================ */

// ==================== SPEECH ====================
let activeVoice = 'Amy';
let puterReady = false;   // true once we've seen Puter is signed in

function switchVoices(event, gender) {
    document.querySelectorAll('.speech-voice-btn').forEach(btn => btn.classList.remove('active'));
    event.target.closest('.speech-voice-btn').classList.add('active');
    activeVoice = gender === 'man' ? 'Brian' : 'Amy';
}

async function initPuter() {
    // Uses the Puter account signed in at login. No guest accounts: if Puter
    // isn't signed in, fall back to the browser voice and let the
    // "Turn on voices" button in the top bar sign in again.
    if (puterReady) return true;
    if (!(window.puter && puter.ai && typeof puter.ai.txt2speech === 'function')) return false;
    puterReady = puter.auth.isSignedIn();
    if (!puterReady) {
        const btn = document.getElementById('puter-btn');
        if (btn) btn.hidden = false;
    }
    return puterReady;
}

async function speak(text, onEnd) {
    const usePuter = await initPuter();   // one-time on first click, instant afterwards

    if (usePuter) {
        puter.ai.txt2speech(text, { voice: activeVoice, engine: 'neural', language: 'en-GB' })
            .then((audio) => {
                if (onEnd) audio.onended = onEnd;
                console.log("Voice: Puter (" + activeVoice + ")");
                return audio.play();
            })
            .catch((err) => {
                console.error("Puter TTS failed, falling back to browser voice:", err);
                browserSpeak(text, onEnd);
            });
    } else {
        browserSpeak(text, onEnd);
        console.log("Voice: Browser built-in voice");
    }
}

function browserSpeak(text, onEnd) {
    if (!window.speechSynthesis) { if (onEnd) onEnd(); return; }
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.rate = 0.85;
    u.pitch = 1.1;
    u.lang = 'en-GB';

    // Best-effort match to the chosen gender in the fallback voice too
    const voices = window.speechSynthesis.getVoices();
    const wantMale = activeVoice === 'Brian';
    const match =
        voices.find(v => v.lang === 'en-GB' && (wantMale ? /male|daniel|george|ryan/i : /female|hazel|libby|sonia|susan/i).test(v.name)) ||
        voices.find(v => v.lang === 'en-GB');
    if (match) u.voice = match;

    if (onEnd) {
        u.onend = onEnd;
        u.onerror = onEnd;   // don't leave the game stuck if speech errors
    }
    window.speechSynthesis.speak(u);
}

// Promise version for games that read several things in a row.
// Resolves when the speech ends, or after a safety timeout so the game
// never gets stuck if audio is blocked.
function speakAsync(text) {
    return new Promise(resolve => {
        let done = false;
        const finish = () => { if (!done) { done = true; resolve(); } };
        setTimeout(finish, 3000 + text.length * 120);
        speak(text, finish);
    });
}
