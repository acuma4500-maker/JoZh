// Her sayfanın ortak başlatıcısı: güvenli bağlam, veritabanı, kilit kontrolü, menü, senkronizasyon, PWA.
import * as db from './storage/local-db.js';
import * as appLock from './storage/app-lock.js';
import { isCryptoAvailable } from './storage/encryption.js';
import { renderNavigation } from './navigation.js';
import { el, clear, toast, errorState, friendlyError } from './ui.js';
import { icon } from './utils/icons.js';
import { replaceWith, go, pageUrl } from './router.js';
import { logError } from './utils/logger.js';
import { registerServiceWorker } from './pwa.js';
import { startSync, onSyncStatus, describeStatus } from './firebase/sync-manager.js';
import { scheduleWeeklyCleanup } from './storage/image-storage.js';

export const APP_VERSION = '1.2.0';

const root = document.documentElement;
let activityStarted = false;

function showFatal(title, message, retry) {
  root.dataset.auth = 'ok';
  const main = document.getElementById('main') || document.body;
  clear(main);
  const box = el('div', { class: 'fatal' },
    icon('alert', { size: 32 }),
    el('h2', null, title),
    el('p', null, message));
  if (retry) box.append(el('button', { type: 'button', class: 'btn btn-primary', onclick: retry }, 'Tekrar dene'));
  main.append(box);
}

function insecureMessage() {
  const h1 = document.querySelector('h1');
  if (h1 && !h1.textContent) h1.textContent = 'JOZH';
  showFatal(
    'Güvenli bağlantı gerekli',
    'JOZH yalnızca HTTPS üzerinden (ya da bilgisayarda localhost ile) çalışır. HTTP bağlantısında tarayıcı şifrelemeyi (Web Crypto) ve çevrimdışı çalışmayı kapatır; PIN ekranı ve Gizli Kasa açılamaz. Uygulamayı https:// ile başlayan adresten aç.'
  );
}

function startActivityTracking() {
  if (activityStarted) return;
  activityStarted = true;
  const touch = () => appLock.touchSession();
  for (const type of ['pointerdown', 'keydown', 'scroll']) {
    window.addEventListener(type, touch, { passive: true, capture: true });
  }
  const check = () => {
    if (!appLock.isSessionValid()) {
      appLock.lock();
      replaceWith('login');
    }
  };
  setInterval(check, 15000);
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') check();
  });
  window.addEventListener('pageshow', (e) => {
    if (e.persisted) check();
  });
}

export function lockNow() {
  appLock.lock();
  replaceWith('login');
}

function renderSyncIndicator() {
  const holder = document.getElementById('sync-status');
  if (!holder) return;
  const link = el('a', { class: 'sync-indicator', href: `${pageUrl('settings')}#sync`, dataset: { state: 'local' } });
  holder.append(link);
  onSyncStatus((status) => {
    const d = describeStatus(status);
    link.dataset.state = d.state;
    clear(link).append(icon(d.icon, { size: 16 }), el('span', { class: 'sync-text' }, d.text));
    link.title = d.text;
  });
}

function setTitle(title) {
  if (!title) return;
  const h1 = document.querySelector('.app-header h1, h1.page-title');
  if (h1) h1.textContent = title;
  document.title = `${title} · JOZH`;
}

// options: { page, title, requireAuth = true, nav = true, sync = true }
export async function initApp({ page, title, requireAuth = true, nav = true, sync = true } = {}) {
  root.dataset.page = page || '';
  setTitle(title);

  if (!isCryptoAvailable()) {
    insecureMessage();
    return false;
  }

  try {
    await db.open();
  } catch (err) {
    logError('db.open', err);
    showFatal('Cihaz depolaması açılamadı', `${friendlyError(err)} Gizli pencerede ya da depolaması kapalı bir tarayıcıda olabilirsin.`, () => location.reload());
    return false;
  }

  window.addEventListener('jozh:db-blocked', () => {
    toast('Başka bir sekmede açık JOZH, veritabanı güncellemesini engelliyor. Diğer sekmeleri kapatıp sayfayı yenile.', { kind: 'warning', duration: 0 });
  });
  window.addEventListener('jozh:db-versionchange', () => {
    toast('Uygulama başka bir sekmede güncellendi. Devam etmek için sayfayı yenile.', { kind: 'warning', actionLabel: 'Yenile', onAction: () => location.reload(), duration: 0 });
  });

  if (requireAuth) {
    let configured = false;
    try {
      configured = await appLock.isConfigured();
    } catch (err) {
      logError('appLock.isConfigured', err);
    }
    if (!configured || !appLock.isSessionValid()) {
      appLock.lock();
      replaceWith('login');
      return false;
    }
    appLock.touchSession(true);
    startActivityTracking();
  }

  root.dataset.auth = 'ok';

  if (nav) renderNavigation({ current: page, onLock: lockNow });
  renderSyncIndicator();

  try {
    if (await db.getMeta('restore:inProgress')) {
      toast('Önceki geri yükleme yarıda kalmış. Veriler eksik olabilir; Yedekleme sayfasından yedeği yeniden geri yükle.', {
        kind: 'warning', actionLabel: 'Yedekleme', onAction: () => go('backup'), duration: 0
      });
    }
  } catch (err) {
    logError('restore.check', err);
  }

  registerServiceWorker();

  if (requireAuth && sync) {
    startSync();
    window.addEventListener('jozh:remote-change', () => {
      toast('Buluttan güncel veriler alındı.', { actionLabel: 'Yenile', onAction: () => location.reload() });
    });
    window.addEventListener('jozh:sync-conflict', () => {
      toast('Senkronizasyonda çakışma var.', { kind: 'warning', actionLabel: 'Gör', onAction: () => go('settings', 'sync') });
    });
    scheduleWeeklyCleanup();
  }
  return true;
}

export function renderLoadError(container, err, retry) {
  logError('load', err);
  clear(container).append(errorState(`Veriler okunamadı. ${friendlyError(err)}`, retry));
}
