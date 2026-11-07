# -*- coding: utf-8 -*-
"""Kervan — bölüm veri modeli ve denetimler."""
from rota import ROTA
from karakterler import K, YAN
import sablonlar

TOPLAM = 50


def para(n):
    return format(n, ",").replace(",", ".") + " ₺"


def S(rol, kimler, mekan, aksiyon, kamera, ses, duygu, replik=None, altyazi="", kasa=None):
    """Bir senaryo. kasa: (eski, yeni) ya da None. replik: (konuşan, 'metin') ya da None."""
    return dict(rol=rol, kimler=list(kimler), mekan=mekan, aksiyon=tuple(aksiyon), kamera=kamera, ses=ses,
                duygu=duygu, replik=replik, altyazi=altyazi, kasa=kasa)


def EP(no, aciklama, etiketler, kapak, senaryolar, kasa_baslar=1, soguk=None):
    """Bir bölüm. Başlık, yer, bölge ve kasa rakamları rota.py'den gelir.
    kasa_baslar: kasa göstergesinin ilk göründüğü senaryo (1–15)."""
    r = ROTA[no - 1]
    if soguk is None:
        soguk = r["bolge"] == "Doğu Anadolu"
    return dict(r, aciklama=aciklama, etiketler=list(etiketler), kapak=dict(kapak), senaryolar=list(senaryolar),
                kasa_baslar=kasa_baslar, soguk=soguk)


def sabit_kasalar(e):
    """Para değişmeyen senaryolar için sabit kasa değerleri: [(değer, [senaryo no, ...]), ...]."""
    out, deger = [], e["kasa_bas"]
    for i, s in enumerate(e["senaryolar"], 1):
        if s["kasa"]:
            deger = s["kasa"][1]
            continue
        if i < e["kasa_baslar"]:
            continue
        if out and out[-1][0] == deger:
            out[-1][1].append(i)
        else:
            out.append((deger, [i]))
    return out


def promptlar(e):
    """Bölümün bütün Flow promptları."""
    k = e["kapak"]
    kargs = dict(no=e["no"], baslik=e["baslik"], ana=k["ana"], yanlar=k["yanlar"], mekan=k["mekan"],
                 kompozisyon=k["kompozisyon"], duygu=k["duygu"], soguk=e["soguk"])
    return dict(
        kapak1=sablonlar.kapak1(**kargs),
        kapak2=sablonlar.kapak2(**kargs),
        senaryolar=[sablonlar.senaryo(no=i, rol=s["rol"], kimler=s["kimler"], mekan=s["mekan"],
                                      aksiyon=s["aksiyon"], kamera=s["kamera"], replik=s["replik"], ses=s["ses"],
                                      duygu=s["duygu"], soguk=e["soguk"])
                    for i, s in enumerate(e["senaryolar"], 1)],
    )


def denetle(bolumler, tam):
    """Hata mesajları listesi; boş liste = geçti."""
    h = []
    if tam and [e["no"] for e in bolumler] != list(range(1, TOPLAM + 1)):
        h.append("tam derleme için %d bölüm gerekli, %d var" % (TOPLAM, len(bolumler)))
    for e in bolumler:
        b = "B%02d" % e["no"]
        sc = e["senaryolar"]
        if len(sc) != 15:
            h.append("%s: %d senaryo (15 olmalı)" % (b, len(sc)))
            continue
        if sc[0]["rol"] != "HOOK" or sc[-1]["rol"] != "CLIFFHANGER":
            h.append("%s: ilk senaryo HOOK, son senaryo CLIFFHANGER olmalı" % b)
        if not 1 <= e["kasa_baslar"] <= 15:
            h.append("%s: kasa_baslar 1–15 arası olmalı" % b)
        deger = e["kasa_bas"]
        for i, s in enumerate(sc, 1):
            for ad in s["kimler"]:
                if ad not in K and ad not in YAN:
                    h.append("%s-S%02d: bilinmeyen karakter %s" % (b, i, ad))
            if s["kasa"]:
                if i < e["kasa_baslar"]:
                    h.append("%s-S%02d: kasa göstergesi başlamadan kasa olayı" % (b, i))
                eski, yeni = s["kasa"]
                if eski != deger:
                    h.append("%s-S%02d: kasa %s olmalıydı, %s yazılmış" % (b, i, para(deger), para(eski)))
                if yeni <= 0 or yeni == eski:
                    h.append("%s-S%02d: geçersiz kasa değişimi" % (b, i))
                deger = yeni
        if deger != e["kasa_son"]:
            h.append("%s: bölüm %s ile bitmeli, %s ile bitiyor" % (b, para(e["kasa_son"]), para(deger)))
        if len(e["aciklama"]) > 2200:
            h.append("%s: açıklama 2200 karakteri geçiyor" % b)
        if "#Kervan" not in e["etiketler"]:
            h.append("%s: #Kervan etiketi yok" % b)
        try:
            promptlar(e)
        except (ValueError, KeyError) as ex:
            h.append("%s: prompt üretilemedi: %s" % (b, ex))
    for a, c in zip(bolumler, bolumler[1:]):
        if c["no"] != a["no"] + 1:
            h.append("B%02d'den sonra B%02d geliyor" % (a["no"], c["no"]))
    return h
