// Özel Kasamız 🔐 — uçtan uca şifreli ortak notlar.
// Güvenlik modeli (README'de ayrıntılı):
//  * Notlar, ikinizin ortak bildiği güçlü KASA PAROLASINDAN türetilen anahtarla bu cihazda şifrelenir.
//    Firestore'da yalnızca şifreli veri bulunur; Firebase yöneticisi, veritabanı sızıntısı veya
//    çalınan bir Firebase oturumu bile notları okuyamaz.
//  * 4 haneli kasa PIN'i tek başına şifreleme sırrı OLAMAZ (10.000 olasılık saniyeler içinde denenir).
//    Bu yüzden PIN yalnızca "bu cihazda hızlı açma" içindir: parola ile bir kez açtıktan sonra
//    dışa aktarılamaz anahtar bu cihazın IndexedDB'sinde saklanır ve PIN ile kilidi açılır.
//    3 hatalı PIN denemesinde cihazdaki anahtar silinir.
import { getState } from '../state.js';
import { userName } from '../constants.js';
import { h, clear, vibrate, sleep, fill, add } from '../utils/helpers.js';
import { icons } from '../utils/icons.js';
import { toast, confirmDialog, emptyState, openModal, field, counted, errorMessage, setLoading, skeletonList } from '../utils/ui.js';
import { relativeTime } from '../utils/dates.js';
import { LIMITS, validateText, isPin } from '../utils/validation.js';
import { col, docRef, listen, query, orderBy, limit } from '../services/firestore.js';
import { doc, getDoc, setDoc, onSnapshot, deleteDoc, serverTimestamp, writeBatch } from '../vendor/firebase.js';
import { db } from '../firebase-config.js';
import { createVaultConfig, unlockVault, encryptJSON, decryptJSON, passphraseStrength, pbkdf2Hex, toB64, randomBytes, safeEqual, VAULT_CHECK } from '../services/crypto.js';
import { keyGet, keySet, keyDel } from '../services/keystore.js';

const AUTO_LOCK_MS = 3 * 60 * 1000;
const QUICK_MAX_FAILS = 3;
const configRef = () => docRef('vault', 'config');

export default async function vault(page, { scope }) {
  const { uid } = getState();
  let key = null;           // bellekteki anahtar (yalnızca kasa açıkken)
  let config = null;
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

  // Kasa yapılandırması değişirse (ör. parola değişti) kilitle.
  fill(body, skeletonList(1));
  scope.add(onSnapshot(configRef(), (snap) => {
    const next = snap.exists() ? snap.data() : null;
    const changed = config && next && next.salt !== config.salt;
    config = next;
    if (!config) { key = null; renderSetup(); return; }
    if (changed) { lock('Kasa parolası değiştirildi; yeni parolayla aç.'); return; }
    if (!key) renderLocked();
  }, (e) => { fill(body, emptyState({ emoji: '🔒', title: 'Kasa yüklenemedi', text: errorMessage(e) })); }));

  // Hareketsizlikte otomatik kilit
  const resetIdle = () => { if (!key) return; clearTimeout(idleTimer); idleTimer = setTimeout(() => lock('Kasa hareketsizlik nedeniyle kilitlendi 🔒'), AUTO_LOCK_MS); };
  ['pointerdown', 'keydown', 'scroll'].forEach((ev) => scope.on(document, ev, resetIdle, { passive: true }));
  scope.on(document, 'visibilitychange', () => { if (document.visibilityState === 'hidden' && key) lock(); });

  // ---------------- Kurulum ----------------
  function renderSetup() {
    const p1 = h('input', { class: 'input', type: 'password', autocomplete: 'new-password', placeholder: 'En az 10 karakter' });
    const p2 = h('input', { class: 'input', type: 'password', autocomplete: 'new-password', placeholder: 'Tekrar yaz' });
    const meter = h('div', { class: 'meter' }, h('span', {}));
    const meterLabel = h('small', { class: 'muted' }, 'Parola gücü');
    p1.addEventListener('input', () => {
      const s = passphraseStrength(p1.value);
      meter.firstChild.style.width = `${Math.min(100, s.bits)}%`;
      meter.dataset.level = s.ok ? (s.bits >= 70 ? 'high' : 'ok') : 'low';
      meterLabel.textContent = p1.value ? `${s.label} (~${s.bits} bit)` : 'Parola gücü';
    });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const btn = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, 'Kasayı oluştur');
    fill(body, h('form', { class: 'card vault-setup', onsubmit: async (e) => {
      e.preventDefault();
      err.textContent = '';
      const s = passphraseStrength(p1.value);
      if (!s.ok) { err.textContent = 'Daha güçlü bir parola seçin: en az 10 karakter; harf, rakam ve sembol karışımı. Örn. bir cümle: "İlkKahvemiz@Moda2026"'; return; }
      if (p1.value !== p2.value) { err.textContent = 'Parolalar eşleşmiyor.'; return; }
      setLoading(btn, true, 'Anahtar oluşturuluyor…');
      try {
        const existing = await getDoc(configRef());
        if (existing.exists()) { toast('Kasa az önce oluşturulmuş; ortak parolayla açın.'); return; }
        const res = await createVaultConfig(p1.value);
        await setDoc(configRef(), { ...res.config, createdBy: uid, createdAt: serverTimestamp(), updatedBy: uid, updatedAt: serverTimestamp() });
        p1.value = p2.value = '';
        await openWith(res.key, true);
      } catch (e2) { err.textContent = errorMessage(e2); setLoading(btn, false); }
    } },
      h('div', { class: 'vault-illu', 'aria-hidden': 'true' }, '🔐'),
      h('h3', {}, 'Kasanızı kuralım'),
      h('p', {}, 'İkinizin birlikte belirleyeceği güçlü bir KASA PAROLASI seçin. Notlar bu parolayla cihazınızda şifrelenir; sunucuya yalnızca şifreli veri gider.'),
      h('div', { class: 'notice notice--warn' }, h('strong', {}, 'Önemli: '), 'Parolayı unutursanız notlar kurtarılamaz. Kimse — biz dahil — sıfırlayamaz. Parolayı sevgilinle yüz yüze paylaş, mesajla gönderme.'),
      field('Kasa parolası', p1), meter, meterLabel, field('Parolayı onayla', p2), err, btn));
  }

  // ---------------- Kilitli ----------------
  async function renderLocked() {
    const quick = await keyGet(`vault:${uid}`).catch(() => null);
    const usable = quick && quick.salt === config?.salt && quick.key;
    if (key || scope.disposed) return;
    clear(body);
    const lockIcon = h('div', { class: 'vault-lock', 'aria-hidden': 'true', svg: icons.lock });
    if (usable) {
      const msg = h('p', { class: 'auth-hint', 'aria-live': 'polite' }, 'Kasa PIN\'ini gir');
      const pad = pinEntry(async (pin) => {
        const ok = safeEqual(await pbkdf2Hex(pin, quick.pinSalt, quick.iter), quick.pinHash);
        if (!ok) {
          quick.fails = (quick.fails || 0) + 1;
          vibrate([30, 40, 30]);
          if (quick.fails >= QUICK_MAX_FAILS) {
            await keyDel(`vault:${uid}`);
            toast('PIN 3 kez hatalı girildi; bu cihazdaki hızlı açma kaldırıldı. Kasa parolasıyla aç.', { type: 'error', duration: 6000 });
            renderLocked(); return false;
          }
          await keySet(`vault:${uid}`, quick);
          msg.textContent = `Hatalı PIN. ${QUICK_MAX_FAILS - quick.fails} hakkın kaldı.`;
          return false;
        }
        try {
          const chk = await decryptJSON(quick.key, config.check, 'check');
          if (chk?.check !== VAULT_CHECK) throw new Error('check');
        } catch { await keyDel(`vault:${uid}`); toast('Cihazdaki anahtar geçersiz; parolayla aç.', { type: 'error' }); renderLocked(); return false; }
        quick.fails = 0; await keySet(`vault:${uid}`, quick);
        await openWith(quick.key, false, lockIcon);
        return true;
      });
      add(body, h('div', { class: 'card vault-locked' }, lockIcon, h('h3', {}, 'Kasa kilitli'), msg, pad,
        h('button', { class: 'link-btn', type: 'button', onclick: () => renderPassphrase(lockIcon) }, 'Kasa parolasıyla aç')));
      return;
    }
    renderPassphrase(lockIcon);
  }

  function renderPassphrase(lockIcon) {
    const pass = h('input', { class: 'input', type: 'password', autocomplete: 'current-password', placeholder: 'Ortak kasa parolası', 'aria-label': 'Kasa parolası' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const btn = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, 'Kilidi aç');
    fill(body, h('form', { class: 'card vault-locked', onsubmit: async (e) => {
      e.preventDefault();
      if (!pass.value) { err.textContent = 'Parolayı yaz.'; return; }
      setLoading(btn, true, 'Açılıyor…');
      await sleep(30);
      const k = await unlockVault(pass.value, config);
      pass.value = '';
      if (!k) { err.textContent = 'Parola hatalı.'; setLoading(btn, false); vibrate([30, 40, 30]); return; }
      await openWith(k, true, lockIcon);
    } }, lockIcon, h('h3', {}, 'Kasa kilitli'), h('p', { class: 'muted' }, 'Notları görmek için ortak kasa parolasını gir.'), pass, err, btn));
    requestAnimationFrame(() => pass.focus());
  }

  async function openWith(k, offerQuick, lockIcon) {
    if (lockIcon) { lockIcon.innerHTML = icons.unlock; lockIcon.classList.add('is-opening'); await sleep(550); }
    key = k;
    resetIdle();
    renderOpen();
    if (offerQuick) {
      const q = await keyGet(`vault:${uid}`).catch(() => null);
      if (!q || q.salt !== config.salt) offerQuickSetup();
    }
  }

  function offerQuickSetup() {
    const capturedKey = key;
    let first = null;
    const msg = h('p', {}, 'Bu cihazda kasayı 4 haneli PIN ile hızlıca açmak ister misin? Parola her seferinde gerekmez.');
    const m = openModal({
      title: 'PIN ile hızlı açma', content: h('div', { class: 'form' }, msg,
        h('div', { class: 'notice' }, 'Nasıl çalışır: Şifreleme anahtarı bu cihazda dışa aktarılamaz biçimde saklanır; PIN yalnızca bu cihazdaki kilidi açar. Sunucudaki veriler yine parolayla korunur. Cihazını kaybedersen buradan "hızlı açmayı kaldır" diyemezsin — bu yüzden telefon ekran kilidini mutlaka kullan.'),
        pinEntry(async (pin) => {
          if (!first) { first = pin; msg.textContent = 'PIN\'i tekrar gir.'; return false; }
          if (first !== pin) { first = null; msg.textContent = 'Eşleşmedi, baştan gir.'; vibrate([30, 40, 30]); return false; }
          const pinSalt = toB64(randomBytes(16));
          const iter = 150000;
          await keySet(`vault:${uid}`, { key: capturedKey, salt: config.salt, pinSalt, iter, pinHash: await pbkdf2Hex(pin, pinSalt, iter), fails: 0 });
          toast('Bu cihazda PIN ile hızlı açma etkin 🔐');
          m.close();
          return true;
        }),
        h('button', { class: 'btn btn--ghost btn--block', type: 'button', onclick: () => m.close() }, 'Hayır, her seferinde parola'))
    });
  }

  // ---------------- Açık kasa ----------------
  function renderOpen() {
    const list = h('div', { class: 'card-list' }, skeletonList(2));
    fill(body, 
      h('div', { class: 'vault-open-bar card' },
        h('span', { class: 'vault-open-bar__icon', svg: icons.unlock, 'aria-hidden': 'true' }),
        h('div', {}, h('strong', {}, 'Kasa açık'), h('small', { class: 'muted' }, '3 dakika işlem yapılmazsa kendiliğinden kilitlenir.')),
        h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => lock('Kasa kilitlendi 🔒') }, h('span', { svg: icons.lock }), 'Kilitle')),
      h('div', { class: 'row row--between' },
        h('button', { class: 'btn btn--primary', type: 'button', onclick: () => editor() }, h('span', { svg: icons.plus }), 'Gizli not'),
        h('button', { class: 'btn btn--ghost btn--sm', type: 'button', onclick: () => settings() }, 'Kasa ayarları')),
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
          n.plain ? h('p', { class: 'card__text' }, n.plain.body) : h('p', { class: 'muted' }, 'Farklı bir parolayla şifrelenmiş ya da bozulmuş olabilir.'),
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

  function settings() {
    const m = openModal({
      title: 'Kasa ayarları', content: h('div', { class: 'action-list' },
        h('button', { class: 'action', type: 'button', onclick: () => { m.close(); changePassphrase(); } }, h('span', { svg: icons.refresh }), 'Kasa parolasını değiştir'),
        h('button', { class: 'action', type: 'button', onclick: () => { m.close(); offerQuickSetup(); } }, h('span', { svg: icons.lock }), 'Bu cihazda PIN ile hızlı açmayı ayarla'),
        h('button', { class: 'action action--danger', type: 'button', onclick: async () => { await keyDel(`vault:${uid}`); m.close(); toast('Bu cihazdaki hızlı açma kaldırıldı'); } }, h('span', { svg: icons.trash }), 'Bu cihazdaki hızlı açmayı kaldır'),
        h('p', { class: 'muted small' }, 'Şifreleme: AES-GCM-256 · Anahtar türetme: PBKDF2-SHA256, 600.000 tur · Her not için rastgele IV.'))
    });
  }

  function changePassphrase() {
    const p1 = h('input', { class: 'input', type: 'password', autocomplete: 'new-password' });
    const p2 = h('input', { class: 'input', type: 'password', autocomplete: 'new-password' });
    const err = h('p', { class: 'form-error', role: 'alert' });
    const btn = h('button', { class: 'btn btn--primary btn--block', type: 'submit' }, 'Parolayı değiştir');
    const m = openModal({ title: 'Yeni kasa parolası', content: h('form', { class: 'form', onsubmit: async (e) => {
      e.preventDefault();
      if (!passphraseStrength(p1.value).ok) { err.textContent = 'Daha güçlü bir parola seçin (en az 10 karakter, karışık).'; return; }
      if (p1.value !== p2.value) { err.textContent = 'Parolalar eşleşmiyor.'; return; }
      if (!key) { err.textContent = 'Kasa kilitlendi.'; return; }
      setLoading(btn, true, 'Notlar yeniden şifreleniyor…');
      try {
        const { getDocs } = await import('../vendor/firebase.js');
        const snap = await getDocs(query(col('vaultNotes'), limit(450)));
        const plain = [];
        for (const d of snap.docs) plain.push({ id: d.id, data: await decryptJSON(key, d.data(), d.id) });
        const res = await createVaultConfig(p1.value);
        const batch = writeBatch(db);
        batch.set(configRef(), { ...res.config, updatedBy: uid, updatedAt: serverTimestamp() }, { merge: true });
        for (const p of plain) batch.set(docRef('vaultNotes', p.id), { v: 1, ...(await encryptJSON(res.key, p.data, p.id)), updatedBy: uid, updatedAt: serverTimestamp() }, { merge: true });
        await batch.commit();
        await keyDel(`vault:${uid}`);
        p1.value = p2.value = '';
        m.close();
        toast('Kasa parolası değişti. Sevgiline yeni parolayı yüz yüze söyle 💌', { duration: 6000 });
      } catch (e2) { err.textContent = e2?.name === 'OperationError' ? 'Bazı notlar çözülemedi; işlem iptal edildi.' : errorMessage(e2); setLoading(btn, false); }
    } }, h('p', { class: 'muted' }, 'Tüm notlar yeni parolayla yeniden şifrelenir. Bu cihazdaki ve diğer cihazlardaki hızlı açma geçersiz olur.'),
      field('Yeni parola', p1), field('Tekrar', p2), err, btn) });
  }
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
