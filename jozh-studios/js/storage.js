/* JOZH STUDIOS · Veri saklama (LocalStorage), JSON dışa / içe aktarma.
   Senaryo içerikleri data.js'te sabittir ve değişmez; burada yalnızca kullanıcının verisi tutulur:
   eklediği kasa işlemleri, "üretildi" işaretleri, notlar, kasa prompt ayarları ve yüklediği kapak görselleri. */
(function (global) {
  "use strict";

  const KEY = "jozh-studios:v1";
  const IMG_KEY = "jozh-studios:gorsel:v1";
  const UYGULAMA = "JOZH STUDIOS · 81 Şehir";
  const BOS = () => ({ surum: 1, islemler: [], uretildi: [], notlar: {}, ayar: { birim: "TL", gecis: "akici", etiket: "var", iletisim: "" }, guncelleme: 0 });

  let durum = BOS();
  let gorsel = {};
  let kalici = true;

  function oku(key) {
    try { const t = localStorage.getItem(key); return t ? JSON.parse(t) : null; } catch (e) { kalici = false; return null; }
  }
  function yaz(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); return true; }
    catch (e) { if (e && (e.name === "QuotaExceededError" || e.code === 22)) throw new Error("KOTA"); kalici = false; return false; }
  }

  function temizIslem(x) {
    if (!x || typeof x !== "object") return null;
    const tutar = Number(x.tutar);
    if (!Number.isInteger(tutar) || tutar <= 0 || tutar > 999999999) return null;
    if (typeof x.tip !== "string") return null;
    return {
      id: String(x.id || ""), no: Number.isInteger(Number(x.no)) ? Number(x.no) : 0,
      sahne: Math.min(6, Math.max(1, Number(x.sahne) || 6)), tip: x.tip, tutar: tutar,
      aciklama: String(x.aciklama || "").slice(0, 300), olusturma: Number(x.olusturma) || Date.now()
    };
  }

  function normalize(d) {
    const o = BOS();
    if (!d || typeof d !== "object") return o;
    const ids = new Set();
    (Array.isArray(d.islemler) ? d.islemler : []).forEach(x => {
      const t = temizIslem(x);
      if (t && t.id && !ids.has(t.id)) { ids.add(t.id); o.islemler.push(t); }
    });
    o.uretildi = [...new Set((Array.isArray(d.uretildi) ? d.uretildi : []).filter(x => typeof x === "string"))];
    if (d.notlar && typeof d.notlar === "object") Object.keys(d.notlar).forEach(k => { if (typeof d.notlar[k] === "string") o.notlar[k] = d.notlar[k].slice(0, 5000); });
    if (d.ayar && typeof d.ayar === "object") {
      if (d.ayar.birim === "₺") o.ayar.birim = "₺";
      if (d.ayar.gecis === "anlik") o.ayar.gecis = "anlik";
      if (d.ayar.etiket === "yok") o.ayar.etiket = "yok";
      if (typeof d.ayar.iletisim === "string") o.ayar.iletisim = d.ayar.iletisim.slice(0, 200);
    }
    o.guncelleme = Number(d.guncelleme) || 0;
    return o;
  }

  function yukle() {
    durum = normalize(oku(KEY));
    const g = oku(IMG_KEY);
    gorsel = g && typeof g === "object" ? g : {};
    return durum;
  }

  function kaydet() {
    durum.guncelleme = Date.now();
    return yaz(KEY, durum);
  }

  const Store = {
    get durum() { return durum; },
    get gorsel() { return gorsel; },
    get kalici() { return kalici; },
    yukle, kaydet,
    yeniId() { return "u-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 8); },

    islemEkle(t) {
      durum.islemler.push(t);
      try { kaydet(); } catch (e) { durum.islemler.pop(); throw e; }
    },
    islemSil(id) {
      const i = durum.islemler.findIndex(x => x.id === id);
      if (i < 0) return false;
      const eski = durum.islemler.splice(i, 1)[0];
      try { kaydet(); } catch (e) { durum.islemler.splice(i, 0, eski); throw e; }
      return true;
    },
    uretildiMi(id) { return durum.uretildi.includes(id); },
    uretildiAyarla(id, v) {
      const s = new Set(durum.uretildi);
      v ? s.add(id) : s.delete(id);
      durum.uretildi = [...s];
      kaydet();
    },
    notAyarla(no, metin) { if (metin) durum.notlar[no] = metin; else delete durum.notlar[no]; kaydet(); },
    ayarAyarla(k, v) { durum.ayar[k] = v; kaydet(); },

    gorselAyarla(k, dataUrl) {
      const eski = gorsel[k];
      if (dataUrl) gorsel[k] = dataUrl; else delete gorsel[k];
      try { yaz(IMG_KEY, gorsel); }
      catch (e) { if (eski) gorsel[k] = eski; else delete gorsel[k]; throw e; }
    },

    disaAktar(gorselDahil) {
      return JSON.stringify({ uygulama: UYGULAMA, surum: 1, tarih: new Date().toISOString(), durum: durum,
                              gorseller: gorselDahil ? gorsel : {} }, null, 2);
    },

    /* İçe aktarma: dosyayı doğrular, normalize eder; onay için özet döner. uygula() ile yazılır. */
    iceAktarHazirla(metin) {
      let j;
      try { j = JSON.parse(metin); } catch (e) { throw new Error("Dosya geçerli bir JSON değil."); }
      if (!j || typeof j !== "object" || !j.durum) throw new Error("Bu dosya bir JOZH STUDIOS yedeği değil (\"durum\" alanı yok).");
      if (j.uygulama && j.uygulama !== UYGULAMA) throw new Error("Bu yedek başka bir uygulamaya ait: " + j.uygulama);
      const ham = Array.isArray(j.durum.islemler) ? j.durum.islemler.length : 0;
      const yeni = normalize(j.durum);
      const g = j.gorseller && typeof j.gorseller === "object" ? j.gorseller : {};
      const gTemiz = {};
      Object.keys(g).forEach(k => { if (typeof g[k] === "string" && g[k].startsWith("data:image/")) gTemiz[k] = g[k]; });
      return { durum: yeni, gorseller: gTemiz, atlanan: ham - yeni.islemler.length };
    },
    iceAktarUygula(h) {
      const eskiD = durum, eskiG = gorsel;
      durum = h.durum;
      gorsel = Object.keys(h.gorseller).length ? h.gorseller : gorsel;
      try { kaydet(); yaz(IMG_KEY, gorsel); }
      catch (e) { durum = eskiD; gorsel = eskiG; try { kaydet(); yaz(IMG_KEY, gorsel); } catch (e2) {} throw e; }
    },
    sifirla() { durum = BOS(); gorsel = {}; kaydet(); yaz(IMG_KEY, gorsel); }
  };

  global.Store = Store;
})(window);
