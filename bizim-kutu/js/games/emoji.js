// OYUN 4 — Emojiyle Anlat. Anlatıcının seçtiği kelime veritabanına yalnızca karma olarak yazılır;
// tahminler anlatıcının cihazında karşılaştırılır, tur sonunda kelime açıklanır ve doğrulanır.
import { h, clear, shuffle, normalizeGuess, fill, add } from '../utils/helpers.js';
import { validateText } from '../utils/validation.js';
import { commitSecret, readSecret, dropSecret, verifySecret, otherOf, toArray, resultTitle, scoreLine, winnerByScore, draft, clearDraft } from './common.js';

export const WORDS = {
  'Film & Dizi': ['Titanik', 'Aslan Kral', 'Harry Potter', 'Yüzüklerin Efendisi', 'Örümcek Adam', 'Karayip Korsanları', 'Buz Devri', 'Shrek', 'Matrix', 'Avatar', 'Kayıp Balık Nemo', 'Oyuncak Hikayesi', 'Karlar Ülkesi', 'Yıldız Savaşları', 'Jurassic Park'],
  'Yemek': ['Pizza', 'Hamburger', 'Mantı', 'Lahmacun', 'Dondurma', 'Baklava', 'Sushi', 'Menemen', 'Kumpir', 'Waffle', 'Çikolatalı pasta', 'Patlamış mısır', 'Kahvaltı', 'Makarna', 'Kokoreç'],
  'Yer': ['Paris', 'Kapadokya', 'Plaj', 'Sinema', 'Hastane', 'Okul', 'Havalimanı', 'Lunapark', 'Kütüphane', 'Kamp', 'Mısır piramitleri', 'Venedik', 'Kayak merkezi', 'Kafe', 'Uzay'],
  'Hayvan': ['Kedi', 'Köpek', 'Penguen', 'Zürafa', 'Fil', 'Ahtapot', 'Kelebek', 'Tavşan', 'Kaplumbağa', 'Aslan', 'Panda', 'Yunus', 'Arı', 'Baykuş', 'Tilki'],
  'Duygu & Durum': ['Aşık olmak', 'Kıskançlık', 'Uykusuzluk', 'Heyecan', 'Özlem', 'Sürpriz', 'Utanmak', 'Mutluluk', 'Sınav stresi', 'Pazartesi sendromu', 'Tatil havası', 'Açlık', 'Romantik akşam', 'Yağmurda yürümek', 'Doğum günü'],
  'Eylem': ['Dans etmek', 'Yemek yapmak', 'Uyumak', 'Yüzmek', 'Kitap okumak', 'Şarkı söylemek', 'Alışveriş yapmak', 'Fotoğraf çekmek', 'Bisiklete binmek', 'Kamp yapmak', 'Resim yapmak', 'Evlenme teklifi', 'Valiz hazırlamak', 'Bulaşık yıkamak', 'Spor yapmak'],
};
export const EMOJI_PALETTE = ['😀', '😂', '😍', '😭', '😱', '😴', '🤔', '😡', '🥶', '🥵', '🤢', '😇', '👶', '👨', '👩', '👴', '👑', '🧙', '🦸', '🧛', '👻', '🤖', '👽', '💀', '❤️', '💔', '🔥', '💧', '⭐', '🌙', '☀️', '🌧️', '❄️', '🌊', '🌋', '🏔️', '🏝️', '🌳', '🌹', '🍕', '🍔', '🍟', '🍝', '🍣', '🍦', '🍰', '🍫', '🍿', '☕', '🍷', '🥟', '🍳', '🐱', '🐶', '🦁', '🐘', '🦒', '🐧', '🐙', '🦋', '🐝', '🐢', '🐰', '🐼', '🐬', '🦊', '🦉', '🚗', '✈️', '🚀', '🚢', '🚲', '🏠', '🏰', '🏫', '🏥', '⛺', '🎡', '🎬', '🎵', '🎤', '📚', '🎨', '📷', '⚽', '🏊', '💃', '🛍️', '💍', '🎂', '🎁', '🎉', '💤', '⏰', '💰', '🔑', '🧳', '🗼', '🗽', '🛸', '⚡', '🧊', '🍽️', '🧽', '🏋️', '1️⃣', '2️⃣', '3️⃣', '➕', '➖', '❓', '❗', '⬆️', '⬇️', '➡️', '⬅️'];
export const ROUNDS = 6;
export const GUESS_SECONDS = 90;
export const MAX_EMOJI = 12;
export const MAX_GUESSES = 5;

export const isCorrect = (guess, word) => normalizeGuess(guess) !== '' && normalizeGuess(guess) === normalizeGuess(word);

const EMOJI_RE = /\p{Extended_Pictographic}|\p{Regional_Indicator}|[0-9#*]\uFE0F?\u20E3/u;
/** Bir metindeki emojileri (grapheme olarak) ayıklar; harf, rakam ve boşlukları atar. */
export function extractEmojis(text, max = MAX_EMOJI) {
  const s = String(text || '');
  const parts = typeof Intl !== 'undefined' && Intl.Segmenter
    ? [...new Intl.Segmenter('tr', { granularity: 'grapheme' }).segment(s)].map((x) => x.segment)
    : [...s];
  return parts.filter((g) => EMOJI_RE.test(g)).slice(0, max);
}

/** Grapheme bazında emoji sayısı. */
export function countGraphemes(s) {
  if (typeof Intl !== 'undefined' && Intl.Segmenter) return [...new Intl.Segmenter('tr', { granularity: 'grapheme' }).segment(s)].length;
  return [...s].length;
}

export default {
  create({ players, host, prev }) {
    const starter = prev ? otherOf(players, prev.firstTeller) : host;
    return { round: 1, rounds: ROUNDS, teller: starter, firstTeller: starter, phase: 'compose', commit: '', category: '', emojis: '', deadline: 0,
      guesses: [], solved: false, reveal: null, scores: { [players[0]]: 0, [players[1]]: 0 } };
  },

  mount(el, api) {
    const root = h('div', { class: 'emoji-game' });
    add(el, root);
    const players = () => Object.keys(api.session.players);
    const tag = (s) => `em${s.round}-${s.state.round}`;
    let composing = { word: '', category: '', emojis: [] };
    let timer = null;
    let judging = false;
    api.scope.add(() => clearInterval(timer));

    async function sendClue() {
      const s = api.session;
      const word = composing.word.trim();
      if (!word || !composing.emojis.length) return api.toast('Bir kelime seç ve en az bir emoji ekle.', { type: 'error' });
      const c = await commitSecret(api.sid, tag(s), word);
      await api.act((sess, st) => {
        if (st.phase !== 'compose' || st.teller !== api.me) return undefined;
        st.commit = c.hash; st.category = composing.category || 'Serbest'; st.emojis = composing.emojis.join('');
        st.phase = 'guess'; st.deadline = api.serverNow() + GUESS_SECONDS * 1000; st.guesses = []; st.solved = false; st.reveal = null;
        return sess;
      });
      composing = { word: '', category: '', emojis: [] };
    }

    const guess = (text) => api.act((s, st) => {
      if (st.phase !== 'guess' || st.teller === api.me || toArray(st.guesses).length >= MAX_GUESSES) return undefined;
      st.guesses = [...toArray(st.guesses), { text, ok: null }];
      return s;
    });

    /** Anlatıcı cihazı: tahminleri kontrol eder, süre dolunca kelimeyi açıklar. */
    async function tellerDuties(s) {
      const st = s.state;
      if (st.teller !== api.me || st.phase !== 'guess' || judging) return;
      const secret = readSecret(api.sid, tag(s));
      if (!secret) return;
      const guesses = toArray(st.guesses);
      const pendingIdx = guesses.findIndex((g) => g.ok === null || g.ok === undefined);
      const expired = api.serverNow() > st.deadline;
      if (pendingIdx === -1 && !expired && guesses.length < MAX_GUESSES) return;
      judging = true;
      await api.act((sess, cur) => {
        if (cur.phase !== 'guess') return undefined;
        const gs = toArray(cur.guesses).map((g) => (g.ok === null || g.ok === undefined ? { ...g, ok: isCorrect(g.text, secret.text) } : g));
        cur.guesses = gs;
        const solved = gs.some((g) => g.ok);
        if (solved || api.serverNow() > cur.deadline || gs.length >= MAX_GUESSES) finishRound(sess, cur, solved, secret);
        return sess;
      });
      judging = false;
    }

    function finishRound(sess, cur, solved, secret) {
      const guesser = otherOf(players(), cur.teller);
      cur.solved = solved;
      if (solved) { cur.scores[guesser] = (cur.scores[guesser] || 0) + 2; cur.scores[cur.teller] = (cur.scores[cur.teller] || 0) + 1; }
      cur.reveal = { text: secret.text, nonce: secret.nonce };
      cur.phase = 'reveal';
      dropSecret(api.sid, `em${sess.round}-${cur.round}`);
    }

    const acceptManually = () => api.act((sess, cur) => {
      const secret = readSecret(api.sid, tag(sess));
      if (cur.phase !== 'guess' || cur.teller !== api.me || !secret) return undefined;
      const gs = toArray(cur.guesses);
      if (!gs.length) return undefined;
      gs[gs.length - 1] = { ...gs[gs.length - 1], ok: true };
      cur.guesses = gs;
      finishRound(sess, cur, true, secret);
      return sess;
    });

    const nextRound = () => api.act((s, st) => {
      if (st.phase !== 'reveal') return undefined;
      if (st.round >= st.rounds) { s.status = 'finished'; s.result = { winner: winnerByScore(st.scores, players()) }; return s; }
      st.round += 1; st.teller = otherOf(players(), st.teller); st.phase = 'compose';
      st.commit = ''; st.emojis = ''; st.category = ''; st.guesses = []; st.solved = false; st.reveal = null; st.deadline = 0;
      return s;
    });

    function renderCompose(st) {
      const cats = Object.keys(WORDS);
      const wordBox = h('div', { class: 'chip-row' });
      const preview = h('div', { class: 'emoji-preview', 'aria-live': 'polite' });
      const custom = h('input', { class: 'input', placeholder: 'ya da kendi kelimeni yaz (örn. ilk buluşmamız)', maxlength: '60', value: composing.category === 'Serbest' ? composing.word : '' });
      // Klavyeden istediğin emojiyi yaz (telefonun emoji klavyesi); aşağıdaki hazır emojilere de dokunabilirsin
      const emojiInput = h('input', { class: 'input emoji-input', type: 'text', inputmode: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false',
        placeholder: 'Klavyeden emoji yaz 😊🎬🍿', 'aria-label': 'Emojiler', value: composing.emojis.join('') });
      const counter = h('small', { class: 'muted' });
      const drawPreview = () => {
        preview.textContent = composing.emojis.join(' ') || 'Emojilerin burada görünecek';
        counter.textContent = `${composing.emojis.length}/${MAX_EMOJI}`;
      };
      const syncInput = () => { emojiInput.value = composing.emojis.join(''); drawPreview(); };
      let warned = false;
      emojiInput.addEventListener('input', () => {
        const raw = emojiInput.value;
        const list = extractEmojis(raw);
        const dropped = extractEmojis(raw, 999).length > MAX_EMOJI;
        const hadText = raw.replace(/\s/g, '') !== extractEmojis(raw, 999).join('');
        composing.emojis = list;
        if (hadText || dropped) {
          emojiInput.value = list.join('');
          if (!warned) { warned = true; api.toast(dropped ? `En fazla ${MAX_EMOJI} emoji 🙂` : 'Sadece emoji yazabilirsin 🙂'); setTimeout(() => { warned = false; }, 2500); }
        }
        drawPreview();
      });
      custom.addEventListener('input', () => { composing.word = custom.value; composing.category = 'Serbest'; });
      fill(root, 
        h('div', { class: 'round-info' }, `Tur ${st.round}/${st.rounds}`, h('span', { class: 'pill' }, 'Anlatıcı sensin 🎭')),
        h('div', { class: 'card game-panel' },
          h('h4', {}, '1) Bir kelime seç'),
          h('div', { class: 'chip-row' }, cats.map((c) => h('button', { class: `chip chip--soft${composing.category === c ? ' chip--primary' : ''}`, type: 'button', onclick: () => { composing.category = c; suggest(c); } }, c))),
          wordBox, custom,
          composing.word ? h('p', { class: 'small' }, 'Seçilen: ', h('strong', {}, composing.word)) : null,
          h('h4', {}, `2) En fazla ${MAX_EMOJI} emojiyle anlat`), preview,
          h('div', { class: 'emoji-input-row' }, emojiInput, counter),
          h('p', { class: 'muted small' }, 'Telefonunun emoji klavyesinden istediğin emojiyi yazabilir ya da aşağıdakilere dokunabilirsin.'),
          h('div', { class: 'emoji-grid emoji-grid--game' }, EMOJI_PALETTE.map((e) => h('button', { class: 'emoji-grid__item', type: 'button', 'aria-label': e, onclick: () => { if (composing.emojis.length < MAX_EMOJI) { composing.emojis.push(e); syncInput(); } } }, e))),
          h('div', { class: 'row row--center' },
            h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => { composing.emojis.pop(); syncInput(); } }, '⌫ Geri al'),
            h('button', { class: 'btn btn--primary', type: 'button', onclick: sendClue }, 'İpucunu gönder'))));
      if (composing.category && WORDS[composing.category]) suggest(composing.category);
      drawPreview();
    }

    let seq = 0;
    async function render(s) {
      const my = ++seq;
      const st = s.state;
      clearInterval(timer);
      const iTell = st.teller === api.me;
      if (st.phase === 'compose') {
        if (iTell) return renderCompose(st);
        fill(root, h('div', { class: 'round-info' }, `Tur ${st.round}/${st.rounds}`), scoreLine(api, st.scores),
          h('div', { class: 'card center game-panel' }, h('span', { class: 'heart-loader' }, '❤'), h('p', {}, `${api.name(st.teller)} emojilerini seçiyor… 🤫`)));
        return;
      }
      const left = h('span', { class: 'timer' });
      const tick = () => {
        const sec = Math.max(0, Math.ceil((st.deadline - api.serverNow()) / 1000));
        left.textContent = `⏱ ${sec} sn`;
        left.classList.toggle('timer--low', sec <= 10);
        if (sec === 0 && iTell) tellerDuties(api.session);
      };
      const guesses = toArray(st.guesses);
      fill(root, 
        h('div', { class: 'round-info' }, `Tur ${st.round}/${st.rounds}`, st.phase === 'guess' ? left : null),
        scoreLine(api, st.scores),
        h('div', { class: 'card question-card pop-in' }, h('small', {}, `Kategori: ${st.category}`), h('div', { class: 'emoji-clue', 'aria-label': `İpucu: ${st.emojis}` }, st.emojis)),
        guesses.length ? h('ul', { class: 'guess-list' }, guesses.map((g) => h('li', { class: g.ok === true ? 'is-ok' : g.ok === false ? 'is-no' : '' }, `${g.ok === true ? '✅' : g.ok === false ? '❌' : '⏳'} ${g.text}`))) : null);
      if (st.phase === 'guess') {
        tick(); timer = setInterval(tick, 500);
        if (iTell) {
          add(root, h('p', { class: 'muted center' }, `${api.name(api.partner)} tahmin ediyor… Doğru tahmin otomatik algılanır.`),
            guesses.length ? h('div', { class: 'row row--center' }, h('button', { class: 'btn btn--soft btn--sm', type: 'button', onclick: acceptManually }, 'Son tahmini doğru say 👍')) : null);
          tellerDuties(s);
        } else if (guesses.length < MAX_GUESSES) {
          const dkey = `em-${s.round}-${st.round}`;
          const input = draft(dkey, h('input', { class: 'input', placeholder: 'Tahminin…', maxlength: '60', 'aria-label': 'Tahmin' }));
          add(root, h('form', { class: 'answer-form', onsubmit: (e) => {
            e.preventDefault();
            const v = validateText(input.value, { label: 'Tahmin', max: 60, multiline: false });
            if (!v.ok) return;
            input.value = '';
            clearDraft(dkey);
            guess(v.value);
          } }, input, h('button', { class: 'btn btn--primary', type: 'submit' }, 'Tahmin et')),
          h('p', { class: 'muted small center' }, `${MAX_GUESSES - guesses.length} tahmin hakkın kaldı`));
        } else add(root, h('p', { class: 'muted center' }, 'Tahmin hakların bitti, cevap açıklanıyor…'));
        return;
      }
      if (st.phase === 'reveal') {
        const ok = await verifySecret(st.reveal, st.commit);
        if (my !== seq) return;
        add(root, h('div', { class: `notice ${st.solved ? 'notice--ok' : ''}` },
          st.solved ? '🎉 Bildi! ' : '⌛ Bilemedi. ', 'Cevap: ', h('strong', {}, st.reveal?.text || '?'), ok ? '' : ' (⚠️ doğrulanamadı)'),
          h('div', { class: 'row row--center' }, h('button', { class: 'btn btn--primary', type: 'button', onclick: nextRound }, st.round >= st.rounds ? 'Sonuçları gör' : 'Sıradaki tur')));
      }
    }

    return { update: (s) => render(s) };
  },

  summary(s, api) {
    return h('div', {}, resultTitle(api, s.result?.winner), scoreLine(api, s.state.scores), h('p', { class: 'muted small' }, 'Doğru tahmin: tahmin edene +2, anlatana +1'));
  },
};
