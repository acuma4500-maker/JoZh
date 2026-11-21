// DOM ve genel yardımcılar. Kullanıcı verisi DAİMA textContent ile yazılır (XSS koruması).

/**
 * Güvenli eleman oluşturucu.
 * h('button', { class: 'btn', onclick: fn, 'aria-label': 'Gönder' }, 'Metin', childEl)
 * - Metin çocukları textContent olarak eklenir; HTML olarak yorumlanmaz.
 * - `svg` özelliği yalnızca uygulamanın kendi sabit ikon metinleri içindir (kullanıcı verisi asla).
 */
export function h(tag, props = {}, ...children) {
  const el = document.createElement(tag);
  for (const [key, val] of Object.entries(props || {})) {
    if (val === undefined || val === null || val === false) continue;
    if (key === 'class') el.className = val;
    else if (key === 'dataset') Object.assign(el.dataset, val);
    else if (key === 'svg') el.insertAdjacentHTML('afterbegin', val);
    else if (key === 'text') el.textContent = val;
    else if (key === 'value') el.value = val;
    else if (key === 'checked' || key === 'disabled' || key === 'selected' || key === 'hidden' || key === 'required' || key === 'autofocus') el[key] = !!val;
    else if (key.startsWith('on') && typeof val === 'function') el.addEventListener(key.slice(2), val);
    else if (key === 'style' && typeof val === 'object') Object.assign(el.style, val);
    else el.setAttribute(key, val === true ? '' : String(val));
  }
  append(el, children);
  return el;
}

export function append(el, children) {
  for (const c of children.flat(Infinity)) {
    if (c === null || c === undefined || c === false || c === true) continue;
    el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return el;
}

export const clear = (el) => { while (el.firstChild) el.firstChild.remove(); return el; };
export const $ = (sel, root = document) => root.querySelector(sel);

/** Sayfa/bileşen ömrü boyunca açılan dinleyicileri tek yerden kapatmak için. */
export function createScope() {
  const fns = [];
  let disposed = false;
  return {
    add(fn) { if (typeof fn === 'function') { if (disposed) { try { fn(); } catch {} } else fns.push(fn); } return fn; },
    get disposed() { return disposed; },
    dispose() {
      disposed = true;
      while (fns.length) { const fn = fns.pop(); try { fn(); } catch (e) { console.warn('cleanup', e); } }
    },
    timeout(fn, ms) { const t = setTimeout(fn, ms); fns.push(() => clearTimeout(t)); return t; },
    interval(fn, ms) { const t = setInterval(fn, ms); fns.push(() => clearInterval(t)); return t; },
    on(target, ev, fn, opts) { target.addEventListener(ev, fn, opts); fns.push(() => target.removeEventListener(ev, fn, opts)); },
  };
}

export function debounce(fn, ms) {
  let t;
  const d = (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
  d.cancel = () => clearTimeout(t);
  return d;
}

/** Kriptografik olarak güvenli rastgele tamsayı [0, max). */
export function randomInt(max) {
  if (max <= 0) return 0;
  const limit = Math.floor(0x100000000 / max) * max;
  const buf = new Uint32Array(1);
  do { crypto.getRandomValues(buf); } while (buf[0] >= limit);
  return buf[0] % max;
}

export function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = randomInt(i + 1); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

export const pick = (arr) => arr[randomInt(arr.length)];

export function randomId(bytes = 12) {
  const b = crypto.getRandomValues(new Uint8Array(bytes));
  return [...b].map((x) => x.toString(16).padStart(2, '0')).join('');
}

export async function sha256Hex(text) {
  const data = new TextEncoder().encode(text);
  const hash = await crypto.subtle.digest('SHA-256', data);
  return [...new Uint8Array(hash)].map((x) => x.toString(16).padStart(2, '0')).join('');
}

/** Tahmin karşılaştırması için Türkçe uyumlu metin normalizasyonu. */
export function normalizeGuess(text) {
  const map = { ç: 'c', ğ: 'g', ı: 'i', ö: 'o', ş: 's', ü: 'u', â: 'a', î: 'i', û: 'u' };
  return String(text || '')
    .toLocaleLowerCase('tr-TR')
    .replace(/[çğıöşüâîû]/g, (c) => map[c])
    .normalize('NFKD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9 ]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export function prefersReducedMotion() {
  return document.documentElement.classList.contains('reduce-motion') ||
    (typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches);
}

export function vibrate(pattern) {
  try { if (!prefersReducedMotion() && navigator.vibrate) navigator.vibrate(pattern); } catch {}
}

/** Elemanı temizleyip null-güvenli şekilde çocukları ekler. */
export const fill = (el, ...children) => append(clear(el), children);
/** Null-güvenli ekleme (yerel Element.append null'ı "null" metni olarak yazar). */
export const add = (el, ...children) => append(el, children);
