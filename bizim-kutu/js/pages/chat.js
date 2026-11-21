// Gerçek zamanlı sohbet (Realtime Database).
import { getState, subscribe, serverNow } from '../state.js';
import { userName, userEmoji } from '../constants.js';
import { h, clear, debounce, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, emojiPicker, errorMessage } from '../utils/ui.js';
import { dayKey, dayLabel, formatTime, lastSeenText } from '../utils/dates.js';
import { LIMITS } from '../utils/validation.js';
import { subscribeMessages, loadOlderMessages, sendMessage, deleteMessage, setTyping, subscribeTyping, markReceipt, messageStatus, TYPING_STALE_MS } from '../services/realtime.js';

const PAGE = 40;

export default async function chat(page, { scope }) {
  const { uid, partnerUid } = getState();
  const msgs = new Map();      // id → mesaj
  const nodes = new Map();     // id → DOM
  const pending = new Set();   // sunucu onayı bekleyenler
  let oldestKey = null, hasMore = true, loadingOlder = false, initial = true;

  // ---- Üst bilgi ----
  const statusLine = h('small', { class: 'chat-head__status' });
  const head = h('div', { class: 'chat-head' },
    h('span', { class: 'chat-head__avatar', 'aria-hidden': 'true' }, userEmoji(partnerUid)),
    h('div', {}, h('strong', {}, userName(partnerUid)), statusLine));

  let partnerTyping = null;
  const drawStatus = () => {
    const s = getState();
    const p = s.presence[partnerUid];
    if (!s.connected) { statusLine.textContent = 'Bağlanıyor…'; statusLine.className = 'chat-head__status'; return; }
    if (partnerTyping?.typing && serverNow() - (partnerTyping.ts || 0) < TYPING_STALE_MS) { statusLine.textContent = 'yazıyor…'; statusLine.className = 'chat-head__status is-typing'; return; }
    statusLine.className = 'chat-head__status';
    statusLine.textContent = p?.online ? 'Çevrim içi' : lastSeenText(p?.lastSeen);
  };
  scope.add(subscribe(drawStatus, ['presence', 'connected']));
  scope.add(subscribeTyping(partnerUid, (v) => { partnerTyping = v; drawStatus(); }));
  scope.interval(drawStatus, 1000); // eskiyen 'yazıyor' sinyali en geç 1 sn'de kalksın
  drawStatus();

  // ---- Liste ----
  const list = h('div', { class: 'chat-list', role: 'log', 'aria-live': 'polite', 'aria-label': 'Mesajlar' });
  const olderBtn = h('button', { class: 'btn btn--ghost btn--sm chat-older', type: 'button', hidden: true, onclick: () => loadOlder() }, 'Daha eski mesajlar');
  const scroller = h('div', { class: 'chat-scroll' }, olderBtn, list);
  const newPill = h('button', { class: 'new-pill', type: 'button', hidden: true, onclick: () => scrollBottom(true) }, 'Yeni mesaj ↓');
  const empty = emptyState({ emoji: '💌', title: 'Sohbetiniz burada başlıyor', text: 'İlk mesajı yaz, kutunuz sıcacık olsun.' });

  const nearBottom = () => scroller.scrollHeight - scroller.scrollTop - scroller.clientHeight < 80;
  function scrollBottom(smooth) {
    scroller.scrollTo({ top: scroller.scrollHeight, behavior: smooth ? 'smooth' : 'auto' });
    newPill.hidden = true;
  }

  function statusIcon(m) {
    if (m.uid !== uid) return null;
    const st = pending.has(m.id) ? 'pending' : messageStatus(m, getState().receipts[partnerUid]);
    const label = { pending: 'Gönderiliyor', sent: 'İletildi', delivered: 'Cihazına ulaştı', read: 'Görüldü' }[st];
    return h('span', { class: `tick tick--${st}`, title: label, 'aria-label': label, svg: st === 'pending' ? icons.clock : st === 'sent' ? icons.check : icons.checks });
  }

  function bubble(m) {
    const mine = m.uid === uid;
    const el = h('div', { class: `msg ${mine ? 'msg--me' : 'msg--them'}${m.deleted ? ' msg--deleted' : ''}`, dataset: { id: m.id } },
      h('div', { class: 'msg__bubble', tabindex: mine && !m.deleted ? '0' : undefined, role: mine && !m.deleted ? 'button' : undefined, 'aria-label': mine && !m.deleted ? 'Mesaj seçenekleri' : undefined },
        h('span', { class: 'sr-only' }, `${userName(m.uid)}: `),
        h('span', { class: 'msg__text' }, m.deleted ? 'Bu mesaj silindi' : m.text),
        h('span', { class: 'msg__meta' }, h('time', {}, typeof m.ts === 'number' ? formatTime(m.ts) : ''), m.deleted ? null : statusIcon(m))));
    if (mine && !m.deleted) {
      const b = el.firstChild;
      b.addEventListener('click', () => msgMenu(m));
      b.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); msgMenu(m); } });
    }
    return el;
  }

  function render() {
    const sorted = [...msgs.values()].sort((a, b) => (a.id < b.id ? -1 : 1));
    const frag = document.createDocumentFragment();
    let lastDay = null, lastUid = null;
    for (const m of sorted) {
      const ts = typeof m.ts === 'number' ? m.ts : Date.now();
      const k = dayKey(ts);
      if (k !== lastDay) { add(frag, h('div', { class: 'day-sep' }, h('span', {}, dayLabel(ts)))); lastDay = k; lastUid = null; }
      let n = nodes.get(m.id);
      if (!n || n.dataset.v !== version(m)) { n = bubble(m); n.dataset.v = version(m); nodes.set(m.id, n); }
      n.classList.toggle('msg--cont', lastUid === m.uid);
      lastUid = m.uid;
      add(frag, n);
    }
    fill(list, frag);
    empty.hidden = sorted.length > 0;
    olderBtn.hidden = !hasMore || sorted.length < PAGE;
    oldestKey = sorted[0]?.id || null;
  }
  const version = (m) => `${m.text}|${m.deleted ? 1 : 0}|${typeof m.ts === 'number' ? m.ts : 'p'}|${m.uid === uid ? (pending.has(m.id) ? 'pending' : messageStatus(m, getState().receipts[partnerUid])) : ''}`;
  const renderSoon = (() => { let raf = 0; return () => { if (!raf) raf = requestAnimationFrame(() => { raf = 0; const stick = nearBottom(); render(); if (stick || initial) scrollBottom(false); }); }; })();

  function markRead() {
    if (document.visibilityState !== 'visible' || !nearBottom()) return;
    let latest = 0;
    for (const m of msgs.values()) if (m.uid === partnerUid && typeof m.ts === 'number' && m.ts > latest) latest = m.ts;
    if (latest) markReceipt(uid, 'readAt', latest);
  }
  const markReadSoon = debounce(markRead, 300);

  scope.add(subscribeMessages({
    onAdd: (m) => {
      const isNew = !initial;
      msgs.set(m.id, m);
      const stick = nearBottom();
      renderSoon();
      if (isNew && m.uid !== uid && !stick) newPill.hidden = false;
      if (isNew && m.uid === uid) requestAnimationFrame(() => scrollBottom(true));
      markReadSoon();
    },
    onChange: (m) => { msgs.set(m.id, m); renderSoon(); },
    onRemove: (id) => { msgs.delete(id); nodes.delete(id); renderSoon(); },
    onError: (e) => toast(errorMessage(e), { type: 'error' }),
  }, PAGE));
  scope.timeout(() => { initial = false; markRead(); }, 600);
  scope.add(subscribe(() => renderSoon(), ['receipts']));
  scope.on(scroller, 'scroll', () => {
    if (nearBottom()) { newPill.hidden = true; markReadSoon(); }
    if (scroller.scrollTop < 40 && hasMore && !loadingOlder && msgs.size >= PAGE) loadOlder();
  }, { passive: true });
  scope.on(document, 'visibilitychange', markReadSoon);
  // Klavye açılıp kapanınca (alan küçülüp büyüyünce) en alttaysa en alta yapışık kal.
  let stuck = true;
  scope.on(scroller, 'scroll', () => { stuck = nearBottom(); }, { passive: true });
  if ('ResizeObserver' in window) {
    const ro = new ResizeObserver(() => { if (stuck) scroller.scrollTop = scroller.scrollHeight; });
    ro.observe(scroller);
    scope.add(() => ro.disconnect());
  }

  async function loadOlder() {
    if (!oldestKey || loadingOlder) return;
    loadingOlder = true;
    olderBtn.textContent = 'Yükleniyor…';
    try {
      const prevH = scroller.scrollHeight;
      const older = await loadOlderMessages(oldestKey, PAGE);
      if (older.length < PAGE) hasMore = false;
      older.forEach((m) => msgs.set(m.id, m));
      render();
      scroller.scrollTop = scroller.scrollHeight - prevH;
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
    finally { loadingOlder = false; olderBtn.textContent = 'Daha eski mesajlar'; }
  }

  async function msgMenu(m) {
    const modal = openModal({
      title: 'Mesaj', content: h('div', { class: 'action-list' },
        h('p', { class: 'action-list__preview' }, m.text),
        h('button', { class: 'action', type: 'button', onclick: async () => { modal.close(); try { await navigator.clipboard.writeText(m.text); toast('Kopyalandı'); } catch { toast('Kopyalanamadı', { type: 'error' }); } } }, h('span', { svg: icons.edit }), 'Kopyala'),
        h('button', { class: 'action action--danger', type: 'button', onclick: async () => {
          modal.close();
          if (!(await confirmDialog({ title: 'Mesaj silinsin mi?', message: 'Mesaj iki taraf için de "Bu mesaj silindi" olarak görünecek.', confirmText: 'Sil', danger: true }))) return;
          try { await deleteMessage(m.id); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
        } }, h('span', { svg: icons.trash }), 'Herkesten sil'))
    });
  }

  // ---- Yazma alanı ----
  const input = h('textarea', { class: 'composer__input', rows: '1', placeholder: 'Bir şeyler yaz…', 'aria-label': 'Mesaj', maxlength: String(LIMITS.message), enterkeyhint: 'send' });
  const sendBtn = h('button', { class: 'composer__send', type: 'submit', 'aria-label': 'Gönder', svg: icons.send, disabled: true });
  const emojiPanel = h('div', { class: 'composer__emoji', hidden: true }, emojiPicker((e) => {
    const { selectionStart: a = input.value.length, selectionEnd: b = input.value.length } = input;
    input.value = input.value.slice(0, a) + e + input.value.slice(b);
    input.selectionStart = input.selectionEnd = a + e.length;
    input.dispatchEvent(new Event('input'));
    input.focus();
  }));
  const emojiBtn = h('button', { class: 'composer__btn', type: 'button', 'aria-label': 'Emoji', 'aria-expanded': 'false', svg: icons.smile, onclick: () => {
    emojiPanel.hidden = !emojiPanel.hidden; emojiBtn.setAttribute('aria-expanded', String(!emojiPanel.hidden));
  } });
  // Son tuştan 6 sn sonra yazma bitti sayılır (düşünürken/öneri seçerken gösterge kaybolmasın)
  const stopTyping = debounce(() => setTyping(uid, false), 6000);
  const activity = () => { if (input.value.trim()) { setTyping(uid, true); stopTyping(); } };
  const autosize = () => { input.style.height = 'auto'; input.style.height = `${Math.min(input.scrollHeight, 140)}px`; };
  input.addEventListener('input', () => {
    autosize();
    sendBtn.disabled = !input.value.trim();
    if (input.value.trim()) activity(); else { stopTyping.cancel(); setTyping(uid, false); }
  });
  // iPhone klavyesi: öneri seçme/tuş olayları da 'yazıyor' sayılır
  ['keydown', 'compositionupdate', 'compositionend'].forEach((ev) => input.addEventListener(ev, () => setTimeout(activity, 0)));
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey && !e.isComposing && matchMedia('(hover: hover)').matches) { e.preventDefault(); form.requestSubmit(); }
  });
  const form = h('form', { class: 'composer', onsubmit: (e) => {
    e.preventDefault();
    const text = input.value;
    if (!text.trim()) return;
    if (text.length > LIMITS.message) { toast(`Mesaj en fazla ${LIMITS.message} karakter olabilir.`, { type: 'error' }); return; }
    try {
      const { id, done } = sendMessage(uid, text);
      pending.add(id);
      done.then(() => { pending.delete(id); nodes.delete(id); renderSoon(); })
        .catch((err) => { pending.delete(id); msgs.delete(id); nodes.delete(id); renderSoon(); toast(errorMessage(err), { type: 'error' }); });
      input.value = ''; autosize(); sendBtn.disabled = true; emojiPanel.hidden = true;
      stopTyping.cancel(); setTyping(uid, false);
      input.focus();
    } catch (err) { toast(err.message, { type: 'error' }); }
  } }, emojiBtn, input, sendBtn);

  scope.add(() => { stopTyping.cancel(); setTyping(uid, false); });
  page.classList.add('chat-page');
  add(page, head, h('div', { class: 'chat-body' }, scroller, empty, newPill), emojiPanel, form);
  empty.hidden = true;
  scope.timeout(() => { if (!msgs.size) empty.hidden = false; }, 1500);
  input.focus({ preventScroll: true });
}
