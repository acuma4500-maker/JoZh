// Gizli Kasa giriş ekranı: kurulum, açma, PIN değiştirme (#change), "PIN'imi unuttum".
import { initApp } from '../app.js';
import * as vault from '../storage/vault-storage.js';
import { createPinPad, formatWait } from '../components/pin-pad.js';
import { el, confirmDialog, toast, toastError } from '../ui.js';
import { go, takeHash } from '../router.js';

const main = document.getElementById('main');
let pad = null;
let mode = 'unlock';
let step = 0;
let pins = [];

function securityInfo() {
  return el('details', { class: 'vault-security' },
    el('summary', null, 'Güvenlik hakkında'),
    el('ul', { class: 'bullets' },
      el('li', null, 'Kasa içerikleri ve fotoğrafları bu cihazda AES-256-GCM ile şifrelenir; buluta, ana panele ve galeriye asla karışmaz.'),
      el('li', null, 'PIN unutulursa kurtarma yoktur. Kasa yalnızca sıfırlanabilir; içerikler kaybolur. Yedek dosyası kasayı şifreli hâliyle taşır.'),
      el('li', null, '4 haneli PIN, cihazın dosyalarına teknik olarak erişebilen birine karşı zayıftır (10.000 olasılık). Bekleme süresi yalnızca bu ekranı korur.'),
      el('li', null, 'Kasa açıkken çözülmüş içerik tarayıcı belleğindedir; tarayıcının belleği tamamen temizleyeceği garanti edilemez. İşin bitince kasayı kilitle.')));
}

function showLockout(until) {
  pad.lockUntil(until, (left) => `Çok fazla yanlış deneme. ${formatWait(left)} sonra tekrar dene.`);
}

function failure(res) {
  if (res.lockedUntil) {
    pad.error('PIN yanlış.');
    showLockout(res.lockedUntil);
  } else {
    pad.error(res.remainingFree > 0 ? `PIN yanlış. Beklemeden ${res.remainingFree} deneme hakkın kaldı.` : 'PIN yanlış.');
  }
}

async function forgot() {
  const ok = await confirmDialog({
    title: 'Kasa PIN\'ini unuttum',
    message: 'Kasa PIN\'i kurtarılamaz. Devam edersen yalnızca Gizli Kasa sıfırlanır: içindeki bütün içerikler ve fotoğraflar kalıcı olarak silinir. Diğer verilerine dokunulmaz.',
    confirmText: 'Kasayı sıfırla',
    danger: true,
    requireText: 'SİL'
  });
  if (!ok) return;
  try {
    await vault.reset();
    toast('Gizli Kasa sıfırlandı. Yeni bir kasa PIN\'i belirle.');
    startSetup();
  } catch (err) {
    toastError('vault.reset', err);
  }
}

function setTexts(title, prompt) {
  pad.reset();
  pad.setTitle(title);
  pad.setPrompt(prompt);
}

function startSetup() {
  mode = 'setup';
  step = 0;
  pins = [];
  setTexts('Gizli Kasa kurulumu', 'Kasa için 4 haneli PIN belirle');
  pad.setMessage('Açılış PIN\'inden farklı bir PIN seçmen önerilir.');
  pad.setLinks([{ label: 'Ana panele dön', onClick: () => go('dashboard') }]);
}

function startUnlock() {
  mode = 'unlock';
  setTexts('Gizli Kasa', 'Kasa PIN\'ini gir');
  pad.setMessage('');
  pad.setLinks([
    { label: 'PIN\'imi unuttum', onClick: forgot },
    { label: 'PIN\'i değiştir', onClick: startChange },
    { label: 'Ana panele dön', onClick: () => go('dashboard') }
  ]);
}

function startChange() {
  mode = 'change';
  step = 0;
  pins = [];
  setTexts('Kasa PIN\'ini değiştir', 'Mevcut kasa PIN\'ini gir');
  pad.setMessage('');
  pad.setLinks([{ label: 'Vazgeç', onClick: startUnlock }]);
}

async function onComplete(pin) {
  if (mode === 'setup') {
    if (step === 0) {
      if (vault.isWeakPin(pin)) {
        pad.error('Aynı ya da ardışık rakamlardan oluşan PIN kullanılamaz.');
        return;
      }
      pins = [pin];
      step = 1;
      setTexts('Gizli Kasa kurulumu', 'Aynı PIN\'i tekrar gir');
      return;
    }
    if (pin !== pins[0]) {
      step = 0;
      pins = [];
      setTexts('Gizli Kasa kurulumu', 'Kasa için 4 haneli PIN belirle');
      pad.error('İki PIN aynı değil. Baştan gir.');
      return;
    }
    pad.setBusy(true, 'Kasa hazırlanıyor…');
    try {
      const key = await vault.setup(pin);
      pad.success('Kasa hazır.');
      await vault.handOff(key);
      go('vault');
    } catch (err) {
      pad.setBusy(false);
      pad.error('Kasa kurulamadı.');
      toastError('vault.setup', err);
    }
    return;
  }

  if (mode === 'unlock') {
    pad.setMessage('Kontrol ediliyor…');
    try {
      const res = await vault.unlock(pin);
      if (!res.ok) {
        failure(res);
        return;
      }
      pad.success('');
      await vault.handOff(res.key);
      go('vault');
    } catch (err) {
      pad.error('Kasa açılamadı.');
      toastError('vault.unlock', err);
    }
    return;
  }

  // PIN değiştir: mevcut → yeni → yeni tekrar
  if (step === 0) {
    pins = [pin];
    step = 1;
    setTexts('Kasa PIN\'ini değiştir', 'Yeni kasa PIN\'ini gir');
    return;
  }
  if (step === 1) {
    if (vault.isWeakPin(pin)) {
      pad.error('Aynı ya da ardışık rakamlardan oluşan PIN kullanılamaz.');
      return;
    }
    pins.push(pin);
    step = 2;
    setTexts('Kasa PIN\'ini değiştir', 'Yeni PIN\'i tekrar gir');
    return;
  }
  if (pin !== pins[1]) {
    pins = [pins[0]];
    step = 1;
    setTexts('Kasa PIN\'ini değiştir', 'Yeni kasa PIN\'ini gir');
    pad.error('Yeni PIN\'ler aynı değil. Yeni PIN\'i baştan gir.');
    return;
  }
  pad.setBusy(true, 'PIN değiştiriliyor…');
  try {
    const res = await vault.changePin(pins[0], pins[1]);
    pad.setBusy(false);
    if (!res.ok) {
      startChange();
      failure(res);
      if (!res.lockedUntil) pad.setMessage('Mevcut PIN yanlış. Baştan başla.', 'error');
      return;
    }
    toast('Kasa PIN\'i değiştirildi.', { kind: 'success' });
    startUnlock();
    pad.setMessage('PIN değiştirildi. Yeni PIN ile kasayı açabilirsin.', 'success');
  } catch (err) {
    pad.setBusy(false);
    startChange();
    toastError('vault.change', err);
  }
}

async function setup() {
  pad = createPinPad({ mount: main, brand: 'JOZH · Gizli Kasa', title: 'Gizli Kasa', prompt: '', onComplete });
  main.querySelector('.pin-info').append(securityInfo());
  const configured = await vault.isConfigured();
  const wantsChange = takeHash('change');
  if (!configured) startSetup();
  else if (wantsChange) startChange();
  else startUnlock();
  const state = await vault.getAttemptState();
  if (configured && state.lockedUntil) showLockout(state.lockedUntil);
  window.addEventListener('hashchange', async () => {
    if (takeHash('change') && (await vault.isConfigured())) startChange();
  });
}

const ready = await initApp({ page: 'vault-login', title: 'Gizli Kasa', nav: false, sync: false });
if (ready) await setup();
