// Service Worker kaydı, güncelleme bildirimi, yükleme ve çevrimdışı durumu.
import { toast } from './ui.js';
import { logError } from './utils/logger.js';

let registrationPromise = null;
let deferredPrompt = null;
let userRequestedUpdate = false;
let registered = false;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  window.dispatchEvent(new CustomEvent('jozh:install-available'));
});

export function isStandalone() {
  return window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
}

export function isIOS() {
  return /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
}

export function canInstall() {
  return Boolean(deferredPrompt);
}

export async function promptInstall() {
  if (!deferredPrompt) return null;
  const e = deferredPrompt;
  deferredPrompt = null;
  e.prompt();
  const choice = await e.userChoice;
  return choice.outcome;
}

function notifyWaiting(worker) {
  toast('Uygulamanın yeni sürümü hazır.', {
    actionLabel: 'Güncelle',
    duration: 0,
    onAction: () => {
      userRequestedUpdate = true;
      worker.postMessage({ type: 'SKIP_WAITING' });
    }
  });
}

function watchRegistration(reg) {
  if (!reg) return;
  if (reg.waiting && navigator.serviceWorker.controller) notifyWaiting(reg.waiting);
  reg.addEventListener('updatefound', () => {
    const worker = reg.installing;
    if (!worker) return;
    worker.addEventListener('statechange', () => {
      // İlk kurulumda (henüz denetleyen yokken) bildirim ve yenileme yapılmaz.
      if (worker.state === 'installed' && navigator.serviceWorker.controller) notifyWaiting(worker);
    });
  });
}

export function registerServiceWorker() {
  if (registered || !('serviceWorker' in navigator)) return registrationPromise;
  registered = true;
  let reloaded = false;
  navigator.serviceWorker.addEventListener('controllerchange', () => {
    if (!userRequestedUpdate || reloaded) return;
    reloaded = true;
    location.reload();
  });
  registrationPromise = navigator.serviceWorker
    .register(new URL('../sw.js', import.meta.url))
    .then((reg) => {
      watchRegistration(reg);
      return reg || null;
    })
    .catch((err) => {
      logError('sw.register', err);
      return null;
    });
  return registrationPromise;
}

async function getRegistration() {
  if (!('serviceWorker' in navigator)) return null;
  return (await registrationPromise) || navigator.serviceWorker.getRegistration();
}

export async function checkForUpdate() {
  const reg = await getRegistration();
  if (!reg) return { supported: false };
  await reg.update();
  return { supported: true, waiting: Boolean(reg.waiting || reg.installing) };
}

function askWorker(worker, message) {
  return new Promise((resolve) => {
    const channel = new MessageChannel();
    const timer = setTimeout(() => resolve(null), 2000);
    channel.port1.onmessage = (e) => {
      clearTimeout(timer);
      resolve(e.data);
    };
    worker.postMessage(message, [channel.port2]);
  });
}

export async function getWorkerVersion() {
  if (!('serviceWorker' in navigator) || !navigator.serviceWorker.controller) return null;
  return askWorker(navigator.serviceWorker.controller, { type: 'GET_VERSION' });
}

// 'ready' | 'partial' | 'preparing' | 'unsupported'
export async function getOfflineStatus() {
  if (!('serviceWorker' in navigator) || !('caches' in window)) return 'unsupported';
  if (!navigator.serviceWorker.controller) return 'preparing';
  const info = await getWorkerVersion();
  if (!info) return 'preparing';
  try {
    const cache = await caches.open(`jozh-app-${info.version}`);
    const keys = await cache.keys();
    return keys.length >= info.assetCount ? 'ready' : 'partial';
  } catch {
    return 'partial';
  }
}
