// Ana panel: gerçek verilerle kartlar. Bir kartın verisi okunamazsa yalnızca o kart hata gösterir.
import { initApp } from '../app.js';
import { getSingleton, listRecords } from '../storage/records.js';
import { getMeta } from '../storage/local-db.js';
import { el, replace, loadingState, errorState, progressBar, chip, iconButton } from '../ui.js';
import { icon } from '../utils/icons.js';
import { logError } from '../utils/logger.js';
import { pageUrl } from '../router.js';
import { todayISO, diffDays, formatDate, calcAge, relativeDayLabel, monthGrid, WEEKDAYS_SHORT_MON, formatMonthYear, addMonths, pad2 } from '../utils/dates.js';
import { formatMoney, initials, truncate, formatNumber } from '../utils/formatters.js';
import { isUpcomingOrOngoing, sortByStart, timingLabel, budgetLabel, isOnDay, planStart, planEnd } from '../utils/plan-helpers.js';
import { nextImportantDate } from '../utils/partner-helpers.js';
import { inMonth, totals, balances, savingsSummary } from '../utils/finance-helpers.js';
import { avatar } from '../components/photos.js';
import { renderDayPlans } from '../components/day-plans.js';
import { openPlanEditor } from '../components/plan-editor.js';
import { PLAN_TYPES } from '../utils/labels.js';

const main = document.getElementById('main');
const today = todayISO();

function card(id, title, link, linkText, extraClass = '') {
  const body = el('div', { class: 'card-body' }, loadingState());
  const node = el('section', { class: `card dash-card${extraClass ? ` ${extraClass}` : ''}`, 'aria-labelledby': `${id}-title` },
    el('div', { class: 'card-header' },
      el('h2', { id: `${id}-title` }, title),
      link ? el('a', { class: 'card-link', href: link }, linkText) : null),
    body);
  return { node, body };
}

async function fill(c, fn) {
  try {
    await fn(c.body);
  } catch (err) {
    logError('dashboard.card', err);
    replace(c.body, errorState('Bu kartın verisi okunamadı.', () => {
      replace(c.body, loadingState());
      fill(c, fn);
    }));
  }
}

async function profileCard(body) {
  const p = await getSingleton('profile');
  if (!p || (!p.firstName && !p.lastName && !p.birthDate)) {
    replace(body, el('p', { class: 'muted' }, 'Profil bilgilerin henüz yok. ', el('a', { href: pageUrl('profile') }, 'Profilini doldur')));
    return;
  }
  const age = calcAge(p.birthDate);
  const facts = [];
  if (age !== null) facts.push(`${age} yaş`);
  if (p.bloodType) facts.push(`Kan grubu ${p.bloodType}`);
  if (p.height) facts.push(`${p.height} cm`);
  if (p.weight) facts.push(`${formatNumber(p.weight, 1)} kg`);
  replace(body, el('div', { class: 'row' },
    avatar({ photoId: p.photoId, text: initials(p.firstName, p.lastName) }),
    el('div', { class: 'grow' },
      el('p', { class: 'item-title' }, [p.firstName, p.lastName].filter(Boolean).join(' ') || 'Adsız'),
      facts.length ? el('p', { class: 'muted small' }, facts.join(' · ')) : null)));
}

async function partnerCard(body) {
  const p = await getSingleton('partner');
  const memories = await listRecords('memories');
  if (!p && !memories.length) {
    replace(body, el('p', { class: 'muted' }, 'Henüz bilgi eklenmedi. ', el('a', { href: pageUrl('partner') }, 'Bilgileri ekle')));
    return;
  }
  const next = nextImportantDate(p);
  const last = memories.slice().sort((a, b) => (b.date || b.createdAt).localeCompare(a.date || a.createdAt))[0];
  replace(body,
    el('div', { class: 'row' },
      avatar({ photoId: p && p.photoId, text: initials(p && p.name, '') }),
      el('p', { class: 'item-title grow warm-accent' }, (p && (p.nickname || p.name)) || 'Sevdiğim kadın')),
    el('dl', { class: 'kv mt' },
      el('dt', null, 'Sıradaki tarih'),
      el('dd', null, next ? `${next.title}${next.note ? ` (${next.note})` : ''} · ${formatDate(next.date, { short: true })} · ${relativeDayLabel(next.daysLeft)}` : 'Yok'),
      el('dt', null, 'Son anı'),
      el('dd', null, last ? `${last.title}${last.date ? ` · ${formatDate(last.date, { short: true })}` : ''}` : 'Henüz anı yok')));
}

function miniCalendar(body, plans) {
  let year = Number(today.slice(0, 4));
  let month0 = Number(today.slice(5, 7)) - 1;
  let selected = today;
  const grid = el('div', { class: 'mini-cal' });
  const title = el('span', { class: 'mini-cal-title', 'aria-live': 'polite' });
  const dayHolder = el('div', { class: 'mini-day mt' });
  const active = plans.filter((p) => p.status !== 'cancelled');

  const showDay = () => replace(dayHolder, renderDayPlans({
    date: selected,
    plans: active,
    today,
    onOpen: (plan) => openPlanEditor({ plan, onSaved: () => location.reload() }),
    onAdd: (date) => openPlanEditor({ defaults: { startDate: date }, onSaved: () => location.reload() })
  }));

  const draw = () => {
    title.textContent = formatMonthYear(year, month0);
    const prefix = `${year}-${pad2(month0 + 1)}`;
    replace(grid, WEEKDAYS_SHORT_MON.map((d) => el('span', { class: 'mini-wd', 'aria-hidden': 'true' }, d.slice(0, 2))));
    for (const iso of monthGrid(year, month0).flat()) {
      const onDay = active.filter((p) => isOnDay(p, iso));
      const multi = onDay.some((p) => planStart(p) !== planEnd(p));
      const single = onDay.some((p) => planStart(p) === planEnd(p));
      const btn = el('button', {
        type: 'button',
        class: `mini-day-btn${iso.startsWith(prefix) ? '' : ' is-other'}${iso === today ? ' is-today' : ''}${iso === selected ? ' is-selected' : ''}`,
        'aria-label': `${formatDate(iso)}${onDay.length ? `, ${onDay.length} plan` : ''}`,
        'aria-pressed': String(iso === selected)
      }, el('span', null, String(Number(iso.slice(8)))),
      el('span', { class: 'mini-marks', 'aria-hidden': 'true' }, multi ? el('span', { class: 'mini-line' }) : null, single ? el('span', { class: 'mini-dot' }) : null));
      btn.addEventListener('click', () => {
        selected = iso;
        draw();
        showDay();
      });
      grid.append(btn);
    }
  };
  const nav = (n) => {
    const m = addMonths(year, month0, n);
    year = m.year;
    month0 = m.month0;
    draw();
  };
  replace(body,
    el('div', { class: 'row mini-cal-head' }, iconButton('chevronLeft', 'Önceki ay', () => nav(-1)), title, iconButton('chevronRight', 'Sonraki ay', () => nav(1))),
    grid,
    el('p', { class: 'muted small mini-legend' }, el('span', { class: 'mini-line', 'aria-hidden': 'true' }), ' Çok günlük plan  ', el('span', { class: 'mini-dot', 'aria-hidden': 'true' }), ' Tek günlük plan'),
    dayHolder);
  draw();
  showDay();
}

function upcomingCard(body, plans) {
  const list = sortByStart(plans.filter((p) => isUpcomingOrOngoing(p, today))).slice(0, 5);
  if (!list.length) {
    replace(body, el('p', { class: 'muted' }, 'Yaklaşan plan yok. ', el('a', { href: pageUrl('plans', 'new') }, 'Plan ekle')));
    return;
  }
  replace(body, el('ul', { class: 'compact-list' }, list.map((p) => {
    const t = timingLabel(p, today);
    const b = budgetLabel(p);
    return el('li', null,
      el('div', { class: 'grow' },
        el('p', { class: 'item-title' }, p.name),
        el('p', { class: 'muted small' }, `${PLAN_TYPES[p.type]} · ${formatDate(p.startDate, { short: true })}${b ? ` · ${b}` : ''}`)),
      chip(t.text, { kind: t.kind }));
  })));
}

async function dreamsCard(body) {
  const dreams = await listRecords('dreams');
  const activeList = dreams.filter((d) => d.status === 'notStarted' || d.status === 'inProgress');
  const done = dreams.filter((d) => d.status === 'completed').length;
  if (!dreams.length) {
    replace(body, el('p', { class: 'muted' }, 'Henüz hedef yok. ', el('a', { href: pageUrl('dreams', 'new') }, 'Hedef ekle')));
    return;
  }
  const top = activeList.sort((a, b) => ({ high: 0, medium: 1, low: 2 }[a.priority] - { high: 0, medium: 1, low: 2 }[b.priority])).slice(0, 4);
  replace(body,
    el('div', { class: 'stats' },
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, String(activeList.length)), el('span', { class: 'stat-label' }, 'Aktif')),
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, String(done)), el('span', { class: 'stat-label' }, 'Tamamlanan'))),
    top.length ? el('ul', { class: 'compact-list mt' }, top.map((d) => el('li', { class: 'stack-s' },
      el('div', { class: 'row' }, el('span', { class: 'grow' }, d.title), el('span', { class: 'small muted' }, `%${d.progress}`)),
      progressBar(d.progress, `${d.title} ilerlemesi`)))) : null);
}

async function diaryCard(body) {
  const entries = (await listRecords('diary')).sort((a, b) => b.date.localeCompare(a.date) || b.createdAt.localeCompare(a.createdAt)).slice(0, 3);
  if (!entries.length) {
    replace(body, el('p', { class: 'muted' }, 'Henüz günlük yazısı yok. ', el('a', { href: pageUrl('diary', 'new') }, 'İlk yazını yaz')));
    return;
  }
  replace(body, el('ul', { class: 'compact-list' }, entries.map((e) => el('li', null,
    el('div', { class: 'grow' }, el('p', { class: 'item-title' }, e.title), el('p', { class: 'muted small' }, `${formatDate(e.date, { short: true })}${e.body ? ` · ${truncate(e.body, 70)}` : ''}`))))));
}

async function notesCard(body) {
  const notes = (await listRecords('notes')).sort((a, b) => (Number(b.pinned) - Number(a.pinned)) || b.updatedAt.localeCompare(a.updatedAt)).slice(0, 4);
  if (!notes.length) {
    replace(body, el('p', { class: 'muted' }, 'Henüz not yok.'));
    return;
  }
  replace(body, el('ul', { class: 'compact-list' }, notes.map((n) => el('li', null,
    n.pinned ? icon('pin', { size: 16, label: 'Sabitlenmiş' }) : null,
    el('div', { class: 'grow' }, el('p', { class: 'item-title' }, n.title || truncate(n.body, 50) || 'Adsız not'), n.title && n.body ? el('p', { class: 'muted small' }, truncate(n.body, 80)) : null)))));
}

async function financeCard(body) {
  const txns = await listRecords('transactions');
  if (!txns.length) {
    replace(body, el('p', { class: 'muted' }, 'Henüz gelir ya da gider kaydı yok. ', el('a', { href: pageUrl('finance', 'new') }, 'İlk kaydı ekle')));
    return;
  }
  const t = totals(txns.filter((x) => inMonth(x, today.slice(0, 7))));
  const b = balances(txns);
  const goals = await listRecords('savings');
  const sv = savingsSummary(goals);
  replace(body, el('div', { class: 'stats' },
    el('div', { class: 'stat' }, el('span', { class: 'stat-value text-green' }, formatMoney(t.income)), el('span', { class: 'stat-label' }, 'Bu ay gelen')),
    el('div', { class: 'stat' }, el('span', { class: 'stat-value text-red' }, formatMoney(t.expense)), el('span', { class: 'stat-label' }, 'Bu ay giden')),
    el('div', { class: 'stat' }, el('span', { class: `stat-value${b.available < 0 ? ' text-red' : ''}` }, `${b.available < 0 ? '−' : ''}${formatMoney(Math.abs(b.available))}`), el('span', { class: 'stat-label' }, 'Nakit + banka')),
    goals.length ? el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, formatMoney(sv.saved)), el('span', { class: 'stat-label' }, `Birikimde (${sv.reached}/${sv.count} hedef)`)) : null));
}

async function interviewCard(body) {
  const { QUESTIONS } = await import('../data/interview-bank.js');
  const settings = (await getMeta('study:settings')) || {};
  const progress = (await getMeta('study:progress')) || {};
  const days = (await getMeta('study:days')) || {};
  const learned = Object.values(progress).filter((p) => p.box >= 4).length;
  const todayCount = days[today] || 0;
  const left = settings.interviewDate ? diffDays(today, settings.interviewDate) : null;
  replace(body,
    el('div', { class: 'stats' },
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, left === null ? '—' : left > 0 ? `${left} gün` : left === 0 ? 'Bugün' : 'Geçti'), el('span', { class: 'stat-label' }, 'Mülakata kalan')),
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, `${todayCount} / ${settings.dailyGoal || 20}`), el('span', { class: 'stat-label' }, 'Bugünkü kartlar')),
      el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, `%${Math.round((learned / QUESTIONS.length) * 100)}`), el('span', { class: 'stat-label' }, 'Öğrenilen'))));
}

async function setup() {
  const cProfile = card('dash-profile', 'Profilim', pageUrl('profile'), 'Profile git');
  const cPartner = card('dash-partner', 'Sevdiğim kadın', pageUrl('partner'), 'Aç', 'warm-card');
  const cCal = card('dash-cal', 'Takvim', pageUrl('calendar'), 'Takvime git', 'span-2');
  const cPlans = card('dash-plans', 'Yaklaşan planlar', pageUrl('plans'), 'Bütün planlar');
  const cDreams = card('dash-dreams', 'Hedefler', pageUrl('dreams', 'new'), 'Hedef ekle');
  const cDiary = card('dash-diary', 'Son günlükler', pageUrl('diary'), 'Günlüğe git');
  const cNotes = card('dash-notes', 'Son notlar', pageUrl('notes', 'new'), 'Yeni not');
  const cFinance = card('dash-finance', 'Gelir ve gider', pageUrl('finance'), 'Ayrıntılar');
  const interview = el('section', { class: 'card dash-card', 'aria-labelledby': 'dash-iv-title' },
    el('div', { class: 'card-header' }, el('h2', { id: 'dash-iv-title' }, 'Mülakat hazırlık'), el('a', { class: 'card-link', href: pageUrl('interview') }, 'Çalış')),
    el('div', { class: 'card-body' }, loadingState()));
  const vault = el('section', { class: 'card dash-card vault-card', 'aria-labelledby': 'dash-vault-title' },
    el('div', { class: 'card-header' }, el('h2', { id: 'dash-vault-title' }, 'Gizli Kasa')),
    el('p', { class: 'muted small' }, 'Kasa içeriği burada asla gösterilmez. Açmak için kasa PIN\'in gerekir.'),
    el('a', { class: 'btn btn-secondary mt', href: pageUrl('vaultLogin') }, icon('shield'), el('span', null, 'Gizli Kasa\'yı aç')));

  replace(main, el('div', { class: 'dash-grid' },
    cProfile.node, cPartner.node, cFinance.node, interview, cCal.node, cPlans.node, cDreams.node, cDiary.node, cNotes.node, vault));
  fill({ body: interview.querySelector('.card-body') }, interviewCard);

  fill(cProfile, profileCard);
  fill(cPartner, partnerCard);
  fill(cFinance, financeCard);
  fill(cDreams, dreamsCard);
  fill(cDiary, diaryCard);
  fill(cNotes, notesCard);
  let plans = null;
  const getPlans = async () => {
    if (!plans) plans = await listRecords('plans');
    return plans;
  };
  fill(cCal, async (body) => miniCalendar(body, await getPlans()));
  fill(cPlans, async (body) => upcomingCard(body, await getPlans()));
}

const ready = await initApp({ page: 'dashboard', title: 'Ana panel' });
if (ready) await setup();
