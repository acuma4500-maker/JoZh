/* JOZH STUDIOS · 81 Şehir · Yönetim paneli
   Tek sayfa, hash yönlendirme. İçerik: window.JOZH_DATA (data.js). Kullanıcı verisi: Store (storage.js). Kasa: KasaMotor / KasaDefter (kasa.js). */
(function () {
  "use strict";

  const D = window.JOZH_DATA;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const pad2 = n => String(n).padStart(2, "0");
  const AY = () => Store.durum.ayar;
  const para = n => (n < 0 ? "−" : "") + KasaMotor.fmt(n) + " " + (AY().birim === "₺" ? "₺" : "TL");
  const isaretli = n => (n > 0 ? "+" : n < 0 ? "−" : "") + KasaMotor.fmt(n) + " " + (AY().birim === "₺" ? "₺" : "TL");
  const KAR = new Map(D.karakterler.map(k => [k.id, k]));
  const EP = new Map(D.bolumler.map(b => [b.no, b]));
  const SEZ = new Map(D.sezonlar.map(s => [s.id, s]));
  const SEHIR_EP = new Map(D.bolumler.filter(b => b.plaka).map(b => [b.plaka, b]));
  const BOLGE = new Map(D.bolgeler.map(b => [b.id, b]));
  const PROMPTS = new Map();
  const TR_UP = s => s.replace(/i/g, "İ").replace(/ı/g, "I").toLocaleUpperCase("tr-TR");

  Store.yukle();
  let DEF = null, SB = null;
  function hesapla() { DEF = KasaDefter.build(D, Store.durum.islemler); SB = KasaDefter.sahneBakiye(D, DEF); }
  hesapla();

  /* ================================================================ prompt kurucular */
  const nokta = s => String(s).trim().replace(/\.+$/, "") + ".";
  const etiket = look => look.split(",")[0].trim();

  function bilgi(ep, cid) {
    const k = KAR.get(cid);
    if (k) {
      const kiy = k.kiyafet && Object.keys(k.kiyafet).length ? (k.kiyafet[ep.kiyafet] || k.kiyafet.temel) : "";
      return { look: k.en + (kiy ? "; wearing " + kiy : ""), ses: k.ses, ad: k.ad };
    }
    const m = ep.misafir[cid];
    return { look: m[1], ses: m[2], ad: m[0] };
  }

  function isikMetni(ep, sc) {
    const base = D.faz[sc.faz];
    let isik = sc.saat ? base.replace("{c}", sc.saat) : base.replace(", around {c}", "");
    let hv = "";
    if (sc.faz.startsWith("iç")) hv = sc.h ? "Through the window: " + D.hava[sc.h] : "";
    else if (!sc.faz.startsWith("anı")) hv = D.hava[sc.h || ep.hava];
    return nokta(isik) + (hv ? " " + nokta(hv) : "") + " The light stays exactly the same for the whole shot, with no flicker.";
  }

  function karakterSatirlari(ep, kim) {
    const gor = [], ses = [];
    kim.forEach(c => (c.startsWith("~") ? ses : gor).push(c.replace(/^~/, "")));
    return {
      gor, ses,
      satir: gor.map(c => { const b = bilgi(ep, c); return "- " + nokta(b.look) + " Voice: " + nokta(b.ses); })
        .concat(ses.map(c => { const b = bilgi(ep, c); return "- " + etiket(b.look) + ": off-screen voice only, NOT visible in the shot (heard from a phone speaker). Voice: " + nokta(b.ses); }))
    };
  }

  function diyalogBlok(ep, dlg, sesler) {
    if (!dlg.length) return "DIALOGUE: none. Nobody speaks in this shot.\nLIP SYNC: all mouths stay closed.";
    const s = dlg.map(d => {
      const b = bilgi(ep, d[0]);
      const off = sesler.includes(d[0]);
      return etiket(b.look) + (off ? " (off-screen, from the phone speaker)" : "") + (d[2] ? " [" + d[2] + "]" : "") + ': "' + d[1] + '"';
    });
    return "DIALOGUE (spoken in Turkish):\n" + s.join("\n") + "\nLIP SYNC: " + nokta(D.sabit.lipsync);
  }

  function sahnePrompt(ep, sc) {
    const k = karakterSatirlari(ep, sc.kim);
    const yer = ep.yerler[sc.yer][1];
    const audio = (sc.dlg.length
      ? "Clear Turkish dialogue over the natural ambient sound of the location"
      : "No speech. Natural ambient sound of the location only") + ", no background music" + (sc.n === 6 ? ", and one subtle low suspense note in the final second" : "");
    return [
      "VIDEO FORMAT: " + D.sabit.format,
      "VISUAL STYLE: " + D.sabit.stil + " Consistent character design in every shot. No subtitles, no captions, no on-screen text, no logos.",
      "",
      "CHARACTER DEFINITIONS (identical in every shot: same face, hair, eyes, body, voice and outfit):\n" + k.satir.join("\n"),
      "",
      "LOCATION: " + nokta(yer),
      "TIME AND LIGHT: " + isikMetni(ep, sc),
      "BACKGROUND: " + nokta(D.sabit.background),
      "",
      "ACTION (one continuous 10-second shot): " + nokta(sc.en),
      "CAMERA: " + nokta(sc.kam) + " Smooth, stable, cinematic.",
      "",
      diyalogBlok(ep, sc.dlg, k.ses),
      "",
      "PHYSICS: " + nokta(D.sabit.physics),
      "AUDIO: " + nokta(audio),
      "AVOID: " + nokta(D.sabit.avoid)
    ].join("\n");
  }

  function sadePrompt(ep, sc) {
    const k = karakterSatirlari(ep, sc.kim);
    const ilkCumle = sc.en.split(/(?<=[.!?;])\s+/)[0];
    const ilk = sc.dlg.slice(0, 1);
    const sat = k.gor.slice(0, 2).map(c => { const b = bilgi(ep, c); return "- " + nokta(b.look) + " Voice: " + nokta(b.ses); });
    if (ilk.length && k.ses.includes(ilk[0][0])) sat.push(k.satir[k.gor.length + k.ses.indexOf(ilk[0][0])]);
    return [
      "VIDEO FORMAT: " + D.sabit.format,
      "VISUAL STYLE: " + D.sabit.stil,
      "",
      "CHARACTER DEFINITIONS (at most two visible, identical design):\n" + sat.join("\n"),
      "LOCATION: " + nokta(ep.yerler[sc.yer][1]),
      "TIME AND LIGHT: " + isikMetni(ep, sc),
      "BACKGROUND: empty and simple, no other people.",
      "ACTION (one simple action): " + nokta(ilkCumle),
      "CAMERA: static locked-off medium shot at eye level on a tripod, no camera movement.",
      "",
      diyalogBlok(ep, ilk, k.ses),
      "",
      "PHYSICS: " + nokta(D.sabit.physics),
      "AUDIO: clear Turkish speech, natural ambient sound, no music.",
      "AVOID: " + nokta(D.sabit.avoid)
    ].join("\n");
  }

  function kapakPrompt(ep, k, stil) {
    const sat = k[1].map(c => "- " + nokta(bilgi(ep, c).look));
    return [stil, "", "CHARACTERS (same fixed design as in the episode):\n" + sat.join("\n"), "",
            "SETTING: " + nokta(ep.yerler[k[0]][1]), "",
            "COMPOSITION: " + nokta(k[2]) + " Expressive, recognizable faces, strong depth, cinematic rim light."].join("\n");
  }

  /* ================================================================ kasa yardımcıları */
  function kasaPrompt(onceki, sonraki) { return KasaMotor.promptFor(onceki, sonraki, AY()); }

  function sosyalKasaDoldur(metin, ep) {
    const son = sonBakiye(ep);
    return metin.replace(/\{KASA\}/g, son == null ? "—" : para(son));
  }
  function sonBakiye(ep) { const x = SB.get(ep.no + "-6"); return x ? x.son : null; }

  /* ================================================================ küçük bileşenler */
  function copyBtn(key, label, cls) { return `<button class="btn ${cls || ""}" type="button" data-copy="${esc(key)}">${icon("copy")}<span>${esc(label || "Kopyala")}</span></button>`; }
  function uretildiKutu(id, label) {
    return `<label class="check"><input type="checkbox" data-made="${esc(id)}" ${Store.uretildiMi(id) ? "checked" : ""}><span>${esc(label || "Üretildi")}</span></label>`;
  }
  function promptKutu(key, text, baslik, extraBtn) {
    PROMPTS.set(key, text);
    return `<div class="pbox">
      <div class="pbox-top"><span class="lbl">${esc(baslik)}</span><div class="btns">${copyBtn(key, "Kopyala", "gold")}${extraBtn || ""}</div></div>
      <details class="pdet" data-pid="${esc(key)}"><summary>Prompt'u göster</summary><pre class="prompt"></pre></details>
    </div>`;
  }
  function metinKutu(key, text, baslik, sinif) {
    PROMPTS.set(key, text);
    return `<div class="tbox ${sinif || ""}"><div class="pbox-top"><span class="lbl">${esc(baslik)}</span>${copyBtn(key, "Kopyala")}</div><pre class="txt">${esc(text)}</pre></div>`;
  }
  function epEtiket(b) { return b.sehir ? `Bölüm ${b.no} · ${b.sehir}` : `Video ${b.no}`; }
  function epLink(b, ic) { return `<a href="#/video/${b.no}" class="eplink">${ic || esc(epEtiket(b) + " – " + b.baslik)}</a>`; }
  function sceneProgress(b) { return b.sahneler.filter(s => Store.uretildiMi(b.no + "-" + s.n)).length; }

  function icon(n) {
    const P = {
      home: "M3 10.5 12 3l9 7.5V21h-6v-6H9v6H3z",
      book: "M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3zM18 20h2V6",
      user: "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm-8 9a8 8 0 0 1 16 0",
      map: "M9 4 3 6v14l6-2 6 2 6-2V4l-6 2zM9 4v14M15 6v14",
      play: "M7 4v16l13-8z",
      cash: "M3 6h18v12H3zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 9v.01M18 15v.01",
      guide: "M12 3 2 8l10 5 10-5zM6 10.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-5.5",
      data: "M12 3c4.4 0 8 1.3 8 3s-3.6 3-8 3-8-1.3-8-3 3.6-3 8-3zM4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6",
      copy: "M9 9h11v11H9zM5 15H4V4h11v1",
      menu: "M3 6h18M3 12h18M3 18h18",
      x: "M5 5l14 14M19 5 5 19",
      img: "M3 5h18v14H3zM3 16l5-5 4 4 3-3 6 6M15.5 9.5v.01",
      chev: "M9 6l6 6-6 6",
      back: "M15 6l-6 6 6 6"
    };
    return `<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="${P[n] || ""}"/></svg>`;
  }

  /* ================================================================ sayfalar */
  function stat(lbl, val, cls, alt) {
    return `<div class="stat ${cls || ""}"><span class="stat-l">${esc(lbl)}</span><span class="stat-v">${val}</span>${alt ? `<span class="stat-a">${alt}</span>` : ""}</div>`;
  }

  function pageHome() {
    const toplamSahne = D.bolumler.reduce((a, b) => a + b.sahneler.length, 0);
    const uretilen = D.bolumler.reduce((a, b) => a + sceneProgress(b), 0);
    const bas = D.bolumler.filter(b => !b.sehir);
    return `
    <section class="hero">
      <p class="eyebrow">JOZH STUDIOS sunar</p>
      <h1 class="brand">JOZH <span>STUDIOS</span></h1>
      <p class="hero-sub">81 Şehir – Bir Ticaret ve Macera Hikâyesi</p>
      <p class="lede">${esc(D.biblio.logline)}</p>
      <div class="hero-cta"><a class="btn gold big" href="#/video/1">${icon("play")}<span>Video 1'den başla</span></a><a class="btn big" href="#/bolgeler">${icon("map")}<span>Bölgeler ve şehirler</span></a></div>
    </section>
    <section class="grid stats">
      ${stat("Toplam video", D.bolumler.length, "", "6 başlangıç + 81 il")}
      ${stat("Toplam şehir", SEHIR_EP.size, "", "81 / 81 il yazıldı")}
      ${stat("Coğrafi bölge", D.bolgeler.length, "", "7 sezon")}
      ${stat("Başlangıç kasası", para(DEF.baslangic), "", "Video 4'te açılır")}
      ${stat("Güncel kasa", para(DEF.guncel), "gold", Store.durum.islemler.length ? Store.durum.islemler.length + " eklenen işlem dahil" : "senaryo sonu")}
      ${stat("Toplam ticari kazanç", isaretli(DEF.net), DEF.net >= 0 ? "up" : "down", "net kâr (borç ödemeleri hariç)")}
      ${stat("Kalan borç", para(DEF.kalanBorc), DEF.kalanBorc > 0 ? "down" : "up", "Cemil Bey · " + para(D.borc))}
      ${stat("Üretilen sahne", uretilen + " / " + toplamSahne, "", "işaretlediğin sahneler")}
    </section>
    <section class="block">
      <div class="block-h"><h2>Başlangıç videoları</h2><a href="#/baslangic" class="more">Tümü ${icon("chev")}</a></div>
      <div class="grid cards6">${bas.map(b => `<a class="card ep-card" href="#/video/${b.no}">
        <span class="ep-no">VİDEO ${b.no}</span><h3>${esc(b.baslik)}</h3><p>${esc(b.ozet)}</p>
        <span class="prog">${sceneProgress(b)}/6 sahne üretildi</span></a>`).join("")}</div>
    </section>
    <section class="block">
      <div class="block-h"><h2>Yedi bölge, yedi sezon</h2><a href="#/bolgeler" class="more">Bölgeler ${icon("chev")}</a></div>
      <div class="grid regions">${D.sezonlar.filter(s => s.bolge).map(regionCard).join("")}</div>
    </section>`;
  }

  function regionCard(s) {
    const eps = D.bolumler.filter(b => b.sezon === s.id);
    const u = eps.reduce((a, b) => a + sceneProgress(b), 0);
    return `<a class="card region r-${s.bolge}" href="#/bolge/${s.bolge}">
      <span class="ep-no">SEZON ${s.no} · ${eps.length} İL</span>
      <h3>${esc(BOLGE.get(s.bolge).ad)}</h3>
      <p class="r-name">${esc(s.ad.replace(/^Sezon \d+ · /, ""))}</p>
      <p class="r-route">${esc(s.rota.join(" → "))}</p>
      <span class="prog">${eps.length}/${s.rota.length} bölüm yazıldı · ${u}/${eps.length * 6} sahne üretildi</span>
    </a>`;
  }

  function pageBiblio() {
    const B = D.biblio;
    return `<section class="block"><p class="eyebrow">Aşama 1</p><h1>Dizi biblisi</h1><p class="lede">${esc(B.logline)}</p></section>
    <section class="block card pad"><h2>Ana hikâye</h2>${B.ana_hikaye.map(p => `<p>${esc(p)}</p>`).join("")}</section>
    <section class="grid two">
      <div class="card pad"><h2>Temalar</h2><ul class="list">${B.temalar.map(t => `<li>${esc(t)}</li>`).join("")}</ul></div>
      <div class="card pad"><h2>Görsel dünya ve format</h2><ul class="list">${B.dunyagorsel.map(t => `<li>${esc(t)}</li>`).join("")}</ul></div>
    </section>
    <section class="block card pad"><h2>Ticaret stratejisi</h2><ul class="list">${B.ticaret.map(t => `<li>${esc(t)}</li>`).join("")}</ul></section>
    <section class="block card pad"><h2>Karakter gelişimi</h2>${B.gelisim.map(g => `<h3>${esc(g[0])}</h3><p>${esc(g[1])}</p>`).join("")}</section>
    <section class="block"><h2>Sezonlar</h2><div class="seasons">${D.sezonlar.map(sezonKart).join("")}</div></section>`;
  }

  function sezonKart(s) {
    const eps = D.bolumler.filter(b => b.sezon === s.id);
    const satir = (l, v) => `<dt>${esc(l)}</dt><dd>${esc(v)}</dd>`;
    return `<article class="card pad season">
      <p class="eyebrow">${esc(s.alt)}</p><h3>${esc(s.ad)}</h3>
      <dl class="kv">${satir("Sezon açılışı", s.acilis)}${satir("Genel hikâye", s.hikaye)}${satir("Ticari hedef", s.hedef)}
      ${satir("Sezon ortası", s.orta)}${satir("Sezon finali", s.final)}${satir("Sonraki sezona geçiş", s.gecis)}
      ${s.taksit ? satir("Taksit", para(s.taksit)) : ""}</dl>
      <p class="route-line"><b>Şehir sırası:</b> ${eps.map(b => `<a href="#/video/${b.no}">${esc(b.sehir || ("Video " + b.no))}</a>`).join(" → ")}</p>
    </article>`;
  }

  function pageKarakterler() {
    const card = k => {
      const kiyafetler = Object.entries(k.kiyafet || {});
      kiyafetler.forEach(([ad, v]) => PROMPTS.set("k-" + k.id + "-" + ad, k.en + "; wearing " + v + ". Voice: " + k.ses + "."));
      if (!kiyafetler.length) PROMPTS.set("k-" + k.id, k.en + ". Voice: " + k.ses + ".");
      return `<article class="card pad char">
        <div class="char-h"><h3>${esc(k.ad)}</h3><span class="pill">${k.yas} yaşında</span>${k.ana ? '<span class="pill gold">Ana karakter</span>' : ""}</div>
        <dl class="kv"><dt>İlk görünüş</dt><dd>${esc(k.ilk)}</dd><dt>Rolü</dt><dd>${esc(k.rol)}</dd><dt>Görünüm</dt><dd>${esc(k.tr)}</dd><dt>Geçmişi</dt><dd>${esc(k.gecmis)}</dd></dl>
        <div class="pbox"><div class="pbox-top"><span class="lbl">Sabit İngilizce karakter tanımı</span></div><pre class="prompt">${esc(k.en)}</pre></div>
        ${kiyafetler.map(([ad, v]) => `<div class="pbox"><div class="pbox-top"><span class="lbl">Kıyafet: ${ad === "temel" ? "başlangıç (Bölüm 1-56)" : "mont (Bölüm 57 Düzce'den itibaren)"}</span>${copyBtn("k-" + k.id + "-" + ad, "Tanım + kıyafet + ses")}</div><pre class="prompt">${esc(v)}</pre></div>`).join("")}
        <div class="pbox"><div class="pbox-top"><span class="lbl">Sabit ses tanımı</span>${kiyafetler.length ? "" : copyBtn("k-" + k.id, "Tanım + ses")}</div><pre class="prompt">${esc(k.ses)}</pre></div>
      </article>`;
    };
    const nesne = Object.entries(D.nesne).map(([k, v]) => `<li><b>${esc(k)}</b>: <span class="mono">${esc(v)}</span></li>`).join("");
    return `<section class="block"><p class="eyebrow">Karakter devamlılığı</p><h1>Karakterler</h1>
      <p class="lede">Yüz, saç, göz, vücut ve ses bütün videolarda aynıdır; bu metinler her sahne prompt'una aynen girer. Kıyafet yalnızca Bölüm 57 Düzce'de, yağmur başlayınca değişir ve sonra hep aynı kalır. Her bölümün konuk karakterleri o bölümün sayfasındadır.</p></section>
      <div class="grid chars">${D.karakterler.map(card).join("")}</div>
      <section class="block card pad"><h2>Sabit nesneler</h2><ul class="list">${nesne}</ul></section>`;
  }

  function pageRehber() {
    PROMPTS.set("stil", D.sabit.format + " " + D.sabit.stil);
    const kurallar = [
      ["VIDEO FORMAT", "Dikey 9:16, 1080x1920, 10 saniye, tek çekim."], ["VISUAL STYLE", "Semi-realistic stylized 3D, Pixar oranları, gerçekçi doku ve sinematik dünya."],
      ["CHARACTER DEFINITIONS", "Sahnede görünen herkesin sabit tarifi, kıyafeti ve sesi. Telefondaki kişi 'görünmez' diye yazılır."],
      ["LOCATION", "O sahnenin gerçekçi mekân tarifi."], ["TIME AND LIGHT", "Saat + günün evresi + hava; aynı evre hep aynı ışık cümlesini alır."],
      ["BACKGROUND", "Sade; en çok üç uzak, bulanık kişi."], ["ACTION", "10 saniyelik tek eylem; fiziksel olarak mümkün."], ["CAMERA", "Tek kamera hareketi."],
      ["DIALOGUE IN TURKISH", "Türkçe, kısa, tonu köşeli parantezde. Sahne başına en çok ~25 kelime."], ["LIP SYNC", "Yalnızca konuşan karakterin ağzı oynar."],
      ["PHYSICS", "Ağırlık, denge, temas; eller tek nesne tutar."], ["AUDIO", "Türkçe konuşma ve ortam sesi, müzik yok."], ["AVOID", "Bozulmalar, kıyafet değişimi, titreyen ışık, yazı, logo."]
    ];
    return `<section class="block"><p class="eyebrow">Flow için</p><h1>Prompt rehberi</h1>
      <p class="lede">Her sahne prompt'u kendi başına Flow'a yapıştırılıp üretilebilir: karakter, mekân ve ışık bilgisi her prompt'ta tekrar yazılıdır. Yer-zaman yazısı ve KASA sayacı prompt'a konmaz; kurguda eklenir.</p></section>
      <section class="card pad block"><h2>Prompt sırası (13 başlık)</h2><ol class="steps">${kurallar.map(k => `<li><b>${esc(k[0])}</b><span>${esc(k[1])}</span></li>`).join("")}</ol></section>
      <section class="grid two">
        <div class="card pad"><h2>Üretince kontrol listesi</h2><ul class="list">
          <li>Yüz önceki sahnelerdeki gibi mi? Saç, sakal, göz rengi aynı mı?</li><li>Kıyafet bölümün kıyafetiyle aynı mı?</li>
          <li>Eller beş parmaklı ve doğal mı? Nesne elde duruyor mu?</li><li>Işık sahne boyunca aynı mı?</li>
          <li>Dudaklar Türkçe sözlerle uyumlu mu? Yalnızca konuşan mı konuşuyor?</li><li>Arka plan sade mi, kalabalık yok mu?</li></ul>
          <p class="muted">Tutmazsa sahneyi 2-3 kez daha üret. Olmazsa kartın altındaki "Sade prompt"u kullan: en çok iki karakter, sabit kamera, tek eylem, tek replik.</p></div>
        <div class="card pad"><h2>Kasa videosu nasıl kullanılır?</h2><ul class="list">
          <li>Kasa açıldıktan sonra (Video 4, Sahne 6) her sahnenin arasında hazır bir kasa prompt'u vardır.</li>
          <li>Para azalınca kırmızı, artınca yeşil değişim satırı; değişmeyen sahnelerde sabit kasa.</li>
          <li>Aynı bakiyeyi taşıyan sabit sahneler tek klibi paylaşır; kart bunu söyler.</li>
          <li>8 saniyelik siyah zeminli klibi sahnenin üstüne koy, karışım modunu Ekran (Screen) ya da Aydınlat (Lighten) yap.</li>
          <li>Rakam bozuk çıkarsa Kasa sayfasındaki ayardan "Anında değişir"i dene.</li></ul></div>
      </section>
      <section class="card pad block"><h2>Ortak stil satırı</h2><pre class="prompt">${esc(D.sabit.format + " " + D.sabit.stil)}</pre>${copyBtn("stil", "Stil satırını kopyala")}
        <h3>Kapak stili</h3><pre class="prompt">${esc(D.sabit.kapak_stil)}</pre><h3>Pek yakında kapağı stili</h3><pre class="prompt">${esc(D.sabit.yakinda_stil)}</pre></section>`;
  }

  function pageBolgeler() {
    return `<section class="block"><p class="eyebrow">Rota</p><h1>Bölgeler ve şehirler</h1>
      <p class="lede">Yolculuk Doğu Anadolu'dan başlar. Her sezon bir coğrafi bölgedir; şehirler coğrafi olarak mantıklı bir gezi rotasıyla sıralanmıştır. Bölgeye dokun, şehirleri gör.</p></section>
      <a class="card region r-baslangic block" href="#/baslangic"><span class="ep-no">SEZON 0 · 6 VİDEO</span><h3>Başlangıç: 800 Bin Lira</h3><p class="r-route">Kaza → 800.000 TL → Para Arayışı → Ticaret Fikri → İlk Ticaret → 81 Şehir Duyurusu</p></a>
      <div class="grid regions">${D.sezonlar.filter(s => s.bolge).map(regionCard).join("")}</div>`;
  }

  function pageBolge(id) {
    const s = D.sezonlar.find(x => x.bolge === id);
    if (!s) return notFound();
    const eps = D.bolumler.filter(b => b.sezon === s.id);
    return `<nav class="crumb"><a href="#/bolgeler">${icon("back")} Bölgeler</a></nav>
      <section class="block"><p class="eyebrow">Sezon ${s.no} · ${esc(s.alt)}</p><h1>${esc(BOLGE.get(id).ad)}</h1><p class="lede">${esc(s.ad)} — ${esc(s.hikaye)}</p></section>
      ${sezonKart(s)}
      <section class="block"><h2>Şehirler (rota sırasıyla)</h2><ol class="cities">${s.rota.map((il, i) => {
        const b = D.bolumler.find(x => x.sehir === il);
        return `<li><a class="card city" href="#/sehir/${b.plaka}"><span class="city-n">${pad2(i + 1)}</span><span class="city-b"><b>${esc(il)}</b><small>Plaka ${pad2(b.plaka)} · Bölüm ${b.no}: ${esc(b.baslik)}</small><small class="urun">${esc(b.urun)}</small></span><span class="prog">${sceneProgress(b)}/6</span></a></li>`;
      }).join("")}</ol></section>`;
  }

  function pageBaslangic() {
    const s = SEZ.get("s0");
    const eps = D.bolumler.filter(b => b.sezon === "s0");
    return `<nav class="crumb"><a href="#/bolgeler">${icon("back")} Bölgeler</a></nav>
      <section class="block"><p class="eyebrow">${esc(s.alt)}</p><h1>${esc(s.ad)}</h1><p class="lede">${esc(s.hikaye)}</p></section>
      ${sezonKart(s)}
      <div class="grid cards6">${eps.map(b => `<a class="card ep-card" href="#/video/${b.no}"><span class="ep-no">VİDEO ${b.no}</span><h3>${esc(b.baslik)}</h3><p>${esc(b.ozet)}</p><span class="prog">${sceneProgress(b)}/6 sahne üretildi</span></a>`).join("")}</div>`;
  }

  function pageSehir(plaka) {
    const b = SEHIR_EP.get(plaka);
    if (!b) return notFound();
    const bol = BOLGE.get(b.bolge);
    const vids = D.bolumler.filter(x => x.plaka === plaka);
    return `<nav class="crumb"><a href="#/bolge/${b.bolge}">${icon("back")} ${esc(bol.ad)}</a></nav>
      <section class="block"><p class="eyebrow">Plaka ${pad2(plaka)} · ${esc(bol.ad)} · ${esc(b.ay)}</p><h1>${esc(b.sehir)}</h1>
      <p class="lede">${esc(b.urun)}</p></section>
      <section class="block"><h2>Bu şehrin videoları</h2><div class="grid cards6">${vids.map(v => `<a class="card ep-card" href="#/video/${v.no}">
        <span class="ep-no">BÖLÜM ${v.no}</span><h3>${esc(v.baslik)}</h3><p>${esc(v.ozet)}</p>
        <span class="prog">${sceneProgress(v)}/6 sahne üretildi · Kasa: ${sonBakiye(v) == null ? "—" : para(sonBakiye(v))}</span></a>`).join("")}</div></section>`;
  }

  /* ---------------------------------------------------------------- video detay */
  function gorselAlan(b, tur, baslik, yazi) {
    const key = b.no + "-" + tur;
    const img = Store.gorsel[key];
    return `<figure class="cover-slot ${tur}">
      <div class="slot" data-slot="${key}">${img ? `<img src="${img}" alt="${esc(baslik)}">` : `<div class="ph">${icon("img")}<b>${esc(baslik)}</b><span>${yazi.map(esc).join("<br>")}</span><small>9:16 · 1080x1920</small></div>`}</div>
      <figcaption><span class="lbl">${esc(baslik)}</span>
        <label class="btn small">${icon("img")}<span>${img ? "Değiştir" : "Görsel yükle"}</span><input type="file" accept="image/*" data-upload="${key}" hidden></label>
        ${img ? `<button class="btn small ghost" type="button" data-unload="${key}">Kaldır</button>` : ""}</figcaption>
    </figure>`;
  }

  function kasaAraKutu(b, sc) {
    const x = SB.get(b.no + "-" + sc.n);
    if (!x) return "";
    const id = b.no + "-" + sc.n + "-kasa";
    const sabit = x.bas === x.son;
    let nereye = `Sahne ${sc.n} üstüne koy`, ayni = "";
    if (sabit) {
      const grup = b.sahneler.filter(s => { const y = SB.get(b.no + "-" + s.n); return y && y.bas === y.son && y.son === x.son; }).map(s => s.n);
      if (grup.length > 1) {
        if (grup[0] === sc.n) nereye = `Sahne ${grup.join(", ")} için tek klip`;
        else { nereye = `Sahne ${grup[0]}'deki sabit klibi kullan`; ayni = `<p class="note">Bakiye Sahne ${grup[0]} ile aynı; o klibi buraya da koy, yeniden üretme.</p>`; }
      }
    }
    const neden = x.islemler.filter(e => e.tip !== "acilis" || true).map(e =>
      `<li><span class="${D.tipler[e.tip].isaret > 0 ? "up" : "down"}">${D.tipler[e.tip].isaret > 0 ? "+" : "−"}${esc(para(e.tutar))}</span> ${esc(D.tipler[e.tip].ad)}: ${esc(e.aciklama)}${e.kaynak === "kullanici" ? ' <em class="pill">eklediğin</em>' : ""}</li>`).join("");
    const deg = x.son - x.bas;
    return `<aside class="kasa-ara ${sabit ? "hold" : deg > 0 ? "up" : "down"}" aria-label="Sahne ${sc.n} kasa videosu">
      <div class="ka-row">
        <div class="ka-mini" aria-hidden="true"><span class="k">KASA</span><span class="b">${esc(para(x.son))}</span>${sabit ? "" : `<span class="c">${esc(isaretli(deg))}</span>`}</div>
        <div class="ka-info">
          <span class="lbl">${sabit ? "Sabit kasa" : "Kasa videosu"} · 8 sn · siyah zemin · ${esc(nereye)}</span>
          <p class="ka-val">${sabit ? `Sabit: ${esc(para(x.son))} · değişim satırı yok` : `${esc(para(x.bas))} → ${esc(para(x.son))} <b>(${esc(isaretli(deg))})</b>`}</p>
          ${neden ? `<ul class="ka-why">${neden}</ul>` : ""}${ayni}
          ${x.islemler.length > 1 ? `<p class="note">Bu sahnede ${x.islemler.length} işlem var; tek klip toplam değişimi gösterir. Ayrı klipler "Kasa hareketleri" bölümünde.</p>` : ""}
        </div>
      </div>
      ${promptKutu(id, kasaPrompt(x.bas, x.son), sabit ? "Sabit kasa prompt'u" : "Kasa animasyonu prompt'u", uretildiKutu(id, "Kasa klibi üretildi"))}
    </aside>`;
  }

  function sahneKart(b, sc) {
    const pid = b.no + "-" + sc.n;
    const yerTr = b.yerler[sc.yer][0];
    const zaman = sc.fb ? "anı" : (sc.saat + " · " + sc.faz);
    const ad = n => { const k = KAR.get(n); return k ? k.ad : (b.misafir[n] ? b.misafir[n][0] : n); };
    return `<article class="scene ${Store.uretildiMi(pid) ? "done" : ""}" id="s-${pid}">
      <header class="sc-h"><h3>SAHNE ${pad2(sc.n)} – ${esc(TR_UP(sc.ad))}</h3>${uretildiKutu(pid)}</header>
      <div class="chips"><span class="pill gold">10 saniye</span><span class="pill">${esc(zaman)}</span><span class="pill">${esc(yerTr)}</span>${sc.h ? `<span class="pill">${esc(sc.h)}</span>` : ""}</div>
      <p class="sc-tr">${esc(sc.tr)}</p>
      ${sc.dlg.length ? `<div class="dlg">${sc.dlg.map(d => `<p><b>${esc(ad(d[0]))}:</b> “${esc(d[1])}”${d[2] ? ` <i>(${esc(d[2])})</i>` : ""}</p>`).join("")}</div>` : `<p class="note">Konuşma yok.</p>`}
      ${sc.kurgu ? `<p class="note"><b>Kurgu notu:</b> ${esc(sc.kurgu)}</p>` : ""}
      ${promptKutu(pid, sahnePrompt(b, sc), "İngilizce Flow prompt'u", copyBtn(pid + "-sade", "Sade prompt"))}
      ${(PROMPTS.set(pid + "-sade", sadePrompt(b, sc)), "")}
    </article>`;
  }

  function hashtagler(b) {
    const base = ["#JozhStudios", "#81Şehir", "#MertVeAli"];
    const il = b.sehir ? ["#" + b.sehir.replace(/\s+/g, "")] : [];
    const bol = b.bolge ? ["#" + BOLGE.get(b.bolge).ad.replace(/ Bölgesi$/, "").replace(/\s+/g, "")] : [];
    return [...new Set(base.concat(il, b.tags, bol, ["#Ticaret", "#Animasyon"]))];
  }

  function pageVideo(no) {
    const b = EP.get(no);
    if (!b) return notFound();
    const sz = SEZ.get(b.sezon);
    const prev = EP.get(no - 1), next = EP.get(no + 1);
    const tags = hashtagler(b);
    const ilet = AY().iletisim || "[iletişim adresin]";
    const kapakYazi = [b.sehir ? `BÖLÜM ${b.no}` : `VİDEO ${b.no}`, b.baslik, b.sehir || "Malatya"];
    const igMetin = sosyalKasaDoldur(b.ig, b);
    const tiktokAciklama = b.tiktok + "\n\n" + b.ozet + "\n\n" + tags.join(" ");
    const sponsor = b.sehir
      ? `${b.sehir} bölümümüz için şehrini tanıtmak isteyen yerel işletmelerle tanışmak istiyoruz. ${b.sponsor || ("Özellikle " + b.urun.toLocaleLowerCase("tr-TR") + " alanında")} çalışan bir işletmen varsa bize yaz: ${ilet}\n\nİş birlikleri videoda her zaman açıkça "reklam / iş birliği" olarak belirtilir. Bu bölümde şu an gerçek bir sponsor yoktur.`
      : `JOZH STUDIOS · 81 Şehir için yerel işletmeler ve markalarla iş birliğine açığız. Şehrinizde bizi ağırlamak ya da ürününüzü tanıtmak isterseniz yazın: ${ilet}\n\nİş birlikleri videoda her zaman açıkça "reklam / iş birliği" olarak belirtilir.`;
    const kasaListe = DEF.entries.filter(e => e.no === b.no);
    const kliplar = b.sahneler.map(sc => ({ sc, x: SB.get(b.no + "-" + sc.n) })).filter(o => o.x);
    const islemSatir = e => {
      const k = "tx-" + e.id;
      PROMPTS.set(k, kasaPrompt(e.onceki, e.sonraki));
      return `<tr><td>S${e.sahne}</td><td>${esc(D.tipler[e.tip].ad)}${e.kaynak === "kullanici" ? ' <em class="pill">eklediğin</em>' : ""}<br><small>${esc(e.aciklama)}</small></td>
        <td class="num">${esc(para(e.onceki))}</td><td class="num ${D.tipler[e.tip].isaret > 0 ? "up" : "down"}">${D.tipler[e.tip].isaret > 0 ? "+" : "−"}${esc(para(e.tutar))}</td>
        <td class="num">${esc(para(e.sonraki))}</td><td>${copyBtn(k, "Prompt", "small")}</td></tr>`;
    };
    const not = Store.durum.notlar[b.no] || "";
    return `<nav class="crumb">${b.sehir ? `<a href="#/sehir/${b.plaka}">${icon("back")} ${esc(b.sehir)}</a>` : `<a href="#/baslangic">${icon("back")} Başlangıç</a>`}
      <span class="crumb-r">${prev ? `<a href="#/video/${prev.no}">‹ ${esc(epEtiket(prev))}</a>` : ""}${next ? `<a href="#/video/${next.no}">${esc(epEtiket(next))} ›</a>` : ""}</span></nav>
    <section class="covers">
      ${gorselAlan(b, "kapak", "Video kapağı", kapakYazi)}
      ${gorselAlan(b, "yakinda", "Pek yakında kapağı", ["PEK YAKINDA", b.baslik])}
    </section>
    <section class="grid two block">
      <div>${promptKutu(b.no + "-kapak", kapakPrompt(b, b.kapak, D.sabit.kapak_stil), "Video kapağı prompt'u", uretildiKutu(b.no + "-kapak", "Kapak üretildi"))}
        <p class="note"><b>Kapak:</b> ${esc(b.kapak[3])}<br><b>Kapağa yazılacak:</b> ${kapakYazi.map(esc).join(" · ")}</p></div>
      <div>${promptKutu(b.no + "-yakinda", kapakPrompt(b, b.yakinda, D.sabit.yakinda_stil), "Pek yakında kapağı prompt'u", uretildiKutu(b.no + "-yakinda", "Yakında kapağı üretildi"))}
        <p class="note"><b>Pek yakında:</b> ${esc(b.yakinda[3])}<br><b>Kapağa yazılacak:</b> PEK YAKINDA · ${esc(b.baslik)}</p></div>
    </section>
    <section class="block vhead">
      <p class="eyebrow">${esc(sz.ad)} · ${esc(epEtiket(b))} · ${esc(b.ay)} · ${esc(b.hava_tr)}</p>
      <h1>${esc(b.baslik)}</h1>
      <p class="lede"><b>Video açıklaması:</b> ${esc(b.ozet)}</p>
      <div class="card pad"><h2>Bölümün hikâyesi</h2><p>${esc(b.hikaye)}</p>
        <p class="note"><b>Bölüm sonu (merak unsuru):</b> ${esc(b.son)}</p>
        ${b.urun ? `<p class="note"><b>Şehrin ürünleri:</b> ${esc(b.urun)}</p>` : ""}
        <p class="note">${sceneProgress(b)}/6 sahne üretildi · Kasa: ${b.no < 4 ? "henüz açılmadı" : b.no === 4 ? "Sahne 6'da açılır: " + esc(para(sonBakiye(b))) : esc(para(SB.get(b.no + "-1").bas)) + " → " + esc(para(sonBakiye(b)))}</p></div>
      ${Object.keys(b.misafir).length ? `<details class="card pad guests"><summary>Bu bölümün konuk karakterleri (${Object.keys(b.misafir).length})</summary>${Object.values(b.misafir).map(m => `<div class="guest"><b>${esc(m[0])}</b><pre class="prompt">${esc(m[1])}. Voice: ${esc(m[2])}.</pre></div>`).join("")}</details>` : ""}
    </section>
    <section class="block"><h2>Altı sahne</h2><div class="scenes">${b.sahneler.map(sc => sahneKart(b, sc) + kasaAraKutu(b, sc)).join("")}</div></section>
    <section class="block card pad"><h2>Kasa hareketleri</h2>
      ${kasaListe.length ? `<div class="table-wrap"><table class="tbl"><thead><tr><th>Sahne</th><th>İşlem</th><th class="num">Önceki</th><th class="num">Tutar</th><th class="num">Yeni bakiye</th><th>Kasa</th></tr></thead><tbody>${kasaListe.map(islemSatir).join("")}</tbody></table></div>` : `<p class="muted">${b.no < 4 ? "Kasa Video 4'ün son sahnesinde açılır." : "Bu bölümde kasa hareketi yok; kasa sabit."}</p>`}
      <p class="note"><a href="#/kasa?no=${b.no}">Bu videoya işlem ekle ${icon("chev")}</a></p></section>
    <section class="block card pad"><h2>Kasa animasyonu prompt'ları</h2>
      ${kliplar.length ? kliplar.map(o => { const k = b.no + "-" + o.sc.n + "-kasa"; return `<div class="krow"><span>Sahne ${o.sc.n}: ${o.x.bas === o.x.son ? "sabit " + esc(para(o.x.son)) : esc(para(o.x.bas)) + " → " + esc(para(o.x.son))}</span>${copyBtn(k, "Kopyala", "small")}</div>`; }).join("") : `<p class="muted">Kasa henüz açılmadı.</p>`}
    </section>
    <section class="block grid two social">
      ${metinKutu(b.no + "-tt", b.tiktok, "TikTok başlığı")}
      ${metinKutu(b.no + "-tta", tiktokAciklama, "TikTok açıklaması")}
      ${metinKutu(b.no + "-ig", igMetin + "\n\n" + tags.join(" "), "Instagram açıklaması")}
      ${metinKutu(b.no + "-tag", tags.join(" "), "Hashtag önerileri")}
      ${metinKutu(b.no + "-sp", sponsor, "Sponsorluk iletişim metni")}
      ${metinKutu(b.no + "-tan", b.teaser, "Bölüm tanıtım metni")}
    </section>
    <section class="block card pad"><h2>Notlarım</h2><textarea class="notes" data-note="${b.no}" rows="3" placeholder="Bu video için not (yerel olarak kaydedilir)">${esc(not)}</textarea></section>
    <nav class="pager">${prev ? `<a class="btn" href="#/video/${prev.no}">‹ ${esc(epEtiket(prev))}</a>` : "<span></span>"}${next ? `<a class="btn gold" href="#/video/${next.no}">${esc(epEtiket(next))} ›</a>` : ""}</nav>`;
  }

  /* ---------------------------------------------------------------- kasa sayfası */
  let sonEklenen = null;
  function pageKasa(q) {
    const t = DEF.toplam, bt = DEF.byTip;
    const secNo = Number(q.no) || 0;
    const opt = D.bolumler.filter(b => b.no >= 5).map(b => `<option value="${b.no}" ${b.no === secNo ? "selected" : ""}>${esc(epEtiket(b) + " – " + b.baslik)}</option>`).join("");
    const tipOpt = Object.entries(D.tipler).filter(([k]) => k !== "acilis").map(([k, v]) => `<option value="${k}">${esc(v.ad)}</option>`).join("");
    const filtre = q.f || "hepsi";
    let list = DEF.entries.slice();
    if (filtre === "kullanici") list = list.filter(e => e.kaynak === "kullanici");
    if (filtre === "borc") list = list.filter(e => e.tip === "borc");
    if (q.no && filtre !== "kullanici") list = list.filter(e => e.no === secNo);
    const satir = e => {
      const b = EP.get(e.no);
      const k = "h-" + e.id;
      PROMPTS.set(k, kasaPrompt(e.onceki, e.sonraki));
      return `<tr><td>${b ? `<a href="#/video/${b.no}">${esc(b.sehir ? b.no + " · " + b.sehir : "V" + b.no)}</a> S${e.sahne}` : "Genel"}</td>
        <td>${esc(D.tipler[e.tip].ad)}${e.kaynak === "kullanici" ? ' <em class="pill">eklediğin</em>' : ""}<br><small>${esc(e.aciklama)}</small></td>
        <td class="num">${esc(para(e.onceki))}</td><td class="num ${D.tipler[e.tip].isaret > 0 ? "up" : "down"}">${D.tipler[e.tip].isaret > 0 ? "+" : "−"}${esc(para(e.tutar))}</td><td class="num"><b>${esc(para(e.sonraki))}</b></td>
        <td class="acts">${copyBtn(k, "Prompt", "small")}${e.kaynak === "kullanici" ? `<button class="btn small danger" type="button" data-del="${esc(e.id)}">Sil</button>` : ""}</td></tr>`;
    };
    const ayarGrup = (ad, lbl, ops) => `<div class="seg" role="radiogroup" aria-label="${esc(lbl)}"><span class="seg-l">${esc(lbl)}</span><div class="seg-o">${ops.map(([v, l]) =>
      `<label><input type="radio" name="ay-${ad}" value="${v}" data-ayar="${ad}" ${AY()[ad] === v ? "checked" : ""}><span>${esc(l)}</span></label>`).join("")}</div></div>`;
    let sonuc = "";
    if (sonEklenen) {
      const e = DEF.entries.find(x => x.id === sonEklenen);
      if (e) {
        const d = e.sonraki - e.onceki;
        sonuc = `<div class="card pad result ${d > 0 ? "up" : "down"}" id="sonuc"><h3>İşlem eklendi · kasa prompt'u hazır</h3>
          <dl class="kv"><dt>Önceki bakiye</dt><dd>${esc(para(e.onceki))}</dd><dt>İşlem miktarı</dt><dd class="${d > 0 ? "up" : "down"}">${esc(isaretli(d))}</dd><dt>Yeni bakiye</dt><dd><b>${esc(para(e.sonraki))}</b></dd><dt>Durum</dt><dd>${d > 0 ? "Artış (yeşil)" : "Azalış (kırmızı)"}</dd></dl>
          ${promptKutu("son-" + e.id, kasaPrompt(e.onceki, e.sonraki), "Kasa animasyonu prompt'u")}</div>`;
      }
    }
    return `<section class="block"><p class="eyebrow">Kurgusal ticaret sermayesi · gerçek banka hesabı değildir</p><h1>Kasa yönetimi</h1></section>
    <section class="grid stats">
      ${stat("Güncel bakiye", para(DEF.guncel), "gold")}
      ${stat("Başlangıç bakiyesi", para(DEF.baslangic))}
      ${stat("Toplam alış maliyeti", para(t.alis), "down")}
      ${stat("Toplam satış geliri", para(t.satis), "up")}
      ${stat("Brüt kâr", isaretli(DEF.brut), DEF.brut >= 0 ? "up" : "down", "satış − alış")}
      ${stat("Diğer giderler", para(t.gider), "down", "ulaşım " + para(bt.ulasim || 0) + " · konaklama " + para(bt.konaklama || 0) + " · yemek " + para(bt.yemek || 0) + " · diğer " + para(bt.diger_gider || 0))}
      ${stat("Diğer gelirler", para(t.gelir), "up", "sponsorluk " + para(bt.sponsor || 0) + " · diğer " + para(bt.diger_gelir || 0))}
      ${stat("Net kâr", isaretli(DEF.net), DEF.net >= 0 ? "up" : "down", "brüt + gelir − gider")}
      ${stat("Borç ödemesi", para(t.borc), "", "kalan: " + para(DEF.kalanBorc))}
    </section>
    <p class="note ${DEF.kontrol ? "" : "warn"}">${DEF.kontrol ? "Kontrol: başlangıç + net kâr − borç ödemesi = güncel bakiye ✓" : "Uyarı: hesap tutmuyor!"} · ${DEF.entries.length} işlem (${Store.durum.islemler.length} tanesini sen ekledin)</p>
    <section class="grid two block">
      <form class="card pad" id="islem-form" novalidate>
        <h2>Yeni ticari işlem</h2>
        <label class="fld"><span>Video</span><select name="no" required><option value="0">Videoya bağlama (genel, en sona)</option>${opt}</select></label>
        <label class="fld"><span>Sahne</span><select name="sahne">${[1, 2, 3, 4, 5, 6].map(n => `<option value="${n}" ${n === 6 ? "selected" : ""}>Sahne ${n}</option>`).join("")}</select></label>
        <label class="fld"><span>İşlem türü</span><select name="tip" required>${tipOpt}</select></label>
        <label class="fld"><span>Tutar (TL)</span><input name="tutar" inputmode="numeric" autocomplete="off" placeholder="örn. 12.500" required></label>
        <label class="fld"><span>Açıklama</span><input name="aciklama" maxlength="200" autocomplete="off" placeholder="örn. 50 kg Antep fıstığı" required></label>
        <p class="form-err" role="alert" id="form-err"></p>
        <button class="btn gold big" type="submit">İşlemi ekle ve prompt'u üret</button>
        <p class="note">Bakiye otomatik hesaplanır. Aynı işlem iki kez eklenmez; işlem, kasayı herhangi bir anda eksiye düşürecekse eklenmez. Eklediğin işlem seçtiğin sahnenin kasa klibine de yansır.</p>
      </form>
      <div class="stack">${sonuc}
        <div class="card pad"><h2>Kasa prompt ayarları</h2>
          ${ayarGrup("birim", "Para birimi", [["TL", "TL"], ["₺", "₺"]])}
          ${ayarGrup("gecis", "Rakamlar", [["akici", "Akıcı sayar"], ["anlik", "Anında değişir"]])}
          ${ayarGrup("etiket", "KASA yazısı", [["var", "Var"], ["yok", "Yok"]])}
          <p class="note">Ayar bütün kasa prompt'larını birlikte değiştirir; sahne prompt'larına dokunmaz.</p></div>
        <form class="card pad" id="serbest-form"><h2>Serbest kasa prompt'u</h2>
          <div class="row2"><label class="fld"><span>Önceki bakiye</span><input name="a" inputmode="numeric" placeholder="100.000"></label><label class="fld"><span>Yeni bakiye</span><input name="b" inputmode="numeric" placeholder="102.500"></label></div>
          <button class="btn" type="submit">Prompt üret</button><div id="serbest-sonuc"></div></form>
      </div>
    </section>
    <section class="block card pad"><div class="block-h"><h2>İşlem geçmişi</h2>
      <div class="filters">${[["hepsi", "Tümü"], ["kullanici", "Eklediklerim"], ["borc", "Borç taksitleri"]].map(([f, l]) => `<a class="pill ${filtre === f ? "gold" : ""}" href="#/kasa?f=${f}${q.no && f !== "kullanici" ? "&no=" + q.no : ""}">${l}</a>`).join("")}${q.no ? `<a class="pill" href="#/kasa">Filtreyi kaldır (Video ${esc(q.no)})</a>` : ""}</div></div>
      <div class="table-wrap"><table class="tbl"><thead><tr><th>Video</th><th>İşlem</th><th class="num">Önceki</th><th class="num">Tutar</th><th class="num">Bakiye</th><th></th></tr></thead><tbody>${list.slice().reverse().map(satir).join("") || `<tr><td colspan="6" class="muted">Kayıt yok.</td></tr>`}</tbody></table></div>
    </section>`;
  }

  function tutarOku(s) {
    const t = String(s || "").replace(/\s|TL|₺/gi, "").replace(/\./g, "").replace(/,/g, "");
    if (!/^\d+$/.test(t)) return null;
    const n = parseInt(t, 10);
    return n > 0 && n <= KasaMotor.MAX ? n : null;
  }

  function islemEkle(form) {
    const err = $("#form-err");
    const fd = new FormData(form);
    const tutar = tutarOku(fd.get("tutar"));
    const aciklama = String(fd.get("aciklama") || "").trim();
    const tip = String(fd.get("tip"));
    const no = Number(fd.get("no")) || 0;
    const sahne = Number(fd.get("sahne")) || 6;
    if (!D.tipler[tip] || tip === "acilis") return (err.textContent = "İşlem türünü seç.");
    if (!tutar) return (err.textContent = "Tutarı tam lira olarak yaz (örn. 12.500).");
    if (!aciklama) return (err.textContent = "Kısa bir açıklama yaz.");
    if (no && (!EP.has(no) || no < 5)) return (err.textContent = "Geçersiz video.");
    const ayni = Store.durum.islemler.find(x => x.no === no && x.sahne === sahne && x.tip === tip && x.tutar === tutar && x.aciklama.toLocaleLowerCase("tr") === aciklama.toLocaleLowerCase("tr"));
    if (ayni) return (err.textContent = "Bu işlem zaten kayıtlı (aynı video, sahne, tür, tutar ve açıklama). Mükerrer kayıt eklenmedi.");
    const yeni = { id: Store.yeniId(), no, sahne, tip, tutar, aciklama, olusturma: Date.now() };
    const deneme = KasaDefter.build(D, Store.durum.islemler.concat([yeni]));
    if (deneme.eksi) {
      const e = deneme.eksi, b = EP.get(e.no);
      return (err.textContent = `Bu işlem kasayı eksiye düşürür (${b ? epEtiket(b) + " sahne " + e.sahne : "genel"}: ${para(e.sonraki)}). Eklenmedi.`);
    }
    try { Store.islemEkle(yeni); } catch (e) { return (err.textContent = e.message === "KOTA" ? "Tarayıcı depolama alanı dolu. Görselleri kaldırıp yeniden dene." : "Kaydedilemedi."); }
    err.textContent = "";
    sonEklenen = yeni.id;
    hesapla();
    toast("İşlem eklendi: " + isaretli(D.tipler[tip].isaret * tutar));
    render();
    setTimeout(() => { const s = $("#sonuc"); if (s) s.scrollIntoView({ block: "start" }); }, 30);
  }

  /* ---------------------------------------------------------------- veri sayfası */
  function pageVeri() {
    const d = Store.durum;
    const gs = Object.keys(Store.gorsel).length;
    return `<section class="block"><p class="eyebrow">LocalStorage</p><h1>Veri ve yedek</h1>
      <p class="lede">Senaryolar, sahneler, prompt'lar ve sosyal medya metinleri panelin içindedir ve silinmez. Senin verilerin (eklediğin kasa işlemleri, üretildi işaretleri, notlar, ayarlar, yüklediğin kapaklar) bu tarayıcıda saklanır. Başka cihaza geçmek için dışa aktar, orada içe aktar.</p></section>
      ${Store.kalici ? "" : `<p class="note warn">Bu tarayıcı yerel depolamaya izin vermiyor (gizli sekme olabilir). Değişiklikler sayfa kapanınca kaybolur.</p>`}
      <section class="grid stats">${stat("Eklediğin işlem", d.islemler.length)}${stat("Üretildi işareti", d.uretildi.length)}${stat("Not", Object.keys(d.notlar).length)}${stat("Yüklenen görsel", gs)}</section>
      <section class="grid two block">
        <div class="card pad"><h2>JSON dışa aktar</h2><p class="muted">Bütün kullanıcı verini tek bir .json dosyası olarak indirir.</p>
          <label class="check"><input type="checkbox" id="gorsel-dahil" ${gs ? "checked" : ""}><span>Yüklediğim görselleri de ekle</span></label>
          <button class="btn gold big" type="button" id="disa">JSON dosyasını indir</button></div>
        <div class="card pad"><h2>JSON içe aktar</h2><p class="muted">Bir JOZH STUDIOS yedeğini seç. Dosya doğrulanır, sonra onayınla mevcut verinin yerine geçer.</p>
          <label class="btn big">Dosya seç<input type="file" accept="application/json,.json" id="ice" hidden></label><div id="ice-sonuc"></div></div>
      </section>
      <section class="card pad block"><h2>İletişim bilgisi</h2><p class="muted">Sponsorluk iletişim metinlerine yazılır (ör. e-posta ya da kullanıcı adı).</p>
        <label class="fld"><span>İletişim</span><input id="iletisim" maxlength="200" value="${esc(d.ayar.iletisim || "")}" placeholder="ornek@eposta.com · @jozhstudios"></label></section>
      <section class="card pad block danger-zone"><h2>Sıfırla</h2><p class="muted">Yalnızca senin verini siler (işlemler, işaretler, notlar, görseller). Senaryo içerikleri kalır.</p>
        <button class="btn danger" type="button" id="sifirla">Kullanıcı verisini sil</button></section>`;
  }

  function notFound() { return `<section class="block"><h1>Sayfa bulunamadı</h1><p><a href="#/">Ana sayfaya dön</a></p></section>`; }

  /* ================================================================ yönlendirme */
  const NAV = [
    ["#/", "Ana sayfa", "home"], ["#/biblio", "Dizi biblisi", "book"], ["#/karakterler", "Karakterler", "user"],
    ["#/baslangic", "Başlangıç videoları", "play"], ["#/bolgeler", "Bölgeler ve şehirler", "map"],
    ["#/kasa", "Kasa", "cash"], ["#/rehber", "Prompt rehberi", "guide"], ["#/veri", "Veri ve yedek", "data"]
  ];
  function navHtml(cur) {
    return NAV.map(([h, l, i]) => `<a href="${h}" class="${cur === h ? "active" : ""}" ${cur === h ? 'aria-current="page"' : ""}>${icon(i)}<span>${l}</span></a>`).join("")
      + `<div class="nav-sep"></div><p class="nav-h">Bölgeler</p>` + D.sezonlar.filter(s => s.bolge).map(s => `<a href="#/bolge/${s.bolge}" class="sub ${cur === "#/bolge/" + s.bolge ? "active" : ""}"><span class="dot r-${s.bolge}"></span><span>${esc(BOLGE.get(s.bolge).ad.replace(" Bölgesi", ""))}</span></a>`).join("");
  }

  function parse() {
    const h = location.hash || "#/";
    const [yol, qs] = h.split("?");
    const q = {};
    (qs || "").split("&").forEach(p => { if (p) { const [k, v] = p.split("="); q[decodeURIComponent(k)] = decodeURIComponent(v || ""); } });
    return { yol: yol === "#" ? "#/" : yol, q };
  }

  let sonYol = "";
  function render() {
    const { yol, q } = parse();
    PROMPTS.clear();
    const parts = yol.replace(/^#\//, "").split("/");
    let html, cur = yol;
    switch (parts[0]) {
      case "": html = pageHome(); cur = "#/"; break;
      case "biblio": html = pageBiblio(); break;
      case "karakterler": html = pageKarakterler(); break;
      case "rehber": html = pageRehber(); break;
      case "bolgeler": html = pageBolgeler(); break;
      case "baslangic": html = pageBaslangic(); break;
      case "bolge": html = pageBolge(parts[1]); cur = "#/bolge/" + parts[1]; break;
      case "sehir": { const b = SEHIR_EP.get(Number(parts[1])); html = pageSehir(Number(parts[1])); cur = b ? "#/bolge/" + b.bolge : yol; break; }
      case "video": { const b = EP.get(Number(parts[1])); html = pageVideo(Number(parts[1])); cur = b ? (b.bolge ? "#/bolge/" + b.bolge : "#/baslangic") : yol; break; }
      case "kasa": html = pageKasa(q); cur = "#/kasa"; break;
      case "veri": html = pageVeri(); break;
      default: html = notFound();
    }
    $("#view").innerHTML = html;
    $("#nav").innerHTML = navHtml(cur);
    document.title = (($("#view h1") || {}).textContent || "Panel") + " · JOZH STUDIOS";
    if (yol !== sonYol) { window.scrollTo(0, 0); sonYol = yol; if (parts[0] !== "kasa") sonEklenen = null; }
    menuKapat();
  }

  /* ================================================================ olaylar */
  function toast(m) {
    const t = $("#toast");
    t.textContent = m; t.classList.add("on");
    clearTimeout(t._t); t._t = setTimeout(() => t.classList.remove("on"), 2200);
  }

  function kopyala(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text).catch(() => eskiKopya(text));
    return eskiKopya(text);
  }
  function eskiKopya(text) {
    return new Promise((res, rej) => {
      const ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.top = "-1000px"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select(); ta.setSelectionRange(0, text.length);
      let ok = false; try { ok = document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
      ok ? res() : rej(new Error("kopya"));
    });
  }

  function menuAc() { document.body.classList.add("menu-open"); $("#menu-btn").setAttribute("aria-expanded", "true"); }
  function menuKapat() { document.body.classList.remove("menu-open"); const m = $("#menu-btn"); if (m) m.setAttribute("aria-expanded", "false"); }

  function gorselYukle(file, key) {
    if (!file || !file.type.startsWith("image/")) return toast("Bir görsel dosyası seç.");
    const fr = new FileReader();
    fr.onload = () => {
      const img = new Image();
      img.onload = () => {
        const r = Math.min(1, 1280 / Math.max(img.width, img.height), 720 / Math.min(img.width, img.height));
        const w = Math.max(1, Math.round(img.width * r)), h = Math.max(1, Math.round(img.height * r));
        const c = document.createElement("canvas"); c.width = w; c.height = h;
        c.getContext("2d").drawImage(img, 0, 0, w, h);
        try { Store.gorselAyarla(key, c.toDataURL("image/jpeg", 0.82)); toast("Görsel kaydedildi"); render(); }
        catch (e) { toast("Depolama alanı dolu; görsel kaydedilemedi."); }
      };
      img.onerror = () => toast("Görsel okunamadı.");
      img.src = fr.result;
    };
    fr.readAsDataURL(file);
  }

  document.addEventListener("click", e => {
    const c = e.target.closest("[data-copy]");
    if (c) {
      const text = PROMPTS.get(c.dataset.copy) || "";
      const span = c.querySelector("span"); const eski = span ? span.textContent : "";
      kopyala(text).then(() => {
        c.classList.add("done"); if (span) span.textContent = "Kopyalandı";
        setTimeout(() => { c.classList.remove("done"); if (span) span.textContent = eski; }, 1400);
      }, () => {
        const d = document.querySelector(`details[data-pid="${CSS.escape(c.dataset.copy)}"]`);
        if (d) { d.open = true; const p = d.querySelector("pre"); if (!p.textContent) p.textContent = text; const r = document.createRange(); r.selectNodeContents(p); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
        toast("Otomatik kopyalanamadı; metin seçildi, kopyala.");
      });
      return;
    }
    if (e.target.closest("#menu-btn")) { document.body.classList.contains("menu-open") ? menuKapat() : menuAc(); return; }
    if (e.target.closest("#scrim")) { menuKapat(); return; }
    const del = e.target.closest("[data-del]");
    if (del) {
      if (!confirm("Bu işlemi silmek istediğine emin misin?")) return;
      const deneme = KasaDefter.build(D, Store.durum.islemler.filter(x => x.id !== del.dataset.del));
      if (deneme.eksi) return toast("Silinirse kasa bir noktada eksiye düşüyor; önce sonraki işlemleri kontrol et.");
      Store.islemSil(del.dataset.del); hesapla(); toast("İşlem silindi"); render(); return;
    }
    const un = e.target.closest("[data-unload]");
    if (un) { Store.gorselAyarla(un.dataset.unload, null); render(); return; }
    if (e.target.id === "disa") {
      const blob = new Blob([Store.disaAktar($("#gorsel-dahil") && $("#gorsel-dahil").checked)], { type: "application/json" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "jozh-studios-yedek-" + new Date().toISOString().slice(0, 10) + ".json";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      toast("Yedek indirildi"); return;
    }
    if (e.target.id === "sifirla") {
      if (!confirm("Eklediğin bütün işlemler, işaretler, notlar ve görseller silinecek. Emin misin?")) return;
      Store.sifirla(); hesapla(); toast("Kullanıcı verisi silindi"); render(); return;
    }
    if (e.target.id === "ice-uygula") {
      try { Store.iceAktarUygula(window.__iceHazir); hesapla(); toast("Yedek içe aktarıldı"); render(); }
      catch (er) { toast("İçe aktarılamadı: depolama alanı yetersiz."); }
      return;
    }
  });

  document.addEventListener("change", e => {
    const m = e.target.closest("[data-made]");
    if (m) {
      Store.uretildiAyarla(m.dataset.made, m.checked);
      const art = m.closest("article.scene"); if (art) art.classList.toggle("done", m.checked);
      return;
    }
    const a = e.target.closest("[data-ayar]");
    if (a) { Store.ayarAyarla(a.dataset.ayar, a.value); const y = scrollY; render(); scrollTo(0, y); return; }
    const up = e.target.closest("[data-upload]");
    if (up && up.files[0]) { gorselYukle(up.files[0], up.dataset.upload); return; }
    if (e.target.id === "ice" && e.target.files[0]) {
      const fr = new FileReader();
      fr.onload = () => {
        const out = $("#ice-sonuc");
        try {
          const h = Store.iceAktarHazirla(fr.result);
          const deneme = KasaDefter.build(D, h.durum.islemler.filter(x => !x.no || (EP.has(x.no) && x.no >= 5)));
          h.durum.islemler = h.durum.islemler.filter(x => (!x.no || (EP.has(x.no) && x.no >= 5)) && D.tipler[x.tip] && x.tip !== "acilis");
          if (deneme.eksi) throw new Error("Yedekteki işlemler kasayı eksiye düşürüyor; dosya uygulanmadı.");
          window.__iceHazir = h;
          out.innerHTML = `<div class="note"><b>Dosya geçerli.</b> ${h.durum.islemler.length} işlem, ${h.durum.uretildi.length} üretildi işareti, ${Object.keys(h.durum.notlar).length} not, ${Object.keys(h.gorseller).length} görsel.${h.atlanan ? " " + h.atlanan + " geçersiz ya da mükerrer işlem atlandı." : ""}</div><button class="btn gold" id="ice-uygula" type="button">Mevcut verinin yerine uygula</button>`;
        } catch (er) { out.innerHTML = `<p class="form-err">${esc(er.message)}</p>`; }
        e.target.value = "";
      };
      fr.readAsText(e.target.files[0]);
    }
  });

  let notT = 0;
  document.addEventListener("input", e => {
    const n = e.target.closest("[data-note]");
    if (n) { clearTimeout(notT); notT = setTimeout(() => Store.notAyarla(n.dataset.note, n.value.trim()), 350); return; }
    if (e.target.id === "iletisim") { clearTimeout(notT); notT = setTimeout(() => Store.ayarAyarla("iletisim", e.target.value.trim()), 350); }
  });

  document.addEventListener("submit", e => {
    if (e.target.id === "islem-form") {
      e.preventDefault();
      const btn = e.target.querySelector("button[type=submit]");
      if (btn.disabled) return;
      btn.disabled = true;
      try { islemEkle(e.target); } finally { const b2 = $("#islem-form button[type=submit]"); if (b2) b2.disabled = false; }
      return;
    }
    if (e.target.id === "serbest-form") {
      e.preventDefault();
      const a = tutarOku(e.target.a.value) ?? (String(e.target.a.value).trim() === "0" ? 0 : null);
      const b = tutarOku(e.target.b.value) ?? (String(e.target.b.value).trim() === "0" ? 0 : null);
      const out = $("#serbest-sonuc");
      if (a == null || b == null) { out.innerHTML = `<p class="form-err">İki bakiyeyi de tam lira olarak yaz.</p>`; return; }
      out.innerHTML = promptKutu("serbest", kasaPrompt(a, b), a === b ? "Sabit kasa prompt'u" : (b > a ? "Artış prompt'u (" : "Azalış prompt'u (") + (a === b ? "" : isaretli(b - a) + ")"));
      const d = out.querySelector("details"); if (d) d.open = true;
    }
  });

  document.addEventListener("toggle", e => {
    const d = e.target;
    if (!d || d.tagName !== "DETAILS" || !d.open || !d.dataset.pid) return;
    const pre = d.querySelector("pre");
    if (pre && !pre.textContent) pre.textContent = PROMPTS.get(d.dataset.pid) || "";
  }, true);

  document.addEventListener("keydown", e => { if (e.key === "Escape") menuKapat(); });
  window.addEventListener("hashchange", render);
  window.addEventListener("storage", ev => { if (ev.key && ev.key.startsWith("jozh-studios")) { Store.yukle(); hesapla(); render(); } });

  // test ve hata ayıklama için
  window.JOZH = { sahnePrompt, sadePrompt, kapakPrompt, defter: () => DEF, sahneBakiye: () => SB, EP };
  render();
})();
