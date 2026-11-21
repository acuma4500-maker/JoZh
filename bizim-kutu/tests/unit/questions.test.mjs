import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const data = JSON.parse(readFileSync(new URL('../../data/questions.json', import.meta.url), 'utf8'));
const all = data.categories.flatMap((c) => c.questions.map((q) => ({ ...q, cat: c.id })));
const norm = (s) => s.toLocaleLowerCase('tr-TR').replace(/[^a-zçğıöşü0-9 ]/g, ' ').replace(/\s+/g, ' ').trim();
const STOP = new Set(['bir', 've', 'mi', 'mı', 'mu', 'mü', 'ne', 'sence', 'en', 'sana', 'seni', 'senin', 'bana', 'beni', 'benim', 'için', 'ile', 'olsa', 'olsan', 'olurdu', 'hangi', 'hangisi', 'daha', 'çok', 'gün', 'birlikte', 'neden', 'nasıl', 'var', 'mı', 'da', 'de', 'bu', 'o', 'yoksa', 'sen', 'ben', 'ikimiz', 'bizim']);
const tokens = (s) => new Set(norm(s).split(' ').filter((w) => w.length > 2 && !STOP.has(w)));

test('tam olarak 400 soru, 8 kategori × 50', () => {
  assert.equal(data.categories.length, 8);
  for (const c of data.categories) assert.equal(c.questions.length, 50, c.id);
  assert.equal(all.length, 400);
  assert.equal(data.total, 400);
});

test('kategori adları istenen sekiz kategori', () => {
  assert.deepEqual(data.categories.map((c) => c.name), ['Romantik', 'Eğlenceli', 'Birbirimizi tanıyalım', 'Gelecek hayalleri', 'İlişkimiz', 'Günlük hayat', 'Derin sorular', 'Rastgele']);
});

test('kimlikler 1..400 ve benzersiz', () => {
  const ids = all.map((q) => q.id).sort((a, b) => a - b);
  assert.deepEqual(ids, Array.from({ length: 400 }, (_, i) => i + 1));
});

test('aynı soru iki kez yok', () => {
  const seen = new Map();
  for (const q of all) {
    const k = norm(q.text);
    assert.ok(!seen.has(k), `tekrar: "${q.text}" ~ "${seen.get(k)}"`);
    seen.set(k, q.text);
  }
});

test('birbirinin küçük varyasyonu olan soru yok (anlamlı kelime benzerliği < %70)', () => {
  const toks = all.map((q) => ({ q, t: tokens(q.text) }));
  const flagged = [];
  for (let i = 0; i < toks.length; i++) for (let j = i + 1; j < toks.length; j++) {
    const a = toks[i].t, b = toks[j].t;
    if (a.size < 2 || b.size < 2) continue;
    const inter = [...a].filter((x) => b.has(x)).length;
    const jac = inter / (a.size + b.size - inter);
    if (jac >= 0.7) flagged.push(`${toks[i].q.text} <> ${toks[j].q.text} (${jac.toFixed(2)})`);
  }
  assert.deepEqual(flagged, []);
});

test('her soru soru işaretiyle biter ve makul uzunlukta', () => {
  for (const q of all) {
    assert.ok(q.text.trim().endsWith('?'), q.text);
    assert.ok(q.text.length >= 12 && q.text.length <= 300, q.text);
  }
});
