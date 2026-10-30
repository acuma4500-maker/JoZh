# -*- coding: utf-8 -*-
"""Sahne veri yardımcıları.

EP(no, misafir, yerler, sahneler)
  misafir : {id: (ad, ingilizce_gorunum, ingilizce_ses)}  -> sadece o bölümde görünen konuk karakterler
  yerler  : {anahtar: (turkce_mekan_adi, ingilizce_mekan_tarifi)}
  sahneler: 6 adet S(...)

S(tr, yer, kim, en, dlg, kam=None, k=None, kurgu=None)
  tr    : sahnede ne olduğu (Türkçe, kullanıcı için)
  yer   : yerler sözlüğündeki anahtar
  kim   : sahnede görünen karakter id'leri ('~ayse' = sadece telefondan sesi duyulur)
  en    : olayın İngilizce anlatımı (Flow prompt'una gider)
  dlg   : [(konuşan_id, "Türkçe replik"), ...]
  kam   : kamera (boşsa sahne sırasına göre varsayılan kullanılır)
  k     : kasa olayı: "s" = satış bu sahnede, "a" = alış bu sahnede
  kurgu : kurgu notu (ekrana yazı, telefon mesajı vb. - Flow'a gitmez)
"""

EPS = {}


def S(tr, yer, kim, en, dlg=(), kam=None, k=None, kurgu=None):
    return dict(tr=tr, yer=yer, kim=list(kim), en=en, dlg=list(dlg), kam=kam, k=k, kurgu=kurgu)


def EP(no, misafir, yerler, sahneler):
    assert len(sahneler) == 6, "Bölüm %d: 6 sahne olmalı" % no
    assert no not in EPS, "Bölüm %d iki kez tanımlandı" % no
    EPS[no] = dict(no=no, misafir=misafir, yerler=yerler, sahneler=sahneler)
