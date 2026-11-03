# -*- coding: utf-8 -*-
"""Ortak yapı taşları: bölgeler, iller, sahne (S) ve bölüm (EP) tanımı, işlem (T) tanımı.

S(z, yer, kim, ad, tr, en, dlg=(), kam="", t=None, h=None, kurgu=None, fb=False, ic=None)
  z    : "09:10 sabah" (saat + evre)
  yer  : bölümün yerler sözlüğündeki anahtar
  kim  : görünen karakterler; "~hatice" = sadece sesi duyulur (telefon)
  ad   : sahne başlığı (kartta "SAHNE 01 – ..." olarak görünür)
  tr   : Türkçe sahne açıklaması
  en   : İngilizce eylem (tek çekim, 10 saniye)
  dlg  : [(konuşan, "Türkçe replik", "ton")]
  kam  : tek kamera hareketi (İngilizce)
  t    : kasa işlemi ya da işlem listesi: T(...)
  h    : bu sahnenin havası (HAVA anahtarı); yoksa bölüm havası
Para etiketleri: {tx} bu sahnenin ilk işlem tutarı, {adet}, {fiyat}. Diyalogda yazıya, açıklamada rakama çevrilir.
"""

BOLGELER = [
    # id, ad, sezon no, renk
    ("dogu", "Doğu Anadolu Bölgesi", 1),
    ("guneydogu", "Güneydoğu Anadolu Bölgesi", 2),
    ("akdeniz", "Akdeniz Bölgesi", 3),
    ("ege", "Ege Bölgesi", 4),
    ("marmara", "Marmara Bölgesi", 5),
    ("karadeniz", "Karadeniz Bölgesi", 6),
    ("icanadolu", "İç Anadolu Bölgesi", 7),
]

# Resmî coğrafi bölgelere göre 81 il (plaka, ad, bölge). Rota sırası sezon dosyalarındadır.
ILLER = {
    1: ("Adana", "akdeniz"), 2: ("Adıyaman", "guneydogu"), 3: ("Afyonkarahisar", "ege"), 4: ("Ağrı", "dogu"),
    5: ("Amasya", "karadeniz"), 6: ("Ankara", "icanadolu"), 7: ("Antalya", "akdeniz"), 8: ("Artvin", "karadeniz"),
    9: ("Aydın", "ege"), 10: ("Balıkesir", "marmara"), 11: ("Bilecik", "marmara"), 12: ("Bingöl", "dogu"),
    13: ("Bitlis", "dogu"), 14: ("Bolu", "karadeniz"), 15: ("Burdur", "akdeniz"), 16: ("Bursa", "marmara"),
    17: ("Çanakkale", "marmara"), 18: ("Çankırı", "icanadolu"), 19: ("Çorum", "karadeniz"), 20: ("Denizli", "ege"),
    21: ("Diyarbakır", "guneydogu"), 22: ("Edirne", "marmara"), 23: ("Elazığ", "dogu"), 24: ("Erzincan", "dogu"),
    25: ("Erzurum", "dogu"), 26: ("Eskişehir", "icanadolu"), 27: ("Gaziantep", "guneydogu"), 28: ("Giresun", "karadeniz"),
    29: ("Gümüşhane", "karadeniz"), 30: ("Hakkari", "dogu"), 31: ("Hatay", "akdeniz"), 32: ("Isparta", "akdeniz"),
    33: ("Mersin", "akdeniz"), 34: ("İstanbul", "marmara"), 35: ("İzmir", "ege"), 36: ("Kars", "dogu"),
    37: ("Kastamonu", "karadeniz"), 38: ("Kayseri", "icanadolu"), 39: ("Kırklareli", "marmara"), 40: ("Kırşehir", "icanadolu"),
    41: ("Kocaeli", "marmara"), 42: ("Konya", "icanadolu"), 43: ("Kütahya", "ege"), 44: ("Malatya", "dogu"),
    45: ("Manisa", "ege"), 46: ("Kahramanmaraş", "akdeniz"), 47: ("Mardin", "guneydogu"), 48: ("Muğla", "ege"),
    49: ("Muş", "dogu"), 50: ("Nevşehir", "icanadolu"), 51: ("Niğde", "icanadolu"), 52: ("Ordu", "karadeniz"),
    53: ("Rize", "karadeniz"), 54: ("Sakarya", "marmara"), 55: ("Samsun", "karadeniz"), 56: ("Siirt", "guneydogu"),
    57: ("Sinop", "karadeniz"), 58: ("Sivas", "icanadolu"), 59: ("Tekirdağ", "marmara"), 60: ("Tokat", "karadeniz"),
    61: ("Trabzon", "karadeniz"), 62: ("Tunceli", "dogu"), 63: ("Şanlıurfa", "guneydogu"), 64: ("Uşak", "ege"),
    65: ("Van", "dogu"), 66: ("Yozgat", "icanadolu"), 67: ("Zonguldak", "karadeniz"), 68: ("Aksaray", "icanadolu"),
    69: ("Bayburt", "karadeniz"), 70: ("Karaman", "icanadolu"), 71: ("Kırıkkale", "icanadolu"), 72: ("Batman", "guneydogu"),
    73: ("Şırnak", "guneydogu"), 74: ("Bartın", "karadeniz"), 75: ("Ardahan", "dogu"), 76: ("Iğdır", "dogu"),
    77: ("Yalova", "marmara"), 78: ("Karabük", "karadeniz"), 79: ("Kilis", "guneydogu"), 80: ("Osmaniye", "akdeniz"),
    81: ("Düzce", "karadeniz"),
}
ILLER_AD = {v[0]: k for k, v in ILLER.items()}

FAZLAR = ["şafak", "sabah", "öğle", "ikindi", "gün batımı", "akşam", "gece", "iç-gündüz", "iç-gece", "anı-gündüz"]
HAVALAR = ["açık", "sıcak", "nemli", "ılık", "serin", "bulutlu", "yağmur", "sis", "rüzgar", "kar"]

TIPLER = {
    # tip: (Türkçe ad, işaret, grup)
    "acilis": ("Kasa açılışı (sermaye)", +1, "acilis"),
    "alis": ("Ürün alımı", -1, "alis"),
    "satis": ("Ürün satışı", +1, "satis"),
    "sponsor": ("Sponsorluk geliri", +1, "gelir"),
    "ulasim": ("Ulaşım gideri", -1, "gider"),
    "konaklama": ("Konaklama gideri", -1, "gider"),
    "yemek": ("Yemek gideri", -1, "gider"),
    "diger_gelir": ("Diğer gelir", +1, "gelir"),
    "diger_gider": ("Diğer gider", -1, "gider"),
    "borc": ("Borç ödemesi (Cemil Bey)", -1, "borc"),
}

EPS = {}


def T(tip, tutar, aciklama, adet=None, birim=None, fiyat=None):
    """Kasa işlemi. Birim fiyatlı alım/satışta tutar=None verip adet ve fiyat yaz; tutar hesaplanır."""
    assert tip in TIPLER, "bilinmeyen işlem tipi: " + tip
    if tutar is None:
        assert adet and fiyat, "tutar yoksa adet ve fiyat zorunlu"
        tutar = adet * fiyat
    if adet and fiyat:
        assert adet * fiyat == tutar, "adet x fiyat tutara eşit değil: %s" % aciklama
    assert isinstance(tutar, int) and tutar > 0, "tutar pozitif tam sayı olmalı: %s" % aciklama
    return dict(tip=tip, tutar=tutar, aciklama=aciklama, adet=adet, birim=birim, fiyat=fiyat)


def U(adet, birim, fiyat, tip, aciklama):
    """Kısa yol: U(150, "kg", 240, "alis", "Gün kurusu kayısı")."""
    return T(tip, None, aciklama, adet=adet, birim=birim, fiyat=fiyat)


def faz_of(z):
    parts = z.split(None, 1)
    return parts[1] if ":" in parts[0] and len(parts) > 1 else z.strip()


def S(z, yer, kim, ad, tr, en, dlg=(), kam="", t=None, h=None, kurgu=None, fb=False, ic=None):
    assert kam, "kamera zorunlu: " + ad
    faz = faz_of(z)
    assert faz in FAZLAR, "bilinmeyen evre '%s' (%s)" % (faz, ad)
    if h is not None:
        assert h in HAVALAR, "bilinmeyen hava '%s'" % h
    if t is None:
        tx = []
    elif isinstance(t, dict):
        tx = [t]
    else:
        tx = list(t)
    return dict(z=z, yer=yer, kim=list(kim), ad=ad, tr=tr, en=en, dlg=[tuple(d) for d in dlg], kam=kam,
                tx=tx, h=h, kurgu=kurgu, fb=fb)


def EP(no, sehir, baslik, ozet, hikaye, yerler, sahneler, misafir=None, hava="açık", ay="",
       kapak=None, yakinda=None, tiktok="", ig="", tags=(), son="", teaser="", kiyafet="temel", sponsor=None, urun=""):
    """sehir: il adı (şehir bölümleri) ya da None (başlangıç videoları).
    kapak / yakinda: (yer_anahtari, [karakterler], ingilizce_kompozisyon, turkce_aciklama)"""
    assert len(sahneler) == 6, "Bölüm %d: 6 sahne olmalı" % no
    assert no not in EPS, "Bölüm %d iki kez tanımlandı" % no
    assert hava in HAVALAR, "Bölüm %d: bilinmeyen hava" % no
    assert kapak and yakinda, "Bölüm %d: kapak ve pek yakında kapağı zorunlu" % no
    assert tiktok and ig and son and teaser, "Bölüm %d: sosyal medya metinleri ve bölüm sonu zorunlu" % no
    assert len(tags) >= 2, "Bölüm %d: en az 2 özel hashtag" % no
    if sehir is not None:
        assert sehir in ILLER_AD, "Bölüm %d: bilinmeyen il %s" % (no, sehir)
    for s in sahneler:
        assert s["yer"] in yerler, "Bölüm %d: bilinmeyen yer '%s'" % (no, s["yer"])
    for k in (kapak, yakinda):
        assert k[0] in yerler, "Bölüm %d: kapak yeri bilinmiyor" % no
    EPS[no] = dict(no=no, sehir=sehir, baslik=baslik, ozet=ozet, hikaye=hikaye, yerler=yerler, sahneler=sahneler,
                   misafir=misafir or {}, hava=hava, ay=ay, kapak=kapak, yakinda=yakinda, tiktok=tiktok, ig=ig,
                   tags=list(tags), son=son, teaser=teaser, kiyafet=kiyafet, sponsor=sponsor, urun=urun)


# ---------------------------------------------------------------- sayılar
B1 = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
B10 = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]


def _uc(n):
    y, o, b = n // 100, (n % 100) // 10, n % 10
    s = ""
    if y:
        s += ("" if y == 1 else B1[y] + " ") + "yüz "
    if o:
        s += B10[o] + " "
    if b:
        s += B1[b] + " "
    return s.strip()


def tr_sayi(n):
    if n == 0:
        return "sıfır"
    out = []
    m, b, r = n // 1000000, (n % 1000000) // 1000, n % 1000
    if m:
        out.append(_uc(m) + " milyon")
    if b:
        out.append(("" if b == 1 else _uc(b) + " ") + "bin")
    if r:
        out.append(_uc(r))
    return " ".join(out).strip()


def nokta_sayi(n):
    return "{:,}".format(n).replace(",", ".")
