// Yedekleme ve geri yükleme. Yedek tek bir şifreli .jozh dosyasıdır; telefon değiştirirken fotoğrafları
// ve Gizli Kasa'yı taşımanın tek yolu budur.
import { initApp } from '../app.js';
import * as db from '../storage/local-db.js';
import { createBackup, inspectBackup, readHeader, restoreBackup, checkFreeSpace } from '../storage/backup-manager.js';
import { el, replace, field, button, toast, toastError, confirmDialog, showFieldErrors, clearFieldErrors, progressBar, friendlyError } from '../ui.js';
import { icon } from '../utils/icons.js';
import { validateBackupPassword, hasErrors } from '../validators.js';
import { formatBytes } from '../utils/formatters.js';
import { formatDateTime } from '../utils/dates.js';
import { STORE_LABELS } from '../utils/labels.js';
import * as appLock from '../storage/app-lock.js';
import { replaceWith } from '../router.js';
import { logError } from '../utils/logger.js';

const main = document.getElementById('main');
let downloadUrl = null;

function progress(label) {
  const holder = el('div', { class: 'stack backup-progress', 'aria-live': 'polite' });
  return {
    node: holder,
    set(done, total, text) {
      const pct = total ? Math.round((done / total) * 100) : 0;
      replace(holder, el('p', { class: 'small' }, `${text || label} %${pct}`), progressBar(pct, label));
    },
    clear() {
      replace(holder);
    }
  };
}

function countsTable(counts) {
  const rows = Object.entries(STORE_LABELS).map(([k, label]) => [label, counts[k] || 0]);
  rows.push(['Fotoğraflar', counts.images || 0], ['Gizli Kasa içerikleri', counts.vault || 0], ['Kasa fotoğrafları', counts.vaultImages || 0]);
  return el('dl', { class: 'kv' }, rows.flatMap(([k, v]) => [el('dt', null, k), el('dd', null, String(v))]));
}

async function lastBackupNotice() {
  const last = await db.getMeta('backup:lastAt');
  if (!last) return el('div', { class: 'notice notice-warning' }, icon('alert'), el('span', null, 'Henüz yedek alınmadı. Fotoğrafların ve Gizli Kasa yalnızca bu cihazda duruyor.'));
  const days = Math.floor((Date.now() - Date.parse(last)) / 86400000);
  if (days > 30) return el('div', { class: 'notice notice-warning' }, icon('alert'), el('span', null, `Son yedek ${days} gün önce alındı (${formatDateTime(last)}). Yeni bir yedek almanın zamanı geldi.`));
  return el('div', { class: 'notice notice-info' }, icon('check'), el('span', null, `Son yedek: ${formatDateTime(last)}.`));
}

function createSection(noticeNode) {
  const result = el('div', { class: 'stack' });
  const prog = progress('Yedek hazırlanıyor');
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Fotoğrafları dahil et', name: 'includePhotos', type: 'checkbox', value: true, hint: 'Kapatırsan dosya küçülür ama fotoğraflar yeni cihaza taşınmaz. Kasa fotoğrafları her zaman dahildir.' }),
    el('div', { class: 'form-grid' },
      field({ label: 'Yedek parolası', name: 'password', type: 'password', autocomplete: 'new-password', hint: 'En az 10 karakter. Bu parola olmadan yedek açılamaz; unutma.' }),
      field({ label: 'Yedek parolası (tekrar)', name: 'passwordRepeat', type: 'password', autocomplete: 'new-password' })),
    el('div', null, button('Yedek oluştur', null, { kind: 'primary', type: 'submit', iconName: 'download' })),
    prog.node,
    result);

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    clearFieldErrors(form);
    replace(result);
    const password = form.elements.password.value;
    const errors = validateBackupPassword(password, form.elements.passwordRepeat.value);
    if (hasErrors(errors)) {
      showFieldErrors(form, errors);
      return;
    }
    const submit = form.querySelector('button[type="submit"]');
    submit.disabled = true;
    try {
      prog.set(0, 1, 'Yedek hazırlanıyor (parola anahtarı türetiliyor)');
      const res = await createBackup(password, {
        includePhotos: form.elements.includePhotos.checked,
        onProgress: (d, t) => prog.set(d, t, 'Yedek hazırlanıyor')
      });
      // Dosya baştan sona yeniden okunup doğrulanır; ancak o zaman kaydetme düğmeleri çıkar.
      const file = new File([res.blob], res.fileName, { type: 'application/octet-stream' });
      prog.set(0, 1, 'Yedek doğrulanıyor');
      const check = await inspectBackup(file, password, (d, t) => prog.set(d, t, 'Yedek doğrulanıyor'));
      prog.clear();
      form.elements.password.value = '';
      form.elements.passwordRepeat.value = '';
      if (downloadUrl) URL.revokeObjectURL(downloadUrl);
      downloadUrl = URL.createObjectURL(res.blob);
      const markSaved = async () => {
        await db.setMeta('backup:lastAt', res.createdAt);
        replace(noticeNode, await lastBackupNotice());
      };
      const saveLink = el('a', { class: 'btn btn-primary', href: downloadUrl, download: res.fileName }, icon('download'), el('span', null, 'Dosyayı kaydet'));
      saveLink.addEventListener('click', () => markSaved());
      const actions = el('div', { class: 'row' }, saveLink);
      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        actions.append(button('Paylaş / Dosyalar\'a kaydet', async () => {
          try {
            await navigator.share({ files: [file], title: 'JOZH yedeği' });
            await markSaved();
          } catch (err) {
            if (err.name !== 'AbortError') toastError('backup.share', err);
          }
        }, { iconName: 'share' }));
      }
      replace(result,
        el('div', { class: 'notice notice-info' }, icon('check'), el('span', null, `Yedek hazır ve doğrulandı: ${res.fileName} (${formatBytes(res.blob.size)}). Dosyayı kaydet ve güvenli bir yerde (ör. iCloud Drive) sakla.`)),
        countsTable(check.counts),
        actions);
    } catch (err) {
      prog.clear();
      logError('backup.create', err);
      replace(result, el('div', { class: 'notice notice-danger', role: 'alert' }, icon('alert'), el('span', null, `Yedek oluşturulamadı: ${friendlyError(err)}`)));
    } finally {
      submit.disabled = false;
    }
  });
  return form;
}

function restoreSection() {
  let file = null;
  let checked = false;
  const info = el('div', { class: 'stack' });
  const result = el('div', { class: 'stack' });
  const prog = progress('Yedek okunuyor');
  const fileInput = el('input', { type: 'file', id: 'restore-file', class: 'input', accept: '.jozh,application/octet-stream' });
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'restore-file' }, 'Yedek dosyası (.jozh)'), fileInput),
    info,
    field({ label: 'Yedek parolası', name: 'password', type: 'password', autocomplete: 'current-password' }));
  const checkBtn = button('Yedeği kontrol et', null, { type: 'submit', iconName: 'check' });
  const restoreBtn = button('Bu yedeği geri yükle', null, { kind: 'danger', iconName: 'upload', disabled: true });
  form.append(el('div', { class: 'row' }, checkBtn, restoreBtn), prog.node, result);

  fileInput.addEventListener('change', async () => {
    checked = false;
    restoreBtn.disabled = true;
    replace(result);
    replace(info);
    file = fileInput.files && fileInput.files[0];
    if (!file) return;
    try {
      const h = await readHeader(file);
      replace(info, el('p', { class: 'small' }, `Oluşturulma: ${formatDateTime(h.createdAt)} · Boyut: ${formatBytes(file.size)}`));
    } catch (err) {
      file = null;
      replace(info, el('p', { class: 'small text-red', role: 'alert' }, friendlyError(err)));
    }
  });
  form.elements.password.addEventListener('input', () => {
    checked = false;
    restoreBtn.disabled = true;
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    clearFieldErrors(form);
    replace(result);
    if (!file) {
      replace(result, el('p', { class: 'small text-red', role: 'alert' }, 'Önce bir yedek dosyası seç.'));
      return;
    }
    if (!form.elements.password.value) {
      showFieldErrors(form, { password: 'Yedek parolasını yaz.' });
      return;
    }
    checkBtn.disabled = true;
    try {
      prog.set(0, 1, 'Yedek kontrol ediliyor');
      const summary = await inspectBackup(file, form.elements.password.value, (d, t) => prog.set(d, t, 'Yedek kontrol ediliyor'));
      prog.clear();
      checked = true;
      restoreBtn.disabled = false;
      replace(result,
        el('div', { class: 'notice notice-info' }, icon('check'), el('span', null, `Yedek sağlam. Oluşturulma: ${formatDateTime(summary.createdAt)}${summary.includesPhotos ? '' : ' · Fotoğraflar dahil değil'}. Mevcut verilerine dokunulmadı.`)),
        countsTable(summary.counts));
    } catch (err) {
      prog.clear();
      replace(result, el('div', { class: 'notice notice-danger', role: 'alert' }, icon('alert'), el('span', null, friendlyError(err))));
    } finally {
      checkBtn.disabled = false;
    }
  });

  restoreBtn.addEventListener('click', async () => {
    if (!checked || !file) return;
    const space = await checkFreeSpace(file);
    if (!space.ok) {
      replace(result, el('div', { class: 'notice notice-danger', role: 'alert' }, icon('alert'), el('span', null, `Cihazda yeterli boş alan yok (boş: ${formatBytes(space.free)}, gereken: yaklaşık ${formatBytes(file.size * 1.5)}).`)));
      return;
    }
    const ok = await confirmDialog({
      title: 'Yedeği geri yükle',
      message: 'Bu cihazdaki bütün JOZH verileri silinip yerine yedektekiler yazılacak. Açılış PIN\'i, Gizli Kasa PIN\'i ve senkronizasyon anahtarı da yedektekiyle değişir.\nBu işlem geri alınamaz.',
      confirmText: 'Sil ve geri yükle',
      danger: true,
      requireText: 'SİL'
    });
    if (!ok) return;
    restoreBtn.disabled = true;
    checkBtn.disabled = true;
    try {
      await restoreBackup(file, form.elements.password.value, (d, t) => prog.set(d, t, 'Geri yükleniyor'));
      prog.clear();
      appLock.lock();
      toast('Geri yükleme tamamlandı. Yedekteki açılış PIN\'i ile giriş yap.', { kind: 'success', duration: 0 });
      setTimeout(() => replaceWith('login'), 1800);
    } catch (err) {
      prog.clear();
      logError('backup.restore', err);
      replace(result, el('div', { class: 'notice notice-danger', role: 'alert' }, icon('alert'), el('span', null, `Geri yükleme tamamlanamadı: ${friendlyError(err)} Yedeği yeniden geri yüklemeyi dene.`)));
      checkBtn.disabled = false;
    }
  });
  return form;
}

async function setup() {
  const noticeNode = el('div', null, await lastBackupNotice());
  replace(main, el('div', { class: 'backup-layout' },
    noticeNode,
    el('section', { class: 'card', 'aria-labelledby': 'create-title' },
      el('h2', { id: 'create-title', class: 'settings-title' }, 'Yedek oluştur'),
      el('p', { class: 'muted small' }, 'Yedek; bütün kayıtları (silinmiş işaretliler dahil), fotoğrafları, Gizli Kasa\'yı (kendi şifresiyle), açılış PIN ayarını, senkronizasyon anahtarını ve taslakları içerir. Dosyanın tamamı yedek parolanla şifrelenir; içinde açık metin yoktur.'),
      createSection(noticeNode)),
    el('section', { class: 'card', 'aria-labelledby': 'restore-title' },
      el('h2', { id: 'restore-title', class: 'settings-title' }, 'Geri yükle'),
      el('p', { class: 'muted small' }, 'Önce "Yedeği kontrol et" ile dosyanın sağlam olduğunu ve parolanın doğru olduğunu denetle. Kontrol mevcut verilere dokunmaz.'),
      restoreSection())));
}

const ready = await initApp({ page: 'backup', title: 'Yedekleme' });
if (ready) await setup();
