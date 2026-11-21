// OYUN 7 — Soru Cevap (400 soru, data/questions.json).
// İkiniz de aynı soruyu gizlice cevaplarsınız (commit–reveal), sonra cevaplar birlikte açılır
// ve Firestore'a (couples/main/qaAnswers) geçmiş olarak kaydedilir.
import { h, clear, add } from '../utils/helpers.js';
import { LIMITS, validateText } from '../utils/validation.js';
import { allQuestions, loadQuestions, pickQuestion } from '../utils/questions-data.js';
import { commitSecret, readSecret, dropSecret, verifySecret, toArray, draft, clearDraft } from './common.js';
import { col, docRef, listen, query, orderBy, limit, countOf } from '../services/firestore.js';
import { runTransaction, serverTimestamp } from '../vendor/firebase.js';
import { db } from '../firebase-config.js';
import { relativeTime } from '../utils/dates.js';

export default {
  async create({ prev }) {
    return { phase: 'pick', category: prev?.category || 'random', qid: 0, text: '', qcat: '', commits: {}, reveals: {}, count: 0, asked: toArray(prev?.asked).slice(-200) };
  },

  mount(el, api) {
    const root = h('div', { class: 'qa' });
    const side = h('aside', { class: 'qa-side card' });
    add(el, h('div', { class: 'qa-layout' }, root, side));
    let all = [], cats = [], answered = new Set(), revealing = false;
    const tag = (s) => `qa${s.round}-${s.state.qid}`;

    // Geçmiş + tamamlanan sayısı
    const countEl = h('strong', {}, '…');
    const histEl = h('div', { class: 'qa-history' });
    add(side, h('h4', {}, 'Tamamlanan sorular'), h('p', { class: 'qa-count' }, countEl, ' / 400'), h('h4', {}, 'Geçmiş cevaplar'), histEl);
    const refreshCount = () => countOf(col('qaAnswers')).then((n) => { countEl.textContent = String(n); }).catch(() => { countEl.textContent = '?'; });
    api.scope.add(listen(query(col('qaAnswers'), orderBy('createdAt', 'desc'), limit(200)), (items) => {
      answered = new Set(items.map((x) => x.qid));
      refreshCount();
      clear(histEl);
      if (!items.length) add(histEl, h('p', { class: 'muted small' }, 'Henüz cevaplanan soru yok.'));
      items.slice(0, 15).forEach((x) => add(histEl, h('details', { class: 'qa-history__item' },
        h('summary', {}, x.question),
        [api.me, api.partner].map((u) => h('p', { class: 'small' }, h('strong', {}, `${api.name(u)}: `), x.answers?.[u] || '—')),
        h('small', { class: 'muted' }, relativeTime(x.createdAt)))));
    }, () => {}));

    const ready = Promise.all([allQuestions(), loadQuestions()]).then(([a, raw]) => { all = a; cats = raw.categories; });

    async function ask(category) {
      await ready;
      const s = api.session;
      const q = pickQuestion(all, category, [...answered, ...toArray(s.state.asked)]);
      await api.act((sess, st) => {
        if (st.phase !== 'pick' && st.phase !== 'reveal') return undefined;
        if (st.phase === 'reveal') st.count = (st.count || 0) + 1;
        st.category = category; st.qid = q.id; st.text = q.text; st.qcat = q.categoryName;
        st.commits = {}; st.reveals = {}; st.phase = 'answer';
        st.asked = [...toArray(st.asked), q.id].slice(-200);
        return sess;
      });
    }

    async function submit(text) {
      const s = api.session;
      const c = await commitSecret(api.sid, tag(s), text);
      await api.act((sess, st) => {
        if (st.phase !== 'answer' || st.qid !== s.state.qid || st.commits?.[api.me]) return undefined;
        st.commits = { ...(st.commits || {}), [api.me]: c.hash };
        return sess;
      });
    }

    async function autoReveal(s) {
      const st = s.state;
      if (revealing || st.phase !== 'answer' || !st.commits?.[api.me] || !st.commits?.[api.partner] || st.reveals?.[api.me]) return;
      const secret = readSecret(api.sid, tag(s));
      if (!secret) return;
      revealing = true;
      await api.act((sess, cur) => {
        if (cur.phase !== 'answer' || cur.qid !== st.qid || cur.reveals?.[api.me]) return undefined;
        cur.reveals = { ...(cur.reveals || {}), [api.me]: { text: secret.text, nonce: secret.nonce } };
        if (cur.reveals[api.partner]) cur.phase = 'reveal';
        return sess;
      });
      revealing = false;
    }

    /** Açılan cevabımı geçmişe kaydet (her kullanıcı yalnızca kendi cevabını yazar). */
    async function persist(s) {
      const st = s.state;
      const mine = st.reveals?.[api.me];
      if (!mine) return;
      const id = `${api.sid}-${st.qid}`;
      try {
        await runTransaction(db, async (tx) => {
          const ref = docRef('qaAnswers', id);
          const snap = await tx.get(ref);
          if (!snap.exists()) tx.set(ref, { qid: st.qid, category: st.category === 'random' ? (all.find((q) => q.id === st.qid)?.category || 'rastgele') : st.category, question: st.text, answers: { [api.me]: mine.text }, sessionId: api.sid, createdBy: api.me, createdAt: serverTimestamp() });
          else if (snap.data().answers?.[api.me] !== mine.text) tx.update(ref, { [`answers.${api.me}`]: mine.text });
        });
        dropSecret(api.sid, tag(s));
      } catch (e) { console.warn('qa kaydı', e); }
    }

    const finish = () => api.act((s, st) => { s.status = 'finished'; s.result = { winner: '' }; st.count = (st.count || 0) + (st.phase === 'reveal' ? 1 : 0); return s; });

    let persisted = '';
    let seq = 0;
    let retry = null;
    api.scope.add(() => clearTimeout(retry));
    async function render(s) {
      const my = ++seq;
      await ready;
      if (my !== seq) return; // daha yeni bir çizim var
      const st = s.state;
      clearTimeout(retry);
      // Güvenlik ağı: iki taraf da taahhüt ettiyse ve açılış takıldıysa tekrar dene
      if (st.phase === 'answer' && st.commits?.[api.me] && st.commits?.[api.partner]) retry = setTimeout(() => autoReveal(api.session), 2000);
      clear(root);
      const catChips = h('div', { class: 'chip-row', role: 'radiogroup', 'aria-label': 'Kategori' },
        h('button', { class: `chip${st.category === 'random' ? ' chip--primary' : ''}`, type: 'button', onclick: () => ask('random') }, '🎲 Karışık (tümü)'),
        cats.map((c) => h('button', { class: `chip${st.category === c.id ? ' chip--primary' : ''}`, type: 'button', onclick: () => ask(c.id) }, `${c.emoji} ${c.name}`)));
      add(root, h('div', { class: 'round-info' }, `Bu oyunda ${st.count || 0} soru`, h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: finish }, 'Bitir')));

      if (st.phase === 'pick') {
        add(root, h('div', { class: 'card game-panel' }, h('h3', {}, 'Bir kategori seçin'), h('p', { class: 'muted' }, 'Seçtiğiniz kategoriden daha önce cevaplamadığınız bir soru gelir.'), catChips));
        return;
      }
      add(root, h('div', { class: 'card question-card pop-in' }, h('small', {}, st.qcat), h('h3', { class: 'question-card__text' }, st.text)));

      if (st.phase === 'answer') {
        if (st.commits?.[api.me] && !readSecret(api.sid, tag(s)) && !st.reveals?.[api.me]) {
          add(root, h('div', { class: 'notice notice--warn' }, 'Cevabın bu cihazda bulunamadı.'),
            h('button', { class: 'btn btn--primary', type: 'button', onclick: () => api.act((sess, cur) => { const c = { ...(cur.commits || {}) }; delete c[api.me]; cur.commits = c; return sess; }) }, 'Yeniden cevapla'));
        } else if (st.commits?.[api.me]) {
          add(root, h('div', { class: 'notice notice--ok' }, '🔒 Cevabın gizlice kaydedildi.'),
            h('p', { class: 'muted center' }, st.commits?.[api.partner] ? 'Cevaplar açılıyor…' : `${api.name(api.partner)} cevaplıyor…`));
          autoReveal(s);
        } else {
          const dkey = `qa-${s.round}-${st.qid}`;
          const ta = draft(dkey, h('textarea', { class: 'input', rows: '3', maxlength: String(LIMITS.answer), placeholder: 'Cevabın… (karşı taraf ikiniz de cevaplayınca görecek)' }));
          add(root, h('form', { class: 'form', onsubmit: (e) => {
            e.preventDefault();
            const v = validateText(ta.value, { label: 'Cevap', max: LIMITS.answer });
            if (!v.ok) return api.toast(v.error, { type: 'error' });
            ta.disabled = true;
            clearDraft(dkey);
            submit(v.value);
          } }, ta, h('div', { class: 'row row--between' },
            h('small', { class: 'muted' }, st.commits?.[api.partner] ? `${api.name(api.partner)} cevapladı ✔` : `${api.name(api.partner)} henüz cevaplamadı`),
            h('button', { class: 'btn btn--primary', type: 'submit' }, 'Gizlice gönder'))));
        }
        return;
      }

      if (st.phase === 'reveal') {
        const [okMe, okP] = await Promise.all([verifySecret(st.reveals?.[api.me], st.commits?.[api.me]), verifySecret(st.reveals?.[api.partner], st.commits?.[api.partner])]);
        if (my !== seq) return;
        add(root, h('div', { class: 'reveal-grid' },
          [[api.me, okMe], [api.partner, okP]].map(([u, ok]) => h('div', { class: 'card reveal-card' },
            h('small', {}, `${api.emoji(u)} ${api.name(u)}`), h('p', {}, st.reveals?.[u]?.text || '—'), ok ? null : h('small', { class: 'text-danger' }, '⚠️ doğrulanamadı')))),
          h('p', { class: 'muted center small' }, 'Sıradaki soru için kategori seçin:'), catChips);
        const key = `${st.qid}-${s.round}`;
        if (persisted !== key) { persisted = key; persist(s); }
      }
    }
    return { update: (s) => render(s) };
  },

  summary(s) {
    return h('div', {}, h('h3', { class: 'result__title' }, 'Güzel sohbetti 💬'), h('p', {}, `Bu oyunda ${s.state.count || 0} soruyu birlikte cevapladınız.`), h('p', { class: 'muted small' }, 'Tüm cevaplar Soru Cevap geçmişinde saklanıyor.'));
  },
};
