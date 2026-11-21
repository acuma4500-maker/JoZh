// OYUN 2 — Birbirimizi Ne Kadar Tanıyoruz?
// Her turda biri "konu" olur ve kendisi hakkında gizlice cevap verir; diğeri tahmin eder.
// İki cevap da taahhüt edildikten (commit–reveal) sonra açılır, konu olan kişi tahmini puanlar.
import { h, clear, shuffle, add } from '../utils/helpers.js';
import { LIMITS, validateText } from '../utils/validation.js';
import { commitSecret, readSecret, dropSecret, verifySecret, otherOf, toArray, resultTitle, scoreLine, winnerByScore, draft, clearDraft } from './common.js';

export const CATEGORIES = [
  { id: 'favoriler', name: 'Favoriler', emoji: '⭐' },
  { id: 'aliskanliklar', name: 'Alışkanlıklar', emoji: '🔁' },
  { id: 'hayaller', name: 'Hayaller', emoji: '🌠' },
  { id: 'iliskimiz', name: 'İlişkimiz', emoji: '💞' },
  { id: 'gunluk', name: 'Günlük yaşam', emoji: '☀️' },
];

export const QUESTIONS = [
  { c: 'favoriler', self: 'En sevdiğin yemek ne?', guess: '{n} en çok hangi yemeği sever?' },
  { c: 'favoriler', self: 'En sevdiğin renk hangisi?', guess: '{n}\'nın en sevdiği renk hangisi?' },
  { c: 'favoriler', self: 'En sevdiğin film hangisi?', guess: '{n}\'nın en sevdiği film hangisi?' },
  { c: 'favoriler', self: 'Şu sıralar en çok dinlediğin şarkı ne?', guess: '{n} şu sıralar en çok hangi şarkıyı dinliyor?' },
  { c: 'favoriler', self: 'En sevdiğin tatlı ne?', guess: '{n}\'nın en sevdiği tatlı ne?' },
  { c: 'favoriler', self: 'En sevdiğin mevsim hangisi?', guess: '{n} en çok hangi mevsimi sever?' },
  { c: 'favoriler', self: 'En sevdiğin çiçek hangisi?', guess: '{n}\'nın en sevdiği çiçek hangisi?' },
  { c: 'favoriler', self: 'En sevdiğin içecek ne?', guess: '{n} en çok ne içmeyi sever?' },
  { c: 'aliskanliklar', self: 'Sabah uyanınca ilk yaptığın şey ne?', guess: '{n} sabah uyanınca ilk ne yapar?' },
  { c: 'aliskanliklar', self: 'Canın sıkılınca ne yaparsın?', guess: '{n} canı sıkılınca ne yapar?' },
  { c: 'aliskanliklar', self: 'Telefonunda en çok vakit geçirdiğin uygulama hangisi?', guess: '{n} telefonda en çok hangi uygulamada vakit geçirir?' },
  { c: 'aliskanliklar', self: 'Stresliyken kendini nasıl rahatlatırsın?', guess: '{n} stresliyken kendini nasıl rahatlatır?' },
  { c: 'aliskanliklar', self: 'Gece kaçta uyumayı seversin?', guess: '{n} genelde kaçta uyumayı sever?' },
  { c: 'aliskanliklar', self: 'Asla vazgeçemediğin küçük bir alışkanlığın ne?', guess: '{n}\'nın asla vazgeçemediği küçük alışkanlığı ne?' },
  { c: 'aliskanliklar', self: 'Hafta sonu en çok ne yapmayı seversin?', guess: '{n} hafta sonları en çok ne yapmayı sever?' },
  { c: 'aliskanliklar', self: 'Çantandan hiç eksik etmediğin şey ne?', guess: '{n}\'nın çantasından hiç eksik olmayan şey ne?' },
  { c: 'hayaller', self: 'En çok gitmek istediğin ülke hangisi?', guess: '{n} en çok hangi ülkeye gitmek ister?' },
  { c: 'hayaller', self: 'Bir gün mutlaka yapmak istediğin şey ne?', guess: '{n}\'nın bir gün mutlaka yapmak istediği şey ne?' },
  { c: 'hayaller', self: 'Hayalindeki ev nerede olurdu?', guess: '{n}\'nın hayalindeki ev nerede?' },
  { c: 'hayaller', self: 'Para sorun olmasaydı hangi işi yapardın?', guess: 'Para sorun olmasaydı {n} hangi işi yapardı?' },
  { c: 'hayaller', self: 'Öğrenmek istediğin bir yetenek ne?', guess: '{n} hangi yeteneği öğrenmek ister?' },
  { c: 'hayaller', self: 'Hayalindeki tatil nasıl olurdu? (tek kelime)', guess: '{n}\'nın hayalindeki tatil? (tek kelime)' },
  { c: 'hayaller', self: 'Bir süper gücün olsa ne olurdu?', guess: '{n}\'nın bir süper gücü olsa ne olurdu?' },
  { c: 'hayaller', self: 'Beş yıl sonra kendini nerede görüyorsun?', guess: '{n} beş yıl sonra kendini nerede görüyor?' },
  { c: 'iliskimiz', self: 'Benimle ilgili ilk dikkatini çeken şey neydi?', guess: '{n}\'nın seninle ilgili ilk dikkatini çeken şey neydi?' },
  { c: 'iliskimiz', self: 'En sevdiğin ortak anımız hangisi?', guess: '{n}\'nın en sevdiği ortak anınız hangisi?' },
  { c: 'iliskimiz', self: 'Sana en çok hangi sözle sevgimi hissettiririm?', guess: '{n} en çok hangi sözle sevildiğini hisseder?' },
  { c: 'iliskimiz', self: 'Birlikte en çok yapmayı sevdiğin şey ne?', guess: '{n} seninle en çok ne yapmayı sever?' },
  { c: 'iliskimiz', self: 'Bana taktığın en sevdiğin lakap ne?', guess: '{n}\'nın sana taktığı en sevdiği lakap ne?' },
  { c: 'iliskimiz', self: 'İlk buluşmamızda en çok neyi hatırlıyorsun?', guess: '{n} ilk buluşmanızdan en çok neyi hatırlıyor?' },
  { c: 'iliskimiz', self: 'Bende en çok sevdiğin huy hangisi?', guess: '{n} sende en çok hangi huyunu seviyor?' },
  { c: 'iliskimiz', self: 'Birlikte gitmek istediğin ilk yer neresi?', guess: '{n} seninle ilk nereye gitmek ister?' },
  { c: 'gunluk', self: 'Kahvaltıda olmazsa olmazın ne?', guess: '{n}\'nın kahvaltıda olmazsa olmazı ne?' },
  { c: 'gunluk', self: 'Günün en sevdiğin saati hangisi?', guess: '{n} günün en çok hangi saatini sever?' },
  { c: 'gunluk', self: 'Seni en çok güldüren şey ne?', guess: '{n}\'yı en çok ne güldürür?' },
  { c: 'gunluk', self: 'Evde en sevdiğin köşe neresi?', guess: '{n} evde en çok nerede oturmayı sever?' },
  { c: 'gunluk', self: 'En sevmediğin ev işi hangisi?', guess: '{n}\'nın en sevmediği ev işi hangisi?' },
  { c: 'gunluk', self: 'Yağmurlu bir günde ne yapmak istersin?', guess: '{n} yağmurlu bir günde ne yapmak ister?' },
  { c: 'gunluk', self: 'Seni en çok sinirlendiren küçük şey ne?', guess: '{n}\'yı en çok sinirlendiren küçük şey ne?' },
  { c: 'gunluk', self: 'Dışarıdan yemek söylesen ne söylersin?', guess: '{n} dışarıdan yemek söylese ne söyler?' },
];

export const ROUNDS = 6;
export const POINTS = { exact: 2, close: 1, miss: 0 };

export function pickQuestions(category, n = ROUNDS) {
  const pool = QUESTIONS.map((q, i) => ({ ...q, i })).filter((q) => category === 'mixed' || q.c === category);
  return shuffle(pool).slice(0, n).map((q) => q.i);
}

export default {
  create({ players, host, prev }) {
    const starter = prev ? otherOf(players, prev.firstSubject) : host;
    return { phase: 'setup', category: prev?.category || 'mixed', qs: [], idx: 0, subject: starter, firstSubject: starter,
      commits: {}, reveals: {}, scores: { [players[0]]: 0, [players[1]]: 0 }, history: [] };
  },

  mount(el, api) {
    const root = h('div', { class: 'knowme' });
    add(el, root);
    const players = () => Object.keys(api.session.players);
    let revealing = false;
    let lastKey = '';

    const start = (cat) => api.act((s, st) => {
      if (st.phase !== 'setup') return undefined;
      st.category = cat; st.qs = pickQuestions(cat); st.idx = 0; st.phase = 'answer'; st.commits = {}; st.reveals = {};
      return s;
    });

    async function submit(text) {
      const st = api.session.state;
      const tag = `km${api.session.round}-${st.idx}`;
      const c = await commitSecret(api.sid, tag, text);
      await api.act((s, cur) => {
        if (cur.phase !== 'answer' || cur.idx !== st.idx || cur.commits?.[api.me]) return undefined;
        cur.commits = { ...(cur.commits || {}), [api.me]: c.hash };
        return s;
      });
    }

    async function autoReveal(s) {
      const st = s.state;
      const tag = `km${s.round}-${st.idx}`;
      if (revealing || st.phase !== 'answer' || !st.commits?.[api.me] || !st.commits?.[api.partner] || st.reveals?.[api.me]) return;
      const secret = readSecret(api.sid, tag);
      if (!secret) return;
      revealing = true;
      await api.act((sess, cur) => {
        if (cur.phase !== 'answer' || cur.idx !== st.idx || cur.reveals?.[api.me]) return undefined;
        cur.reveals = { ...(cur.reveals || {}), [api.me]: { text: secret.text, nonce: secret.nonce } };
        if (cur.reveals[api.partner]) cur.phase = 'judge';
        return sess;
      });
      revealing = false;
    }

    const judge = (kind) => api.act((s, st) => {
      if (st.phase !== 'judge' || st.subject !== api.me) return undefined;
      const guesser = otherOf(players(), api.me);
      const q = QUESTIONS[toArray(st.qs)[st.idx]];
      st.scores[guesser] = (st.scores[guesser] || 0) + POINTS[kind];
      st.history = [...toArray(st.history), { q: q.self, subject: api.me, answer: st.reveals[api.me].text, guess: st.reveals[guesser].text, result: kind }];
      dropSecret(api.sid, `km${s.round}-${st.idx}`);
      st.idx += 1;
      st.commits = {}; st.reveals = {};
      st.subject = guesser;
      if (st.idx >= toArray(st.qs).length) { s.status = 'finished'; s.result = { winner: winnerByScore(st.scores, players()) }; st.phase = 'done'; }
      else st.phase = 'answer';
      return s;
    });

    function renderSetup(st) {
      add(root, h('div', { class: 'card game-panel' },
        h('h3', {}, 'Kategori seçin'),
        h('p', { class: 'muted' }, `${ROUNDS} tur oynanır. Her turda biriniz kendisi hakkında cevap verir, diğeri tahmin eder. Tam bilmek 2, yakın tahmin 1 puan.`),
        h('div', { class: 'chip-row' },
          h('button', { class: 'chip chip--primary', type: 'button', onclick: () => start('mixed') }, '🎲 Karışık'),
          CATEGORIES.map((c) => h('button', { class: 'chip', type: 'button', onclick: () => start(c.id) }, `${c.emoji} ${c.name}`)))));
      void st;
    }

    let retry = null;
    api.scope.add(() => clearTimeout(retry));
    async function render(s) {
      const st = s.state;
      clearTimeout(retry);
      if (st.phase === 'answer' && st.commits?.[api.me] && st.commits?.[api.partner]) retry = setTimeout(() => autoReveal(api.session), 2000);
      clear(root);
      if (st.phase === 'setup') return renderSetup(st);
      const qIdx = toArray(st.qs)[st.idx];
      const q = QUESTIONS[qIdx];
      if (!q) return;
      const iAmSubject = st.subject === api.me;
      const guesser = otherOf(players(), st.subject);
      add(root, h('div', { class: 'round-info' }, `Tur ${st.idx + 1}/${toArray(st.qs).length}`, h('span', { class: 'pill' }, CATEGORIES.find((c) => c.id === q.c)?.name)));
      add(root, h('div', { class: 'score-mini' }, `${api.name(api.me)} ${st.scores[api.me] || 0} · ${api.name(api.partner)} ${st.scores[api.partner] || 0}`));
      const questionText = iAmSubject ? q.self : q.guess.replace('{n}', api.name(st.subject));
      add(root, h('div', { class: 'card question-card pop-in' },
        h('small', { class: 'muted' }, iAmSubject ? 'Kendin hakkında, dürüstçe 🙈' : `${api.name(st.subject)} hakkında tahmin et 🤔`),
        h('h3', { class: 'question-card__text' }, questionText)));

      if (st.phase === 'answer') {
        if (st.commits?.[api.me] && !readSecret(api.sid, `km${s.round}-${st.idx}`) && !st.reveals?.[api.me]) {
          add(root, h('div', { class: 'notice notice--warn' }, 'Cevabın bu cihazda bulunamadı (başka cihazdan cevaplamış olabilirsin).'),
            h('button', { class: 'btn btn--primary', type: 'button', onclick: () => api.act((sess, cur) => {
              if (cur.phase !== 'answer' || cur.idx !== st.idx || cur.reveals?.[api.me]) return undefined;
              const c = { ...(cur.commits || {}) }; delete c[api.me]; cur.commits = c; return sess;
            }) }, 'Yeniden cevapla'));
        } else if (st.commits?.[api.me]) {
          add(root, h('div', { class: 'notice notice--ok' }, '🔒 Cevabın gizlice kaydedildi.'),
            h('p', { class: 'muted center' }, st.commits?.[api.partner] ? 'Cevaplar açılıyor…' : `${api.name(api.partner)} cevaplıyor…`));
        } else {
          const dkey = `km-${s.round}-${st.idx}`;
          const input = draft(dkey, h('input', { class: 'input', placeholder: iAmSubject ? 'Senin cevabın' : 'Tahminin', maxlength: '200', 'aria-label': 'Cevap' }));
          const err = h('p', { class: 'form-error', role: 'alert' });
          add(root, h('form', { class: 'answer-form', onsubmit: (e) => {
            e.preventDefault();
            const v = validateText(input.value, { label: 'Cevap', max: 200, multiline: false });
            if (!v.ok) { err.textContent = v.error; return; }
            input.disabled = true;
            clearDraft(dkey);
            submit(v.value);
          } }, input, h('button', { class: 'btn btn--primary', type: 'submit' }, 'Gizlice gönder'), err),
          h('p', { class: 'muted small center' }, st.commits?.[api.partner] ? `${api.name(api.partner)} cevabını verdi ✔` : `${api.name(api.partner)} henüz cevaplamadı`));
        }
        autoReveal(s);
        return;
      }

      if (st.phase === 'judge') {
        const ans = st.reveals[st.subject], gss = st.reveals[guesser];
        const [okA, okG] = await Promise.all([verifySecret(ans, st.commits[st.subject]), verifySecret(gss, st.commits[guesser])]);
        if (lastKey !== `${s.round}-${st.idx}-judge`) return;
        add(root, h('div', { class: 'reveal-grid' },
          h('div', { class: 'card reveal-card' }, h('small', {}, `${api.name(st.subject)}'nın cevabı`), h('strong', {}, ans.text), okA ? null : h('small', { class: 'text-danger' }, '⚠️ doğrulanamadı')),
          h('div', { class: 'card reveal-card' }, h('small', {}, `${api.name(guesser)}'nın tahmini`), h('strong', {}, gss.text), okG ? null : h('small', { class: 'text-danger' }, '⚠️ doğrulanamadı'))));
        if (iAmSubject) {
          add(root, h('p', { class: 'center' }, 'Sence bildi mi?'), h('div', { class: 'row row--center' },
            h('button', { class: 'btn btn--primary', type: 'button', onclick: () => judge('exact') }, '✅ Bildi (+2)'),
            h('button', { class: 'btn btn--soft', type: 'button', onclick: () => judge('close') }, '🤏 Yakın (+1)'),
            h('button', { class: 'btn btn--ghost', type: 'button', onclick: () => judge('miss') }, '❌ Bilemedi')));
        } else add(root, h('p', { class: 'muted center' }, `${api.name(st.subject)} puanlıyor…`));
      }
    }

    return {
      update(s) {
        lastKey = `${s.round}-${s.state.idx}-${s.state.phase}`;
        render(s);
      },
    };
  },

  summary(s, api) {
    const st = s.state;
    const per = Math.max(1, Math.ceil(toArray(st.qs).length / 2)) * POINTS.exact;
    const pct = (u) => Math.round(((st.scores?.[u] || 0) / per) * 100);
    return h('div', {}, resultTitle(api, s.result?.winner), scoreLine(api, st.scores),
      h('p', {}, `Sen ${api.name(api.partner)}'yı %${pct(api.me)} tanıyorsun, ${api.name(api.partner)} seni %${pct(api.partner)} tanıyor 💞`),
      h('details', { class: 'history' }, h('summary', {}, 'Tüm cevaplar'),
        toArray(st.history).map((x) => h('p', { class: 'small' }, `• ${x.q} — ${api.name(x.subject)}: "${x.answer}" / tahmin: "${x.guess}" ${x.result === 'exact' ? '✅' : x.result === 'close' ? '🤏' : '❌'}`))));
  },
};
