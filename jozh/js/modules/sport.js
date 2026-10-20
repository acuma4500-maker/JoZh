// Antrenman: ekipmansız 8 haftalık fiziki hazırlık programı, sesli/zamanlayıcılı antrenman yöneticisi,
// rütbe ve rozetler, gelişim grafikleri, hareket kütüphanesi.
// Veriler cihazda (meta 'sport:*') tutulur ve yedeğe dahildir; buluta gönderilmez.
// Test sonuçları Mülakat → Fiziki sekmesiyle ortak kayda ('study:fitness') da yazılır.
import { initApp } from '../app.js';
import * as db from '../storage/local-db.js';
import * as appLock from '../storage/app-lock.js';
import { el, replace, button, iconButton, segmented, field, openDialog, toast, toastError, chip, progressBar, confirmDialog, showFieldErrors, clearFieldErrors, loadingState } from '../ui.js';
import { icon } from '../utils/icons.js';
import { EXERCISES, GROUPS, RANKS } from '../data/exercises.js';
import * as T from '../utils/training.js';
import { todayISO, addDays, formatDate, WEEKDAYS_SHORT_MON, WEEKDAYS, weekdayIndexMon, parseISODate } from '../utils/dates.js';
import { formatNumber, matchesSearch, parseTrNumber } from '../utils/formatters.js';
import { shortId } from '../utils/id-generator.js';
import { barChart } from '../components/charts.js';

const main = document.getElementById('main');
const KEYS = { profile: 'sport:profile', sessions: 'sport:sessions', active: 'sport:active' };
const FIT_KEY = 'study:fitness';
const TAB_KEY = 'jozh.sportTab';
const TABS = [['today', 'Bugün'], ['program', 'Program'], ['progress', 'Gelişim'], ['moves', 'Hareketler']];
const SVG_NS = 'http://www.w3.org/2000/svg';

const S = {
  tab: readTab(),
  profile: null,
  sessions: [],
  active: null,
  moveQuery: '',
  moveGroup: 'all'
};

const TIPS = [
  'Şınavda sayılan tekrar, göğüs yere yaklaşıp kollar tam kilitlenen tekrardır. Antrenmanda da sınav standardında çalış.',
  'Koşu günlerinde ilk turları yavaş başla; aralıklı koşuda bütün tekrarları aynı hızda bitirmek, ilkini hızlı koşmaktan değerlidir.',
  'Kaslar dinlenirken güçlenir. Gecede 7–8 saat uyku, programın kendisi kadar önemlidir.',
  'Antrenmandan 1–2 saat önce hafif bir öğün, sonrasında protein (yumurta, yoğurt, baklagil) ve bol su.',
  'Mekikte boynunu elle çekme; hareket karından gelsin. Sınavda elle başı çekmek tekrarın sayılmamasına yol açabilir.',
  'Koşu ayakkabın aşınmışsa baldır ve diz ağrısı yapabilir; sınav öncesi alıştığın ayakkabıyla koş.',
  'Ağrı ile yorgunluğu ayır: keskin eklem ağrısında dur. Yorgunluk normaldir, ağrı değildir.',
  'Sınav haftası yük azaltılır; amaç yorgun değil, dinç girmek.',
  'Disiplin motivasyondan güçlüdür: planlı gününde canın istemese de en azından ısınmayı yap, gerisi gelir.'
];

function readTab() {
  try {
    const t = localStorage.getItem(TAB_KEY);
    return TABS.some(([k]) => k === t) ? t : 'today';
  } catch {
    return 'today';
  }
}

async function save(key, value) {
  try {
    await db.setMeta(key, value);
    return true;
  } catch (err) {
    toastError('sport.save', err);
    return false;
  }
}

const today = () => todayISO();
const totalXp = () => S.sessions.reduce((sum, s) => sum + (s.xp || 0), 0);
const currentWeek = () => T.weekIndex(S.profile, today());

function exName(key) {
  return (EXERCISES[key] || {}).name || key;
}

function targetText(s) {
  if (s.test) return s.label;
  if (s.kind === 'reps') return s.amrap ? `${s.target}+ tekrar` : `${s.target} tekrar`;
  return T.formatClock(s.target);
}

function rowText(r) {
  if (r.test) return r.label;
  const unit = r.kind === 'reps' ? `${r.target} tekrar` : T.formatClock(r.target);
  return r.count > 1 ? `${r.count} × ${unit}${r.amrap ? ' (son set: yapabildiğin kadar)' : ''}` : `${unit}${r.amrap ? ' (yapabildiğin kadar)' : ''}`;
}

// --- Rütbe işareti (SVG) ---

function svg(tag, attrs = {}) {
  const n = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, String(v));
  return n;
}

function insignia(index, size = 56) {
  const root = svg('svg', { viewBox: '0 0 48 56', width: size, height: Math.round(size * 56 / 48), class: 'sp-insignia', role: 'img', 'aria-label': `Rütbe: ${RANKS[index].name}` });
  root.append(svg('path', { d: 'M6 4h36v34L24 52 6 38z', class: 'sp-insignia-shield' }));
  const chevrons = index === 0 ? 0 : index <= 4 ? index : 3;
  const stars = index >= 5 ? index - 4 : 0;
  const top = stars ? 26 : 14 + (4 - chevrons) * 3;
  for (let i = 0; i < chevrons; i++) {
    const y = top + i * 7;
    root.append(svg('path', { d: `M13 ${y}l11 6 11-6`, class: 'sp-insignia-mark' }));
  }
  for (let i = 0; i < stars; i++) {
    const cx = stars === 1 ? 24 : 16 + i * (16 / (stars - 1));
    const cy = 15;
    const pts = [];
    for (let k = 0; k < 10; k++) {
      const r = k % 2 ? 2.4 : 5.5;
      const a = -Math.PI / 2 + (k * Math.PI) / 5;
      pts.push(`${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`);
    }
    root.append(svg('polygon', { points: pts.join(' '), class: 'sp-insignia-star' }));
  }
  if (!chevrons && !stars) root.append(svg('path', { d: 'M16 24h16', class: 'sp-insignia-mark' }));
  return root;
}

// --- Profil formu (kurulum ve düzenleme) ---

function profileForm(p, { intro = false } = {}) {
  const dayBoxes = WEEKDAYS_SHORT_MON.map((d, i) => {
    const id = `sp-day-${i}`;
    return el('label', { class: 'sp-day-pick', for: id },
      el('input', { type: 'checkbox', id, name: `day${i}`, class: 'checkbox', checked: p.days.includes(i) }),
      el('span', null, d));
  });
  const form = el('form', { class: 'form-stack', novalidate: true },
    intro ? el('p', { class: 'muted' }, 'Program senin seviyene göre kurulur. Aşağıdaki değerleri bugün dinçken test edip yaz; bilmiyorsan tahmini gir, ilk ara testte kendiliğinden düzelir.') : null,
    el('fieldset', { class: 'sp-fieldset' },
      el('legend', { class: 'field-label' }, 'Antrenman günlerin (3–5 gün)'),
      el('div', { class: 'sp-days' }, dayBoxes),
      el('p', { class: 'field-hint' }, '3 gün: üst vücut, aralıklı koşu, bacak. 4 gün: + uzun koşu. 5 gün: + komando devresi.'),
      el('p', { id: 'sp-days-error', class: 'field-error', hidden: true })),
    el('div', { class: 'form-grid' },
      field({ label: 'En çok şınav (durmadan)', name: 'pushups', value: p.maxes.pushups, inputmode: 'numeric', required: true }),
      field({ label: 'En çok mekik (durmadan)', name: 'situps', value: p.maxes.situps, inputmode: 'numeric', required: true }),
      field({ label: 'En çok squat (durmadan)', name: 'squats', value: p.maxes.squats, inputmode: 'numeric', required: true }),
      field({ label: 'En uzun plank (saniye)', name: 'plank', value: p.maxes.plank, inputmode: 'numeric', required: true, hint: '1 dk 30 sn = 90' }),
      field({ label: 'Durmadan kaç dakika koşabiliyorsun?', name: 'runBase', value: p.runBase, inputmode: 'numeric', required: true, hint: 'Rahat tempoda. Hiç koşmuyorsan 3 yaz.' }),
      field({ label: 'Testte süre sınırı', name: 'testCap', type: 'select', value: String(p.testCap), options: [['0', 'Süresiz (bırakana kadar)'], ['60', '1 dakika'], ['120', '2 dakika']], hint: 'Başvuru kılavuzundaki test kuralına göre seç.' })));
  form.addEventListener('submit', (e) => e.preventDefault());
  const read = () => {
    clearFieldErrors(form);
    const errors = {};
    const days = WEEKDAYS_SHORT_MON.map((_, i) => i).filter((i) => form.elements[`day${i}`].checked);
    const dayErr = form.querySelector('#sp-days-error');
    dayErr.hidden = true;
    const int = (name, lo, hi) => {
      const v = String(form.elements[name].value).trim();
      if (!/^\d{1,4}$/.test(v) || Number(v) < lo || Number(v) > hi) {
        errors[name] = `${lo}–${hi} arası bir sayı yaz.`;
        return null;
      }
      return Number(v);
    };
    const maxes = { pushups: int('pushups', 1, 300), situps: int('situps', 1, 300), squats: int('squats', 1, 500), plank: int('plank', 5, 1200) };
    const runBase = int('runBase', 1, 120);
    if (days.length < 3 || days.length > 5) {
      dayErr.textContent = '3, 4 ya da 5 gün seç.';
      dayErr.hidden = false;
      if (!Object.keys(errors).length) form.querySelector('.sp-days input').focus();
    }
    if (Object.keys(errors).length) showFieldErrors(form, errors);
    if (Object.keys(errors).length || days.length < 3 || days.length > 5) return null;
    return { days, maxes, runBase, testCap: Number(form.elements.testCap.value) };
  };
  return { form, read };
}

function openProfileEditor() {
  const { form, read } = profileForm(S.profile);
  openDialog({
    title: 'Programı düzenle',
    content: form,
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet', kind: 'primary',
        onClick: async (d) => {
          const v = read();
          if (!v) return;
          S.profile = { ...S.profile, ...v };
          if (await save(KEYS.profile, S.profile)) {
            await d.close(true);
            toast('Program güncellendi.', { kind: 'success' });
            render();
          }
        }
      }
    ]
  });
}

function renderSetup() {
  const p = structuredClone(T.DEFAULT_PROFILE);
  const { form, read } = profileForm(p, { intro: true });
  const create = async (firstTest) => {
    const v = read();
    if (!v) return;
    S.profile = { ...p, ...v, startDate: today(), firstMaxes: { ...v.maxes } };
    if (!(await save(KEYS.profile, S.profile))) return;
    if (firstTest) {
      startWorkout(T.buildWorkout(S.profile, currentWeek(), 'T'), { extra: true });
    } else {
      toast('Program hazır. İlk görev seni bekliyor.', { kind: 'success' });
      renderShell();
    }
  };
  replace(main,
    el('section', { class: 'card sp-setup' },
      el('div', { class: 'sp-setup-head' }, insignia(0, 64),
        el('div', null, el('h2', null, 'Fiziki hazırlık programı'),
          el('p', { class: 'muted' }, 'Ekipmansız, 8 haftalık; şınav, mekik, koşu ve kondisyon. Yük her antrenmandan sonra verdiğin puana göre kendini ayarlar.'))),
      form,
      el('div', { class: 'row mt' },
        button('Programı başlat', () => create(false), { kind: 'primary', iconName: 'play' }),
        button('Önce seviye testi yap', () => create(true), { iconName: 'target' }))));
}

// --- Sekmeler ---

const shell = {
  tabs: null,
  panels: {
    today: el('div', { class: 'sp-panel' }),
    program: el('div', { class: 'sp-panel' }),
    progress: el('div', { class: 'sp-panel' }),
    moves: el('div', { class: 'sp-panel' })
  }
};

function renderShell() {
  shell.tabs = segmented(TABS, S.tab, (v) => {
    S.tab = v;
    try {
      localStorage.setItem(TAB_KEY, v);
    } catch {
      // yok say
    }
    render();
  }, 'Bölüm');
  shell.tabs.classList.add('sp-tabs');
  replace(main, shell.tabs, ...Object.values(shell.panels));
  render();
}

function render() {
  if (!S.profile) {
    renderSetup();
    return;
  }
  if (!shell.tabs || !main.contains(shell.tabs)) {
    renderShell();
    return;
  }
  for (const [k, node] of Object.entries(shell.panels)) node.hidden = k !== S.tab;
  if (S.tab === 'today') renderToday();
  else if (S.tab === 'program') renderProgram();
  else if (S.tab === 'progress') renderProgress();
  else renderMoves();
}

function heroStats() {
  const xp = totalXp();
  const rank = T.rankOf(xp);
  const wk = currentWeek();
  const ph = T.phaseOf(wk);
  const rot = T.rotationFor(S.profile, wk);
  const doneThisWeek = S.sessions.filter((s) => s.week === wk && !s.extra).length;
  const streak = T.weekStreak(S.profile, wk, S.sessions);
  return el('section', { class: 'sp-hero', 'aria-label': 'Durum' },
    el('div', { class: 'card sp-rank' },
      insignia(rank.index, 52),
      el('div', { class: 'sp-rank-text' },
        el('span', { class: 'stat-label' }, 'Rütbe'),
        el('span', { class: 'sp-rank-name' }, rank.name),
        rank.next ? progressBar(rank.pct, `${rank.next.name} rütbesine ilerleme`) : null,
        el('span', { class: 'small muted' }, rank.next ? `${formatNumber(xp)} puan · ${rank.next.name} için ${formatNumber(rank.toNext)}` : `${formatNumber(xp)} puan · en yüksek rütbe`))),
    el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, `Dönem ${T.cycleOf(wk)}`), el('span', { class: 'stat-value' }, `Hafta ${(wk % T.CYCLE_WEEKS) + 1}/${T.CYCLE_WEEKS}`), el('span', { class: 'small muted' }, ph.name)),
    el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'Bu hafta'), el('span', { class: 'stat-value' }, `${Math.min(doneThisWeek, rot.length)}/${rot.length}`), progressBar((doneThisWeek / rot.length) * 100, 'Haftalık görev')),
    el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'Seri'), el('span', { class: 'stat-value sp-streak' }, icon('flame', { size: 22 }), `${streak} hafta`), el('span', { class: 'small muted' }, streak ? 'Planı aksatmadan sürdür' : 'Bu haftayı tamamla, seri başlasın')));
}

function weekStrip(wk) {
  const plan = T.weekPlan(S.profile, wk, S.sessions);
  const monday = addDays(T.mondayOf(S.profile.startDate), wk * 7);
  const t = today();
  return el('ol', { class: 'sp-week', 'aria-label': 'Bu haftanın planı' }, WEEKDAYS_SHORT_MON.map((d, i) => {
    const date = addDays(monday, i);
    const item = plan.find((x) => x.date === date);
    const extra = S.sessions.filter((s) => s.date === date && s.extra).length;
    const cls = ['sp-day', item ? 'is-planned' : 'is-rest', item && item.done ? 'is-done' : '', date === t ? 'is-today' : ''].filter(Boolean).join(' ');
    const label = item ? T.TYPES[item.type].short : 'İzin';
    return el('li', { class: cls, 'aria-current': date === t ? 'date' : null },
      el('span', { class: 'sp-day-name' }, d),
      el('span', { class: 'sp-day-icon', 'aria-hidden': 'true' }, item ? icon(item.done ? 'check' : T.TYPES[item.type].icon, { size: 18 }) : '·'),
      el('span', { class: 'sp-day-label' }, label, item && item.done ? el('span', { class: 'visually-hidden' }, ' (tamamlandı)') : null, extra ? el('span', { class: 'visually-hidden' }, ` + ${extra} ekstra`) : null));
  }));
}

function workoutPreview(workout) {
  return el('ol', { class: 'sp-preview' }, T.summarize(workout.steps).map((r) => el('li', null,
    el('span', { class: 'sp-preview-block' }, r.block),
    el('span', { class: 'sp-preview-name' }, exName(r.ex)),
    el('span', { class: 'sp-preview-target' }, rowText(r)))));
}

function openPreview(workout, meta) {
  openDialog({
    title: `${workout.title} · ~${Math.round(workout.estimate / 60)} dk`,
    content: el('div', { class: 'stack' },
      el('p', { class: 'small muted' }, `Hafta ${(workout.week % T.CYCLE_WEEKS) + 1} · ${workout.phase}. Hareket adına dokunursan doğru form açıklaması çıkar.`),
      workoutPreview(workout)),
    actions: [
      { label: 'Kapat', onClick: (d) => d.close() },
      { label: 'Başla', kind: 'primary', icon: 'play', onClick: async (d) => { await d.close(true); startWorkout(workout, meta); } }
    ]
  });
}

function missionCard() {
  const wk = currentWeek();
  const next = T.nextSlot(S.profile, wk, S.sessions);
  const t = today();
  const isTrainingDay = S.profile.days.includes(weekdayIndexMon(t));
  if (!next) {
    const extraA = T.buildWorkout(S.profile, wk, 'E');
    const extraB = T.buildWorkout(S.profile, wk, 'D');
    return el('section', { class: 'card sp-mission is-complete' },
      el('div', { class: 'sp-mission-head' }, icon('medal', { size: 28 }), el('div', null, el('h2', null, 'Haftanın görevleri tamam'), el('p', { class: 'muted' }, 'Gelecek pazartesi yeni hafta açılır. Dinlenmek de antrenmanın parçası.'))),
      el('p', { class: 'small muted' }, 'Yine de enerjin varsa ekstra yapabilirsin (seriyi etkilemez, puan kazandırır):'),
      el('div', { class: 'row' },
        button(`Ekstra: ${extraA.title}`, () => openPreview(extraA, { extra: true }), { iconName: 'flame' }),
        button(`Ekstra: ${extraB.title}`, () => openPreview(extraB, { extra: true }), { iconName: 'run' })));
  }
  const workout = T.buildWorkout(S.profile, wk, next.type);
  const plan = T.weekPlan(S.profile, wk, S.sessions);
  const planned = plan[next.slot];
  const when = planned.date === t ? chip('Bugün planlı', { kind: 'green' })
    : planned.date < t ? chip('Geride kaldı, bugün yapabilirsin', { kind: 'yellow' })
      : chip(`Planlı gün: ${WEEKDAYS[parseISODate(planned.date).getDay()]}`);
  const rows = T.summarize(workout.steps).filter((r) => r.block !== 'Isınma' && r.block !== 'Esneme' && r.block !== 'Soğuma');
  const shown = rows.slice(0, 6);
  return el('section', { class: `card sp-mission${next.type === 'T' ? ' is-test' : ''}`, 'aria-labelledby': 'sp-mission-title' },
    el('div', { class: 'sp-mission-head' },
      el('span', { class: 'sp-mission-icon', 'aria-hidden': 'true' }, icon(T.TYPES[next.type].icon, { size: 26 })),
      el('div', null,
        el('span', { class: 'stat-label' }, `Görev ${next.slot + 1}/${plan.length} · Hafta ${(wk % T.CYCLE_WEEKS) + 1}`),
        el('h2', { id: 'sp-mission-title' }, workout.title),
        el('div', { class: 'row sp-mission-meta' }, when, chip(`~${Math.round(workout.estimate / 60)} dk`), chip(workout.phase)))),
    !isTrainingDay && planned.date > t ? el('p', { class: 'small muted' }, 'Bugün dinlenme günün. İstersen sıradaki görevi şimdi de yapabilirsin.') : null,
    next.type === 'T' ? el('p', { class: 'notice notice-info' }, icon('info'), el('span', null, 'Test günü: her hareketi tam formla, yapabildiğin kadar yap. Sonuçlar programını ve Mülakat → Fiziki kayıtlarını günceller.')) : null,
    el('ul', { class: 'sp-mission-list' }, shown.map((r) => el('li', null, el('span', null, exName(r.ex)), el('span', { class: 'muted' }, rowText(r))))),
    rows.length > shown.length ? el('p', { class: 'small muted' }, `+ ${rows.length - shown.length} hareket daha, ısınma ve esneme dahil`) : null,
    el('div', { class: 'row sp-mission-actions' },
      button('Başla', () => startWorkout(workout, { slot: next.slot }), { kind: 'primary', iconName: 'play', className: 'sp-start' }),
      button('Ayrıntılar', () => openPreview(workout, { slot: next.slot }), { iconName: 'list' })));
}

function renderToday() {
  const wk = currentWeek();
  const tip = TIPS[(Math.floor(Date.now() / 86400000)) % TIPS.length];
  replace(shell.panels.today,
    heroStats(),
    S.active ? el('section', { class: 'notice notice-warning sp-resume' }, icon('clock'),
      el('div', { class: 'stack' },
        el('span', null, `Yarım kalan antrenman: ${T.TYPES[S.active.type].title} (${S.active.index}/${S.active.total} adım).`),
        el('div', { class: 'row' },
          button('Devam et', resumeWorkout, { kind: 'primary', iconName: 'play' }),
          button('Sil', async () => {
            S.active = null;
            await db.setMeta(KEYS.active, null);
            render();
          }, { iconName: 'trash' })))) : null,
    missionCard(),
    el('section', { class: 'card mt' }, el('h2', { class: 'sp-h2' }, 'Bu hafta'), weekStrip(wk)),
    el('section', { class: 'card sp-tip mt' }, icon('info'), el('p', null, el('strong', null, 'Günün notu: '), tip)));
}

// --- Program sekmesi ---

function renderProgram() {
  const wk = currentWeek();
  const cycleStart = wk - (wk % T.CYCLE_WEEKS);
  const p = S.profile;
  const pctLabel = (v) => `%${Math.round(v * 100)}`;
  const rot = T.rotationFor(p, wk);
  replace(shell.panels.program,
    el('section', { class: 'card' },
      el('div', { class: 'card-header' }, el('h2', null, `Dönem ${T.cycleOf(wk)} · 8 hafta`)),
      el('ol', { class: 'sp-timeline' }, T.PHASES.map((ph, i) => {
        const w = cycleStart + i;
        const total = T.rotationFor(p, w).length;
        const done = Math.min(total, S.sessions.filter((s) => s.week === w && !s.extra).length);
        const state = w < wk ? (done >= total ? 'is-done' : 'is-missed') : w === wk ? 'is-current' : '';
        return el('li', { class: `sp-tl ${state}`, 'aria-current': w === wk ? 'step' : null },
          el('span', { class: 'sp-tl-week' }, `H${i + 1}`),
          el('span', { class: 'sp-tl-body' },
            el('span', { class: 'sp-tl-name' }, ph.name, ph.test ? chip('Test', { kind: 'yellow' }) : null),
            el('span', { class: 'small muted' }, `Yük ${pctLabel(ph.pct)} · ana hareket ${ph.sets} set`)),
          el('span', { class: 'sp-tl-done' }, w <= wk ? `${done}/${total}` : ''));
      }))),
    el('section', { class: 'card mt' },
      el('div', { class: 'card-header' }, el('h2', null, 'Bu haftanın antrenmanları')),
      el('div', { class: 'stack' }, rot.map((type, i) => {
        const w = T.buildWorkout(p, wk, type);
        return el('details', { class: 'sp-plan-day' },
          el('summary', null, el('span', null, `${i + 1}. ${w.title}`), el('span', { class: 'muted small' }, `~${Math.round(w.estimate / 60)} dk`)),
          workoutPreview(w));
      }))),
    el('section', { class: 'card mt' },
      el('div', { class: 'card-header' }, el('h2', null, 'Seviyen ve ayarlar'), iconButton('edit', 'Programı düzenle', openProfileEditor)),
      el('dl', { class: 'sp-dl' },
        el('dt', null, 'Günler'), el('dd', null, p.days.slice().sort((a, b) => a - b).map((d) => WEEKDAYS_SHORT_MON[d]).join(', ')),
        el('dt', null, 'Şınav maks.'), el('dd', null, `${p.maxes.pushups}`),
        el('dt', null, 'Mekik maks.'), el('dd', null, `${p.maxes.situps}`),
        el('dt', null, 'Squat maks.'), el('dd', null, `${p.maxes.squats}`),
        el('dt', null, 'Plank'), el('dd', null, T.formatClock(p.maxes.plank)),
        el('dt', null, 'Kesintisiz koşu'), el('dd', null, `${p.runBase} dk`),
        el('dt', null, 'Yük ayarı'), el('dd', null, `Üst ${pctLabel(p.adjust.push)}, karın ${pctLabel(p.adjust.core)}, bacak ${pctLabel(p.adjust.legs)}, koşu ${pctLabel(p.adjust.run)}`)),
      el('p', { class: 'small muted' }, 'Yük ayarı, antrenman sonunda verdiğin "Kolay / Tam kıvamında / Zor" puanına göre kendiliğinden değişir. "Yapabildiğin kadar" setlerinde beklenenden çok yaparsan maksimumun da yükselir.'),
      el('div', { class: 'row mt' },
        button('Seviye testi yap', () => openPreview(T.buildWorkout(p, wk, 'T'), { extra: true }), { iconName: 'target' }),
        button('Yeni dönem başlat', newCycle, { iconName: 'refresh' }),
        button('Programı sıfırla', resetProgram, { kind: 'danger', iconName: 'trash' }))));
}

async function newCycle() {
  const ok = await confirmDialog({ title: 'Yeni dönem', message: 'Program 1. haftadan yeniden başlar. Maksimumların, rütben ve geçmişin korunur.', confirmText: 'Başlat' });
  if (!ok) return;
  S.profile = { ...S.profile, startDate: today() };
  // Hafta numaraları başlangıca göre olduğundan eski kayıtlar yeni dönemle karışmasın
  S.sessions = S.sessions.map((s) => ({ ...s, week: s.week - 10000 }));
  await save(KEYS.sessions, S.sessions);
  await save(KEYS.profile, S.profile);
  toast('Yeni dönem başladı.', { kind: 'success' });
  render();
}

async function resetProgram() {
  const ok = await confirmDialog({ title: 'Programı sıfırla', message: 'Program ayarların, antrenman geçmişin ve rütben silinir. Mülakat → Fiziki kayıtların kalır.\nBu işlem geri alınamaz.', confirmText: 'Sıfırla', danger: true, requireText: 'SIFIRLA' });
  if (!ok) return;
  await db.setMeta(KEYS.profile, null);
  await db.setMeta(KEYS.sessions, []);
  await db.setMeta(KEYS.active, null);
  S.profile = null;
  S.sessions = [];
  S.active = null;
  shell.tabs = null;
  render();
}

// --- Gelişim sekmesi ---

function heatmap() {
  const weeks = 12;
  const start = addDays(T.mondayOf(today()), -(weeks - 1) * 7);
  const byDate = {};
  for (const s of S.sessions) byDate[s.date] = (byDate[s.date] || 0) + 1;
  let count = 0;
  const cells = [];
  for (let w = 0; w < weeks; w++) {
    for (let d = 0; d < 7; d++) {
      const date = addDays(start, w * 7 + d);
      const n = date > today() ? -1 : byDate[date] || 0;
      if (n > 0) count += n;
      cells.push(el('span', { class: `sp-heat-cell lv${n < 0 ? 'x' : Math.min(n, 2)}`, title: n < 0 ? '' : `${formatDate(date, { short: true })}: ${n ? `${n} antrenman` : 'antrenman yok'}` }));
    }
  }
  return el('figure', { class: 'sp-heat-wrap' },
    el('div', { class: 'sp-heat', 'aria-hidden': 'true' }, cells),
    el('figcaption', { class: 'small muted' }, `Son 12 haftada ${count} antrenman. Her sütun bir hafta, yukarıdan aşağı pazartesi → pazar.`));
}

function weeklyChart() {
  const wk = currentWeek();
  const groups = [];
  for (let w = Math.max(0, wk - 7); w <= wk; w++) {
    const list = S.sessions.filter((s) => s.week === w);
    const reps = list.reduce((sum, s) => sum + ((s.totals && s.totals.reps) || 0), 0);
    const run = list.reduce((sum, s) => sum + ((s.totals && s.totals.runSec) || 0), 0);
    groups.push({ label: `H${(w % T.CYCLE_WEEKS) + 1}`, title: `Hafta ${(w % T.CYCLE_WEEKS) + 1} (dönem ${T.cycleOf(w)})`, values: { reps }, note: `Koşu: ${Math.round(run / 60)} dk · ${list.length} antrenman` });
  }
  return barChart({
    title: 'Haftalık toplam tekrar',
    tableCaption: 'Haftalık toplam tekrar',
    rowHeader: 'Hafta',
    series: [{ key: 'reps', name: 'Tekrar', className: 'series-income' }],
    format: (v) => formatNumber(v),
    groups
  });
}

async function readFitness() {
  const f = await db.getMeta(FIT_KEY);
  return f && Array.isArray(f.entries) ? f : { entries: [], targets: { run: '', pushups: '', situps: '' } };
}

async function renderProgress() {
  const xp = totalXp();
  const rank = T.rankOf(xp);
  const wk = currentWeek();
  const badges = T.earnedBadges(S.profile, S.sessions, wk);
  const first = S.profile.firstMaxes || S.profile.maxes;
  const fit = await readFitness();
  const tests = fit.entries.slice().sort((a, b) => a.date.localeCompare(b.date)).slice(-10);
  const maxRow = (label, key, fmt = String) => {
    const a = Number(first[key]) || 0;
    const b = Number(S.profile.maxes[key]) || 0;
    const d = b - a;
    return el('div', { class: 'card stat' },
      el('span', { class: 'stat-label' }, label),
      el('span', { class: 'stat-value' }, fmt(b)),
      el('span', { class: `small ${d > 0 ? 'sp-up' : 'muted'}` }, d > 0 ? `Başlangıçtan +${key === 'plank' ? T.formatClock(d) : d}` : `Başlangıç ${fmt(a)}`));
  };
  replace(shell.panels.progress,
    el('div', { class: 'stats sp-max-stats' },
      maxRow('Şınav', 'pushups'), maxRow('Mekik', 'situps'), maxRow('Squat', 'squats'), maxRow('Plank', 'plank', T.formatClock)),
    el('section', { class: 'card mt' },
      el('div', { class: 'card-header' }, el('h2', null, 'Rütbe yolu'), chip(`${formatNumber(xp)} puan`)),
      el('ol', { class: 'sp-ranks' }, RANKS.map((r, i) => el('li', { class: `sp-rank-step${i < rank.index ? ' is-past' : i === rank.index ? ' is-current' : ''}`, 'aria-current': i === rank.index ? 'step' : null },
        insignia(i, 30),
        el('span', { class: 'sp-rank-step-name' }, r.name),
        el('span', { class: 'small muted' }, `${formatNumber(r.xp)} puan`)))),
      el('p', { class: 'small muted' }, 'Puan: her tekrar 1, her 5 saniyelik süreli hareket 1, her dakika koşu 10 puan; antrenmanı bitirmek +50, test +100.')),
    el('section', { class: 'card mt' },
      el('div', { class: 'card-header' }, el('h2', null, 'Rozetler'), chip(`${badges.filter((b) => b.earned).length}/${badges.length}`)),
      el('ul', { class: 'sp-badges' }, badges.map((b) => el('li', { class: `sp-badge${b.earned ? ' is-earned' : ''}` },
        icon(b.earned ? 'medal' : 'lock', { size: 22 }),
        el('span', { class: 'sp-badge-name' }, b.name, el('span', { class: 'visually-hidden' }, b.earned ? ' (kazanıldı)' : ' (henüz değil)')),
        el('span', { class: 'small muted' }, b.desc))))),
    el('section', { class: 'card chart-card mt' }, el('h2', null, 'Haftalık hacim'), weeklyChart()),
    tests.length >= 2 ? el('section', { class: 'card chart-card mt' },
      el('h2', null, 'Test sonuçları'),
      barChart({
        title: 'Testlerde şınav ve mekik',
        tableCaption: 'Test sonuçları',
        rowHeader: 'Tarih',
        series: [{ key: 'pushups', name: 'Şınav', className: 'series-income' }, { key: 'situps', name: 'Mekik', className: 'series-expense' }],
        format: (v) => formatNumber(v),
        groups: tests.map((e) => ({ label: formatDate(e.date, { short: true, year: false }), title: formatDate(e.date), values: { pushups: e.pushups || 0, situps: e.situps || 0 } }))
      })) : null,
    el('section', { class: 'card mt' }, el('h2', { class: 'sp-h2' }, 'Antrenman takvimi'), heatmap()),
    historyCard());
}

function historyCard() {
  const list = S.sessions.slice().sort((a, b) => (b.startedAt || b.date).localeCompare(a.startedAt || a.date)).slice(0, 30);
  const rating = { easy: 'Kolay', ok: 'Tam kıvamında', hard: 'Zor' };
  return el('section', { class: 'card mt' },
    el('div', { class: 'card-header' }, el('h2', null, 'Geçmiş'), chip(`${S.sessions.length} antrenman`)),
    list.length ? el('ul', { class: 'sp-history' }, list.map((s) => el('li', null,
      el('span', { class: 'sp-history-main' },
        el('span', { class: 'sp-history-title' }, s.title, s.extra ? chip('Ekstra') : null),
        el('span', { class: 'small muted' }, [formatDate(s.date, { short: true }), T.formatDuration(s.durationSec), `${s.xp} puan`, rating[s.rating], s.distanceKm ? `${formatNumber(s.distanceKm)} km` : ''].filter(Boolean).join(' · ')),
        s.note ? el('span', { class: 'small' }, s.note) : null),
      iconButton('trash', `${s.title} kaydını sil`, () => deleteSession(s))))) : el('p', { class: 'muted' }, 'Henüz antrenman yok. İlk görevini Bugün sekmesinden başlat.'));
}

async function deleteSession(s) {
  const ok = await confirmDialog({ title: 'Kaydı sil', message: `${formatDate(s.date)} tarihli "${s.title}" kaydı ve kazandığı ${s.xp} puan silinsin mi? Program maksimumların değişmez.`, confirmText: 'Sil', danger: true });
  if (!ok) return;
  S.sessions = S.sessions.filter((x) => x.id !== s.id);
  await save(KEYS.sessions, S.sessions);
  render();
}

// --- Hareketler sekmesi ---

function exerciseDetail(key, { open = false } = {}) {
  const e = EXERCISES[key];
  return el('details', { class: 'sp-move', open },
    el('summary', null, el('span', { class: 'sp-move-name' }, e.name), el('span', { class: 'small muted' }, GROUPS[e.group])),
    el('div', { class: 'sp-move-body' },
      el('p', { class: 'small muted' }, e.muscles),
      el('h3', null, 'Doğru form'),
      el('ul', { class: 'bullets' }, e.cues.map((c) => el('li', null, c))),
      e.mistakes.length ? el('h3', null, 'Sık yapılan hatalar') : null,
      e.mistakes.length ? el('ul', { class: 'bullets' }, e.mistakes.map((c) => el('li', null, c))) : null,
      el('p', { class: 'small' }, el('strong', null, 'Kolaylaştır: '), e.easier),
      el('p', { class: 'small' }, el('strong', null, 'Zorlaştır: '), e.harder)));
}

function renderMoves() {
  const panel = shell.panels.moves;
  const list = el('div', { class: 'stack sp-moves' });
  const search = el('input', { type: 'search', class: 'input', placeholder: 'Hareket ara', 'aria-label': 'Hareket ara', value: S.moveQuery });
  const groups = segmented([['all', 'Hepsi'], ...Object.entries(GROUPS)], S.moveGroup, (v) => {
    S.moveGroup = v;
    fill();
  }, 'Hareket grubu');
  groups.classList.add('sp-groups');
  const fill = () => {
    const keys = Object.keys(EXERCISES).filter((k) => (S.moveGroup === 'all' || EXERCISES[k].group === S.moveGroup) && matchesSearch(S.moveQuery, EXERCISES[k].name, EXERCISES[k].muscles));
    replace(list, keys.length ? keys.map((k) => exerciseDetail(k)) : el('p', { class: 'muted' }, 'Eşleşen hareket yok.'));
  };
  search.addEventListener('input', () => {
    S.moveQuery = search.value;
    fill();
  });
  replace(panel,
    el('p', { class: 'small muted' }, 'Bütün hareketler ekipmansızdır. Formu bozulmadan yapamadığın tekrarı sayma; kolaylaştırılmış hâliyle devam et.'),
    el('div', { class: 'sp-moves-tools' }, search, groups),
    list);
  fill();
}

// --- Antrenman yöneticisi (oynatıcı) ---

const P = {
  workout: null,
  meta: null,
  index: 0,
  phase: 'ready',
  results: [],
  startedAt: '',
  endAt: 0,
  phaseStart: 0,
  paused: false,
  pausedLeft: 0,
  timer: 0,
  keepAlive: 0,
  wakeLock: null,
  audio: null,
  done: 0,
  lastBeep: -1,
  view: null
};

function say(text) {
  if (!S.profile.voice || !('speechSynthesis' in window)) return;
  try {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'tr-TR';
    u.rate = 1.05;
    window.speechSynthesis.speak(u);
  } catch {
    // ses yoksa sessiz devam
  }
}

function beep(freq = 880, ms = 140) {
  if (!S.profile.sound) return;
  try {
    if (!P.audio) {
      const Ctx = window.AudioContext || window.webkitAudioContext;
      if (!Ctx) return;
      P.audio = new Ctx();
    }
    const ctx = P.audio;
    if (ctx.state === 'suspended') ctx.resume();
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.frequency.value = freq;
    o.type = 'sine';
    g.gain.setValueAtTime(0.0001, ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.3, ctx.currentTime + 0.01);
    g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + ms / 1000);
    o.connect(g).connect(ctx.destination);
    o.start();
    o.stop(ctx.currentTime + ms / 1000 + 0.02);
  } catch {
    // yok say
  }
  if (navigator.vibrate) navigator.vibrate(ms);
}

async function requestWakeLock() {
  try {
    if ('wakeLock' in navigator && document.visibilityState === 'visible') P.wakeLock = await navigator.wakeLock.request('screen');
  } catch {
    P.wakeLock = null;
  }
}

function releaseWakeLock() {
  try {
    if (P.wakeLock) P.wakeLock.release();
  } catch {
    // yok say
  }
  P.wakeLock = null;
}

function onVisibility() {
  if (P.workout && document.visibilityState === 'visible') {
    requestWakeLock();
    appLock.touchSession(true);
  }
}

async function persistActive() {
  if (!P.workout) return;
  S.active = {
    type: P.workout.type,
    week: P.workout.week,
    slot: P.meta.slot ?? null,
    extra: Boolean(P.meta.extra),
    index: P.index,
    total: P.workout.steps.length,
    results: P.results,
    startedAt: P.startedAt,
    date: today()
  };
  try {
    await db.setMeta(KEYS.active, S.active);
  } catch {
    // kayıt yapılamazsa antrenman yine sürer
  }
}

function startWorkout(workout, meta = {}, resume = null) {
  P.workout = workout;
  P.meta = meta;
  P.index = resume ? resume.index : 0;
  P.results = resume ? resume.results : [];
  P.startedAt = resume ? resume.startedAt : new Date().toISOString();
  P.paused = false;
  beep(660, 60);
  requestWakeLock();
  document.addEventListener('visibilitychange', onVisibility);
  // Antrenman ekranı açıkken (ekran açık ve görünürken) kilit süresi dolmasın
  clearInterval(P.keepAlive);
  P.keepAlive = setInterval(() => {
    if (document.visibilityState === 'visible') appLock.touchSession(true);
  }, 15000);
  appLock.touchSession(true);
  P.view = el('section', { class: 'sp-player', 'aria-label': 'Antrenman' });
  replace(main, P.view);
  window.scrollTo(0, 0);
  if (P.index >= workout.steps.length) finish();
  else enterReady(P.index === 0 ? 10 : 5);
}

function resumeWorkout() {
  const a = S.active;
  if (!a) return;
  const workout = T.buildWorkout(S.profile, a.week, a.type);
  startWorkout(workout, { slot: a.slot, extra: a.extra }, a);
}

function setPhase(phase, seconds) {
  P.phase = phase;
  P.phaseStart = Date.now();
  P.endAt = seconds ? Date.now() + seconds * 1000 : 0;
  P.paused = false;
  P.lastBeep = -1;
  clearInterval(P.timer);
  P.timer = setInterval(tick, 200);
  draw();
}

function current() {
  return P.workout.steps[P.index];
}

function enterReady(seconds) {
  const s = current();
  say(`Hazır ol. ${exName(s.ex)}${s.test ? ', test' : ''}.`);
  setPhase('ready', seconds);
}

function enterWork() {
  const s = current();
  beep(1040, 260);
  if (s.test && s.cap) {
    say('Başla!');
    setPhase('work', s.cap);
  } else if (s.kind === 'time') {
    say('Başla!');
    setPhase('work', s.target);
  } else if (s.kind === 'stopwatch') {
    say('Başla! Bırakınca düğmeye dokun.');
    setPhase('work', 0);
  } else {
    say(s.amrap ? `Son set! Yapabildiğin kadar.` : s.test ? 'Başla! Yapabildiğin kadar.' : `${s.target} tekrar. Başla!`);
    P.pending = s.test ? 0 : s.target;
    setPhase('work', 0);
  }
}

function record(done) {
  const s = current();
  P.results[P.index] = { ex: s.ex, kind: s.kind === 'stopwatch' ? 'time' : s.kind, target: s.target, done: Math.max(0, Math.round(done)), amrap: s.amrap, test: s.test || '' };
}

function afterStep() {
  const s = current();
  const nextIndex = P.index + 1;
  const last = nextIndex >= P.workout.steps.length;
  P.index = nextIndex;
  persistActive();
  if (last) {
    finish();
    return;
  }
  const n = P.workout.steps[nextIndex];
  if (s.rest > 0) {
    say(`Dinlen. Sıradaki: ${exName(n.ex)}.`);
    beep(520, 200);
    // Dinlenme bittiğinde sıradaki adım kendiliğinden başlar
    P.index = nextIndex - 1;
    P.restFor = nextIndex;
    setPhase('rest', s.rest);
  } else {
    beep(780, 120);
    if (n.kind === 'time' && !n.test) {
      say(exName(n.ex));
      enterWork();
    } else {
      enterReady(5);
    }
  }
}

function completeWork() {
  const s = current();
  if (s.kind === 'time') record(s.target);
  else if (s.kind === 'stopwatch') record((Date.now() - P.phaseStart) / 1000);
  else record(P.pending);
  afterStep();
}

function tick() {
  if (P.paused || !P.workout) return;
  if (P.endAt) {
    const left = (P.endAt - Date.now()) / 1000;
    const whole = Math.ceil(left);
    if (whole <= 3 && whole >= 1 && whole !== P.lastBeep && (P.phase !== 'work' || current().kind === 'time' || current().cap)) {
      P.lastBeep = whole;
      beep(660, 90);
    }
    if (left <= 0) {
      onTimerEnd();
      return;
    }
  }
  drawClock();
}

function onTimerEnd() {
  clearInterval(P.timer);
  const s = current();
  if (P.phase === 'ready') {
    enterWork();
  } else if (P.phase === 'rest') {
    P.index = P.restFor;
    const n = current();
    if (n.kind === 'time' && !n.test) enterWork();
    else enterReady(3);
  } else if (P.phase === 'work') {
    if (s.test && s.cap) {
      beep(400, 500);
      say('Dur! Kaç tekrar yaptın?');
      P.pending = 0;
      P.phase = 'input';
      P.endAt = 0;
      draw();
    } else {
      completeWork();
    }
  }
}

function togglePause() {
  if (!P.endAt && P.phase !== 'work') return;
  if (P.paused) {
    P.paused = false;
    if (P.endAt) P.endAt = Date.now() + P.pausedLeft;
    say('Devam');
  } else {
    P.paused = true;
    if (P.endAt) P.pausedLeft = P.endAt - Date.now();
  }
  draw();
}

function skip() {
  if (P.phase === 'ready') {
    clearInterval(P.timer);
    enterWork();
  } else if (P.phase === 'rest') {
    P.endAt = Date.now();
    P.paused = false;
    tick();
  } else if (P.phase === 'work') {
    const s = current();
    clearInterval(P.timer);
    if (s.test && s.cap) {
      // Süre dolmadan bıraktı: sonucu girsin
      P.pending = 0;
      P.phase = 'input';
      P.endAt = 0;
      draw();
      return;
    }
    if (s.kind === 'time') record(P.paused ? (s.target - P.pausedLeft / 1000) : (Date.now() - P.phaseStart) / 1000);
    else record(s.kind === 'reps' && !s.test ? 0 : P.pending || 0);
    afterStep();
  }
}

function addRest(sec) {
  if (P.phase !== 'rest') return;
  if (P.paused) P.pausedLeft += sec * 1000;
  else P.endAt += sec * 1000;
  drawClock();
}

async function exitPlayer() {
  const ok = await confirmDialog({
    title: 'Antrenmandan çık',
    message: 'İlerlemen kaydedildi; Bugün sekmesinden kaldığın yerden devam edebilirsin.',
    confirmText: 'Çık'
  });
  if (!ok) return;
  await persistActive();
  closePlayer();
}

async function finishEarly() {
  const ok = await confirmDialog({ title: 'Antrenmanı bitir', message: 'Kalan adımlar atlanır ve yaptığın kadarı kaydedilir.', confirmText: 'Bitir ve kaydet' });
  if (ok) finish();
}

function closePlayer() {
  clearInterval(P.timer);
  clearInterval(P.keepAlive);
  document.removeEventListener('visibilitychange', onVisibility);
  releaseWakeLock();
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  P.workout = null;
  P.view = null;
  shell.tabs = null;
  render();
}

// --- Oynatıcı çizimi ---

const R = 88;
const CIRC = 2 * Math.PI * R;

function ring(fraction, text, sub) {
  const root = svg('svg', { viewBox: '0 0 200 200', class: 'sp-ring', 'aria-hidden': 'true' });
  root.append(svg('circle', { cx: 100, cy: 100, r: R, class: 'sp-ring-track' }));
  const arc = svg('circle', { cx: 100, cy: 100, r: R, class: 'sp-ring-arc', 'stroke-dasharray': CIRC.toFixed(1), 'stroke-dashoffset': (CIRC * (1 - fraction)).toFixed(1), transform: 'rotate(-90 100 100)' });
  root.append(arc);
  const wrap = el('div', { class: 'sp-ring-wrap' }, root,
    el('div', { class: 'sp-ring-center' }, el('span', { class: 'sp-clock' }, text), sub ? el('span', { class: 'sp-clock-sub' }, sub) : null));
  return wrap;
}

function clockState() {
  const s = current();
  if (P.endAt) {
    const total = P.phase === 'ready' ? (P.endAt - P.phaseStart) / 1000 : P.phase === 'rest' ? (P.endAt - P.phaseStart) / 1000 : (s.cap || s.target);
    const left = Math.max(0, P.paused ? P.pausedLeft / 1000 : (P.endAt - Date.now()) / 1000);
    return { fraction: total ? left / total : 0, text: P.phase === 'ready' ? String(Math.ceil(left)) : T.formatClock(left) };
  }
  const el2 = (Date.now() - P.phaseStart) / 1000;
  return { fraction: 1, text: T.formatClock(el2) };
}

function drawClock() {
  if (!P.view) return;
  const arc = P.view.querySelector('.sp-ring-arc');
  const txt = P.view.querySelector('.sp-clock');
  if (!arc || !txt) return;
  const c = clockState();
  arc.setAttribute('stroke-dashoffset', (CIRC * (1 - c.fraction)).toFixed(1));
  txt.textContent = c.text;
}

function stepper() {
  const s = current();
  const value = el('output', { class: 'sp-count', 'aria-live': 'polite' }, String(P.pending));
  const set = (v) => {
    P.pending = Math.max(0, Math.min(999, v));
    value.textContent = String(P.pending);
  };
  const minus = button('', () => set(P.pending - 1), { className: 'sp-step-btn' });
  minus.setAttribute('aria-label', 'Bir azalt');
  minus.textContent = '−';
  const plus = button('', () => set(P.pending + 1), { className: 'sp-step-btn' });
  plus.setAttribute('aria-label', 'Bir artır');
  plus.textContent = '+';
  const plus5 = button('+5', () => set(P.pending + 5), { className: 'sp-step-btn sp-step-5' });
  plus5.setAttribute('aria-label', 'Beş artır');
  return el('div', { class: 'sp-stepper' },
    el('span', { class: 'sp-stepper-label' }, s.test || s.amrap ? 'Kaç tekrar yaptın?' : 'Yapılan tekrar'),
    el('div', { class: 'sp-stepper-row' }, minus, value, plus, plus5));
}

function draw() {
  if (!P.view) return;
  const steps = P.workout.steps;
  const s = current();
  const def = EXERCISES[s.ex];
  const doneSteps = P.phase === 'rest' ? P.restFor : P.index;
  const phaseLabel = { ready: 'Hazır ol', work: s.test ? 'Test' : 'Çalış', rest: 'Dinlen', input: 'Sonucu gir' }[P.phase];
  const showNext = P.phase === 'rest' ? steps[P.restFor] : s;
  const nextDef = EXERCISES[showNext.ex];
  const setText = showNext.sets ? `${showNext.block} · ${showNext.set}/${showNext.sets}` : showNext.block;

  const head = el('div', { class: 'sp-player-head' },
    iconButton('close', 'Antrenmandan çık', exitPlayer),
    el('div', { class: 'sp-player-title' },
      el('span', { class: 'small muted' }, `${P.workout.title} · adım ${Math.min(doneSteps + 1, steps.length)}/${steps.length}`),
      progressBar((doneSteps / steps.length) * 100, 'Antrenman ilerlemesi')),
    iconButton(S.profile.voice ? 'speaker' : 'mute', S.profile.voice ? 'Sesli komutu kapat' : 'Sesli komutu aç', async () => {
      S.profile.voice = !S.profile.voice;
      await save(KEYS.profile, S.profile);
      if (!S.profile.voice && 'speechSynthesis' in window) window.speechSynthesis.cancel();
      draw();
    }));

  let center;
  const c = clockState();
  if (P.phase === 'ready' || P.phase === 'rest' || (P.phase === 'work' && (s.kind === 'time' || s.kind === 'stopwatch' || s.cap))) {
    center = ring(c.fraction, c.text, P.phase === 'rest' ? 'dinlenme' : P.phase === 'ready' ? 'saniye' : s.kind === 'stopwatch' ? 'geçen süre' : 'kalan');
  } else if (P.phase === 'work') {
    center = el('div', { class: 'sp-big-target' },
      el('span', { class: 'sp-big-num' }, s.test ? 'Maks.' : String(s.target)),
      el('span', { class: 'sp-big-unit' }, s.test ? 'yapabildiğin kadar' : s.amrap ? 'en az · sonra devam et' : 'tekrar'));
  } else {
    center = el('div', { class: 'sp-big-target' }, el('span', { class: 'sp-big-unit' }, 'Süre doldu'));
  }

  const actions = el('div', { class: 'sp-player-actions' });
  if (P.phase === 'work' && s.kind === 'reps' && !(s.test && s.cap)) {
    actions.append(stepper(), button(s.test ? 'Kaydet' : 'Bitti', completeWork, { kind: 'primary', iconName: 'check', className: 'sp-main-btn' }));
  } else if (P.phase === 'input') {
    actions.append(stepper(), button('Kaydet', completeWork, { kind: 'primary', iconName: 'check', className: 'sp-main-btn' }));
  } else if (P.phase === 'work' && s.kind === 'stopwatch') {
    actions.append(button('Bıraktım', completeWork, { kind: 'primary', iconName: 'check', className: 'sp-main-btn' }));
  } else {
    const row = el('div', { class: 'sp-ctrl-row' });
    if (P.endAt) row.append(button(P.paused ? 'Devam' : 'Duraklat', togglePause, { iconName: P.paused ? 'play' : 'pause' }));
    if (P.phase === 'rest') row.append(button('+15 sn', () => addRest(15), { iconName: 'plus' }));
    row.append(button(P.phase === 'work' ? (s.test ? 'Bıraktım' : 'Geç') : 'Atla', skip, { iconName: P.phase === 'work' && s.test ? 'check' : 'skip' }));
    actions.append(row);
  }

  replace(P.view,
    head,
    el('div', { class: `sp-stage phase-${P.phase}` },
      el('div', { class: 'sp-info' },
        el('span', { class: 'sp-phase', role: 'status' }, phaseLabel, P.paused ? ' · duraklatıldı' : ''),
        el('h2', { class: 'sp-ex-name' }, P.phase === 'rest' ? `Sıradaki: ${nextDef.name}` : def.name),
        el('span', { class: 'sp-ex-set muted' }, [setText, P.phase === 'rest' || P.phase === 'ready' ? targetText(showNext) : (showNext.label || '')].filter(Boolean).join(' · ')),
        el('details', { class: 'sp-cues' },
          el('summary', null, 'Doğru form'),
          el('ul', { class: 'bullets' }, nextDef.cues.map((t) => el('li', null, t))))),
      el('div', { class: 'sp-center' }, center),
      actions),
    el('div', { class: 'row sp-player-foot' },
      button('Antrenmanı bitir', finishEarly, { kind: 'ghost', iconName: 'check' })));
  if (P.paused) P.view.querySelector('.sp-stage').classList.add('is-paused');
}

// --- Bitiş ---

function finish() {
  clearInterval(P.timer);
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  const results = P.results.filter(Boolean);
  const workout = P.workout;
  if (!results.length) {
    toast('Hiç adım tamamlanmadığı için kaydedilecek bir şey yok.');
    S.active = null;
    db.setMeta(KEYS.active, null).catch(() => {});
    closePlayer();
    return;
  }
  const durationSec = Math.round((Date.now() - new Date(P.startedAt).getTime()) / 1000);
  const totals = T.totalsOf(results);
  const isTest = results.some((r) => r.test);
  const xp = T.xpOf(results) + (results.length ? 50 : 0) + (isTest ? 100 : 0);
  const before = T.rankOf(totalXp());
  const after = T.rankOf(totalXp() + xp);
  const isRun = workout.type === 'B' || workout.type === 'D';
  beep(880, 120);
  setTimeout(() => beep(1180, 260), 160);
  say(after.index > before.index ? `Tebrikler! Yeni rütbe: ${after.name}.` : 'Antrenman tamam. Aferin!');
  let rating = 'ok';
  const rate = segmented([['easy', 'Kolay'], ['ok', 'Tam kıvamında'], ['hard', 'Zor']], rating, (v) => {
    rating = v;
  }, 'Antrenman nasıldı?');
  rate.classList.add('sp-rate');
  const form = el('form', { class: 'form-stack', novalidate: true },
    isRun ? field({ label: 'Koşulan mesafe (km, isteğe bağlı)', name: 'distance', inputmode: 'decimal', placeholder: 'ör. 4,2', hint: 'Telefonun ya da saatin ölçtüyse yaz; tempo hesaplanır.' }) : null,
    field({ label: 'Not (isteğe bağlı)', name: 'note', maxlength: 200, placeholder: 'ör. sol omuz hafif ağrıdı' }));
  form.addEventListener('submit', (e) => e.preventDefault());
  const tests = results.filter((r) => r.test);
  replace(P.view,
    el('section', { class: 'card sp-finish' },
      el('div', { class: 'sp-finish-head' }, insignia(after.index, 64),
        el('div', null,
          el('h2', null, after.index > before.index ? `Terfi: ${after.name}` : 'Antrenman tamamlandı'),
          el('p', { class: 'muted' }, `${workout.title} · +${xp} puan`))),
      el('div', { class: 'stats' },
        el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, T.formatDuration(durationSec)), el('span', { class: 'stat-label' }, 'Süre')),
        el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, formatNumber(totals.reps)), el('span', { class: 'stat-label' }, 'Toplam tekrar')),
        totals.runSec ? el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, `${Math.round(totals.runSec / 60)} dk`), el('span', { class: 'stat-label' }, 'Koşu')) : null,
        el('div', { class: 'stat' }, el('span', { class: 'stat-value' }, `+${xp}`), el('span', { class: 'stat-label' }, 'Puan'))),
      tests.length ? el('ul', { class: 'sp-mission-list' }, tests.map((r) => el('li', null, el('span', null, exName(r.ex)), el('strong', null, r.test === 'plank' ? T.formatClock(r.done) : `${r.done} tekrar`)))) : null,
      el('div', { class: 'stack' }, el('span', { class: 'field-label' }, 'Nasıldı? (bir sonraki yükü belirler)'), rate),
      form,
      el('div', { class: 'row mt' },
        button('Kaydet', () => saveSession({ workout, results, durationSec, totals, xp, rating: () => rating, form }), { kind: 'primary', iconName: 'check', className: 'sp-main-btn' }),
        button('Kaydetmeden çık', async () => {
          const ok = await confirmDialog({ title: 'Kaydetmeden çık', message: 'Bu antrenman ve puanı kaydedilmez.', confirmText: 'Çık', danger: true });
          if (!ok) return;
          S.active = null;
          await db.setMeta(KEYS.active, null);
          closePlayer();
        }, { kind: 'ghost' }))));
}

async function saveSession({ workout, results, durationSec, totals, xp, rating, form }) {
  clearFieldErrors(form);
  let distanceKm = null;
  if (form.elements.distance && form.elements.distance.value.trim()) {
    const d = parseTrNumber(form.elements.distance.value);
    if (!Number.isFinite(d) || d <= 0 || d > 100) {
      showFieldErrors(form, { distance: '0 ile 100 km arası bir sayı yaz (ör. 4,2).' });
      return;
    }
    distanceKm = Math.round(d * 100) / 100;
  }
  const r = rating();
  const test = {};
  for (const x of results) if (x.test) test[x.test] = x.done;
  const session = {
    id: shortId(),
    date: today(),
    week: workout.week,
    slot: P.meta.slot ?? null,
    extra: Boolean(P.meta.extra),
    type: workout.type,
    title: workout.title,
    startedAt: P.startedAt,
    durationSec,
    xp,
    rating: r,
    note: form.elements.note.value.trim(),
    distanceKm,
    results,
    totals,
    test: Object.keys(test).length ? test : null
  };
  const { profile, changes } = T.adaptProfile(S.profile, workout, results, r);
  const hadBadges = new Set(S.profile.badges || []);
  // Seviye testiyle başlandıysa başlangıç değerleri testin sonuçları olsun
  if (!S.sessions.length && session.test) profile.firstMaxes = { ...profile.maxes };
  S.sessions = [...S.sessions, session];
  S.profile = profile;
  const earned = T.earnedBadges(S.profile, S.sessions, currentWeek()).filter((b) => b.earned);
  S.profile.badges = earned.map((b) => b.key);
  const fresh = earned.filter((b) => !hadBadges.has(b.key));
  if (!(await save(KEYS.sessions, S.sessions))) return;
  await save(KEYS.profile, S.profile);
  S.active = null;
  await db.setMeta(KEYS.active, null);
  if (session.test && (test.pushups || test.situps)) {
    try {
      const fit = await readFitness();
      fit.entries.push({ id: shortId(), date: session.date, run: null, pushups: test.pushups ?? null, situps: test.situps ?? null, note: 'Antrenman sayfasındaki test' });
      await db.setMeta(FIT_KEY, fit);
    } catch (err) {
      toastError('sport.fitness', err);
    }
  }
  const names = { pushups: 'şınav', situps: 'mekik', squats: 'squat', plank: 'plank' };
  const up = changes.filter((c) => c.to !== c.from).map((c) => `${names[c.base]} ${c.base === 'plank' ? T.formatClock(c.from) : c.from} → ${c.base === 'plank' ? T.formatClock(c.to) : c.to}`);
  toast(up.length ? `Kaydedildi. Seviyen güncellendi: ${up.join(', ')}.` : 'Antrenman kaydedildi.', { kind: 'success' });
  if (fresh.length) toast(`Yeni rozet: ${fresh.map((b) => b.name).join(', ')}`, { kind: 'success' });
  closePlayer();
}

// --- Başlangıç ---

async function load() {
  S.profile = (await db.getMeta(KEYS.profile)) || null;
  if (S.profile) S.profile = { ...structuredClone(T.DEFAULT_PROFILE), ...S.profile, maxes: { ...T.DEFAULT_PROFILE.maxes, ...S.profile.maxes }, adjust: { ...T.DEFAULT_PROFILE.adjust, ...S.profile.adjust } };
  const sessions = await db.getMeta(KEYS.sessions);
  S.sessions = Array.isArray(sessions) ? sessions : [];
  S.active = (await db.getMeta(KEYS.active)) || null;
  if (S.active && !T.TYPES[S.active.type]) S.active = null;
}

async function setup() {
  replace(main, loadingState());
  try {
    await load();
  } catch (err) {
    toastError('sport.load', err);
  }
  render();
  window.addEventListener('pagehide', () => {
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  });
}

const ready = await initApp({ page: 'sport', title: 'Antrenman' });
if (ready) await setup();
