// data/questions.json yükleyici (önbellekli).
import { dayOfYearIndex } from './dates.js';
import { randomInt } from './helpers.js';
let cache = null;
export async function loadQuestions() {
  if (!cache) {
    cache = fetch(new URL('../../data/questions.json', import.meta.url)).then((r) => {
      if (!r.ok) throw new Error('Sorular yüklenemedi');
      return r.json();
    }).catch((e) => { cache = null; throw e; });
  }
  return cache;
}
/** { id, category, categoryName, text } listesi. */
export async function allQuestions() {
  const data = await loadQuestions();
  return data.categories.flatMap((c) => c.questions.map((q) => ({ ...q, category: c.id, categoryName: c.name, emoji: c.emoji })));
}
export async function questionOfDay(now = new Date()) {
  const all = await allQuestions();
  return all[(dayOfYearIndex(now) * 37) % all.length];
}

/** Kategoriden, daha önce sorulmamış rastgele soru seçer. */
export function pickQuestion(all, category, exclude) {
  const ex = new Set(exclude);
  const pool = all.filter((q) => (category === 'random' || q.category === category));
  const fresh = pool.filter((q) => !ex.has(q.id));
  const src = fresh.length ? fresh : pool;
  return src[randomInt(src.length)];
}
