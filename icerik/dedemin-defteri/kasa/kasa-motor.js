/* Kasa promptu motoru. Tek kaynak: "Dedemin Defteri" sayfası ve "Kasa Prompt Aracı" bu dosyayı build sırasında aynen içine alır.
   parseLine(satır) -> {ok:true, sabit, old, neu, delta, abs, up} ya da {ok:false, msg, fixes?}
   buildPrompt(o, cfg) -> Flow'a yapıştırılacak sabit İngilizce prompt.
   cfg = {birim:"₺"|"TL", gecis:"akici"|"anlik", etiket:"var"|"yok"} */
const KasaMotor = (function(){
"use strict";
const MAX = 999999999;
const fmt = n => String(Math.abs(Math.trunc(n))).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
const sg = n => (n < 0 ? "−" : "+") + fmt(n);
const bad = (msg, extra) => Object.assign({ ok: false, msg: msg }, extra || {});
const canon = (a, b) => fmt(a) + " ₺ → " + fmt(b) + " ₺ (" + sg(b - a) + " ₺)";

/* ---------- satırı oku ---------- */
function norm(raw){
  return raw
    .replace(/[-−–—‒]{1,2}>|=+>|[→➜➝➔⇒>]/g, " → ")
    .replace(/[−–—‒]/g, "-")
    .replace(/₺|\bTRY\b|\bTL\b|\blira\b/gi, " ")
    .replace(/\b(?:s[aA]b[iİıI]t|k[aA]s[aA])\b:?/gi, " ")
    .replace(/[()\[\]{}]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function parseLine(raw){
  const s = norm(raw);
  if (!s) return null;
  const arrows = (s.match(/→/g) || []).length;
  if (arrows > 1) return bad("Satırda tek bir ok olmalı: eski → yeni.");
  const arrowAt = s.indexOf("→");
  const re = /([+-])?(\d{1,3}(?:[.,]\d{3})+|\d+)(?:([.,])(\d+))?/g;
  const toks = [];
  let m;
  while ((m = re.exec(s))) {
    if (m[3]) return bad("Kuruş desteklenmiyor. Tam lira yaz, örnek: 7.000");
    if (m[1] && m.index > 0 && /\d/.test(s[m.index - 1])) {
      return bad("Sayıların arasında eksi işareti var ve ok yok. Eski ve yeni bakiyenin arasına → koy: 7.000 ₺ → 6.700 ₺");
    }
    toks.push({ sign: m[1] || "", val: parseInt(m[2].replace(/[.,]/g, ""), 10), side: arrows && m.index > arrowAt ? 1 : 0 });
  }
  const rest = s.replace(new RegExp(re.source, "g"), " ").replace(/→/g, " ").replace(/\s+/g, " ").trim();
  if (rest) return bad("\"" + rest + "\" kısmını anlayamadım. Satırda yalnızca sayı, ₺ ve → kullan.");
  if (!toks.length) return bad("Bu satırda bakiye göremedim. Şöyle yaz: 7.000 ₺ → 6.700 ₺ (−300 ₺)");

  let old, neu, typed = null;
  if (arrows === 1) {
    const L = toks.filter(t => t.side === 0), R = toks.filter(t => t.side === 1);
    if (L.length !== 1 || L[0].sign) return bad("Okun soluna yalnızca eski bakiyeyi yaz: 7.000 ₺ → 6.700 ₺");
    if (R.length < 1 || R.length > 2 || R[0].sign) return bad("Okun sağına yeni bakiyeyi, istersen parantez içinde farkı yaz: 7.000 ₺ → 6.700 ₺ (−300 ₺)");
    old = L[0].val; neu = R[0].val;
    if (R[1]) typed = { sign: R[1].sign === "-" ? -1 : R[1].sign === "+" ? 1 : 0, val: R[1].val };
  } else if (toks.length === 1 && !toks[0].sign) {
    old = neu = toks[0].val;
  } else if (toks.length === 2 && !toks[0].sign && toks[1].sign) {
    old = toks[0].val;
    typed = { sign: toks[1].sign === "-" ? -1 : 1, val: toks[1].val };
    neu = old + typed.sign * typed.val;
  } else {
    return bad("Eski ve yeni bakiyenin arasına → koy. Örnek: 7.000 ₺ → 6.700 ₺ (−300 ₺). Kasa değişmiyorsa tek sayı yaz: 7.000 ₺");
  }

  if (old > MAX || neu > MAX || (typed && typed.val > MAX)) return bad("Sayı çok büyük. En fazla " + fmt(MAX) + " ₺ yazabilirsin.");
  if (neu < 0) return bad("Yeni bakiye eksiye düşüyor (" + sg(neu) + " ₺). Kasa eksiye inmez, sayıları kontrol et.");
  const calc = neu - old;
  const t = !typed ? calc : typed.sign !== 0 ? typed.sign * typed.val : (calc === 0 ? typed.val : Math.sign(calc) * typed.val);
  if (t !== calc) {
    const fixes = [{
      label: calc === 0 ? "Bakiyeleri kullan (sabit kasa)" : "Bakiyeleri kullan (" + sg(calc) + " ₺)",
      text: calc === 0 ? fmt(old) + " ₺" : canon(old, neu)
    }];
    if (t !== 0 && old + t >= 0 && old + t <= MAX) fixes.push({ label: "Farkı kullan (yeni bakiye " + fmt(old + t) + " ₺)", text: canon(old, old + t) });
    return bad("Fark tutmuyor: " + fmt(old) + " ₺ ile " + fmt(neu) + " ₺ arası " + (calc === 0 ? "fark yok" : sg(calc) + " ₺") + ", ama sen " + sg(t) + " ₺ yazmışsın.", { fixes: fixes });
  }
  if (calc === 0) return { ok: true, sabit: true, old: old, neu: neu, delta: 0, abs: 0, up: false };
  return { ok: true, sabit: false, old: old, neu: neu, delta: calc, abs: Math.abs(calc), up: calc > 0 };
}

/* ---------- sabit prompt ---------- */
function buildPrompt(o, cfg){
  const U = cfg && cfg.birim === "TL" ? "TL" : "₺";
  const lab = !(cfg && cfg.etiket === "yok");
  const anlik = !!(cfg && cfg.gecis === "anlik");
  const money = n => fmt(n) + " " + U;
  const b0 = money(o.old), b1 = money(o.neu);
  const sabit = !!o.sabit;
  const chg = (o.up ? "+" : "-") + money(o.abs);
  const colorTxt = o.up ? "bright GREEN (#00E676)" : "bright RED (#FF1744)";
  const colorWord = o.up ? "green" : "red";
  const dir = o.up ? "UP" : "DOWN";
  const balSize = "Its digits are about 3.2% of the frame height tall and it is the largest element";

  const stack = [];
  if (lab) stack.push("the label \"KASA\" in light grey (#A0A0A0), tiny capital letters, about 45% of the balance size");
  if (sabit) {
    stack.push("the BALANCE in bold white (#FFFFFF) monospaced cash-register digits followed by the currency sign, written exactly \"" + b0 + "\". " + balSize);
  } else {
    stack.push("the BALANCE in bold white (#FFFFFF) monospaced cash-register digits followed by the currency sign, written exactly \"" + b0 + "\" at the start. " + balSize);
    stack.push("directly under the balance, with a small gap, the CHANGE line in " + colorTxt + ": \"" + chg + "\". Bold, same monospaced font, about 65% of the balance size");
  }
  const layout = stack.map((t, i) => (i + 1) + ") " + t + (i < stack.length - 1 ? ";" : ".")).join("\n")
    + (sabit ? "\nThere is no change line: nothing appears under the balance." : "");

  let tl;
  if (sabit) {
    tl = ["0.0-8.0 s: " + (lab ? "\"KASA\" and the balance \"" + b0 + "\" are" : "the balance \"" + b0 + "\" is") + " visible and perfectly still for the entire video. Nothing changes, nothing moves and nothing else appears."];
  } else {
    const first = lab ? "only \"KASA\" and the balance \"" + b0 + "\" are visible" : "only the balance \"" + b0 + "\" is visible";
    tl = [
      "0.0-1.0 s: " + first + ", perfectly still. The change line is not visible yet.",
      "1.0-1.4 s: the change line \"" + chg + "\" fades in directly under the balance. Nothing else moves."
    ];
    if (anlik) {
      tl.push("1.4 s: the balance changes instantly, in a single frame, from \"" + b0 + "\" to \"" + b1 + "\". No counting, no rolling, no fade, no animation.");
      tl.push("1.4-8.0 s: everything stays frozen. The final frame shows exactly \"" + b1 + "\" in white and \"" + chg + "\" in " + colorWord + ", unchanged until the end.");
    } else {
      tl.push("1.4-3.4 s: the balance counts smoothly " + dir + " from \"" + b0 + "\" to \"" + b1 + "\": the digits roll in place like a simple counter, in one direction only, without flicker and without overshooting.");
      tl.push("3.4-8.0 s: everything freezes. The final frame shows exactly \"" + b1 + "\" in white and \"" + chg + "\" in " + colorWord + ", unchanged until the end.");
    }
  }
  const texts = sabit
    ? (lab ? "\"KASA\" and \"" + b0 + "\"" : "\"" + b0 + "\"")
    : (lab ? "\"KASA\", " : "") + "\"" + b0 + "\", \"" + b1 + "\" and \"" + chg + "\"";

  return [
    "Vertical 9:16 video, 8 seconds. Flat 2D motion-graphics overlay, not a cinematic scene. PURE SOLID BLACK background (#000000) filling the entire frame, made to be layered over another video with a Screen / Lighten blend mode. Locked static camera: no movement, no zoom, no cuts, no transitions. Silent: no sound, no music.",
    "LAYOUT: one small cash counter in the TOP-RIGHT corner and nothing else. Its right edge is 5% from the right edge of the frame and its top edge is 6% from the top edge. All lines are right-aligned to the same right edge and stacked from top to bottom:\n" + layout + "\nThe counter stays within 45% of the frame width and 12% of the frame height. The rest of the frame stays pure black. Position, size and colors never change during the video.",
    "TIMELINE (exact):\n" + tl.join("\n"),
    "TEXT: the only text in the whole video is " + texts + ", written exactly like this. Digits are crisp, sharp and fully legible at all times.",
    "AVOID: money effects, banknotes, coins, particles, sparkles, glow, light rays, shine, bloom, confetti, arrows, icons, boxes, borders, shadows, gradients, vignette, film grain, textures, characters, hands, objects, scenery, extra text, subtitles, logos, watermarks."
  ].join("\n\n");
}

return { MAX: MAX, fmt: fmt, sg: sg, canon: canon, parseLine: parseLine, buildPrompt: buildPrompt };
})();
