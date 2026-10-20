// Antrenman programı motoru: 8 haftalık dönem, kişisel maksimumlardan türetilen setler,
// "nasıldı?" puanına göre kendini ayarlayan yük, rütbe/rozet hesapları. DOM kullanmaz.
import { EXERCISES, RANKS, BADGES } from '../data/exercises.js';
import { addDays, diffDays, weekdayIndexMon } from './dates.js';

export const CYCLE_WEEKS = 8;

export const PHASES = [
  { name: 'Temel', pct: 0.55, sets: 3 },
  { name: 'Temel', pct: 0.6, sets: 4 },
  { name: 'Gelişim', pct: 0.63, sets: 4 },
  { name: 'Gelişim', pct: 0.68, sets: 5 },
  { name: 'Toparlanma + ara test', pct: 0.5, sets: 3, deload: true, test: true },
  { name: 'Yoğun', pct: 0.72, sets: 5 },
  { name: 'Yoğun', pct: 0.77, sets: 5 },
  { name: 'Sınav haftası', pct: 0.5, sets: 3, deload: true, test: true }
];

export const TYPES = {
  A: { title: 'Üst vücut + karın', short: 'Üst vücut', focus: ['push', 'core'], icon: 'medal' },
  B: { title: 'Aralıklı koşu', short: 'Aralıklı koşu', focus: ['run'], icon: 'run' },
  C: { title: 'Bacak + kondisyon', short: 'Bacak', focus: ['legs'], icon: 'flame' },
  D: { title: 'Uzun koşu', short: 'Uzun koşu', focus: ['run'], icon: 'run' },
  E: { title: 'Komando devresi', short: 'Komando', focus: ['push', 'legs', 'core'], icon: 'flame' },
  T: { title: 'Fiziki test', short: 'Test', focus: [], icon: 'target' }
};

const ROTATIONS = { 3: ['A', 'B', 'C'], 4: ['A', 'B', 'C', 'D'], 5: ['A', 'B', 'C', 'E', 'D'] };

export const DEFAULT_PROFILE = {
  startDate: '',
  days: [0, 2, 4],
  maxes: { pushups: 15, situps: 25, squats: 30, plank: 60 },
  runBase: 15,
  testCap: 60,
  adjust: { push: 1, core: 1, legs: 1, run: 1 },
  voice: true,
  sound: true
};

const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));

export function mondayOf(iso) {
  return addDays(iso, -weekdayIndexMon(iso));
}

export function weekIndex(profile, today) {
  return Math.max(0, Math.floor(diffDays(mondayOf(profile.startDate), today) / 7));
}

export function phaseOf(week) {
  return PHASES[week % CYCLE_WEEKS];
}

export function cycleOf(week) {
  return Math.floor(week / CYCLE_WEEKS) + 1;
}

export function rotationFor(profile, week) {
  const rot = [...(ROTATIONS[profile.days.length] || ROTATIONS[3])];
  if (phaseOf(week).test) rot[rot.length - 1] = 'T';
  return rot;
}

// Haftanın planı: seçili günlere sırayla antrenman dağıtılır.
export function weekPlan(profile, week, sessions) {
  const rot = rotationFor(profile, week);
  const monday = addDays(mondayOf(profile.startDate), week * 7);
  const done = sessions.filter((s) => s.week === week && !s.extra);
  let days = [...profile.days].sort((a, b) => a - b);
  // Başlangıç haftası: başlangıçtan önceki günler sayılmaz; eksik görevler sonraki boş günlere kayar
  if (week === 0) {
    const startDay = weekdayIndexMon(profile.startDate);
    const free = [0, 1, 2, 3, 4, 5, 6].filter((d) => d >= startDay);
    days = days.filter((d) => d >= startDay);
    for (const d of free) if (days.length < rot.length && !days.includes(d)) days.push(d);
    days.sort((a, b) => a - b);
    if (!days.length) days = [6];
  }
  return rot.map((type, i) => ({
    type,
    date: addDays(monday, days[i] ?? days[days.length - 1]),
    done: Boolean(done.find((s) => s.slot === i)) || done.length > i
  }));
}

export function nextSlot(profile, week, sessions) {
  const rot = rotationFor(profile, week);
  const doneCount = sessions.filter((s) => s.week === week && !s.extra).length;
  return doneCount < rot.length ? { slot: doneCount, type: rot[doneCount] } : null;
}

function reps(profile, base, ratio, pct, group) {
  const max = Number(profile.maxes[base]) || 10;
  return Math.max(3, Math.round(max * ratio * pct * (profile.adjust[group] || 1)));
}

function secs(profile, base, ratio, pct, group) {
  const max = Number(profile.maxes[base]) || 30;
  return Math.max(15, Math.round((max * ratio * pct * (profile.adjust[group] || 1)) / 5) * 5);
}

function step(ex, opts = {}) {
  const def = EXERCISES[ex];
  return { ex, kind: def.type, target: opts.target ?? 30, rest: opts.rest ?? 0, block: opts.block || '', set: opts.set || 0, sets: opts.sets || 0, amrap: Boolean(opts.amrap), test: opts.test || '', cap: opts.cap || 0, label: opts.label || '' };
}

function sets(out, ex, n, target, rest, block, { amrapLast = false } = {}) {
  for (let i = 1; i <= n; i++) {
    out.push(step(ex, { target, rest: i === n ? Math.max(rest, 60) : rest, block, set: i, sets: n, amrap: amrapLast && i === n }));
  }
}

function timed(out, list, block, rest = 0) {
  for (const [ex, sec] of list) out.push(step(ex, { target: sec, rest, block }));
}

function cooldown(out, list) {
  timed(out, list.map((ex) => [ex, 40]), 'Esneme');
}

function warmupStrength(out) {
  timed(out, [['jumpingJack', 45], ['armCircles', 30], ['hipOpener', 30], ['inchworm', 40]], 'Isınma');
  out[out.length - 1].rest = 20;
}

function buildA(p, wk, ph) {
  const out = [];
  warmupStrength(out);
  const pushRest = ph.name === 'Yoğun' ? 90 : 75;
  sets(out, 'pushup', ph.sets, reps(p, 'pushups', 1, ph.pct, 'push'), pushRest, 'Ana set', { amrapLast: true });
  const w = wk % CYCLE_WEEKS;
  if (ph.deload || w < 2) {
    sets(out, 'wideP', 2, reps(p, 'pushups', 0.8, ph.pct, 'push'), 60, 'Yardımcı');
  } else if (w < 5) {
    sets(out, 'diamondP', 3, reps(p, 'pushups', 0.55, ph.pct, 'push'), 60, 'Yardımcı');
    timed(out, [['plankShoulder', 30]], 'Yardımcı', 45);
  } else {
    sets(out, 'pikeP', 3, reps(p, 'pushups', 0.45, ph.pct, 'push'), 60, 'Yardımcı');
    sets(out, 'explosiveP', 2, reps(p, 'pushups', 0.35, ph.pct, 'push'), 75, 'Güç');
  }
  sets(out, 'situp', Math.max(2, ph.sets - 1), reps(p, 'situps', 1, ph.pct, 'core'), 60, 'Karın', { amrapLast: !ph.deload });
  sets(out, 'plank', 2, secs(p, 'plank', 1, ph.pct + 0.1, 'core'), 45, 'Karın');
  sets(out, 'legRaise', 2, reps(p, 'situps', 0.5, ph.pct, 'core'), 45, 'Karın');
  if (w >= 2 && !ph.deload) timed(out, [['hollowHold', secs(p, 'plank', 0.4, ph.pct + 0.2, 'core')]], 'Karın', 30);
  timed(out, [['superman', 40]], 'Karın', 20);
  cooldown(out, ['stretchChest', 'childPose']);
  return out;
}

function buildC(p, wk, ph) {
  const out = [];
  timed(out, [['highKnees', 40], ['hipOpener', 40], ['jumpingJack', 40]], 'Isınma');
  out[out.length - 1].rest = 20;
  const w = wk % CYCLE_WEEKS;
  sets(out, 'squat', ph.sets, reps(p, 'squats', 1, ph.pct, 'legs'), 60, 'Ana set', { amrapLast: true });
  sets(out, 'lunge', 3, reps(p, 'squats', 0.5, ph.pct, 'legs'), 45, 'Yardımcı');
  if (w >= 2 && !ph.deload) sets(out, 'jumpSquat', 3, reps(p, 'squats', 0.4, ph.pct, 'legs'), 60, 'Güç');
  sets(out, 'calfRaise', 2, reps(p, 'squats', 0.8, ph.pct, 'legs'), 30, 'Yardımcı');
  sets(out, 'wallSit', 2, secs(p, 'plank', 0.8, ph.pct + 0.1, 'legs'), 45, 'Dayanıklılık');
  // Bitiriş: Tabata (20 sn çalış / 10 sn dinlen ×8) ya da başlangıç haftalarında 30/30
  if (w >= 2 && !ph.deload) {
    for (let i = 0; i < 8; i++) out.push(step(i % 2 ? 'mountainClimber' : 'burpee', { target: 20, rest: 10, block: 'Tabata', set: i + 1, sets: 8 }));
  } else {
    for (let i = 0; i < 4; i++) out.push(step(i % 2 ? 'mountainClimber' : 'burpee', { target: 30, rest: 30, block: 'Bitiriş', set: i + 1, sets: 4 }));
  }
  out[out.length - 1].rest = 30;
  cooldown(out, ['stretchQuad', 'stretchHam', 'calfStretch']);
  return out;
}

function runBase(p) {
  return clamp(Math.round((Number(p.runBase) || 10) * (p.adjust.run || 1)), 3, 90);
}

function buildB(p, wk, ph) {
  const out = [];
  const w = wk % CYCLE_WEEKS;
  const base = runBase(p);
  out.push(step('runWalk', { target: 300, block: 'Isınma', label: 'Tempolu yürüyüş, sonra hafif jog' }));
  const n = ph.deload ? 4 : clamp(4 + Math.floor(w / 2), 4, 8);
  let fast = w < 2 ? 60 : w < 5 ? 90 : 120;
  if (base < 10) fast = Math.min(fast, 45);
  const easy = w >= 5 ? Math.round(fast * 0.75) : fast;
  for (let i = 1; i <= n; i++) {
    out.push(step('runFast', { target: fast, block: 'Aralık', set: i, sets: n }));
    if (i < n) out.push(step('runWalk', { target: easy, block: 'Aralık', set: i, sets: n, label: 'Toparlan' }));
  }
  out.push(step('runWalk', { target: 300, block: 'Soğuma', label: 'Yavaşla, yürüyerek soğu' }));
  cooldown(out, ['calfStretch', 'stretchHam']);
  return out;
}

function buildD(p, wk, ph) {
  const out = [];
  const w = wk % CYCLE_WEEKS;
  const base = runBase(p);
  let minutes = clamp(Math.round(base * (1 + 0.1 * w)), 8, 50);
  if (ph.deload) minutes = Math.round(minutes * 0.8);
  out.push(step('runWalk', { target: 180, block: 'Isınma', label: 'Tempolu yürüyüş' }));
  if (base < 8) {
    // Başlangıç seviyesi: 2 dk koş / 1 dk yürü
    const rounds = Math.max(3, Math.round(minutes / 3));
    for (let i = 1; i <= rounds; i++) {
      out.push(step('runEasy', { target: 120, block: 'Koş-yürü', set: i, sets: rounds }));
      if (i < rounds) out.push(step('runWalk', { target: 60, block: 'Koş-yürü', set: i, sets: rounds }));
    }
  } else if (w >= 5 && !ph.deload) {
    // Yoğun haftalar: rahat koşunun ortasına tempo bölümü
    const tempo = clamp(Math.round(minutes * 0.35), 5, 15);
    out.push(step('runEasy', { target: (minutes - tempo) * 30, block: 'Koşu' }));
    out.push(step('runTempo', { target: tempo * 60, block: 'Koşu' }));
    out.push(step('runEasy', { target: (minutes - tempo) * 30, block: 'Koşu' }));
  } else {
    out.push(step('runEasy', { target: minutes * 60, block: 'Koşu' }));
  }
  out.push(step('runWalk', { target: 180, block: 'Soğuma' }));
  cooldown(out, ['calfStretch', 'stretchQuad', 'stretchHam']);
  return out;
}

function buildE(p, wk, ph) {
  const out = [];
  warmupStrength(out);
  const w = wk % CYCLE_WEEKS;
  const rounds = ph.deload ? 3 : w < 2 ? 3 : w < 5 ? 4 : 5;
  const list = [
    ['burpee', 'time', 40],
    ['pushup', 'reps', reps(p, 'pushups', 0.5, ph.pct, 'push')],
    ['squat', 'reps', reps(p, 'squats', 0.6, ph.pct, 'legs')],
    ['mountainClimber', 'time', 40],
    ['situp', 'reps', reps(p, 'situps', 0.5, ph.pct, 'core')],
    ['bearCrawl', 'time', 30]
  ];
  for (let r = 1; r <= rounds; r++) {
    list.forEach(([ex, , target], i) => {
      out.push(step(ex, { target, rest: i === list.length - 1 ? (r === rounds ? 30 : 90) : 15, block: `Tur ${r}/${rounds}`, set: r, sets: rounds }));
    });
  }
  cooldown(out, ['stretchChest', 'stretchQuad', 'childPose']);
  return out;
}

function buildT(p) {
  const out = [];
  warmupStrength(out);
  out[out.length - 1].rest = 60;
  const cap = Number(p.testCap) || 0;
  out.push(step('pushup', { target: 0, test: 'pushups', cap, rest: 180, block: 'Test', label: cap ? `${cap} sn içinde en çok` : 'Durmadan yapabildiğin kadar' }));
  out.push(step('situp', { target: 0, test: 'situps', cap, rest: 180, block: 'Test', label: cap ? `${cap} sn içinde en çok` : 'Durmadan yapabildiğin kadar' }));
  out.push(step('squat', { target: 0, test: 'squats', cap, rest: 120, block: 'Test', label: cap ? `${cap} sn içinde en çok` : 'Durmadan yapabildiğin kadar' }));
  out.push(step('plank', { target: 0, test: 'plank', rest: 0, block: 'Test', label: 'Bırakana kadar tut' }));
  out[out.length - 1].kind = 'stopwatch';
  cooldown(out, ['stretchChest', 'stretchHam', 'childPose']);
  return out;
}

const BUILDERS = { A: buildA, B: buildB, C: buildC, D: buildD, E: buildE, T: buildT };

export function buildWorkout(profile, week, type) {
  const ph = phaseOf(week);
  const steps = BUILDERS[type](profile, week, ph);
  return { type, week, title: TYPES[type].title, phase: ph.name, steps, estimate: estimateSeconds(steps) };
}

const REP_SECONDS = 2.5;

export function stepSeconds(s) {
  if (s.kind === 'time') return s.target;
  if (s.kind === 'stopwatch') return 90;
  if (s.test) return s.cap || 90;
  return Math.round(s.target * REP_SECONDS + 10);
}

export function estimateSeconds(steps) {
  return steps.reduce((sum, s) => sum + stepSeconds(s) + s.rest, 0) + 10;
}

// Antrenman özeti: aynı hareketin setleri tek satırda.
export function summarize(steps) {
  const rows = [];
  for (const s of steps) {
    const last = rows[rows.length - 1];
    if (last && last.ex === s.ex && last.block === s.block && last.kind === s.kind && last.target === s.target) {
      last.count += 1;
      last.amrap = last.amrap || s.amrap;
    } else {
      rows.push({ ex: s.ex, block: s.block, kind: s.kind, target: s.target, count: 1, amrap: s.amrap, test: s.test, label: s.label });
    }
  }
  return rows;
}

// --- Sonuçlar ---

export function xpOf(results) {
  let xp = 0;
  for (const r of results) {
    if (!r.done) continue;
    const def = EXERCISES[r.ex];
    if (r.kind === 'reps') xp += r.done;
    else if (def.group === 'run') xp += Math.round(r.done / 6);
    else xp += Math.round(r.done / 5);
  }
  return xp;
}

export function totalsOf(results) {
  const t = { pushups: 0, situps: 0, squats: 0, runSec: 0, reps: 0 };
  for (const r of results) {
    if (!r.done) continue;
    const def = EXERCISES[r.ex];
    if (r.kind === 'reps') t.reps += r.done;
    if (def.base === 'pushups' && r.kind === 'reps') t.pushups += r.done;
    if (r.ex === 'situp' || r.ex === 'legRaise') t.situps += r.done;
    if (def.base === 'squats' && r.kind === 'reps') t.squats += r.done;
    if (def.group === 'run' && r.ex !== 'runWalk') t.runSec += r.done;
  }
  return t;
}

// Puan + son "yapabildiğin kadar" setleri → yeni yük çarpanı ve maksimum tahmini.
export function adaptProfile(profile, workout, results, rating) {
  const next = { ...profile, maxes: { ...profile.maxes }, adjust: { ...profile.adjust } };
  const delta = rating === 'easy' ? 0.05 : rating === 'hard' ? -0.07 : 0;
  for (const g of TYPES[workout.type].focus) {
    next.adjust[g] = Math.round(clamp((next.adjust[g] || 1) + delta, 0.8, 1.3) * 100) / 100;
  }
  const ph = phaseOf(workout.week);
  const changes = [];
  for (const r of results) {
    if (r.amrap && r.done) {
      const base = EXERCISES[r.ex].base;
      if (!base || EXERCISES[r.ex].ratio) continue;
      const cur = Number(next.maxes[base]) || 0;
      const estimate = Math.round((r.done / ph.pct) * 0.85);
      const capped = Math.min(Math.round(cur * 1.1) || estimate, estimate);
      if (capped > cur) {
        next.maxes[base] = capped;
        changes.push({ base, from: cur, to: capped });
      }
    }
    // 10 saniyenin altındaki plank testi yanlışlıkla dokunma sayılır, seviyeyi düşürmez
    if (r.test && r.done && !(r.test === 'plank' && r.done < 10)) {
      const cur = Number(next.maxes[r.test]) || 0;
      next.maxes[r.test] = r.done;
      changes.push({ base: r.test, from: cur, to: r.done });
    }
  }
  return { profile: next, changes };
}

// --- Rütbe, seri, rozetler ---

export function rankOf(xp) {
  let idx = 0;
  RANKS.forEach((r, i) => {
    if (xp >= r.xp) idx = i;
  });
  const cur = RANKS[idx];
  const nxt = RANKS[idx + 1] || null;
  const pct = nxt ? ((xp - cur.xp) / (nxt.xp - cur.xp)) * 100 : 100;
  return { index: idx, name: cur.name, next: nxt, pct, toNext: nxt ? nxt.xp - xp : 0 };
}

export function weekCompleted(profile, week, sessions) {
  return sessions.filter((s) => s.week === week && !s.extra).length >= rotationFor(profile, week).length;
}

// Planı eksiksiz tamamlanan art arda haftalar (bu hafta henüz bitmediyse geçen haftadan sayılır).
export function weekStreak(profile, currentWeek, sessions) {
  let w = weekCompleted(profile, currentWeek, sessions) ? currentWeek : currentWeek - 1;
  let n = 0;
  while (w >= 0 && weekCompleted(profile, w, sessions)) {
    n += 1;
    w -= 1;
  }
  return n;
}

export function earnedBadges(profile, sessions, currentWeek) {
  // Kazanılan rozet kalıcıdır (yeni dönemde ya da kayıt silinince geri alınmaz)
  const got = new Set(profile.badges || []);
  const tests = sessions.filter((s) => s.test);
  const best = (k) => Math.max(0, ...tests.map((s) => s.test[k] || 0), ...sessions.flatMap((s) => (s.results || []).filter((r) => r.test === k).map((r) => r.done || 0)));
  if (sessions.length >= 1) got.add('first');
  if (sessions.length >= 10) got.add('ten');
  if (sessions.length >= 50) got.add('fifty');
  for (let w = 0; w <= currentWeek; w++) if (weekCompleted(profile, w, sessions)) got.add('week');
  if (weekStreak(profile, currentWeek, sessions) >= 3) got.add('streak3');
  if (best('pushups') >= 50) got.add('push50');
  if (best('situps') >= 60) got.add('sit60');
  if (best('plank') >= 180) got.add('plank3');
  if (sessions.some((s) => (s.results || []).some((r) => (r.ex === 'runEasy' || r.ex === 'runTempo') && r.done >= 1800))) got.add('run30');
  if (sessions.some((s) => s.type === 'T' && (s.week % CYCLE_WEEKS) === CYCLE_WEEKS - 1)) got.add('cycle');
  return BADGES.map((b) => ({ ...b, earned: got.has(b.key) }));
}

export function formatDuration(sec) {
  const s = Math.max(0, Math.round(sec));
  const m = Math.floor(s / 60);
  const r = s % 60;
  if (m >= 60) return `${Math.floor(m / 60)} sa ${m % 60} dk`;
  return r && m < 10 ? `${m}:${String(r).padStart(2, '0')}` : `${m} dk`;
}

export function formatClock(sec) {
  const s = Math.max(0, Math.ceil(sec));
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}
