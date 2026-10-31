# -*- coding: utf-8 -*-
"""Sahne veri yardımcıları. Kurallar için BIBLE.md'ye bak.

EP(no, misafir, yerler, sahneler, hava="açık", kasa=None, kasa_baslar=0, kapak=None, son=None)
  misafir    : {id: (ad, ingilizce_gorunum, ingilizce_ses)}  sadece bu bölümde görünen konuklar
  yerler     : {anahtar: (turkce_ad, ingilizce_tarif)}
  hava       : dış çekimlerin varsayılan havası (HAVA anahtarlarından biri)
  kasa       : kasa olaylarının sahne indeksleri, örn. dict(y=0, s=1, m=2, a=4)
  kasa_baslar: kasa göstergesinin ilk göründüğü sahne indeksi (sadece B4'te 3)
  kapak      : (yer_anahtari, [karakterler], ingilizce_kompozisyon, turkce_aciklama)
  son        : (opsiyonel) bölüm sonu metnini geçersiz kılar

S(z, yer, kim, tr, en, dlg=(), kam="", kurgu=None, h=None, fb=False, et=None, basit=None)
  z    : "07:10 şafak" (saat + evre). Anı sahnesinde sadece evre: "anı-gece".
  yer  : yerler sözlüğündeki anahtar
  kim  : görünen karakterler. "~ayse" = sadece sesi duyulur.
  tr   : Türkçe özet (ne olur, neden, hangi saat/yer bağlantısıyla)
  en   : tek çekimlik İngilizce eylem
  dlg  : [(konuşan, "Türkçe replik"), (konuşan, "replik", "ton")]
  kam  : tek hareketli kamera tarifi (İngilizce)
  h    : bu sahne için hava (HAVA anahtarı)
  fb   : anı sahnesi (saat sırası kontrolü yapılmaz)
  et   : ekran yazısı için yer adı (kurguda eklenir); ilk sahnede otomatik
  basit: yeniden deneme prompt'u için tek cümlelik eylem (boşsa en'in ilk cümlesi)
"""

EPS = {}

FAZLAR = ["şafak", "sabah", "öğle", "ikindi", "gün batımı", "akşam", "gece",
          "iç-gündüz", "iç-gece", "anı-gündüz", "anı-gece"]
HAVALAR = ["açık", "ılık", "bulutlu", "yağmur", "kar", "tipi", "sis", "rüzgar"]


def faz_of(z):
    parts = z.split(None, 1)
    return parts[1] if ":" in parts[0] and len(parts) > 1 else z.strip()


def S(z, yer, kim, tr, en, dlg=(), kam="", kurgu=None, h=None, fb=False, et=None, basit=None):
    assert kam, "kamera zorunlu: " + tr[:40]
    faz = faz_of(z)
    assert faz in FAZLAR, "bilinmeyen evre '%s' (%s)" % (faz, tr[:40])
    if h is not None:
        assert h in HAVALAR, "bilinmeyen hava '%s'" % h
    return dict(z=z, yer=yer, kim=list(kim), tr=tr, en=en, dlg=[tuple(d) for d in dlg], kam=kam,
                kurgu=kurgu, h=h, fb=fb, et=et, basit=basit)


def EP(no, misafir, yerler, sahneler, hava="açık", kasa=None, kasa_baslar=0, kapak=None, son=None):
    assert len(sahneler) == 6, "Bölüm %d: 6 sahne olmalı" % no
    assert no not in EPS, "Bölüm %d iki kez tanımlandı" % no
    assert hava in HAVALAR, "Bölüm %d: bilinmeyen hava" % no
    assert kapak, "Bölüm %d: kapak zorunlu" % no
    for s in sahneler:
        assert s["yer"] in yerler, "Bölüm %d: bilinmeyen yer '%s'" % (no, s["yer"])
    assert kapak[0] in yerler, "Bölüm %d: kapak yeri bilinmiyor" % no
    EPS[no] = dict(no=no, misafir=misafir, yerler=yerler, sahneler=sahneler, hava=hava,
                   kasa=kasa or {}, kasa_baslar=kasa_baslar, kapak=kapak, son=son)
