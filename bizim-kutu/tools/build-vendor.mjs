// Firebase SDK'sını tarayıcıda doğrudan çalışan tek bir ES modülüne paketler.
// Çalıştırma: npm run build:vendor  (çıktı: js/vendor/firebase.js — repoya dahildir)
import { build } from 'esbuild';
import { readFileSync } from 'node:fs';
const version = JSON.parse(readFileSync(new URL('../node_modules/firebase/package.json', import.meta.url))).version;
await build({
  entryPoints: [new URL('./firebase-entry.js', import.meta.url).pathname],
  bundle: true, format: 'esm', minify: true, target: ['es2020', 'safari14'],
  platform: 'browser', legalComments: 'none',
  banner: { js: `/* Firebase JS SDK ${version} — Apache-2.0 — https://github.com/firebase/firebase-js-sdk */` },
  outfile: new URL('../js/vendor/firebase.js', import.meta.url).pathname,
});
console.log('firebase', version, '→ js/vendor/firebase.js');
