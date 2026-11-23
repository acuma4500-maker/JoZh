// Özel Kasamız 🔐 — sabit 4 haneli kasa PIN'i ile açılan, şifreli ortak notlar.
// Güvenlik modeli:
//  * Kasa PIN'i kodda YOKTUR; Firestore'daki secrets/pins belgesinin "vault" alanındadır (istemci okuyamaz).
//  * Girilen PIN vaultTry/{cihaz} kaydına yazılır; güvenlik kuralları onu secrets ile karşılaştırır.
//    Eşleşmezse kasa yapılandırması ve notlar OKUNAMAZ (telefon girişli olsa bile).
//  * Deneme sınırı: cihaz başına 10 dakikada en fazla 10 deneme (kurallar zorlar).
//  * Doğru PIN'den sonra sunucu erişimi 15 dakika geçerlidir; ekranda kasa 3 dk hareketsizlikte kilitlenir.
//  * Notlar ayrıca PIN'den türetilen anahtarla (PBKDF2 600.000 tur + AES-GCM) şifrelenir; Firebase
//    Console'da düz metin görünmez. 4 haneli PIN'den türetilen anahtar, güçlü bir parolaya göre zayıftır.
import { getState, serverNow } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, vibrate, sleep, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, field, counted, errorMessage, setLoading, skeletonList } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { LIMITS, validateText, isPin } from '../utils/validation.js';
import { col, docRef, listen, query, orderBy, limit } from '../services/firestore.js';
import { doc, getDoc, getDocs, setDoc, deleteDoc, serverTimestamp, writeBatch } from '../vendor/firebase.js';
import { db, auth } from '../firebase-config.js';
import { createVaultConfig, unlockVault, keyMatches, deriveVaultKey, encryptJSON, decryptJSON } from '../services/crypto.js';

const AUTO_LOCK_MS = 3 * 60 * 1000;
export const VAULT_MAX_TRIES = 10;
export const VAULT_WINDOW_MS = 10 * 60 * 1000;
const configRef = () => docRef('vault', 'config');

// Hız için: kasanın tuzu (gizli değildir) cihazda tutulur; böylece PIN'den anahtar türetme,
// sunucu doğrulamasıyla AYNI ANDA başlayabilir. Anahtarın kendisi ya da PIN hiçbir yere kaydedilmez.
const SALT_KEY = 'bk.vaultSalt';
const readSalt = () => { try { const v = JSON.parse(localStorage.getItem(SALT_KEY) || 'null'); return v?.salt && v?.iterations ? v : null; } catch { return null; } };
const saveSalt = (c) => { try { localStorage.setItem(SALT_KEY, JSON.stringify({ salt: c.salt, iterations: c.iterations })); } catch {} };
const tryRef = () => doc(db, 'vaultTry', auth.currentUser?.uid || '-');

/** Kasa PIN'ini sunucuda doğrular. Döner: { ok, config } | { ok:false, remaining } | { locked, waitMin } */
async function verifyVaultPin(pin, prefetched) {
  const dev = auth.currentUser?.uid;
  if (!dev) throw new Error('Oturum bulunamadı.');
  const ref = doc(db, 'vaultTry', dev);
  const prevSnap = await (prefetched || getDoc(ref)).catch(() => null); // kilit ekranı açılınca önceden okunur
  const prev = prevSnap?.exists() ? prevSnap.data() : null;
  const prevAt = prev?.at?.toMillis?.() || 0;
  const windowOver = serverNow() - prevAt > VAULT_WINDOW_MS + 15000; // küçük saat farkı payı
  let n = !prev ? 1 : windowOver ? 1 : (prev.n || 0) + 1;
  if (n > VAULT_MAX_TRIES) return { locked: true, waitMin: Math.max(1, Math.ceil((prevAt + VAULT_WINDOW_MS - serverNow()) / 60000)) };
  const write = (k) => setDoc(ref, { pin: Number(pin), pinText: pin, n: k, at: serverTimestamp() });
  try { await write(n); }
  catch {
    // Sayaç sıfırlama zamanı henüz gelmemiş olabilir: normal artışla dene
    n = (prev?.n || 0) + 1;
    if (n > VAULT_MAX_TRIES) return { locked: true, waitMin: 10 };
    await write(n);
  }
  try {
    const c = await getDoc(configRef());
    return { ok: true, config: c.exists() ? c.data() : null };
  } catch { return { ok: false, remaining: VAULT_MAX_TRIES - n }; }
}

export default async function vault(page, { scope }) {
  const { uid } = getState();
  let key = null;           // bellekteki anahtar (yalnızca kasa açıkken)
  let notesUnsub = null;
  let idleTimer = null;
  const body = h('div', { class: 'vault' });
  add(page,
    h('div', { class: 'page-head' }, h('div', {}, h('h2', { class: 'page-title' }, 'Özel Kasamız 🔐'), h('p', { class: 'page-sub' }, 'Sadece ikimizin okuyabileceği notlar.'))),
    body);

  const lock = (reason) => {
    key = null;
    notesUnsub?.(); notesUnsub = null;
    clearTimeout(idleTimer);
    if (!scope.disposed) { renderLocked(); if (reason) toast(reason); }
  };
  scope.add(() => { key = null; notesUnsub?.(); clearTimeout(idleTimer); });

  // Hareketsizlikte otomatik kilit
  const resetIdle = () => { if (!key) return; clearTimeout(idleTimer); idleTimer = setTimeout(() => lock('Kasa hareketsizlik nedeniyle kilitlendi 🔒'), AUTO_LOCK_MS); };
  ['pointerdown', 'keydown', 'scroll'].forEach((ev) => scope.on(document, ev, resetIdle, { passive: true }));
  scope.on(document, 'visibilitychange', () => { if (document.visibilityState === 'hidden' && key) lock(); });

  // ---------------- Kilitli: kasa PIN'i ----------------
  function renderLocked() {
    const lockIcon = h('div', { class: 'vault-lock', 'aria-hidden': 'true', svg: icons.lock });
    const msg = h('p', { class: 'auth-hint', 'aria-live': 'polite' }, 'Kasa PIN\'ini gir');
    let prevTry = getDoc(tryRef()).catch(() => null); // PIN yazılırken deneme sayacını önceden oku
    const pad = pinEntry(async (pin) => {
      msg.textContent = 'Kontrol ediliyor…';
      // Anahtar türetme (yavaş kısım) sunucu kontrolüyle paralel başlar
      const cached = readSalt();
      const early = cached ? deriveVaultKey(pin, cached.salt, cached.iterations).catch(() => null) : null;
      try {
        const r = await verifyVaultPin(pin, prevTry);
        prevTry = getDoc(tryRef()).catch(() => null);
        if (r.locked) { msg.textContent = `Çok fazla deneme. ${r.waitMin} dakika sonra tekrar dene.`; vibrate([30, 40, 30]); return false; }
        if (!r.ok) { msg.textContent = r.remaining > 0 ? `PIN hatalı. ${r.remaining} deneme hakkın kaldı.` : 'PIN hatalı. Deneme hakkın bitti, 10 dakika sonra tekrar dene.'; vibrate([30, 40, 30]); return false; }
        msg.textContent = 'Kasa açılıyor…';
        let k;
        if (!r.config) {
          // İlk açılış: kasa bu PIN ile oluşturulur
          const res = await createVaultConfig(pin);
          await setDoc(configRef(), { ...res.config, createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp() });
          k = res.key;
          saveSalt(res.config);
        } else {
          const same = cached && cached.salt === r.config.salt && cached.iterations === r.config.iterations;
          const pre = same ? await early : null;
          k = (pre && await keyMatches(pre, r.config)) || await unlockVault(pin, r.config);
          if (!k) { renderMismatch(pin); return true; }
          saveSalt(r.config);
        }
        lockIcon.innerHTML = icons.unlock; lockIcon.classList.add('is-opening');
        await sleep(200);
        openWith(k);
        return true;
      } catch (e) { msg.textContent = errorMessage(e); return false; }
    });
    fill(body, h('div', { class: 'card vault-locked' }, lockIcon, h('h3', {}, 'Kasa kilitli'), msg, pad,
      h('p', { class: 'muted small' }, 'Kasa 3 dakika işlem yapılmazsa ve uygulamadan çıkınca kilitlenir.')));
  }

  /** Kasa daha önce farklı bir şifreyle kurulmuşsa: sıfırlama seçeneği. */
  function renderMismatch(pin) {
    fill(body, h('div', { class: 'card vault-locked' },
      h('div', { class: 'vault-illu', 'aria-hidden': 'true' }, '🔁'),
      h('h3', {}, 'Kasa farklı bir şifreyle kurulmuş'),
      h('p', { class: 'muted' }, 'Kasa daha önce başka bir parolayla oluşturulmuş; mevcut notlar bu PIN ile açılamıyor. Kasayı bu PIN ile yeniden kurabilirsiniz — eski (açılamayan) notlar silinir.'),
      h('button', { class: 'btn btn--danger btn--block', type: 'button', onclick: async (e) => {
        if (!(await confirmDialog({ title: 'Kasa sıfırlansın mı?', message: 'Eski notlar kalıcı olarak silinecek.', confirmText: 'Sıfırla', danger: true }))) return;
        setLoading(e.currentTarget, true, 'Sıfırlanıyor…');
        try {
          const snap = await getDocs(query(col('vaultNotes'), limit(450)));
          const batch = writeBatch(db);
          snap.docs.forEach((d) => batch.delete(d.ref));
          const res = await createVaultConfig(pin);
          batch.set(configRef(), { ...res.config, updatedBy: uid, updatedAt: serverTimestamp() }, { merge: true });
          await batch.commit();
          saveSalt(res.config);
          toast('Kasa yeni PIN ile kuruldu 🔐');
          openWith(res.key);
        } catch (e2) { toast(errorMessage(e2), { type: 'error' }); renderLocked(); }
      } }, 'Kasayı bu PIN ile yeniden kur'),
      h('button', { class: 'btn btn--ghost btn--block', type: 'button', onclick: () => renderLocked() }, 'Vazgeç')));
  }

  function openWith(k) {
    key = k;
    resetIdle();
    renderOpen();
  }

  function renderOpen() {
    const list = h('div', { class: 'card-list' }, skeletonList(2));
    fill(body, 
      h('div', { class: 'vault-open-bar card' },
        h('span', { class: 'vault-open-bar__icon', svg: icons.unlock, 'aria-hidden': 'true' }),
        h('div', {}, h('strong', {}, 'Kasa açık'), h('small', { class: 'muted' }, '3 dakika işlem yapılmazsa kendiliğinden kilitlenir.')),
        h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => lock('Kasa kilitlendi 🔒') }, h('span', { svg: icons.lock }), 'Kilitle')),
      h('div', { class: 'row' },
        h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor() }, h('span', { svg: icons.plus }), 'Gizli not')),
      list);
    notesUnsub?.();
    notesUnsub = listen(query(col('vaultNotes'), orderBy('updatedAt', 'desc'), limit(200)), async (items) => {
      const k = key;
      if (!k) return;
      const dec = await Promise.all(items.map(async (n) => {
        try { return { ...n, plain: await decryptJSON(k, n, n.id) }; } catch { return { ...n, plain: null }; }
      }));
      if (key !== k) return;
      clear(list);
      if (!dec.length) { add(list, emptyState({ emoji: '🤫', title: 'Kasa boş', text: 'Sadece ikinizin bileceği bir şey yazın.' })); return; }
      for (const n of dec) {
        add(list, h('article', { class: 'card vault-note' },
          n.plain ? h('h4', { class: 'card__title' }, n.plain.title || 'Başlıksız') : h('h4', { class: 'card__title text-danger' }, 'Bu not çözülemedi'),
          n.plain ? h('p', { class: 'card__text' }, n.plain.body) : h('p', { class: 'muted' }, 'Farklı bir şifreyle şifrelenmiş ya da bozulmuş olabilir.'),
          h('div', { class: 'card__footer' },
            h('small', { class: 'card__meta' }, `${userName(n.updatedBy)} · ${relativeTime(n.updatedAt)}`),
            n.plain ? h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Düzenle', svg: icons.edit, onclick: () => editor(n) }) : null,
            h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => removeNote(n) }))));
      }
    }, (e) => toast(errorMessage(e), { type: 'error' }));
  }

  async function removeNote(n) {
    if (!(await confirmDialog({ title: 'Not silinsin mi?', message: 'Bu gizli not kalıcı olarak silinecek.', confirmText: 'Sil', danger: true }))) return;
    try { await deleteDoc(docRef('vaultNotes', n.id)); toast('Not silindi'); } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  function editor(n = null) {
    if (!key) return;
    const title = h('input', { class: 'input', value: n?.plain?.title || '', placeholder: 'Başlık' });
    const text = h('textarea', { class: 'input', rows: '8', placeholder: 'Gizli notunuz…', value: n?.plain?.body || '' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, h('span', { svg: icons.lock }), 'Şifrele ve kaydet');
    const form = h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      const t = validateText(title.value, { label: 'Başlık', min: 0, max: 80, multiline: false });
      const b = validateText(text.value, { label: 'Not', max: LIMITS.vaultPlain });
      if (!t.ok || !b.ok) { err.textContent = (t.ok ? b : t).error; return; }
      if (!key) { err.textContent = 'Kasa kilitlendi.'; return; }
      setLoading(save, true, 'Şifreleniyor…');
      try {
        const ref = n ? docRef('vaultNotes', n.id) : doc(col('vaultNotes'));
        const payload = await encryptJSON(key, { title: t.value, body: b.value }, ref.id);
        if (payload.ct.length > LIMITS.vaultCipher) throw new Error('Not çok uzun.');
        const data = { v: 1, ...payload, updatedBy: uid, updatedAt: serverTimestamp() };
        if (!n) Object.assign(data, { createdBy: uid, createdAt: serverTimestamp() });
        await setDoc(ref, data, { merge: !!n });
        toast('Not şifrelenip kaydedildi 🔐');
        m.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } }, field('Başlık', title), field('Not', counted(text, LIMITS.vaultPlain)), err, save);
    const m = openModal({ title: n ? 'Notu düzenle' : 'Yeni gizli not', content: form });
  }

  renderLocked();
}

/** Kasa için kompakt PIN girişi. onComplete(pin) true dönerse temizlenir. */
function pinEntry(onComplete) {
  let v = '';
  const dots = h('div', { class: 'pin-dots' }, Array.from({ length: 4 }, () => h('span', { class: 'pin-dot' })));
  const paint = () => [...dots.children].forEach((d, i) => d.classList.toggle('is-filled', i < v.length));
  let busy = false;
  const press = async (k) => {
    if (busy) return;
    v = k === 'back' ? v.slice(0, -1) : (v.length < 4 ? v + k : v);
    paint();
    if (v.length === 4 && isPin(v)) {
      busy = true;
      const ok = await onComplete(v).catch(() => false);
      if (!ok) { dots.classList.add('shake'); setTimeout(() => dots.classList.remove('shake'), 450); }
      v = ''; paint(); busy = false;
    }
  };
  return h('div', { class: 'pin pin--compact' }, dots,
    h('div', { class: 'pin-pad' }, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '0', 'back'].map((k) => k === ''
      ? h('span') : h('button', { class: 'pin-key', type: 'button', 'aria-label': k === 'back' ? 'Sil' : k, svg: k === 'back' ? icons.backspace : undefined, onclick: () => press(k) }, k === 'back' ? null : k))));
}
