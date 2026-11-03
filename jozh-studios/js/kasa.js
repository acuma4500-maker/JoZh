/* JOZH STUDIOS · Kasa
   KasaMotor : sabit kasa animasyonu prompt şablonu (azalış / artış / sabit). Yalnızca rakamlar değişir.
   KasaDefter: senaryo işlemleri + kullanıcının eklediği işlemlerden sıralı defter, sahne bakiyeleri ve toplamlar. */
(function (global) {
  "use strict";

  const MAX = 999999999;
  const fmt = n => String(Math.abs(Math.trunc(n))).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  const sg = n => (n < 0 ? "−" : "+") + fmt(n);

  /* ------------------------------------------------------------ prompt şablonu
     o   = { sabit:bool, old:int, neu:int, abs:int, up:bool }
     cfg = { birim:"TL"|"₺", gecis:"akici"|"anlik", etiket:"var"|"yok" } */
  function buildPrompt(o, cfg) {
    const U = cfg && cfg.birim === "₺" ? "₺" : "TL";
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
    if (lab) stack.push("The label \"KASA\" in light grey (#A0A0A0), small capital letters, about 45% of the balance size");
    if (sabit) {
      stack.push("The balance in bold white (#FFFFFF) monospaced digits followed by the currency, written exactly \"" + b0 + "\". " + balSize);
    } else {
      stack.push("The balance in bold white (#FFFFFF) monospaced digits followed by the currency, written exactly \"" + b0 + "\" at the start. " + balSize);
      stack.push("The change line in " + colorTxt + ": \"" + chg + "\", bold, same monospaced font, about 65% of the balance size, directly under the balance");
    }
    const layout = stack.map((t, i) => (i + 1) + ". " + t + ".").join("\n")
      + (sabit ? "\nThere is NO change line: nothing appears under the balance." : "");

    let tl;
    if (sabit) {
      tl = ["0.0-8.0 s: " + (lab ? "\"KASA\" and the balance \"" + b0 + "\" are" : "The balance \"" + b0 + "\" is") +
            " visible and perfectly still for the entire video. Nothing changes, nothing moves, nothing else appears."];
    } else {
      tl = [
        "0.0-1.0 s: Starting balance visible: " + (lab ? "only \"KASA\" and \"" + b0 + "\"" : "only \"" + b0 + "\"") + ", perfectly still. The change line is not visible yet.",
        "1.0-1.4 s: Change line fades in: \"" + chg + "\" appears directly under the balance. Nothing else moves."
      ];
      if (anlik) {
        tl.push("1.4 s: The balance changes instantly, in a single frame, from \"" + b0 + "\" to \"" + b1 + "\". No counting, no rolling, no fade.");
        tl.push("1.4-8.0 s: Everything freezes. The final frame shows exactly \"" + b1 + "\" in white and \"" + chg + "\" in " + colorWord + ".");
      } else {
        tl.push("1.4-3.4 s: Balance counts smoothly " + dir + " from \"" + b0 + "\" to the new balance \"" + b1 + "\": the digits roll in place like a simple counter, in one direction only, without flicker and without overshooting.");
        tl.push("3.4-8.0 s: Everything freezes. The final frame shows exactly \"" + b1 + "\" in white and \"" + chg + "\" in " + colorWord + ".");
      }
    }
    const texts = sabit
      ? (lab ? "KASA and the balance \"" + b0 + "\"" : "the balance \"" + b0 + "\"")
      : (lab ? "KASA, " : "") + "the starting balance \"" + b0 + "\", the final balance \"" + b1 + "\" and the change amount \"" + chg + "\"";

    return [
      "Vertical 9:16 video, 8 seconds. Flat 2D motion-graphics overlay, not a cinematic scene. PURE SOLID BLACK background (#000000) filling the entire frame, made to be layered over another video with a Screen / Lighten blend mode. Locked static camera: no movement, no zoom, no cuts, no transitions. Silent: no sound, no music.",
      "LAYOUT: one small cash counter in the TOP-RIGHT corner and nothing else. Its right edge is 5% from the right edge of the frame and its top edge is 6% from the top edge. All lines are right-aligned to the same right edge and stacked from top to bottom:\n" + layout +
        "\nThe counter stays within 45% of the frame width and 12% of the frame height. The rest of the frame stays pure black. Position, size and colors never change.",
      "TIMELINE:\n" + tl.join("\n"),
      "The only text is " + texts + ", written exactly like this. Digits stay crisp and fully legible.",
      "AVOID: money effects, banknotes, coins, particles, sparkles, glow, borders, shadows, gradients, characters, hands, scenery, extra text, subtitles, logos, watermarks."
    ].join("\n\n");
  }

  function promptFor(onceki, sonraki, cfg) {
    const d = sonraki - onceki;
    if (d === 0) return buildPrompt({ sabit: true, old: sonraki, neu: sonraki }, cfg);
    return buildPrompt({ sabit: false, old: onceki, neu: sonraki, abs: Math.abs(d), up: d > 0 }, cfg);
  }

  /* ------------------------------------------------------------ defter
     DATA.bolumler[].sahneler[].tx = senaryo işlemleri (Python'da doğrulanmış)
     kullanıcı işlemi = { id, no (bölüm ya da 0 = genel), sahne (1-6), tip, tutar, aciklama, olusturma } */
  function build(DATA, userTxs) {
    const T = DATA.tipler;
    const epIndex = new Map(DATA.bolumler.map((b, i) => [b.no, i]));
    const entries = [];
    let seq = 0;
    DATA.bolumler.forEach(b => b.sahneler.forEach(s => s.tx.forEach((t, k) => {
      entries.push({ id: "s-" + b.no + "-" + s.n + "-" + k, kaynak: "senaryo", no: b.no, sahne: s.n, tip: t.tip, tutar: t.tutar,
                     aciklama: t.aciklama, adet: t.adet, birim: t.birim, fiyat: t.fiyat, _o: [epIndex.get(b.no), s.n, 0, seq++] });
    })));
    (userTxs || []).forEach(u => {
      const ei = u.no && epIndex.has(u.no) ? epIndex.get(u.no) : 1e6;
      entries.push(Object.assign({}, u, { kaynak: "kullanici", _o: [ei, u.no ? (u.sahne || 6) : 0, 1, u.olusturma || 0] }));
    });
    entries.sort((a, b) => { for (let i = 0; i < 4; i++) { if (a._o[i] !== b._o[i]) return a._o[i] - b._o[i]; } return 0; });

    let bal = null, eksi = null;
    const tot = { alis: 0, satis: 0, gelir: 0, gider: 0, borc: 0 }, byTip = {};
    entries.forEach(e => {
      const tp = T[e.tip];
      if (e.tip === "acilis") { bal = 0; }
      if (bal === null) bal = 0;
      e.onceki = bal;
      bal += tp.isaret * e.tutar;
      e.sonraki = bal;
      if (bal < 0 && !eksi) eksi = e;
      if (tp.grup !== "acilis") { tot[tp.grup] += e.tutar; byTip[e.tip] = (byTip[e.tip] || 0) + e.tutar; }
    });
    const acilis = entries.find(e => e.tip === "acilis");
    const baslangic = acilis ? acilis.tutar : DATA.baslangic_kasa;
    const brut = tot.satis - tot.alis;
    const net = brut + tot.gelir - tot.gider;
    return {
      entries, eksi, byTip, toplam: tot, brut, net,
      baslangic, guncel: bal === null ? baslangic : bal,
      kalanBorc: DATA.borc - tot.borc,
      kontrol: (baslangic + net - tot.borc) === (bal === null ? baslangic : bal)
    };
  }

  /* Sahne başı/sonu bakiyesi. Kasa açılmadan önceki sahneler null döner. */
  function sahneBakiye(DATA, defter) {
    const byScene = new Map();
    defter.entries.forEach(e => {
      if (!e.no) return;
      const k = e.no + "-" + e.sahne;
      if (!byScene.has(k)) byScene.set(k, []);
      byScene.get(k).push(e);
    });
    const out = new Map();
    let bal = null;
    DATA.bolumler.forEach(b => b.sahneler.forEach(s => {
      const list = byScene.get(b.no + "-" + s.n) || [];
      const bas = bal;
      list.forEach(e => { bal = e.sonraki; });
      const acilisVar = list.some(e => e.tip === "acilis");
      if (bal === null) { out.set(b.no + "-" + s.n, null); return; }
      out.set(b.no + "-" + s.n, { bas: acilisVar ? 0 : bas, son: bal, islemler: list, acilis: acilisVar });
    }));
    return out;
  }

  global.KasaMotor = { MAX, fmt, sg, buildPrompt, promptFor };
  global.KasaDefter = { build, sahneBakiye };
})(window);
