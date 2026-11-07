# -*- coding: utf-8 -*-
"""Bölüm dosyalarının ortak kısaltmaları."""
from karakterler import KAMYONET  # noqa: F401
from model import EP, S  # noqa: F401
from rota import ROTA

EKIP = ["kerem", "defne", "kaan"]
VAN = KAMYONET


def s(rol, kim, mekan, aksiyon, kamera, ses, duygu, r=None, alt="", k=None):
    """Kısa senaryo yazımı: r=(konuşan, replik), alt=altyazı, k=(eski, yeni) kasa."""
    return S(rol, kim, mekan, aksiyon, kamera, ses, duygu, replik=r, altyazi=alt, kasa=k)


def ac(no, emoji, metin, soru):
    """Video açıklaması (başlık rota.py'den)."""
    baslik = " ".join(w[:1] + w[1:].replace("I", "ı").replace("İ", "i").lower()
                      for w in ROTA[no - 1]["baslik"].split())
    sonraki = "Bölüm %d yolda 🐪" % (no + 1) if no < 50 else "Sezon 2 yolda 🐪"
    return "Bölüm %d: %s %s\n\n%s\n\n%s 👇\nTakip et, yolculuğu kaçırma. %s" % (no, baslik, emoji, metin, soru, sonraki)


def et(no, *yer):
    return ["#Kervan", "#KervanBölüm%d" % no, "#animasyon", "#dizi"] + ["#" + y for y in yer] + \
        ["#macera", "#gizem", "#ticaret", "#keşfet", "#reels"]


def kapak(ana, yanlar, mekan, kompozisyon, duygu):
    return dict(ana=ana, yanlar=yanlar, mekan=mekan, kompozisyon=kompozisyon, duygu=duygu)
