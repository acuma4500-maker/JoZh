// OYUN 6 — Birlikte Hikâye. Sırayla cümle eklenir; bitince Firestore'a (couples/main/stories) kaydedilir.
import { h, clear, add } from '../utils/helpers.js';
import { LIMITS, validateText, cleanText } from '../utils/validation.js';
import { otherOf, toArray } from './common.js';
import { docRef } from '../services/firestore.js';
import { setDoc, getDoc, serverTimestamp } from '../vendor/firebase.js';

import { OPENINGS, MAX_LINES, createStory } from './story-data.js';
export { OPENINGS, MAX_LINES };

export default {
  create: createStory,

  mount(el, api) {
    const root = h('div', { class: 'story' });
    add(el, root);
    const players = () => Object.keys(api.session.players);
    let draft = '';

    const addLine = (text) => api.act((s, st) => {
      if (st.turn !== api.me || toArray(st.lines).length >= MAX_LINES) return undefined;
      st.lines = [...toArray(st.lines), { uid: api.me, text }];
      st.turn = otherOf(players(), api.me);
      return s;
    });
    const setTitle = (title) => api.act((s, st) => { st.title = title; return s; });

    async function save() {
      const s = api.session;
      const st = s.state;
      const lines = toArray(st.lines);
      if (lines.length < 2) return api.toast('Kaydetmeden önce en az iki cümle yazın.', { type: 'error' });
      const id = `${api.sid}-${s.round || 1}`;
      const authors = {};
      lines.forEach((l) => { authors[l.uid] = (authors[l.uid] || 0) + 1; });
      const text = cleanText([st.opening, ...lines.map((l) => l.text)].join(' '), LIMITS.storyText);
      try {
        const existing = await getDoc(docRef('stories', id));
        if (!existing.exists()) {
          await setDoc(docRef('stories', id), {
            title: cleanText(st.title || 'Adsız hikâyemiz', LIMITS.storyTitle, { multiline: false }), opening: st.opening, text,
            lines: lines.map((l) => ({ uid: l.uid, text: cleanText(l.text, LIMITS.storyLine) })), authors, sessionId: api.sid,
            createdBy: api.me, createdAt: serverTimestamp(),
          });
        }
        await api.act((sess, cur) => { cur.saved = id; sess.status = 'finished'; sess.result = { winner: '', storyId: id }; return sess; });
        api.toast('Hikâyeniz kaydedildi 📜');
      } catch (e) { api.toast(e?.message || 'Kaydedilemedi', { type: 'error' }); }
    }

    return {
      update(s) {
        const st = s.state;
        const lines = toArray(st.lines);
        const focused = document.activeElement?.classList?.contains('story-input');
        clear(root);
        const titleIn = h('input', { class: 'input story-title', value: st.title || '', placeholder: 'Hikâyemizin adı…', maxlength: String(LIMITS.storyTitle), 'aria-label': 'Hikâye başlığı' });
        titleIn.addEventListener('change', () => { const v = validateText(titleIn.value, { min: 0, max: LIMITS.storyTitle, multiline: false }); if (v.ok) setTitle(v.value); });
        const paper = h('div', { class: 'story-paper' },
          h('p', { class: 'story-line story-line--opening' }, st.opening),
          lines.map((l) => h('p', { class: `story-line ${l.uid === api.me ? 'is-me' : 'is-them'}` }, h('span', { class: 'story-line__who', 'aria-label': api.name(l.uid) }, api.emoji(l.uid)), ' ', l.text)));
        add(root, titleIn, paper, h('p', { class: 'muted small center' }, `${lines.length}/${MAX_LINES} cümle`));
        if (st.turn === api.me && lines.length < MAX_LINES) {
          const ta = h('textarea', { class: 'input story-input', rows: '2', maxlength: String(LIMITS.storyLine), placeholder: 'Sıradaki cümleyi sen yaz…', value: draft });
          ta.addEventListener('input', () => { draft = ta.value; });
          add(root, h('form', { class: 'form', onsubmit: (e) => {
            e.preventDefault();
            const v = validateText(ta.value, { label: 'Cümle', max: LIMITS.storyLine });
            if (!v.ok) return api.toast(v.error, { type: 'error' });
            draft = '';
            addLine(v.value);
          } }, ta, h('button', { class: 'btn btn--primary', type: 'submit' }, 'Cümleyi ekle ✍️')));
          if (focused) requestAnimationFrame(() => ta.focus());
        } else if (lines.length < MAX_LINES) add(root, h('p', { class: 'muted center' }, `${api.name(st.turn)} yazıyor… ✍️`));
        add(root, h('div', { class: 'row row--center' }, h('button', { class: 'btn btn--soft', type: 'button', onclick: save }, '📜 Hikâyeyi tamamla ve kaydet')));
        paper.scrollTop = paper.scrollHeight;
      },
    };
  },

  summary(s) {
    return h('div', {}, h('h3', { class: 'result__title' }, 'Hikâyeniz kaydedildi 📜'),
      h('p', {}, s.state.title || 'Adsız hikâyemiz'),
      h('a', { class: 'btn btn--soft btn--sm', href: '#/stories' }, 'Hikâyelerimize git'));
  },
};
