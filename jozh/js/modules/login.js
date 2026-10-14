// Açılış PIN ekranı: ilk kurulum (iki kez tuşla), açma, "PIN'imi unuttum".
import { initApp } from '../app.js';
import * as appLock from '../storage/app-lock.js';
import { createPinPad, formatWait } from '../components/pin-pad.js';
import { confirmDialog, toastError } from '../ui.js';
import { replaceWith } from '../router.js';

const main = document.getElementById('main');
let pad = null;
let firstPin = null;

function goHome() {
  appLock.startSession();
  setTimeout(() => replaceWith('dashboard'), 250);
}

async function forgot() {
  const ok = await confirmDialog({
    title: 'PIN\'imi unuttum',
    message: 'Açılış PIN\'i kurtarılamaz. Devam edersen bu cihazdaki bütün JOZH verileri (kayıtlar, fotoğraflar, Gizli Kasa) silinir ve kurulum yeniden başlar.\nVerilerini daha önce aldığın bir yedek dosyasından ya da senkronizasyon anahtarınla geri getirebilirsin.',
    confirmText: 'Bu cihazdaki verileri sil',
    danger: true,
    requireText: 'SİL'
  });
  if (!ok) return;
  try {
    await appLock.resetDevice();
    location.reload();
  } catch (err) {
    toastError('login.reset', err);
  }
}

function showLockout(until) {
  pad.lockUntil(until, (left) => `Çok fazla yanlış deneme. ${formatWait(left)} sonra tekrar dene.`);
}

async function setupFlow(pin) {
  if (firstPin === null) {
    if (appLock.isWeakPin(pin)) {
      pad.error('Aynı ya da ardışık rakamlardan oluşan PIN kullanılamaz (1111, 1234 gibi).');
      return;
    }
    firstPin = pin;
    pad.reset();
    pad.setTitle('PIN\'i onayla');
    pad.setPrompt('Aynı PIN\'i tekrar gir');
    pad.setMessage('');
    return;
  }
  if (pin !== firstPin) {
    firstPin = null;
    pad.setTitle('PIN belirle');
    pad.setPrompt('Açılış için 4 haneli PIN belirle');
    pad.error('İki PIN aynı değil. Baştan gir.');
    return;
  }
  pad.setBusy(true, 'PIN kaydediliyor…');
  try {
    await appLock.setupPin(pin);
    firstPin = null;
    pad.success('PIN kaydedildi.');
    goHome();
  } catch (err) {
    firstPin = null;
    pad.setBusy(false);
    pad.error('PIN kaydedilemedi. Tekrar dene.');
    toastError('login.setup', err);
  }
}

async function unlockFlow(pin) {
  pad.setMessage('Kontrol ediliyor…');
  try {
    const res = await appLock.verifyPin(pin);
    if (res.ok) {
      pad.success('');
      goHome();
      return;
    }
    if (res.lockedUntil) {
      pad.error('PIN yanlış.');
      showLockout(res.lockedUntil);
      return;
    }
    pad.error(res.remainingFree > 0
      ? `PIN yanlış. Beklemeden ${res.remainingFree} deneme hakkın kaldı.`
      : 'PIN yanlış.');
  } catch (err) {
    pad.error('PIN kontrol edilemedi.');
    toastError('login.verify', err);
  }
}

async function setup() {
  const configured = await appLock.isConfigured();
  if (configured && appLock.isSessionValid()) {
    replaceWith('dashboard');
    return;
  }
  appLock.lock();
  pad = createPinPad({
    mount: main,
    title: configured ? 'Hoş geldin' : 'PIN belirle',
    prompt: configured ? 'PIN\'ini gir' : 'Açılış için 4 haneli PIN belirle',
    onComplete: (pin) => (configured ? unlockFlow(pin) : setupFlow(pin))
  });
  if (configured) {
    pad.setLinks([{ label: 'PIN\'imi unuttum', onClick: forgot }]);
    const state = await appLock.getAttemptState();
    if (state.lockedUntil) showLockout(state.lockedUntil);
  } else {
    pad.setMessage('PIN\'i yalnızca sen bileceksin; kurtarılamaz. Bunu unutma.');
  }
}

const ready = await initApp({ page: 'login', title: 'Kilit', requireAuth: false, nav: false, sync: false });
if (ready) await setup();
