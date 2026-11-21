// Yerel geliştirme/test sunucusu. Kullanım: node tools/serve.mjs [port]
// ?emulator ile açılan sayfalar için CSP'ye yerel emülatör adresleri eklenir (yalnızca bu yerel sunucuda).
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('..', import.meta.url)));
const PORT = Number(process.argv[2] || process.env.PORT || 5173);
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2' };
const EMU = "http://127.0.0.1:9099 http://127.0.0.1:8080 http://127.0.0.1:9000 ws://127.0.0.1:9000";

createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://x');
    let path = normalize(decodeURIComponent(url.pathname)).replace(/^(\.\.[/\\])+/, '');
    if (path.endsWith('/')) path += 'index.html';
    const file = join(ROOT, path);
    if (!file.startsWith(ROOT) || /(^|[/\\])(node_modules|tests|tools|firebase)([/\\]|$)/.test(path)) { res.writeHead(403).end(); return; }
    await stat(file);
    let body = await readFile(file);
    if (file.endsWith('index.html')) body = Buffer.from(body.toString().replace("connect-src 'self'", `connect-src 'self' ${EMU}`).replace("script-src 'self'", "script-src 'self' http://127.0.0.1:9000").replace('frame-src ', 'frame-src http://127.0.0.1:9000 '));
    res.writeHead(200, { 'Content-Type': TYPES[extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(body);
  } catch { res.writeHead(404).end('not found'); }
}).listen(PORT, '127.0.0.1', () => console.log(`Bizim Kutu → http://127.0.0.1:${PORT}/`));
