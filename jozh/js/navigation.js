// Menü: full (etiketli yan menü), rail (simgeli dar menü), drawer (çekmece).
import { el, clear } from './ui.js';
import { icon } from './utils/icons.js';
import { pageUrl } from './router.js';

const MAIN_ITEMS = [
  ['dashboard', 'Ana panel', 'home'],
  ['profile', 'Profilim', 'user'],
  ['partner', 'Sevdiğim kadın', 'partner'],
  ['diary', 'Günlük', 'book'],
  ['dreams', 'Hayaller ve hedefler', 'target'],
  ['plans', 'Planlar', 'map'],
  ['calendar', 'Takvim', 'calendar'],
  ['notes', 'Notlar', 'note'],
  ['finance', 'Gelir ve gider', 'wallet'],
  ['interview', 'Mülakat hazırlık', 'medal'],
  ['sport', 'Antrenman', 'run'],
  ['kisla', 'Kışla', 'flag']
];

const BOTTOM_ITEMS = [
  ['vaultLogin', 'Gizli Kasa', 'shield'],
  ['backup', 'Yedekleme', 'backup'],
  ['settings', 'Ayarlar', 'settings']
];

const root = document.documentElement;

function storedNavPref() {
  try {
    return localStorage.getItem('jozh.nav') || 'expanded';
  } catch {
    return 'expanded';
  }
}

export function computeNavMode() {
  const w = window.innerWidth;
  const h = window.innerHeight;
  if (w <= 699) return 'drawer';
  if (h <= 500) return 'rail';
  return storedNavPref() === 'collapsed' ? 'rail' : 'full';
}

function navLink(page, label, iconName, current) {
  const active = page === current || (page === 'vaultLogin' && current === 'vault');
  return el('li', null,
    el('a', {
      class: `nav-link${active ? ' is-active' : ''}`,
      href: pageUrl(page),
      'aria-current': active ? 'page' : null,
      title: label,
      dataset: { page }
    }, icon(iconName, { size: 20 }), el('span', { class: 'nav-label' }, label)));
}

export function renderNavigation({ current, onLock }) {
  const nav = document.getElementById('app-nav');
  if (!nav) return;
  clear(nav);
  nav.setAttribute('aria-label', 'Ana menü');

  const collapseBtn = el('button', { type: 'button', class: 'nav-link nav-collapse', 'aria-label': 'Menüyü daralt', title: 'Menüyü daralt' },
    icon('sidebar', { size: 20 }), el('span', { class: 'nav-label' }, 'Menüyü daralt'));
  collapseBtn.addEventListener('click', () => {
    const next = storedNavPref() === 'collapsed' ? 'expanded' : 'collapsed';
    try {
      localStorage.setItem('jozh.nav', next);
    } catch {
      // yok say
    }
    applyMode();
  });

  const lockBtn = el('button', { type: 'button', class: 'nav-link nav-lock', title: 'Kilitle' },
    icon('lock', { size: 20 }), el('span', { class: 'nav-label' }, 'Kilitle'));
  lockBtn.addEventListener('click', onLock);

  nav.append(
    el('div', { class: 'nav-brand' },
      el('span', { class: 'brand-mark', 'aria-hidden': 'true' }, 'J'),
      el('span', { class: 'nav-label brand-name' }, 'JOZH'),
      el('button', { type: 'button', class: 'btn-icon nav-close', 'aria-label': 'Menüyü kapat', onclick: closeDrawer }, icon('close'))),
    el('ul', { class: 'nav-list' }, MAIN_ITEMS.map(([p, l, i]) => navLink(p, l, i, current))),
    el('ul', { class: 'nav-list nav-bottom' },
      BOTTOM_ITEMS.map(([p, l, i]) => navLink(p, l, i, current)),
      el('li', null, lockBtn),
      el('li', { class: 'collapse-item' }, collapseBtn))
  );

  const toggle = document.getElementById('nav-toggle');
  if (toggle) {
    clear(toggle).append(icon('menu'));
    toggle.addEventListener('click', openDrawer);
  }
  let backdrop = document.querySelector('.nav-backdrop');
  if (!backdrop) {
    backdrop = el('div', { class: 'nav-backdrop', hidden: true });
    backdrop.addEventListener('click', closeDrawer);
    document.body.append(backdrop);
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && root.dataset.navOpen === 'true') closeDrawer();
  });
  window.addEventListener('resize', applyMode);
  applyMode();
}

function applyMode() {
  const mode = computeNavMode();
  root.dataset.navMode = mode;
  const collapseBtn = document.querySelector('.nav-collapse');
  if (collapseBtn) {
    const collapsed = storedNavPref() === 'collapsed';
    const text = collapsed ? 'Menüyü genişlet' : 'Menüyü daralt';
    collapseBtn.setAttribute('aria-label', text);
    collapseBtn.title = text;
    collapseBtn.querySelector('.nav-label').textContent = text;
  }
  if (mode !== 'drawer') closeDrawer();
}

export function openDrawer() {
  root.dataset.navOpen = 'true';
  const backdrop = document.querySelector('.nav-backdrop');
  if (backdrop) backdrop.hidden = false;
  const first = document.querySelector('#app-nav .nav-link');
  if (first) first.focus();
}

export function closeDrawer() {
  if (root.dataset.navOpen !== 'true') return;
  root.dataset.navOpen = 'false';
  const backdrop = document.querySelector('.nav-backdrop');
  if (backdrop) backdrop.hidden = true;
  const toggle = document.getElementById('nav-toggle');
  if (toggle && root.dataset.navMode === 'drawer') toggle.focus();
}
