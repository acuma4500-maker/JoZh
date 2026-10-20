// Mülakat hazırlık: akıllı tekrar kartları, deneme mülakatı, kişisel cevaplar, fiziki hazırlık, rehber.
// İlerleme cihazda (meta 'study:*') tutulur ve yedeğe dahildir; buluta gönderilmez.
import { initApp } from '../app.js';
import * as db from '../storage/local-db.js';
import { el, replace, button, iconButton, segmented, field, openDialog, toast, toastError, chip, progressBar, debounce, confirmDialog, showFieldErrors, clearFieldErrors, saveStatus, loadingState } from '../ui.js';
import { icon } from '../utils/icons.js';
import { CATEGORIES, QUESTIONS, PERSONAL_PROMPTS, CHECKLIST, GUIDE } from '../data/interview-bank.js';
import { todayISO, addDays, diffDays, formatDate, isValidISODate } from '../utils/dates.js';
import { matchesSearch, formatNumber } from '../utils/formatters.js';
import { createAutosave } from '../utils/autosave.js';
import { shortId } from '../utils/id-generator.js';
import { barChart } from '../components/charts.js';
import { pageUrl } from '../router.js';

const main = document.getElementById('main');
const KEYS = {
  progress: 'study:progress',
  settings: 'study:settings',
  days: 'study:days',
  answers: 'study:answers',
  fitness: 'study:fitness',
  custom: 'study:custom',
  checklist: 'study:checklist',
  mocks: 'study:mocks'
};
// Leitner kutuları: kutu → kaç gün sonra tekrar
const INTERVALS = [0, 0, 1, 3, 7, 14];
const LEARNED_BOX = 4;
const TAB_KEY = 'jozh.interviewTab';

const S = {
  tab: readTab(),
  progress: {},
  settings: { interviewDate: '', dailyGoal: 20 },
  days: {},
  answers: {},
  fitness: { entries: [], targets: { run: '', pushups: '', situps: '' } },
  custom: [],
  checklist: {},
  mocks: [],
  cat: 'all',
  mode: 'smart'
};

const hero = el('section', { class: 'iv-hero', 'aria-label': 'Durum' });
const panels = {
  study: el('div', { class: 'iv-panel' }),
  mock: el('div', { class: 'iv-panel' }),
  answers: el('div', { class: 'iv-panel' }),
  fitness: el('div', { class: 'iv-panel' }),
  guide: el('div', { class: 'iv-panel' })
};

function readTab() {
  try {
    const t = localStorage.getItem(TAB_KEY);
    return ['study', 'mock', 'answers', 'fitness', 'guide'].includes(t) ? t : 'study';
  } catch {
    return 'study';
  }
}

function allQuestions() {
  return [...QUESTIONS, ...S.custom.map((c) => ({ ...c, custom: true }))];
}

function catName(key) {
  if (key === 'custom') return 'Kendi sorularım';
  return (CATEGORIES.find((c) => c.key === key) || {}).name || key;
}

async function save(key, value) {
  try {
    await db.setMeta(key, value);
  } catch (err) {
    toastError('interview.save', err);
  }
}

// --- Konuşma (soruyu sesli okuma) ---

function canSpeak() {
  return 'speechSynthesis' in window && typeof SpeechSynthesisUtterance === 'function';
}

function speak(text) {
  if (!canSpeak()) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'tr-TR';
  u.rate = 0.95;
  const voice = window.speechSynthesis.getVoices().find((v) => v.lang && v.lang.toLowerCase().startsWith('tr'));
  if (voice) u.voice = voice;
  window.speechSynthesis.speak(u);
}

// --- İstatistikler ---

function learnedCount(list) {
  return list.filter((q) => (S.progress[q.id] && S.progress[q.id].box >= LEARNED_BOX)).length;
}

function isDue(q, today = todayISO()) {
  const p = S.progress[q.id];
  if (!p) return true;
  return addDays(p.last, INTERVALS[p.box] || 0) <= today;
}

function streak() {
  let n = 0;
  let d = todayISO();
  if (!S.days[d]) d = addDays(d, -1);
  while (S.days[d]) {
    n += 1;
    d = addDays(d, -1);
  }
  return n;
}

function renderHero() {
  const all = allQuestions();
  const learned = learnedCount(all);
  const pct = all.length ? Math.round((learned / all.length) * 100) : 0;
  const today = S.days[todayISO()] || 0;
  const goal = S.settings.dailyGoal || 20;
  let countdown;
  if (isValidISODate(S.settings.interviewDate)) {
    const left = diffDays(todayISO(), S.settings.interviewDate);
    countdown = el('div', { class: 'card stat iv-countdown' },
      el('span', { class: 'stat-label' }, 'Mülakat'),
      el('span', { class: 'stat-value' }, left > 0 ? `${left} gün kaldı` : left === 0 ? 'Bugün! Başarılar' : 'Geçti'),
      el('button', { type: 'button', class: 'link-button small', onclick: openSettings }, formatDate(S.settings.interviewDate)));
  } else {
    countdown = el('div', { class: 'card stat iv-countdown' },
      el('span', { class: 'stat-label' }, 'Mülakat tarihi'),
      button('Tarihi gir', openSettings, { className: 'btn-small', iconName: 'calendar' }));
  }
  replace(hero,
    countdown,
    el('div', { class: 'card stat' },
      el('span', { class: 'stat-label' }, 'Bugün çalışılan'),
      el('span', { class: 'stat-value' }, `${today} / ${goal}`),
      progressBar(Math.min(100, (today / goal) * 100), 'Günlük hedef')),
    el('div', { class: 'card stat' },
      el('span', { class: 'stat-label' }, 'Öğrenilen'),
      el('span', { class: 'stat-value' }, `%${pct}`),
      el('span', { class: 'small muted' }, `${learned} / ${all.length} soru`)),
    el('div', { class: 'card stat' },
      el('span', { class: 'stat-label' }, 'Çalışma serisi'),
      el('span', { class: 'stat-value' }, `${streak()} gün`),
      el('span', { class: 'small muted' }, 'Her gün en az bir kart')));
}

function openSettings() {
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Mülakat tarihi', name: 'interviewDate', type: 'date', value: S.settings.interviewDate }),
    field({ label: 'Günlük kart hedefi', name: 'dailyGoal', type: 'number', value: String(S.settings.dailyGoal || 20), min: '5', max: '200', inputmode: 'numeric' }));
  form.addEventListener('submit', (e) => e.preventDefault());
  openDialog({
    title: 'Mülakat ayarları',
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet',
        kind: 'primary',
        onClick: async (d) => {
          clearFieldErrors(form);
          const goal = Number(form.elements.dailyGoal.value);
          if (!Number.isInteger(goal) || goal < 5 || goal > 200) {
            showFieldErrors(form, { dailyGoal: '5 ile 200 arasında bir sayı yaz.' });
            return;
          }
          S.settings = { interviewDate: form.elements.interviewDate.value, dailyGoal: goal };
          await save(KEYS.settings, S.settings);
          await d.close(true);
          renderHero();
        }
      }
    ]
  });
}

// --- Çalış: kartlar ---

let queue = [];
let current = null;
let revealed = false;
const cardHolder = el('div', { class: 'iv-card-holder' });
const catBar = el('div', { class: 'chips iv-cats', role: 'group', 'aria-label': 'Kategori' });

function pool() {
  const all = allQuestions();
  return S.cat === 'all' ? all : all.filter((q) => (S.cat === 'custom' ? q.custom : q.cat === S.cat));
}

function buildQueue() {
  const list = pool();
  const today = todayISO();
  if (S.mode === 'wrong') {
    queue = list.filter((q) => S.progress[q.id] && S.progress[q.id].box <= 2);
  } else if (S.mode === 'shuffle') {
    queue = list.slice();
  } else {
    queue = list.filter((q) => isDue(q, today));
  }
  // Akıllı tekrar: düşük kutular önce, aynı kutu içinde karışık
  for (let i = queue.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [queue[i], queue[j]] = [queue[j], queue[i]];
  }
  if (S.mode === 'smart') queue.sort((a, b) => ((S.progress[a.id] || { box: 0 }).box) - ((S.progress[b.id] || { box: 0 }).box));
}

function renderCats() {
  const all = allQuestions();
  const cats = [['all', 'Tümü', all], ...CATEGORIES.map((c) => [c.key, c.name, all.filter((q) => q.cat === c.key && !q.custom)])];
  if (S.custom.length) cats.push(['custom', 'Kendi sorularım', all.filter((q) => q.custom)]);
  replace(catBar, cats.map(([key, name, list]) => {
    const b = el('button', { type: 'button', class: 'chip chip-button', 'aria-pressed': String(S.cat === key) },
      name, el('span', { class: 'chip-count' }, ` ${learnedCount(list)}/${list.length}`));
    b.addEventListener('click', () => {
      S.cat = key;
      renderCats();
      buildQueue();
      nextCard();
    });
    return b;
  }));
}

function nextCard() {
  current = queue.shift() || null;
  revealed = false;
  renderCard();
}

function renderCard() {
  if (!current) {
    const doneToday = S.days[todayISO()] || 0;
    replace(cardHolder, el('div', { class: 'card iv-card iv-empty' },
      icon('check', { size: 32 }),
      el('h2', null, S.mode === 'wrong' ? 'Bilemediğin kart kalmadı' : 'Bu bölümde şimdilik tekrar edilecek kart yok'),
      el('p', { class: 'muted' }, doneToday ? `Bugün ${doneToday} kart çalıştın. Harika gidiyorsun!` : 'Başka bir kategori seç ya da karışık modda çalış.'),
      el('div', { class: 'row' },
        button('Karışık çalış', () => {
          S.mode = 'shuffle';
          renderStudy();
        }, { iconName: 'refresh' }))));
    return;
  }
  const q = current;
  const p = S.progress[q.id];
  const answer = el('div', { class: 'iv-answer', hidden: !revealed },
    el('p', { class: 'prose' }, q.a),
    q.tip ? el('p', { class: 'notice notice-info small' }, icon('info'), el('span', null, q.tip)) : null,
    q.check ? el('p', { class: 'notice notice-warning small' }, icon('alert'), el('span', null, 'Bu bilgi zamanla değişebilir; mülakattan önce güncelliğini resmî kaynaklardan kontrol et.')) : null);
  const rate = el('div', { class: 'iv-rate', hidden: !revealed },
    button('Bilemedim', () => grade(0), { className: 'iv-bad' }),
    button('Kısmen', () => grade(1), { className: 'iv-mid' }),
    button('Bildim', () => grade(2), { kind: 'primary', className: 'iv-good' }));
  const reveal = button('Cevabı göster', () => {
    revealed = true;
    answer.hidden = false;
    rate.hidden = false;
    reveal.hidden = true;
    rate.querySelector('.iv-good').focus();
  }, { kind: 'primary', iconName: 'eye', className: 'iv-reveal' });
  reveal.hidden = revealed;
  replace(cardHolder, el('article', { class: 'card iv-card', 'aria-live': 'polite' },
    el('div', { class: 'row iv-card-head' },
      chip(catName(q.custom ? 'custom' : q.cat), { kind: 'accent' }),
      p ? chip(`Kutu ${p.box}/5`) : chip('Yeni', { kind: 'yellow' }),
      el('span', { class: 'grow' }),
      canSpeak() ? iconButton('speaker', 'Soruyu sesli oku', () => speak(q.q)) : null,
      q.custom ? iconButton('edit', 'Soruyu düzenle', () => openCustomEditor(q)) : null),
    el('h2', { class: 'iv-question' }, q.q),
    reveal,
    answer,
    rate,
    el('p', { class: 'small muted iv-left' }, `Sırada ${queue.length} kart · Klavye: Boşluk = cevap, 1/2/3 = Bilemedim/Kısmen/Bildim`)));
}

async function grade(level) {
  const q = current;
  const today = todayISO();
  const prev = S.progress[q.id] || { box: 0, right: 0, wrong: 0, seen: 0 };
  let box = prev.box || 0;
  if (level === 2) box = Math.min(5, Math.max(1, box) + 1);
  else if (level === 1) box = Math.max(1, Math.min(box, 3));
  else box = 1;
  S.progress[q.id] = { box, last: today, seen: (prev.seen || 0) + 1, right: (prev.right || 0) + (level === 2 ? 1 : 0), wrong: (prev.wrong || 0) + (level === 0 ? 1 : 0) };
  // Bilemediği kart aynı oturumda biraz sonra tekrar gelir
  if (level === 0) queue.splice(Math.min(queue.length, 4), 0, q);
  S.days[today] = (S.days[today] || 0) + 1;
  await save(KEYS.progress, S.progress);
  await save(KEYS.days, S.days);
  renderHero();
  renderCats();
  nextCard();
}

function onStudyKey(e) {
  if (S.tab !== 'study' || !current || document.querySelector('dialog[open]')) return;
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;
  if (e.key === ' ' && !revealed) {
    e.preventDefault();
    cardHolder.querySelector('.iv-reveal').click();
  } else if (revealed && ['1', '2', '3'].includes(e.key)) {
    grade(Number(e.key) - 1);
  }
}

function renderBankList(holder, query) {
  const list = pool().filter((q) => matchesSearch(query, q.q, q.a));
  replace(holder, list.length ? el('ul', { class: 'iv-bank' }, list.slice(0, 400).map((q) => el('li', null,
    el('details', null,
      el('summary', null, q.q, q.check ? el('span', { class: 'chip chip-yellow iv-check' }, 'kontrol et') : null),
      el('p', { class: 'prose small' }, q.a))))) : el('p', { class: 'muted small' }, 'Aramaya uyan soru yok.'));
}

function renderStudy() {
  buildQueue();
  const mode = segmented([['smart', 'Akıllı tekrar'], ['wrong', 'Bilemediklerim'], ['shuffle', 'Karışık']], S.mode, (v) => {
    S.mode = v;
    buildQueue();
    nextCard();
  }, 'Çalışma şekli');
  const search = el('input', { type: 'search', class: 'input', id: 'iv-search', placeholder: 'Soru bankasında ara', autocomplete: 'off' });
  const listHolder = el('div');
  search.addEventListener('input', debounce(() => renderBankList(listHolder, search.value), 150));
  renderCats();
  replace(panels.study,
    catBar,
    el('div', { class: 'row iv-modes' }, mode, el('span', { class: 'grow' }), button('Soru ekle', () => openCustomEditor(null), { iconName: 'plus', className: 'btn-small' })),
    cardHolder,
    el('details', { class: 'card iv-bank-card' },
      el('summary', null, 'Bütün soruları listele ve ara'),
      el('div', { class: 'field mt' }, el('label', { class: 'field-label', for: 'iv-search' }, 'Ara'), search),
      listHolder));
  renderBankList(listHolder, '');
  nextCard();
}

function openCustomEditor(q) {
  const form = el('form', { class: 'form-stack', novalidate: true },
    field({ label: 'Kategori', name: 'cat', type: 'select', value: q ? q.cat : 'kisisel', options: CATEGORIES.map((c) => [c.key, c.name]) }),
    field({ label: 'Soru', name: 'q', type: 'textarea', value: q ? q.q : '', rows: 2, maxlength: 300, required: true }),
    field({ label: 'Cevap', name: 'a', type: 'textarea', value: q ? q.a : '', rows: 5, maxlength: 2000, required: true }));
  form.addEventListener('submit', (e) => e.preventDefault());
  const actions = [];
  if (q) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        S.custom = S.custom.filter((c) => c.id !== q.id);
        await save(KEYS.custom, S.custom);
        await d.close(true);
        renderStudy();
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet',
    kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      const data = { cat: form.elements.cat.value, q: form.elements.q.value.trim(), a: form.elements.a.value.trim() };
      const errors = {};
      if (!data.q) errors.q = 'Soruyu yaz.';
      if (!data.a) errors.a = 'Cevabı yaz.';
      if (Object.keys(errors).length) {
        showFieldErrors(form, errors);
        return;
      }
      if (q) S.custom = S.custom.map((c) => (c.id === q.id ? { ...c, ...data } : c));
      else S.custom.push({ id: `custom-${shortId()}`, ...data });
      await save(KEYS.custom, S.custom);
      await d.close(true);
      toast(q ? 'Soru güncellendi.' : 'Soru eklendi; "Kendi sorularım" kategorisinde.', { kind: 'success' });
      renderStudy();
    }
  });
  openDialog({ title: q ? 'Soruyu düzenle' : 'Soru ekle', content: form, actions });
}

// --- Deneme mülakatı ---

let mock = null;
let mockTimer = null;

function pickMock(count) {
  const shuffle = (arr) => arr.map((x) => [Math.random(), x]).sort((a, b) => a[0] - b[0]).map((x) => x[1]);
  const personal = shuffle(QUESTIONS.filter((q) => q.cat === 'kisisel' && !['kisisel-001'].includes(q.id)));
  const scenario = shuffle(QUESTIONS.filter((q) => q.cat === 'durum'));
  const knowledge = shuffle(allQuestions().filter((q) => !['kisisel', 'durum'].includes(q.cat)));
  const intro = QUESTIONS.find((q) => q.id === 'kisisel-001');
  const nPersonal = Math.max(1, Math.round(count * 0.3));
  const nScenario = Math.max(1, Math.round(count * 0.2));
  const rest = count - 1 - nPersonal - nScenario;
  return [intro, ...shuffle([...personal.slice(0, nPersonal), ...scenario.slice(0, nScenario), ...knowledge.slice(0, Math.max(0, rest))])];
}

function stopTimer() {
  clearInterval(mockTimer);
  mockTimer = null;
}

function renderMock() {
  stopTimer();
  if (!mock) {
    const last = S.mocks.slice(-5).reverse();
    const countSel = el('select', { class: 'input select', id: 'mock-count' }, [5, 10, 15, 20].map((n) => el('option', { value: String(n), selected: n === 10 }, `${n} soru`)));
    const speakBox = el('input', { type: 'checkbox', id: 'mock-speak', class: 'checkbox', checked: canSpeak() });
    replace(panels.mock,
      el('section', { class: 'card stack' },
        el('h2', null, 'Deneme mülakatı'),
        el('p', { class: 'muted' }, 'Komisyonun karşısındaymış gibi çalış: soru gelir, yüksek sesle cevap verirsin, sonra örnek cevaba bakıp kendine puan verirsin. İlk soru her zaman "Kendinizi tanıtın" olur.'),
        el('div', { class: 'row' },
          el('div', { class: 'field' }, el('label', { class: 'field-label', for: 'mock-count' }, 'Soru sayısı'), countSel),
          canSpeak() ? el('label', { class: 'check-label', for: 'mock-speak' }, speakBox, el('span', null, 'Soruları sesli oku')) : null),
        el('div', null, button('Başla', () => {
          mock = { list: pickMock(Number(countSel.value)), i: 0, scores: [], speak: speakBox.checked, started: Date.now() };
          renderMock();
        }, { kind: 'primary', iconName: 'chevronRight' }))),
      last.length ? el('section', { class: 'card stack mt' },
        el('h3', null, 'Son denemeler'),
        el('ul', { class: 'compact-list' }, last.map((m) => el('li', null,
          el('span', { class: 'grow' }, `${formatDate(m.date, { short: true })} · ${m.count} soru`),
          chip(`%${m.score}`, { kind: m.score >= 70 ? 'green' : m.score >= 50 ? 'yellow' : 'red' }))))) : null);
    return;
  }
  if (mock.i >= mock.list.length) {
    const total = mock.scores.reduce((s, x) => s + x.score, 0);
    const pct = Math.round((total / (mock.scores.length * 5)) * 100);
    const weak = mock.scores.filter((x) => x.score <= 2);
    S.mocks.push({ date: todayISO(), count: mock.scores.length, score: pct });
    save(KEYS.mocks, S.mocks.slice(-50));
    const done = mock;
    mock = null;
    replace(panels.mock, el('section', { class: 'card stack' },
      el('h2', null, `Deneme bitti: %${pct}`),
      progressBar(pct, 'Deneme puanı'),
      el('p', { class: 'muted' }, pct >= 70 ? 'Çok iyi! Zayıf kalan soruları tekrar edip bir deneme daha yap.' : 'Zayıf kalan sorular çalışma listene eklenebilir; birkaç gün sonra tekrar dene.'),
      weak.length ? el('div', { class: 'stack' },
        el('h3', null, 'Zayıf kalan sorular'),
        el('ul', { class: 'compact-list' }, weak.map((x) => el('li', null, el('span', { class: 'grow' }, x.q.q), chip(`${x.score}/5`, { kind: 'red' })))),
        el('div', null, button('Bunları çalışma listeme ekle', async () => {
          for (const x of weak) {
            const prev = S.progress[x.q.id] || {};
            S.progress[x.q.id] = { ...prev, box: 1, last: addDays(todayISO(), -1), seen: prev.seen || 0, right: prev.right || 0, wrong: (prev.wrong || 0) + 1 };
          }
          await save(KEYS.progress, S.progress);
          toast('Zayıf sorular "Bilemediklerim" listene eklendi.', { kind: 'success' });
        }, { iconName: 'plus' }))) : el('p', null, 'Zayıf kalan soru yok.'),
      el('div', { class: 'row' }, button('Yeni deneme', () => renderMock(), { kind: 'primary', iconName: 'refresh' })),
      el('p', { class: 'small muted' }, `Süre: ${Math.round((Date.now() - done.started) / 60000)} dakika`)));
    renderHero();
    return;
  }
  const q = mock.list[mock.i];
  const startedAt = Date.now();
  const timer = el('span', { class: 'iv-timer', 'aria-live': 'off' }, '0:00');
  const answer = el('div', { class: 'iv-answer', hidden: true },
    el('h3', { class: 'small muted' }, 'Örnek cevap'),
    el('p', { class: 'prose' }, q.a),
    q.tip ? el('p', { class: 'small muted' }, q.tip) : null);
  const scoreRow = el('div', { class: 'iv-score', hidden: true, role: 'group', 'aria-label': 'Kendine puan ver' },
    el('p', { class: 'small' }, 'Cevabın nasıldı?'),
    el('div', { class: 'row' }, [[1, 'Zayıf'], [2, 'Eksik'], [3, 'Orta'], [4, 'İyi'], [5, 'Mükemmel']].map(([n, label]) =>
      button(`${n} · ${label}`, () => {
        mock.scores.push({ q, score: n });
        mock.i += 1;
        renderMock();
      }, { className: 'btn-small' }))));
  const doneBtn = button('Cevabımı verdim', () => {
    stopTimer();
    answer.hidden = false;
    scoreRow.hidden = false;
    doneBtn.hidden = true;
  }, { kind: 'primary', iconName: 'check' });
  replace(panels.mock, el('article', { class: 'card iv-card' },
    el('div', { class: 'row iv-card-head' },
      chip(`Soru ${mock.i + 1} / ${mock.list.length}`, { kind: 'accent' }),
      chip(catName(q.custom ? 'custom' : q.cat)),
      el('span', { class: 'grow' }),
      timer,
      canSpeak() ? iconButton('speaker', 'Soruyu tekrar oku', () => speak(q.q)) : null),
    el('h2', { class: 'iv-question' }, q.q),
    el('p', { class: 'small muted' }, 'Yüksek sesle, komisyona konuşur gibi cevap ver. Hedef: 30-60 saniye.'),
    doneBtn,
    answer,
    scoreRow,
    el('div', { class: 'row mt' }, button('Denemeyi bitir', async () => {
      if (await confirmDialog({ title: 'Denemeyi bitir', message: 'Cevaplanan sorularla sonuç gösterilsin mi?', confirmText: 'Bitir' })) {
        mock.list = mock.list.slice(0, mock.i);
        renderMock();
      }
    }, { kind: 'ghost', className: 'btn-small' }))));
  mockTimer = setInterval(() => {
    const s = Math.floor((Date.now() - startedAt) / 1000);
    timer.textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
    timer.classList.toggle('is-long', s > 90);
  }, 500);
  if (mock.speak) speak(q.q);
}

// --- Kendi cevaplarım ---

function wordCount(text) {
  return (text.trim().match(/\S+/g) || []).length;
}

function renderAnswers() {
  const status = saveStatus();
  const autosave = createAutosave({
    delay: 700,
    save: () => db.setMeta(KEYS.answers, S.answers),
    onState: (s, info) => status.set(s, s === 'error' ? { err: info } : undefined)
  });
  replace(panels.answers,
    el('p', { class: 'notice notice-info' }, icon('info'), el('span', null, 'Bu sorular neredeyse her mülakatta sorulur. Cevabını kendi cümlelerinle yaz, sonra ezberlemeden, yüksek sesle prova et. Konuşma süresi yaklaşık olarak hesaplanır.')),
    status.node,
    el('div', { class: 'stack' }, PERSONAL_PROMPTS.map((p) => {
      const id = `ans-${p.id}`;
      const meta = el('p', { class: 'small muted' });
      const ta = el('textarea', { id, class: 'input textarea', rows: 4, maxlength: 2000, 'aria-describedby': `${id}-hint` });
      ta.value = S.answers[p.id] || '';
      const update = () => {
        const w = wordCount(ta.value);
        meta.textContent = w ? `${w} kelime · yaklaşık ${Math.max(5, Math.round(w / 2.2))} saniye` : '';
      };
      update();
      ta.addEventListener('input', () => {
        S.answers[p.id] = ta.value;
        update();
        autosave.schedule();
      });
      return el('section', { class: 'card stack iv-prompt' },
        el('label', { class: 'item-title', for: id }, p.q),
        el('p', { class: 'small muted', id: `${id}-hint` }, p.hint),
        ta,
        el('div', { class: 'row' }, meta, el('span', { class: 'grow' }),
          canSpeak() ? button('Sesli dinle', () => speak(ta.value || p.q), { className: 'btn-small', iconName: 'speaker' }) : null));
    })));
}

// --- Fiziki hazırlık ---

function parseRun(text) {
  const t = String(text || '').trim();
  if (!t) return null;
  const m = /^(\d{1,2})[:.,](\d{2})$/.exec(t);
  if (m) return Number(m[1]) * 60 + Number(m[2]);
  if (/^\d{1,4}$/.test(t)) return Number(t);
  return NaN;
}

function fmtRun(sec) {
  if (!sec && sec !== 0) return '—';
  return `${Math.floor(sec / 60)}:${String(sec % 60).padStart(2, '0')}`;
}

function renderFitness() {
  const entries = S.fitness.entries.slice().sort((a, b) => a.date.localeCompare(b.date));
  const t = S.fitness.targets;
  const best = {
    run: Math.min(...entries.map((e) => e.run).filter((x) => x > 0)),
    pushups: Math.max(0, ...entries.map((e) => e.pushups || 0)),
    situps: Math.max(0, ...entries.map((e) => e.situps || 0))
  };
  const targetRun = parseRun(t.run);
  const status = (ok) => (ok ? chip('Hedef geçildi', { kind: 'green' }) : chip('Hedefin altında', { kind: 'yellow' }));
  const recent = entries.slice(-10);
  replace(panels.fitness,
    el('p', { class: 'notice notice-warning' }, icon('alert'), el('span', null, 'Fiziki yeterlilik testinin branşları (mekik, şınav, koşu), süreleri ve baraj puanları her alımda kılavuzda yayımlanır. Hedeflerini kendi başvuru kılavuzundaki tabloya göre gir.')),
    el('div', { class: 'stats iv-fit-stats' },
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'En iyi koşu'), el('span', { class: 'stat-value' }, Number.isFinite(best.run) ? fmtRun(best.run) : '—'),
        t.run && Number.isFinite(best.run) ? status(best.run <= targetRun) : el('span', { class: 'small muted' }, t.run ? `Hedef ${t.run}` : 'Hedef girilmedi')),
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'En çok şınav'), el('span', { class: 'stat-value' }, String(best.pushups || '—')),
        t.pushups && best.pushups ? status(best.pushups >= Number(t.pushups)) : el('span', { class: 'small muted' }, t.pushups ? `Hedef ${t.pushups}` : 'Hedef girilmedi')),
      el('div', { class: 'card stat' }, el('span', { class: 'stat-label' }, 'En çok mekik'), el('span', { class: 'stat-value' }, String(best.situps || '—')),
        t.situps && best.situps ? status(best.situps >= Number(t.situps)) : el('span', { class: 'small muted' }, t.situps ? `Hedef ${t.situps}` : 'Hedef girilmedi'))),
    el('p', { class: 'notice notice-info mt' }, icon('run'), el('span', null, 'Ekipmansız 8 haftalık program, sesli zamanlayıcı ve seviye testleri için ', el('a', { href: pageUrl('sport') }, 'Antrenman sayfasına'), ' geç. Oradaki test sonuçları buraya da yazılır.')),
    el('div', { class: 'row mt' },
      button('Antrenman kaydet', () => openFitnessEntry(null), { kind: 'primary', iconName: 'plus' }),
      button('Hedefleri gir', openTargets, { iconName: 'target' })),
    recent.length >= 2 ? el('section', { class: 'card chart-card mt' },
      el('h2', null, 'Şınav ve mekik gelişimi'),
      barChart({
        title: 'Son antrenmanlarda şınav ve mekik sayıları',
        tableCaption: 'Şınav ve mekik',
        rowHeader: 'Tarih',
        series: [{ key: 'pushups', name: 'Şınav', className: 'series-income' }, { key: 'situps', name: 'Mekik', className: 'series-expense' }],
        format: (v) => formatNumber(v),
        groups: recent.map((e) => ({ label: formatDate(e.date, { short: true, year: false }), title: formatDate(e.date), values: { pushups: e.pushups || 0, situps: e.situps || 0 }, note: e.run ? `Koşu: ${fmtRun(e.run)}` : '' }))
      })) : null,
    entries.length ? el('section', { class: 'card mt' },
      el('h2', null, 'Antrenman kayıtları'),
      el('div', { class: 'table-wrap' }, el('table', { class: 'table' },
        el('thead', null, el('tr', null, el('th', null, 'Tarih'), el('th', { class: 'num' }, 'Koşu'), el('th', { class: 'num' }, 'Şınav'), el('th', { class: 'num' }, 'Mekik'), el('th', null, 'Not'), el('th', null, el('span', { class: 'visually-hidden' }, 'İşlem')))),
        el('tbody', null, entries.slice().reverse().map((e) => el('tr', null,
          el('td', null, formatDate(e.date, { short: true })),
          el('td', { class: 'num' }, e.run ? fmtRun(e.run) : '—'),
          el('td', { class: 'num' }, e.pushups ?? '—'),
          el('td', { class: 'num' }, e.situps ?? '—'),
          el('td', null, e.note || ''),
          el('td', null, iconButton('edit', 'Kaydı düzenle', () => openFitnessEntry(e))))))))) : el('p', { class: 'muted mt' }, 'Henüz antrenman kaydı yok.'));
}

function openTargets() {
  const t = S.fitness.targets;
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('p', { class: 'small muted' }, 'Kılavuzdaki tabloda yaşına göre yazan değerleri gir (ör. koşu için 1:30).'),
    field({ label: 'Koşu hedef süresi (dk:sn)', name: 'run', value: t.run, placeholder: 'ör. 1:30' }),
    field({ label: 'Şınav hedefi (adet)', name: 'pushups', value: t.pushups, inputmode: 'numeric' }),
    field({ label: 'Mekik hedefi (adet)', name: 'situps', value: t.situps, inputmode: 'numeric' }));
  form.addEventListener('submit', (e) => e.preventDefault());
  openDialog({
    title: 'Fiziki hedefler',
    content: form,
    size: 'sm',
    actions: [
      { label: 'Vazgeç', onClick: (d) => d.close() },
      {
        label: 'Kaydet',
        kind: 'primary',
        onClick: async (d) => {
          clearFieldErrors(form);
          const run = form.elements.run.value.trim();
          const errors = {};
          if (run && !Number.isFinite(parseRun(run))) errors.run = 'Süreyi dk:sn biçiminde yaz (ör. 1:30).';
          for (const k of ['pushups', 'situps']) if (form.elements[k].value && !/^\d{1,3}$/.test(form.elements[k].value.trim())) errors[k] = 'Adet olarak yaz.';
          if (Object.keys(errors).length) {
            showFieldErrors(form, errors);
            return;
          }
          S.fitness.targets = { run, pushups: form.elements.pushups.value.trim(), situps: form.elements.situps.value.trim() };
          await save(KEYS.fitness, S.fitness);
          await d.close(true);
          renderFitness();
        }
      }
    ]
  });
}

function openFitnessEntry(entry) {
  const e = entry || { date: todayISO(), run: null, pushups: null, situps: null, note: '' };
  const form = el('form', { class: 'form-stack', novalidate: true },
    el('div', { class: 'form-grid' },
      field({ label: 'Tarih', name: 'date', type: 'date', value: e.date, required: true }),
      field({ label: 'Koşu süresi (dk:sn)', name: 'run', value: e.run ? fmtRun(e.run) : '', placeholder: 'ör. 1:28' }),
      field({ label: 'Şınav (adet)', name: 'pushups', value: e.pushups ?? '', inputmode: 'numeric' }),
      field({ label: 'Mekik (adet)', name: 'situps', value: e.situps ?? '', inputmode: 'numeric' })),
    field({ label: 'Not', name: 'note', value: e.note, maxlength: 200, placeholder: 'ör. 400 m pist, rüzgârlı' }));
  form.addEventListener('submit', (ev) => ev.preventDefault());
  const actions = [];
  if (entry) {
    actions.push({
      label: 'Sil', kind: 'danger', icon: 'trash', className: 'mr-auto',
      onClick: async (d) => {
        S.fitness.entries = S.fitness.entries.filter((x) => x.id !== entry.id);
        await save(KEYS.fitness, S.fitness);
        await d.close(true);
        renderFitness();
      }
    });
  }
  actions.push({ label: 'Vazgeç', onClick: (d) => d.close() });
  actions.push({
    label: 'Kaydet',
    kind: 'primary',
    onClick: async (d) => {
      clearFieldErrors(form);
      const f = form.elements;
      const errors = {};
      if (!isValidISODate(f.date.value)) errors.date = 'Tarih seç.';
      const run = parseRun(f.run.value);
      if (Number.isNaN(run)) errors.run = 'Süreyi dk:sn biçiminde yaz (ör. 1:28).';
      const num = (v, name) => {
        const s = String(v).trim();
        if (!s) return null;
        if (!/^\d{1,3}$/.test(s)) {
          errors[name] = 'Adet olarak yaz.';
          return null;
        }
        return Number(s);
      };
      const pushups = num(f.pushups.value, 'pushups');
      const situps = num(f.situps.value, 'situps');
      if (!Object.keys(errors).length && run === null && pushups === null && situps === null) errors.run = 'En az bir değer gir.';
      if (Object.keys(errors).length) {
        showFieldErrors(form, errors);
        return;
      }
      const item = { id: entry ? entry.id : shortId(), date: f.date.value, run, pushups, situps, note: f.note.value.trim() };
      S.fitness.entries = entry ? S.fitness.entries.map((x) => (x.id === entry.id ? item : x)) : [...S.fitness.entries, item];
      await save(KEYS.fitness, S.fitness);
      await d.close(true);
      toast('Antrenman kaydedildi.', { kind: 'success' });
      renderFitness();
    }
  });
  openDialog({ title: entry ? 'Kaydı düzenle' : 'Antrenman kaydet', content: form, actions });
}

// --- Rehber ---

function renderGuide() {
  const doneCount = CHECKLIST.filter((_, i) => S.checklist[i]).length;
  replace(panels.guide,
    el('section', { class: 'card stack' },
      el('div', { class: 'card-header' }, el('h2', null, 'Mülakat günü kontrol listesi'), chip(`${doneCount}/${CHECKLIST.length}`, { kind: doneCount === CHECKLIST.length ? 'green' : '' })),
      el('ul', { class: 'check-list' }, CHECKLIST.map((text, i) => {
        const id = `chk-${i}`;
        const cb = el('input', { type: 'checkbox', id, class: 'checkbox', checked: Boolean(S.checklist[i]) });
        cb.addEventListener('change', async () => {
          S.checklist[i] = cb.checked;
          await save(KEYS.checklist, S.checklist);
          renderGuide();
        });
        return el('li', { class: `check-row${S.checklist[i] ? ' is-done' : ''}` }, cb, el('label', { for: id, class: 'check-text' }, text));
      }))),
    GUIDE.map((g) => el('section', { class: 'card stack mt' },
      el('h2', null, g.title),
      el('ul', { class: 'bullets' }, g.items.map((t) => el('li', null, t))))),
    el('p', { class: 'small muted mt' }, 'Resmî bilgi: başvuru kılavuzu ve duyurular için personeltemin.msb.gov.tr adresini takip et. Bu sayfadaki sorular resmî "çıkmış sorular" değildir; MSB kitapçıkları ve adayların sık aktardığı soru türlerinden derlenmiştir.'));
}

// --- Genel ---

function render() {
  for (const [k, node] of Object.entries(panels)) node.hidden = k !== S.tab;
  if (S.tab !== 'mock') stopTimer();
  if (S.tab !== 'mock' && canSpeak()) window.speechSynthesis.cancel();
  if (S.tab === 'study') renderStudy();
  else if (S.tab === 'mock') renderMock();
  else if (S.tab === 'answers') renderAnswers();
  else if (S.tab === 'fitness') renderFitness();
  else renderGuide();
}

async function load() {
  const get = async (k, def) => {
    const v = await db.getMeta(k);
    return v === undefined || v === null ? def : v;
  };
  S.progress = await get(KEYS.progress, {});
  S.settings = { ...S.settings, ...(await get(KEYS.settings, {})) };
  S.days = await get(KEYS.days, {});
  S.answers = await get(KEYS.answers, {});
  S.fitness = { ...S.fitness, ...(await get(KEYS.fitness, {})) };
  S.custom = await get(KEYS.custom, []);
  S.checklist = await get(KEYS.checklist, {});
  S.mocks = await get(KEYS.mocks, []);
}

async function setup() {
  replace(main, loadingState());
  try {
    await load();
  } catch (err) {
    toastError('interview.load', err);
  }
  const tabs = segmented([['study', 'Çalış'], ['mock', 'Deneme'], ['answers', 'Cevaplarım'], ['fitness', 'Fiziki'], ['guide', 'Rehber']], S.tab, (v) => {
    S.tab = v;
    try {
      localStorage.setItem(TAB_KEY, v);
    } catch {
      // yok say
    }
    render();
  }, 'Bölüm');
  tabs.classList.add('iv-tabs');
  replace(main, hero, tabs, ...Object.values(panels));
  renderHero();
  render();
  document.addEventListener('keydown', onStudyKey);
  window.addEventListener('pagehide', () => {
    if (canSpeak()) window.speechSynthesis.cancel();
  });
}

const ready = await initApp({ page: 'interview', title: 'Mülakat hazırlık' });
if (ready) await setup();
