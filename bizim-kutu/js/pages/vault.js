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
import { createVaultConfig, unlockVault, encryptJSON, decryptJSON } from '../services/crypto.js';
import { saveMedia, loadMedia, deleteMedia, compressImage, createRecorder, MAX_AUDIO_SECONDS } from '../services/vault-media.js';

const AUTO_LOCK_MS = 3 * 60 * 1000;
export const VAULT_MAX_TRIES = 10;
export const VAULT_WINDOW_MS = 10 * 60 * 1000;
const configRef = () => docRef('vault', 'config');

/** Kasa PIN'ini sunucuda doğrular. Döner: { ok, config } | { ok:false, remaining } | { locked, waitMin } */
async function verifyVaultPin(pin) {
  const dev = auth.currentUser?.uid;
  if (!dev) throw new Error('Oturum bulunamadı.');
  const ref = doc(db, 'vaultTry', dev);
  const prevSnap = await getDoc(ref).catch(() => null);
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

  // Çözülmüş medya yalnızca bellekte (blob URL) tutulur; kilitlenince silinir.
  const mediaUrls = new Map();
  const dropMedia = () => { mediaUrls.forEach((p) => p.then((u) => u && URL.revokeObjectURL(u)).catch(() => {})); mediaUrls.clear(); };
  const lock = (reason) => {
    dropMedia();
    key = null;
    notesUnsub?.(); notesUnsub = null;
    clearTimeout(idleTimer);
    if (!scope.disposed) { renderLocked(); if (reason) toast(reason); }
  };
  scope.add(() => { dropMedia(); key = null; notesUnsub?.(); clearTimeout(idleTimer); });

  // Hareketsizlikte otomatik kilit
  const resetIdle = () => { if (!key) return; clearTimeout(idleTimer); idleTimer = setTimeout(() => lock('Kasa hareketsizlik nedeniyle kilitlendi 🔒'), AUTO_LOCK_MS); };
  ['pointerdown', 'keydown', 'scroll'].forEach((ev) => scope.on(document, ev, resetIdle, { passive: true }));
  scope.on(document, 'visibilitychange', () => { if (document.visibilityState === 'hidden' && key) lock(); });

  // ---------------- Kilitli: kasa PIN'i ----------------
  function renderLocked() {
    const lockIcon = h('div', { class: 'vault-lock', 'aria-hidden': 'true', svg: icons.lock });
    const msg = h('p', { class: 'auth-hint', 'aria-live': 'polite' }, 'Kasa PIN\'ini gir');
    const pad = pinEntry(async (pin) => {
      msg.textContent = 'Kontrol ediliyor…';
      try {
        const r = await verifyVaultPin(pin);
        if (r.locked) { msg.textContent = `Çok fazla deneme. ${r.waitMin} dakika sonra tekrar dene.`; vibrate([30, 40, 30]); return false; }
        if (!r.ok) { msg.textContent = r.remaining > 0 ? `PIN hatalı. ${r.remaining} deneme hakkın kaldı.` : 'PIN hatalı. Deneme hakkın bitti, 10 dakika sonra tekrar dene.'; vibrate([30, 40, 30]); return false; }
        msg.textContent = 'Kasa açılıyor…';
        let k;
        if (!r.config) {
          // İlk açılış: kasa bu PIN ile oluşturulur
          const res = await createVaultConfig(pin);
          await setDoc(configRef(), { ...res.config, createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp() });
          k = res.key;
        } else {
          k = await unlockVault(pin, r.config);
          if (!k) { renderMismatch(pin); return true; }
        }
        lockIcon.innerHTML = icons.unlock; lockIcon.classList.add('is-opening');
        await sleep(450);
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
    const photoInput = h('input', { type: 'file', accept: 'image/*', hidden: true, 'aria-label': 'Fotoğraf seç',
      onchange: (e) => { const f = e.target.files?.[0]; e.target.value = ''; if (f) photoFlow(f); } });
    fill(body, 
      h('div', { class: 'vault-open-bar card' },
        h('span', { class: 'vault-open-bar__icon', svg: icons.unlock, 'aria-hidden': 'true' }),
        h('div', {}, h('strong', {}, 'Kasa açık'), h('small', { class: 'muted' }, '3 dakika işlem yapılmazsa kendiliğinden kilitlenir.')),
        h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => lock('Kasa kilitlendi 🔒') }, h('span', { svg: icons.lock }), 'Kilitle')),
      h('div', { class: 'row vault-actions' },
        h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor() }, h('span', { svg: icons.plus }), 'Gizli not'),
        h('button', { class: 'btn btn--soft', type: 'button', onclick: () => photoInput.click() }, '📷 Fotoğraf'),
        h('button', { class: 'btn btn--soft', type: 'button', onclick: () => audioFlow() }, '🎙️ Ses kaydı'),
        photoInput),
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
          n.plain?.media ? mediaView(n) : null,
          n.plain ? (n.plain.body ? h('p', { class: 'card__text' }, n.plain.body) : null) : h('p', { class: 'muted' }, 'Farklı bir şifreyle şifrelenmiş ya da bozulmuş olabilir.'),
          h('div', { class: 'card__footer' },
            h('small', { class: 'card__meta' }, `${userName(n.updatedBy)} · ${relativeTime(n.updatedAt)}`),
            n.plain ? h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Düzenle', svg: icons.edit, onclick: () => editor(n) }) : null,
            h('button', { class: 'icon-btn icon-btn--sm', type: 'button', 'aria-label': 'Sil', svg: icons.trash, onclick: () => removeNote(n) }))));
      }
    }, (e) => toast(errorMessage(e), { type: 'error' }));
  }

  async function removeNote(n) {
    if (!(await confirmDialog({ title: 'Not silinsin mi?', message: 'Bu gizli not kalıcı olarak silinecek.', confirmText: 'Sil', danger: true }))) return;
    try {
      if (n.plain?.media) await deleteMedia(n.id, n.plain.media.n);
      await deleteDoc(docRef('vaultNotes', n.id)); toast('Silindi');
    } catch (e) { toast(errorMessage(e), { type: 'error' }); }
  }

  /** Şifreli fotoğraf/ses görünümü: ilk gösterimde çözülür, bellekte tutulur. */
  function mediaView(n) {
    const m = n.plain.media;
    const box = h('div', { class: `vault-media vault-media--${m.kind}` }, h('span', { class: 'muted small' }, '🔐 Çözülüyor…'));
    const k = key;
    if (!mediaUrls.has(n.id)) {
      mediaUrls.set(n.id, loadMedia(k, n.id, m.n).then((bytes) => URL.createObjectURL(new Blob([bytes], { type: m.mime }))).catch(() => null));
    }
    mediaUrls.get(n.id).then((url) => {
      if (key !== k) return;
      if (!url) { fill(box, h('span', { class: 'text-danger small' }, 'Dosya açılamadı.')); return; }
      if (m.kind === 'image') {
        fill(box, h('img', { class: 'vault-photo', src: url, alt: n.plain.title || 'Fotoğraf', loading: 'lazy',
          onclick: () => openModal({ title: n.plain.title || 'Fotoğraf', wide: true, content: h('img', { class: 'vault-photo vault-photo--full', src: url, alt: n.plain.title || 'Fotoğraf' }) }) }));
      } else {
        fill(box, h('audio', { class: 'vault-audio', controls: true, preload: 'metadata', src: url }),
          m.seconds ? h('small', { class: 'muted' }, `${Math.floor(m.seconds / 60)}:${String(m.seconds % 60).padStart(2, '0')}`) : null);
      }
    });
    return box;
  }

  /** Medya notunu kaydeder: önce şifreli parçalar, sonra şifreli not. */
  async function saveMediaNote({ bytes, mime, kind, title, body, extra = {} }, onProgress) {
    const ref = doc(col('vaultNotes'));
    const n = await saveMedia(key, ref.id, bytes, uid, onProgress);
    const media = { kind, mime, n, size: bytes.length, ...extra };
    try {
      const payload = await encryptJSON(key, { title, body, media }, ref.id);
      await setDoc(ref, { v: 1, ...payload, createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp() });
    } catch (e) { await deleteMedia(ref.id, n); throw e; }
  }

  async function photoFlow(file) {
    if (!key) return;
    let img;
    try { img = await compressImage(file); } catch (e) { toast(e.message || 'Fotoğraf açılamadı.', { type: 'error' }); return; }
    const url = URL.createObjectURL(new Blob([img.bytes], { type: img.mime }));
    const title = h('input', { class: 'input', placeholder: 'Başlık (isteğe bağlı)', maxlength: '80' });
    const note = h('textarea', { class: 'input', rows: '2', placeholder: 'Not (isteğe bağlı)', maxlength: String(LIMITS.vaultPlain) });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, h('span', { svg: icons.lock }), 'Şifrele ve kaydet');
    const m = openModal({ title: 'Gizli fotoğraf', onClose: () => URL.revokeObjectURL(url), content: h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      if (!key) { err.textContent = 'Kasa kilitlendi.'; return; }
      setLoading(save, true, 'Şifreleniyor…');
      try {
        await saveMediaNote({ bytes: img.bytes, mime: img.mime, kind: 'image', title: title.value.trim().slice(0, 80), body: note.value.trim(), extra: { w: img.w, h: img.h } },
          (p) => { save.textContent = `Yükleniyor… %${Math.round(p * 100)}`; });
        toast('Fotoğraf şifrelenip kaydedildi 🔐');
        m.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } },
      h('img', { class: 'vault-photo', src: url, alt: 'Seçilen fotoğraf' }),
      h('small', { class: 'muted' }, `${img.w}×${img.h} · ${Math.round(img.bytes.length / 1024)} KB`),
      field('Başlık', title), field('Not', note), err, save) });
  }

  function audioFlow() {
    if (!key) return;
    const rec = createRecorder();
    if (!rec.supported) { toast('Bu tarayıcı ses kaydını desteklemiyor.', { type: 'error' }); return; }
    let result = null, timer = null, url = null;
    const time = h('div', { class: 'rec-time', 'aria-live': 'polite' }, '0:00');
    const recBtn = h('button', { class: 'rec-btn', type: 'button', 'aria-label': 'Kaydı başlat' }, '🎙️');
    const preview = h('div', { class: 'rec-preview' });
    const title = h('input', { class: 'input', placeholder: 'Başlık (isteğe bağlı)', maxlength: '80' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const save = h('button', { class: 'btn btn--primary btn--block', type: 'submit', disabled: true }, h('span', { svg: icons.lock }), 'Şifrele ve kaydet');
    const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
    const stop = async () => {
      clearInterval(timer);
      result = await rec.stop();
      recBtn.classList.remove('is-recording'); recBtn.textContent = '🔁'; recBtn.setAttribute('aria-label', 'Yeniden kaydet');
      if (result?.bytes?.length) {
        url && URL.revokeObjectURL(url);
        url = URL.createObjectURL(new Blob([result.bytes], { type: result.mime }));
        fill(preview, h('audio', { class: 'vault-audio', controls: true, src: url }));
        save.disabled = false;
      }
    };
    recBtn.addEventListener('click', async () => {
      if (recBtn.classList.contains('is-recording')) { stop(); return; }
      try {
        result = null; save.disabled = true; clear(preview); err.textContent = '';
        await rec.start();
        recBtn.classList.add('is-recording'); recBtn.textContent = '⏹'; recBtn.setAttribute('aria-label', 'Kaydı durdur');
        timer = setInterval(() => { const e = rec.elapsed(); time.textContent = fmt(e); if (e >= MAX_AUDIO_SECONDS) stop(); }, 250);
      } catch { err.textContent = 'Mikrofona erişilemedi. Tarayıcıdan mikrofon izni ver.'; }
    });
    const m = openModal({ title: 'Gizli ses kaydı', onClose: () => { clearInterval(timer); rec.cancel(); url && URL.revokeObjectURL(url); }, content: h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      if (!result?.bytes?.length) return;
      if (!key) { err.textContent = 'Kasa kilitlendi.'; return; }
      setLoading(save, true, 'Şifreleniyor…');
      try {
        await saveMediaNote({ bytes: result.bytes, mime: result.mime, kind: 'audio', title: title.value.trim().slice(0, 80), body: '', extra: { seconds: result.seconds } });
        toast('Ses kaydı şifrelenip kaydedildi 🔐');
        m.close();
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(save, false); }
    } },
      h('div', { class: 'rec' }, recBtn, time, h('small', { class: 'muted' }, `Dokun ve konuş · en fazla ${MAX_AUDIO_SECONDS / 60} dakika`)),
      preview, field('Başlık', title), err, save) });
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
      const b = validateText(text.value, { label: 'Not', min: n?.plain?.media ? 0 : 1, max: LIMITS.vaultPlain });
      if (!t.ok || !b.ok) { err.textContent = (t.ok ? b : t).error; return; }
      if (!key) { err.textContent = 'Kasa kilitlendi.'; return; }
      setLoading(save, true, 'Şifreleniyor…');
      try {
        const ref = n ? docRef('vaultNotes', n.id) : doc(col('vaultNotes'));
        const payload = await encryptJSON(key, { title: t.value, body: b.value, ...(n?.plain?.media ? { media: n.plain.media } : {}) }, ref.id);
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
