// index.html: kilit açıksa ana panele, değilse açılış ekranına gider.
import { initApp } from './app.js';
import * as appLock from './storage/app-lock.js';
import { el, replace } from './ui.js';
import { replaceWith } from './router.js';

const main = document.getElementById('main');
replace(main, el('div', { class: 'lock-screen' }, el('div', { class: 'stack' }, el('h1', { class: 'page-title' }, 'JOZH'), el('p', { class: 'muted' }, 'Açılıyor…'))));

async function setup() {
  const configured = await appLock.isConfigured();
  replaceWith(configured && appLock.isSessionValid() ? 'dashboard' : 'login');
}

const ready = await initApp({ page: 'index', title: 'JOZH', requireAuth: false, nav: false, sync: false });
if (ready) await setup();
