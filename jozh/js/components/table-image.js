// Liste/çizelgeyi PNG resme çizer (dış kütüphane yok, çevrimdışı çalışır) ve paylaşır ya da indirir.
import { toastError, toast } from '../ui.js';

const FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif';

function wrapText(ctx, text, maxWidth) {
  const words = String(text).split(/\s+/);
  const lines = [];
  let line = '';
  for (const w of words) {
    const test = line ? `${line} ${w}` : w;
    if (ctx.measureText(test).width > maxWidth && line) {
      lines.push(line);
      line = w;
    } else {
      line = test;
    }
  }
  if (line) lines.push(line);
  return lines.length ? lines : [''];
}

/**
 * title, subtitle, head: ['Sütun', ...], rows: [['hücre', ...]], widths: [oran, ...], footer, highlight: satır indeksi
 */
export function drawTable({ title, subtitle = '', head, rows, widths, footer = '', highlight = -1 }) {
  const scale = 2;
  const W = 900;
  const pad = 32;
  const lineH = 26;
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  const inner = W - pad * 2;
  const total = widths.reduce((a, b) => a + b, 0);
  const cols = widths.map((w) => (w / total) * inner);
  ctx.font = `16px ${FONT}`;
  const rowLines = rows.map((r) => r.map((cell, i) => wrapText(ctx, cell, cols[i] - 20)));
  const rowHeights = rowLines.map((cells) => Math.max(...cells.map((l) => l.length)) * lineH + 18);
  const headerH = subtitle ? 104 : 80;
  const H = headerH + 46 + rowHeights.reduce((a, b) => a + b, 0) + (footer ? 52 : 24);
  canvas.width = W * scale;
  canvas.height = H * scale;
  ctx.scale(scale, scale);
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = '#151a2b';
  ctx.fillRect(0, 0, W, headerH);
  ctx.fillStyle = '#ffffff';
  ctx.font = `700 26px ${FONT}`;
  ctx.textBaseline = 'top';
  ctx.fillText(title, pad, 24);
  if (subtitle) {
    ctx.fillStyle = '#a8b0c8';
    ctx.font = `16px ${FONT}`;
    ctx.fillText(subtitle, pad, 62);
  }
  let y = headerH;
  ctx.fillStyle = '#eef1f7';
  ctx.fillRect(0, y, W, 46);
  ctx.fillStyle = '#4a5370';
  ctx.font = `700 14px ${FONT}`;
  let x = pad;
  head.forEach((h, i) => {
    ctx.fillText(h.toLocaleUpperCase('tr-TR'), x + 10, y + 16);
    x += cols[i];
  });
  y += 46;
  rowLines.forEach((cells, r) => {
    const h = rowHeights[r];
    if (r === highlight) {
      ctx.fillStyle = '#fff4d6';
      ctx.fillRect(0, y, W, h);
    } else if (r % 2) {
      ctx.fillStyle = '#f7f8fb';
      ctx.fillRect(0, y, W, h);
    }
    x = pad;
    cells.forEach((lines, i) => {
      ctx.fillStyle = i === 0 ? '#151a2b' : '#252b3d';
      ctx.font = `${i === 0 ? 700 : 400} 16px ${FONT}`;
      lines.forEach((ln, k) => ctx.fillText(ln, x + 10, y + 10 + k * lineH));
      x += cols[i];
    });
    ctx.fillStyle = '#e3e7ef';
    ctx.fillRect(pad, y + h - 1, inner, 1);
    y += h;
  });
  if (footer) {
    ctx.fillStyle = '#8a91a8';
    ctx.font = `13px ${FONT}`;
    ctx.fillText(footer, pad, y + 18);
  }
  return canvas;
}

export async function shareCanvas(canvas, fileName, title) {
  try {
    const blob = await new Promise((res, rej) => canvas.toBlob((b) => (b ? res(b) : rej(new Error('Resim oluşturulamadı.'))), 'image/png'));
    const file = new File([blob], fileName, { type: 'image/png' });
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      try {
        await navigator.share({ files: [file], title });
        return;
      } catch (err) {
        if (err.name === 'AbortError') return;
      }
    }
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 2000);
    toast('Resim indirildi.', { kind: 'success' });
  } catch (err) {
    toastError('image.share', err);
  }
}

export async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    toast('Metin kopyalandı. WhatsApp\'a yapıştırabilirsin.', { kind: 'success' });
  } catch (err) {
    toastError('copy', err);
  }
}
