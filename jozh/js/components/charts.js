// Çubuk grafik (SVG). Tek ya da çok seri, ortak sıfır tabanlı tek eksen.
// İnce çubuklar, 4 px yuvarlatılmış uç, seriler arası 2 px boşluk, sönük ızgara.
// Her grup için çubuktan büyük dokunma alanı: üstüne gelince/dokununca/odaklanınca bilgi balonu.
// Renk tek başına anlam taşımaz: ≥2 seride gösterge (legend) ve tablo görünümü vardır.
import { el, clear } from '../ui.js';

const SVG_NS = 'http://www.w3.org/2000/svg';
const num = new Intl.NumberFormat('tr-TR', { maximumFractionDigits: 1 });

// Eksen etiketi: 40.000 → "40 bin", 1.200.000 → "1,2 mn"
function compact(v) {
  if (v >= 1e6) return `${num.format(v / 1e6)} mn`;
  if (v >= 1e3) return `${num.format(v / 1e3)} bin`;
  return num.format(v);
}

function svg(tag, attrs = {}) {
  const node = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v !== undefined && v !== null) node.setAttribute(k, String(v));
  }
  return node;
}

// 0'dan başlayan "güzel" eksen üst sınırı ve adımı
function niceScale(max, ticks = 4) {
  if (!(max > 0)) return { top: 1, step: 0.25 };
  const raw = max / ticks;
  const pow = 10 ** Math.floor(Math.log10(raw));
  const unit = [1, 2, 2.5, 5, 10].find((m) => m * pow >= raw) * pow;
  return { top: unit * Math.ceil(max / unit), step: unit };
}

// Yalnızca üst köşeleri yuvarlatılmış, tabana oturan çubuk
function barPath(x, y, w, h, r) {
  const rr = Math.min(r, w / 2, h);
  return `M${x},${y + h}V${y + rr}Q${x},${y} ${x + rr},${y}H${x + w - rr}Q${x + w},${y} ${x + w},${y + rr}V${y + h}Z`;
}

/**
 * options:
 *  title        grafik başlığı (erişilebilir ad)
 *  series       [{ key, name, className }]  className rengi verir (.series-income gibi)
 *  groups       [{ label, title, values: { key: sayı }, note? }]
 *  format       değer biçimi (balon ve tablo)
 *  tickEvery    x etiketlerinden kaçta biri gösterilsin (varsayılan: sığdığı kadar)
 *  height       çizim yüksekliği (px)
 *  tableCaption tablo görünümü başlığı
 */
export function barChart({ title, series, groups, format = String, tickEvery, height = 220, tableCaption, rowHeader = 'Dönem' }) {
  const wrap = el('div', { class: 'chart' });
  const legend = series.length > 1
    ? el('ul', { class: 'chart-legend', 'aria-label': 'Gösterge' }, series.map((s) => el('li', null, el('span', { class: `chart-swatch ${s.className}`, 'aria-hidden': 'true' }), s.name)))
    : null;
  const stage = el('div', { class: 'chart-stage' });
  const tip = el('div', { class: 'chart-tip', role: 'status', 'aria-live': 'polite', hidden: true });
  stage.append(tip);
  const table = el('details', { class: 'chart-table' },
    el('summary', null, 'Tablo olarak göster'),
    el('div', { class: 'table-wrap' }, el('table', { class: 'table' },
      tableCaption ? el('caption', { class: 'visually-hidden' }, tableCaption) : null,
      el('thead', null, el('tr', null, el('th', { scope: 'col' }, rowHeader), series.map((s) => el('th', { scope: 'col', class: 'num' }, s.name)))),
      el('tbody', null, groups.map((g) => el('tr', null, el('th', { scope: 'row' }, g.title || g.label), series.map((s) => el('td', { class: 'num' }, format(g.values[s.key] || 0)))))))));
  if (legend) wrap.append(legend);
  wrap.append(stage, table);

  let active = -1;

  function showTip(i, hit, plotLeft, bandW) {
    active = i;
    const g = groups[i];
    clear(tip).append(
      el('p', { class: 'chart-tip-title' }, g.title || g.label),
      el('ul', null, series.map((s) => el('li', null,
        el('span', { class: `chart-swatch ${s.className}`, 'aria-hidden': 'true' }),
        el('span', { class: 'grow' }, s.name),
        el('strong', null, format(g.values[s.key] || 0))))),
      g.note ? el('p', { class: 'chart-tip-note' }, g.note) : null);
    tip.hidden = false;
    const stageW = stage.clientWidth;
    const center = plotLeft + bandW * (i + 0.5);
    const tw = tip.offsetWidth;
    tip.style.left = `${Math.max(4, Math.min(stageW - tw - 4, center - tw / 2))}px`;
    for (const h of stage.querySelectorAll('.chart-hit')) h.classList.toggle('is-active', h === hit);
  }

  function hideTip() {
    active = -1;
    tip.hidden = true;
    for (const h of stage.querySelectorAll('.chart-hit')) h.classList.remove('is-active');
  }

  function draw() {
    const width = Math.max(260, stage.clientWidth || 600);
    const margin = { top: 10, right: 6, bottom: 26, left: 52 };
    const plotW = width - margin.left - margin.right;
    const plotH = height - margin.top - margin.bottom;
    const max = Math.max(0, ...groups.flatMap((g) => series.map((s) => g.values[s.key] || 0)));
    const { top, step } = niceScale(max);
    const y = (v) => margin.top + plotH - (v / top) * plotH;
    const bandW = plotW / groups.length;
    const gap = 2;
    const groupW = Math.min(bandW * 0.72, series.length * 30);
    const barW = Math.max(2, (groupW - gap * (series.length - 1)) / series.length);
    const every = tickEvery || Math.max(1, Math.ceil(groups.length / Math.floor(plotW / 44)));

    const root = svg('svg', { width, height, viewBox: `0 0 ${width} ${height}`, class: 'chart-svg', role: 'img', 'aria-label': title });
    const grid = svg('g', { class: 'chart-grid' });
    for (let v = 0; v <= top + step / 2; v += step) {
      const yy = Math.round(y(v)) + 0.5;
      grid.append(svg('line', { x1: margin.left, x2: width - margin.right, y1: yy, y2: yy, class: v === 0 ? 'chart-baseline' : '' }));
      const label = svg('text', { x: margin.left - 6, y: yy, 'text-anchor': 'end', 'dominant-baseline': 'middle', class: 'chart-axis' });
      label.textContent = v === 0 ? '0' : compact(v);
      grid.append(label);
    }
    root.append(grid);

    const bars = svg('g', { class: 'chart-bars' });
    const ticks = svg('g', { class: 'chart-ticks' });
    const hits = svg('g', { class: 'chart-hits' });
    groups.forEach((g, i) => {
      const gx = margin.left + bandW * i + (bandW - groupW) / 2;
      series.forEach((s, k) => {
        const v = g.values[s.key] || 0;
        if (v <= 0) return;
        const h = Math.max(1, (v / top) * plotH);
        bars.append(svg('path', { d: barPath(gx + k * (barW + gap), margin.top + plotH - h, barW, h, 4), class: `chart-bar ${s.className}` }));
      });
      if (i % every === 0 || i === groups.length - 1) {
        const t = svg('text', { x: margin.left + bandW * (i + 0.5), y: height - 8, 'text-anchor': 'middle', class: 'chart-axis' });
        t.textContent = g.label;
        ticks.append(t);
      }
      const hit = svg('rect', {
        x: margin.left + bandW * i, y: margin.top, width: bandW, height: plotH,
        class: 'chart-hit', tabindex: '0', role: 'button', focusable: 'true',
        'aria-label': `${g.title || g.label}: ${series.map((s) => `${s.name} ${format(g.values[s.key] || 0)}`).join(', ')}`
      });
      hit.addEventListener('pointerenter', (e) => {
        if (e.pointerType === 'mouse') showTip(i, hit, margin.left, bandW);
      });
      hit.addEventListener('pointerleave', (e) => {
        if (e.pointerType === 'mouse') hideTip();
      });
      hit.addEventListener('click', () => (active === i ? hideTip() : showTip(i, hit, margin.left, bandW)));
      hit.addEventListener('focus', () => showTip(i, hit, margin.left, bandW));
      hit.addEventListener('blur', hideTip);
      hit.addEventListener('keydown', (e) => {
        const all = [...hits.children];
        if (e.key === 'ArrowRight' && all[i + 1]) all[i + 1].focus();
        if (e.key === 'ArrowLeft' && all[i - 1]) all[i - 1].focus();
        if (e.key === 'Escape') hideTip();
      });
      hits.append(hit);
    });
    root.append(bars, ticks, hits);
    const old = stage.querySelector('svg');
    if (old) old.replaceWith(root);
    else stage.prepend(root);
    hideTip();
  }

  let lastW = 0;
  const ro = new ResizeObserver(() => {
    if (!wrap.isConnected && lastW) {
      ro.disconnect();
      return;
    }
    const w = stage.clientWidth;
    if (w && Math.abs(w - lastW) > 2) {
      lastW = w;
      draw();
    }
  });
  ro.observe(stage);
  requestAnimationFrame(() => {
    if (!lastW) draw();
  });
  return wrap;
}
