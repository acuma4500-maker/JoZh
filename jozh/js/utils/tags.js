// Etiketler: virgülle yazılır, en çok 20 etiket, her biri en çok 40 karakter.
import { normalizeSearch } from './formatters.js';

export const MAX_TAGS = 20;
export const MAX_TAG_LENGTH = 40;

export function parseTags(input) {
  const raw = Array.isArray(input) ? input : String(input || '').split(',');
  const seen = new Set();
  const out = [];
  for (const part of raw) {
    const tag = String(part || '').trim().replace(/\s+/g, ' ').slice(0, MAX_TAG_LENGTH);
    if (!tag) continue;
    const key = normalizeSearch(tag);
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(tag);
  }
  return out;
}

export function tagsToInput(tags) {
  return (tags || []).join(', ');
}

// Kayıtlardaki bütün etiketler, kullanım sayısına göre.
export function collectTags(records) {
  const counts = new Map();
  const display = new Map();
  for (const r of records) {
    for (const t of r.tags || []) {
      const key = normalizeSearch(t);
      counts.set(key, (counts.get(key) || 0) + 1);
      if (!display.has(key)) display.set(key, t);
    }
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || display.get(a[0]).localeCompare(display.get(b[0]), 'tr'))
    .map(([key]) => display.get(key));
}

export function hasTag(record, tag) {
  if (!tag) return true;
  const key = normalizeSearch(tag);
  return (record.tags || []).some((t) => normalizeSearch(t) === key);
}
