// Ayarlar: görünüm, takvim, senkronizasyon ve çakışmalar, Gizli Kasa, cihaz depolaması, yedek özeti, uygulama.
import { initApp, APP_VERSION } from '../app.js';
import { getSingleton, saveSingleton, countActiveRecords } from '../storage/records.js';
import * as db from '../storage/local-db.js';
import { el, replace, button, toast, toastError, segmented, confirmDialog, field, showFieldErrors, clearFieldErrors, loadingState } from '../ui.js';
import { icon } from '../utils/icons.js';
import { STORE_LABELS, fieldLabel, recordTitle } from '../utils/labels.js';
import { formatBytes, formatNumber } from '../utils/formatters.js';
import { formatDateTime } from '../utils/dates.js';
import { generateKey, normalizeKey, isValidKey, formatKey, maskKey, getKey } from '../storage/sync-key.js';
import { enableSync, disableSync, runSync, onSyncStatus, describeStatus, getConflicts, resolveConflict, diffFields } from '../firebase/sync-manager.js';
import { testConnection } from '../firebase/firestore.js';
import { stats as imageStats, cleanupOrphans } from '../storage/image-storage.js';
import { isStandalone, isIOS, canInstall, promptInstall, checkForUpdate, getOfflineStatus, getWorkerVersion } from '../pwa.js';
import { pageUrl } from '../router.js';
import { SYNCED_STORES } from '../storage/schemas.js';

const main = document.getElementById('main');

function sectionCard(id, title, ...children) {
  return el('section', { class: 'card settings-section', id, 'aria-labelledby': `${id}-title` },
    el('h2', { id: `${id}-title`, class: 'settings-title' }, title), ...children);
}

// --- Görünüm ---

function applyTheme(pref) {
  try {
    localStorage.setItem('jozh.theme', pref);
  } catch {
    // yok say
  }
  const resolved = pref === 'system'
    ? (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark')
    : pref;
  document.documentElement.dataset.theme = resolved;
  document.documentElement.dataset.themePref = pref;
}

async function appearanceSection() {
  const pref = document.documentElement.dataset.themePref || 'system';
  const settings = await getSingleton('settings');
  return sectionCard('appearance', 'Görünüm',
    el('div', { class: 'settings-row' },
      el('span', { class: 'settings-label', id: 'theme-label' }, 'Tema'),
      segmented([['dark', 'Koyu'], ['light', 'Açık'], ['system', 'Sistem']], pref, applyTheme, 'Tema')),
    el('div', { class: 'settings-row' },
      el('span', { class: 'settings-label' }, 'Takvim varsayılanı'),
      segmented([['month', 'Ay'], ['agenda', 'Liste']], (settings && settings.calendarView) || 'month', async (v) => {
        try {
          await saveSingleton('settings', { calendarView: v });
          toast('Takvim varsayılanı kaydedildi.', { kind: 'success' });
        } catch (err) {
          toastError('settings.calendar', err);
        }
      }, 'Takvim varsayılanı')));
}

// --- Senkronizasyon ---

const syncBody = el('div', { class: 'stack' });
const syncStatusBody = el('div', { class: 'stack' });
const conflictsBody = el('div', { class: 'stack' });

async function renderSync() {
  const key = await getKey();
  if (!key) {
    const connectForm = el('form', { class: 'form-stack', novalidate: true },
      field({ label: 'Başka cihazdaki senkronizasyon anahtarı', name: 'key', placeholder: 'xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xx', autocomplete: 'off', hint: 'Boşluk, tire ve büyük harf önemsizdir.' }),
      el('div', null, button('Bu anahtarla bağlan', null, { type: 'submit', iconName: 'cloud' })));
    connectForm.elements.key.setAttribute('autocapitalize', 'none');
    connectForm.elements.key.setAttribute('spellcheck', 'false');
    connectForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFieldErrors(connectForm);
      const k = normalizeKey(connectForm.elements.key.value);
      if (!isValidKey(k)) {
        showFieldErrors(connectForm, { key: 'Anahtar geçersiz: 26 karakter olmalı ve yalnızca a–z harfleri ile 2–7 rakamlarını içermeli.' });
        return;
      }
      const ok = await confirmDialog({ title: 'Anahtarla bağlan', message: 'Bu cihaz, anahtarın bulut verileriyle birleştirilecek. Bu cihazdaki kayıtlar silinmez; iki tarafta farklı olan kayıtlar için seçim yapman istenir.', confirmText: 'Bağlan' });
      if (!ok) return;
      try {
        await enableSync(k);
        toast('Senkronizasyon açıldı.', { kind: 'success' });
        renderSync();
      } catch (err) {
        toastError('sync.connect', err);
      }
    });
    replace(syncBody,
      el('p', { class: 'muted' }, 'Senkronizasyon kapalı: bütün verilerin yalnızca bu cihazda. Açarsan kayıtların (fotoğraflar, Gizli Kasa ve taslaklar hariç) Firestore\'a gönderilir ve aynı anahtarı giren başka cihazlarla eşitlenir.'),
      el('div', null, button('Senkronizasyonu aç', async () => {
        const ok = await confirmDialog({ title: 'Senkronizasyonu aç', message: 'Bu cihaz için yeni bir rastgele anahtar üretilecek. Anahtar bir paroladır; kimseyle paylaşma.', confirmText: 'Aç' });
        if (!ok) return;
        try {
          await enableSync(generateKey());
          toast('Senkronizasyon açıldı. Anahtarını güvenli bir yere not et.', { kind: 'success' });
          renderSync();
        } catch (err) {
          toastError('sync.enable', err);
        }
      }, { kind: 'primary', iconName: 'cloud' })),
      el('hr', { class: 'divider' }),
      connectForm);
    return;
  }
  let shown = false;
  const keyText = el('code', { class: 'sync-key', 'aria-live': 'polite' }, maskKey(key));
  const toggle = button('Anahtarı göster', () => {
    shown = !shown;
    keyText.textContent = shown ? formatKey(key) : maskKey(key);
    toggle.querySelector('span').textContent = shown ? 'Anahtarı gizle' : 'Anahtarı göster';
  }, { iconName: 'eye', className: 'btn-small' });
  replace(syncBody,
    el('div', { class: 'notice notice-warning' }, icon('alert'), el('span', null, 'Anahtar bir paroladır; paylaşma. Anahtarı bilen herkes bulut verilerini okuyabilir. Anahtar yedek dosyasında da bulunur.')),
    el('div', { class: 'row' }, keyText),
    el('div', { class: 'row' },
      toggle,
      button('Kopyala', async () => {
        try {
          await navigator.clipboard.writeText(formatKey(key));
          toast('Anahtar kopyalandı.', { kind: 'success' });
        } catch {
          toast('Kopyalanamadı; anahtarı gösterip elle kopyala.', { kind: 'warning' });
        }
      }, { iconName: 'copy', className: 'btn-small' }),
      button('Şimdi senkronize et', () => runSync({ force: true }), { iconName: 'refresh', className: 'btn-small' }),
      button('Senkronizasyonu kapat', async () => {
        const ok = await confirmDialog({ title: 'Senkronizasyonu kapat', message: 'Bu cihaz artık buluta veri göndermez ve almaz. Bu cihazdaki veriler silinmez; buluttaki veriler de olduğu gibi kalır.', confirmText: 'Kapat', danger: true });
        if (!ok) return;
        try {
          await disableSync();
          toast('Senkronizasyon kapatıldı.');
          renderSync();
          renderConflicts();
        } catch (err) {
          toastError('sync.disable', err);
        }
      }, { kind: 'danger', className: 'btn-small' })));
}

async function renderSyncStatus(status) {
  const d = describeStatus(status);
  const rows = [
    ['Durum', d.text],
    ['Son senkronizasyon', status.lastSyncAt ? formatDateTime(status.lastSyncAt) : 'Henüz yok'],
    ['Gönderilmeyi bekleyen', String(status.pending)]
  ];
  if (status.lastError) rows.push(['Son hata', `${status.lastError.message}${status.lastError.code ? ` (${status.lastError.code})` : ''} · ${formatDateTime(status.lastError.at)}`]);
  if (status.nextRetryAt) rows.push(['Yeniden deneme', formatDateTime(new Date(status.nextRetryAt).toISOString())]);
  const testResult = el('p', { class: 'small', 'aria-live': 'polite' });
  replace(syncStatusBody,
    el('dl', { class: 'kv' }, rows.flatMap(([k, v]) => [el('dt', null, k), el('dd', null, v)])),
    el('div', { class: 'row' }, button('Firebase bağlantısını dene', async () => {
      testResult.textContent = 'Deneniyor…';
      testResult.className = 'small';
      const res = await testConnection(await getKey());
      testResult.textContent = res.ok ? `Bağlantı başarılı (${res.ms} ms).` : res.message;
      testResult.className = `small ${res.ok ? 'text-green' : 'text-red'}`;
    }, { iconName: 'cloud', className: 'btn-small' })),
    testResult);
}

function valuePreview(v) {
  if (v === null || v === undefined || v === '') return '—';
  if (Array.isArray(v)) return `${v.length} madde`;
  if (typeof v === 'object') return 'ayrıntılı bilgi';
  if (typeof v === 'boolean') return v ? 'evet' : 'hayır';
  const s = String(v);
  return s.length > 60 ? `${s.slice(0, 59)}…` : s;
}

async function renderConflicts() {
  const list = await getConflicts();
  if (!list.length) {
    replace(conflictsBody, el('p', { class: 'muted small' }, 'Çakışma yok.'));
    return;
  }
  replace(conflictsBody, el('p', { class: 'small' }, 'Aynı kayıt hem bu cihazda hem bulutta farklı değiştirilmiş. Hangisinin kalacağını seç.'),
    el('ul', { class: 'list' }, list.map((c) => {
      const local = c.local;
      const remote = c.remote;
      const fields = diffFields(local, remote);
      return el('li', { class: 'list-item conflict-item' },
        el('div', { class: 'item-main' },
          el('p', { class: 'item-title' }, `${STORE_LABELS[c.store] || c.store}: ${recordTitle(c.store, local || remote)}`),
          el('div', { class: 'table-wrap mt' }, el('table', { class: 'table' },
            el('thead', null, el('tr', null, el('th', null, 'Alan'), el('th', null, 'Bu cihazda'), el('th', null, 'Bulutta'))),
            el('tbody', null,
              el('tr', null, el('td', null, 'Son değişiklik'), el('td', null, local ? formatDateTime(local.updatedAt) : '—'), el('td', null, remote ? formatDateTime(remote.updatedAt) : '—')),
              el('tr', null, el('td', null, 'Silinmiş'), el('td', null, local && local.deleted ? 'Evet' : 'Hayır'), el('td', null, remote && remote.deleted ? 'Evet' : 'Hayır')),
              fields.filter((f) => f !== 'deleted').map((f) => el('tr', null, el('td', null, fieldLabel(c.store, f)), el('td', null, valuePreview(local && local[f])), el('td', null, valuePreview(remote && remote[f]))))))),
          el('div', { class: 'row mt' },
            button('Bu cihazdakini tut', async () => {
              await resolveConflict(c.key, 'local');
              toast('Bu cihazdaki sürüm buluta yazılacak.', { kind: 'success' });
              renderConflicts();
            }, { className: 'btn-small' }),
            button('Buluttakini al', async () => {
              await resolveConflict(c.key, 'remote');
              toast('Buluttaki sürüm alındı.', { kind: 'success' });
              renderConflicts();
            }, { className: 'btn-small' }))));
    })));
}

// --- Depolama ---

async function storageSection() {
  const body = el('div', { class: 'stack' }, loadingState());
  const node = sectionCard('storage', 'Cihazdaki depolama', body);
  const render = async () => {
    const info = await db.getStorageInfo();
    const counts = [];
    for (const store of SYNCED_STORES) {
      if (['settings'].includes(store)) continue;
      counts.push([STORE_LABELS[store], await countActiveRecords(store)]);
    }
    const img = await imageStats();
    const vaultCount = await db.count('vault');
    const selfTest = el('p', { class: 'small', 'aria-live': 'polite' });
    replace(body,
      el('dl', { class: 'kv' },
        el('dt', null, 'Şema sürümü'), el('dd', null, String(info.dbVersion)),
        el('dt', null, 'Kullanılan alan'), el('dd', null, info.usage !== null ? `${formatBytes(info.usage)}${info.quota ? ` / ${formatBytes(info.quota)}` : ''}` : 'Bilinmiyor'),
        el('dt', null, 'Kalıcı depolama'), el('dd', null, info.persisted === null ? 'Desteklenmiyor' : info.persisted ? 'Açık (tarayıcı verileri kendiliğinden silmez)' : 'Kapalı'),
        el('dt', null, 'Fotoğraflar'), el('dd', null, `${formatNumber(img.count)} fotoğraf · ${formatBytes(img.bytes)}`),
        el('dt', null, 'Gizli Kasa'), el('dd', null, `${vaultCount} şifreli kayıt`)),
      el('h3', { class: 'section-title' }, 'Kayıt sayıları'),
      el('dl', { class: 'kv' }, counts.flatMap(([k, v]) => [el('dt', null, k), el('dd', null, String(v))])),
      el('div', { class: 'row mt' },
        button('Kalıcı depolama iste', async () => {
          const res = await db.requestPersistentStorage();
          toast(res === null ? 'Bu tarayıcı kalıcı depolamayı desteklemiyor.' : res ? 'Kalıcı depolama açıldı.' : 'Tarayıcı izin vermedi. Uygulamayı ana ekrana ekleyince genellikle izin verilir.', { kind: res ? 'success' : 'warning' });
          render();
        }, { className: 'btn-small' }),
        button('Depolama testi', async () => {
          selfTest.textContent = 'Deneniyor…';
          const res = await db.runSelfTest();
          selfTest.textContent = res.ok ? `Depolama sorunsuz çalışıyor (${res.steps.join(', ')}).` : `Depolama testi başarısız: ${res.steps.length ? `${res.steps.join(', ')} çalıştı, sonraki adım` : 'ilk adım'} başarısız.`;
          selfTest.className = `small ${res.ok ? 'text-green' : 'text-red'}`;
        }, { className: 'btn-small' }),
        button('Kullanılmayan fotoğrafları temizle', async () => {
          try {
            const res = await cleanupOrphans(60 * 60 * 1000);
            toast(res.count ? `${res.count} fotoğraf silindi (${formatBytes(res.bytes)}).` : 'Temizlenecek fotoğraf yok.', { kind: 'success' });
            render();
          } catch (err) {
            toastError('settings.cleanup', err);
          }
        }, { className: 'btn-small' })),
      el('p', { class: 'muted small' }, 'iPhone\'da Safari, uzun süre açılmayan sitelerin verilerini silebilir. Kalıcı depolama iste ve düzenli yedek al.'),
      selfTest);
  };
  render().catch((err) => toastError('settings.storage', err));
  return node;
}

// --- Yedek özeti ---

async function backupSection() {
  const last = await db.getMeta('backup:lastAt');
  const days = last ? Math.floor((Date.now() - Date.parse(last)) / 86400000) : null;
  return sectionCard('backup-summary', 'Yedekleme',
    el('p', { class: days === null || days > 30 ? 'text-yellow' : '' },
      last ? `Son yedek: ${formatDateTime(last)} (${days === 0 ? 'bugün' : `${days} gün önce`})` : 'Henüz yedek alınmadı.'),
    days === null || days > 30 ? el('p', { class: 'muted small' }, 'Fotoğrafların ve Gizli Kasa yalnızca bu cihazda; telefon değiştirirken onları taşımanın tek yolu yedektir.') : null,
    el('div', null, el('a', { class: 'btn btn-secondary', href: pageUrl('backup') }, icon('backup'), el('span', null, 'Yedekleme sayfası'))));
}

// --- Uygulama ---

async function appSection() {
  const offline = el('dd', null, 'Denetleniyor…');
  const workerVer = el('dd', null, '…');
  const installHolder = el('div', { class: 'row' });
  const node = sectionCard('app', 'Uygulama',
    el('dl', { class: 'kv' },
      el('dt', null, 'Sürüm'), el('dd', null, APP_VERSION),
      el('dt', null, 'Çevrimdışı önbellek'), workerVer,
      el('dt', null, 'Açılış biçimi'), el('dd', null, isStandalone() ? 'Ana ekran uygulaması' : 'Tarayıcı sekmesi'),
      el('dt', null, 'Çevrimdışı durumu'), offline,
      el('dt', null, 'Bağlantı'), el('dd', null, window.isSecureContext ? 'Güvenli (HTTPS)' : 'Güvensiz')),
    isIOS() && !isStandalone() ? el('div', { class: 'notice notice-info' }, icon('info'), el('span', null, 'iPhone\'da ana ekrana eklemek için Safari\'de Paylaş düğmesine dokun, ardından "Ana Ekrana Ekle"yi seç.')) : null,
    installHolder);
  const renderInstall = () => {
    replace(installHolder,
      canInstall() ? button('Uygulamayı yükle', async () => {
        const outcome = await promptInstall();
        if (outcome === 'accepted') toast('Uygulama yüklendi.', { kind: 'success' });
        renderInstall();
      }, { kind: 'primary', iconName: 'download' }) : null,
      button('Güncellemeleri denetle', async () => {
        const res = await checkForUpdate();
        if (!res.supported) toast('Bu tarayıcı çevrimdışı çalışmayı desteklemiyor.', { kind: 'warning' });
        else if (res.waiting) toast('Yeni sürüm indiriliyor; hazır olunca "Güncelle" bildirimi çıkacak.');
        else toast('Uygulama güncel.', { kind: 'success' });
      }, { iconName: 'refresh' }));
  };
  renderInstall();
  window.addEventListener('jozh:install-available', renderInstall);
  getOfflineStatus().then((s) => {
    offline.textContent = { ready: 'Hazır: internet olmadan açılır', partial: 'Kısmen hazır', preparing: 'Hazırlanıyor (sayfayı bir kez yenile)', unsupported: 'Desteklenmiyor' }[s];
  });
  getWorkerVersion().then((v) => {
    workerVer.textContent = v ? `${v.version} (${v.assetCount} dosya)` : 'Henüz yok';
  });
  return node;
}

async function setup() {
  replace(main, loadingState());
  const syncSection = sectionCard('sync', 'Bulut senkronizasyonu', syncBody,
    el('h3', { class: 'section-title' }, 'Senkronizasyon durumu'), syncStatusBody,
    el('h3', { class: 'section-title', id: 'conflicts' }, 'Çakışmalar'), conflictsBody);
  const vaultSection = sectionCard('vault-settings', 'Gizli Kasa',
    el('p', { class: 'muted small' }, 'Kasa içerikleri cihazda şifrelenir ve hiçbir zaman buluta gönderilmez.'),
    el('div', null, el('a', { class: 'btn btn-secondary', href: pageUrl('vaultLogin', 'change') }, icon('lock'), el('span', null, 'Gizli Kasa PIN\'ini değiştir'))));
  replace(main, el('div', { class: 'settings-layout' },
    await appearanceSection(),
    syncSection,
    vaultSection,
    await storageSection(),
    await backupSection(),
    await appSection()));
  await renderSync();
  await renderConflicts();
  let lastConflicts = -1;
  onSyncStatus((s) => {
    renderSyncStatus(s);
    if (s.conflicts !== lastConflicts) {
      lastConflicts = s.conflicts;
      renderConflicts();
    }
  });
  if (location.hash === '#sync' || location.hash === '#conflicts') {
    document.getElementById(location.hash.slice(1)).scrollIntoView();
  }
}

const ready = await initApp({ page: 'settings', title: 'Ayarlar' });
if (ready) await setup();
