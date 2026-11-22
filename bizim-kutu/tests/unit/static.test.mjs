// Statik denetimler: import yolları, önbellek listesi, gizli değerler, güvenli DOM kullanımı.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, dirname, resolve, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const walk = (dir) => readdirSync(dir).flatMap((f) => { const p = join(dir, f); return statSync(p).isDirectory() ? walk(p) : [p]; });
const webFiles = ['index.html', 'service-worker.js', 'manifest.json', ...['js', 'css', 'data', 'assets'].flatMap((d) => walk(join(ROOT, d)).map((p) => relative(ROOT, p)))];
const appJs = webFiles.filter((f) => f.endsWith('.js') && f.startsWith('js/') && !f.startsWith('js/vendor/'));

test('tüm göreli import yolları mevcut dosyalara gider', () => {
  const missing = [];
  for (const f of appJs) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    for (const m of src.matchAll(/(?:import|export)\s[^'"`]*?from\s*['"](\.[^'"]+)['"]|import\(\s*['"](\.[^'"]+)['"]\s*\)/g)) {
      const spec = m[1] || m[2];
      if (!existsSync(resolve(ROOT, dirname(f), spec))) missing.push(`${f} → ${spec}`);
    }
  }
  assert.deepEqual(missing, []);
});

test('vendor paketindeki tüm adlandırılmış içe aktarmalar dışa aktarılıyor', async () => {
  const vendor = readFileSync(join(ROOT, 'js/vendor/firebase.js'), 'utf8');
  const exportBlock = vendor.match(/export\s*\{([^}]*)\}\s*;?\s*$/);
  assert.ok(exportBlock, 'vendor export bloğu');
  const exported = new Set(exportBlock[1].split(',').map((s) => s.trim().split(/\s+as\s+/).pop()));
  const bad = [];
  for (const f of appJs) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    for (const m of src.matchAll(/import\s*\{([^}]*)\}\s*from\s*['"][^'"]*vendor\/firebase\.js['"]/g)) {
      for (const name of m[1].split(',').map((s) => s.trim().split(/\s+as\s+/)[0]).filter(Boolean)) if (!exported.has(name)) bad.push(`${f}: ${name}`);
    }
    for (const m of src.matchAll(/const\s*\{([^}]*)\}\s*=\s*await import\(['"][^'"]*vendor\/firebase\.js['"]\)/g)) {
      for (const name of m[1].split(',').map((s) => s.trim()).filter(Boolean)) if (!exported.has(name)) bad.push(`${f}: ${name}`);
    }
  }
  assert.deepEqual(bad, []);
});

test('service worker uygulama dosyalarının tamamını önbelleğe alır', () => {
  const sw = readFileSync(join(ROOT, 'service-worker.js'), 'utf8');
  const listed = new Set([...sw.matchAll(/'\.\/([^']+)'/g)].map((m) => m[1]));
  const need = webFiles.filter((f) => /^(js|css|data)\//.test(f) || /^assets\/(icons|fonts)\/.*\.(png|svg|woff2)$/.test(f));
  const missing = need.filter((f) => !listed.has(f));
  const stale = [...listed].filter((f) => f && !existsSync(join(ROOT, f)));
  assert.deepEqual(missing, [], 'eksik');
  assert.deepEqual(stale, [], 'var olmayan');
});

test('PIN değerleri ve parolalar kaynak kodda yok', () => {
  const offenders = [];
  for (const f of webFiles.filter((x) => /\.(js|html|json)$/.test(x) && !x.startsWith('js/vendor/') && !x.startsWith('data/'))) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    if (/\b0822\b|\b2208\b/.test(src)) offenders.push(f);
    if (/password\s*[:=]\s*['"][^'"]+['"]/i.test(src)) offenders.push(`${f} (parola)`);
  }
  assert.deepEqual(offenders, []);
});

test('Firebase Storage kullanılmıyor; dosya seçimi yalnızca Özel Kasa\'da (şifreli)', () => {
  const entry = readFileSync(join(ROOT, 'tools/firebase-entry.js'), 'utf8');
  assert.ok(!/firebase\/storage/.test(entry));
  for (const f of appJs) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    assert.ok(!/firebase\/storage|getStorage|uploadBytes/.test(src), f);
    if (!f.endsWith('pages/vault.js')) assert.ok(!/type:\s*['"]file['"]/.test(src), `${f}: dosya girişi yalnızca kasada olabilir`);
  }
});

test('innerHTML yalnızca sabit ikon metinleriyle kullanılır', () => {
  const hits = [];
  for (const f of appJs) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    for (const line of src.split('\n')) {
      if (/\.innerHTML\s*=|insertAdjacentHTML|outerHTML\s*=|document\.write/.test(line)) hits.push(`${f}: ${line.trim()}`);
    }
  }
  const allowed = hits.filter((l) => /insertAdjacentHTML\('afterbegin', val\)/.test(l) || /innerHTML = icons\./.test(l));
  assert.deepEqual(hits.filter((l) => !allowed.includes(l)), []);
  // svg özelliği yalnızca icons/logoSvg sabitleriyle çağrılır
  const svgProps = [];
  for (const f of appJs) {
    const src = readFileSync(join(ROOT, f), 'utf8');
    for (const m of src.matchAll(/svg:\s*([^,}\n]+)/g)) if (!/^(icons\.|icons\[|logoSvg|k === 'back' \? icons|st === 'pending' \? icons|undefined)/.test(m[1].trim())) svgProps.push(`${f}: ${m[1].trim()}`);
  }
  assert.deepEqual(svgProps, []);
});

test('index.html: CSP, manifest ve modül girişi', () => {
  const html = readFileSync(join(ROOT, 'index.html'), 'utf8');
  assert.match(html, /Content-Security-Policy/);
  assert.match(html, /script-src 'self'/);
  assert.ok(!/unsafe-inline|unsafe-eval/.test(html));
  assert.match(html, /<script type="module" src="js\/app\.js">/);
  assert.match(html, /rel="manifest" href="manifest\.json"/);
  const manifest = JSON.parse(readFileSync(join(ROOT, 'manifest.json'), 'utf8'));
  for (const i of manifest.icons) assert.ok(existsSync(join(ROOT, i.src)), i.src);
});

test('güvenlik kuralları iki UID dışında kimseye izin vermez ve genel joker izni yok', () => {
  const fs = readFileSync(join(ROOT, 'firebase/firestore.rules'), 'utf8');
  assert.ok(!/match\s+\/\{document=\*\*\}/.test(fs));
  assert.ok(!/allow\s+(read|write)[^;]*:\s*if\s+true/.test(fs));
  const db = JSON.parse(readFileSync(join(ROOT, 'firebase/database.rules.json'), 'utf8'));
  assert.equal(db.rules['.read'], false); assert.equal(db.rules['.write'], false);
});

test('yerel Element.append kullanılmıyor (null "null" olarak yazılır) — add()/fill() kullanılmalı', () => {
  const hits = [];
  for (const f of appJs.filter((x) => !x.endsWith('helpers.js'))) {
    readFileSync(join(ROOT, f), 'utf8').split('\n').forEach((l, i) => { if (/\.append\(/.test(l)) hits.push(`${f}:${i + 1}`); });
  }
  assert.deepEqual(hits, []);
});
