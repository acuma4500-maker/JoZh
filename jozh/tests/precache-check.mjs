// sw.js içindeki APP_ASSETS listesinin pages/, css/, js/, assets/icons/ altındaki dosyalarla birebir
// eşleştiğini ve VERSION ile APP_VERSION'ın aynı olduğunu denetler. Çalıştırma: node tests/precache-check.mjs
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const sw = readFileSync(join(root, 'sw.js'), 'utf8');
const app = readFileSync(join(root, 'js/app.js'), 'utf8');

function walk(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else out.push(`./${relative(root, p).split('\\').join('/')}`);
  }
  return out;
}

const listMatch = /const APP_ASSETS = \[([\s\S]*?)\];/.exec(sw);
if (!listMatch) {
  console.error('sw.js içinde APP_ASSETS bulunamadı.');
  process.exit(1);
}
const listed = new Set([...listMatch[1].matchAll(/'([^']+)'/g)].map((m) => m[1]));
const expected = new Set(['./', './index.html', './manifest.json', ...['pages', 'css', 'js', 'assets/icons'].flatMap((d) => walk(join(root, d)))]);

const missing = [...expected].filter((f) => !listed.has(f));
const extra = [...listed].filter((f) => !expected.has(f));
let failed = false;
if (missing.length) {
  failed = true;
  console.error('APP_ASSETS listesinde eksik dosyalar:\n  ' + missing.join('\n  '));
}
if (extra.length) {
  failed = true;
  console.error('APP_ASSETS listesinde olup diskte olmayan dosyalar:\n  ' + extra.join('\n  '));
}
const swVersion = /const VERSION = '([^']+)'/.exec(sw)?.[1];
const appVersion = /export const APP_VERSION = '([^']+)'/.exec(app)?.[1];
if (!swVersion || swVersion !== appVersion) {
  failed = true;
  console.error(`Sürüm uyuşmuyor: sw.js VERSION=${swVersion}, js/app.js APP_VERSION=${appVersion}`);
}
if (failed) process.exit(1);
console.log(`Önbellek listesi tamam: ${listed.size} dosya, sürüm ${swVersion}.`);
