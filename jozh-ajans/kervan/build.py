# -*- coding: utf-8 -*-
"""Kervan üretim sayfasını derler: yayin/kervan.html

Kullanım:
  python3 build.py          50 bölümün hepsi yazılmış olmalı
  python3 build.py kismi    yalnızca yazılmış bölümleri derler (diğerleri "hazırlanıyor" görünür)
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import bolumler  # noqa: E402
import model  # noqa: E402
import sablonlar  # noqa: E402
from karakterler import K, YAN, referans_prompt, tarif  # noqa: E402
from rota import ROTA  # noqa: E402

MOTOR = os.path.join(HERE, "..", "..", "icerik", "dedemin-defteri", "kasa", "kasa-motor.js")
SABLON = os.path.join(HERE, "sablon.html")
CIKTI = os.path.join(HERE, "yayin", "kervan.html")

ROL_TR = {"HOOK": "Kanca", "ARRIVAL": "Varış", "TRADE": "Ticaret", "CRISIS": "Kriz", "SECRET": "Sır",
          "CLIFFHANGER": "Cliffhanger"}

KARAKTER_TR = [
    ("kerem", "Kerem", "20 · gezi şirketi", "Defteri okur, yolu bulur. Hardal ceket, boynunda pirinç pusula."),
    ("defne", "Defne", "19 · dükkân ve kasa", "Pazarlık ve hesap ustası. Bordo kapüşonlu, altın gözlük, kulağında kalem."),
    ("kaan", "Kaan", "18 · kafe", "Lezzet tutkunu, komik, aceleci. Ters lacivert şapka, turuncu tişört, tahta kaşık."),
    ("sahaf", "Sahaf", "70'li yaşlar · yan karakter", "Kapalıçarşı'daki sahaf. Gümüş topuz, zincirli gözlük, yeşil hırka."),
]

BIYO = ("Üç genç, tek bir hayal ✨\n"
        "Ellerinde bir defter, önlerinde bütün Türkiye 🐪\n"
        "Kâr da var, zarar da, sır da…\n"
        "Yeni bölümler yolda 👇")


def bolum_verisi(e):
    p = model.promptlar(e)
    senaryolar = []
    for i, (s, prompt) in enumerate(zip(e["senaryolar"], p["senaryolar"]), 1):
        senaryolar.append(dict(
            kod="B%02d-S%02d" % (e["no"], i), n=i, rol=ROL_TR[s["rol"]],
            sure="%d:%02d–%d:%02d" % (divmod((i - 1) * 8, 60) + divmod(i * 8, 60)),
            prompt=prompt, replik=list(s["replik"]) if s["replik"] else None, altyazi=s["altyazi"],
            kasa=list(s["kasa"]) if s["kasa"] else None, gizli=i < e["kasa_baslar"]))
    return dict(
        no=e["no"], sehir=e["sehir"], bolge=e["bolge"], baslik=e["baslik"], kasa_bas=e["kasa_bas"],
        kasa_son=e["kasa_son"], aciklama=e["aciklama"] + "\n\n" + " ".join(e["etiketler"]),
        kapak1=p["kapak1"], kapak2=p["kapak2"],
        sabit=[dict(deger=d, sahneler=n) for d, n in model.sabit_kasalar(e)],
        senaryolar=senaryolar)


def veri(eps):
    yazili = {e["no"]: bolum_verisi(e) for e in eps}
    return dict(
        rota=[dict(no=r["no"], sehir=r["sehir"], bolge=r["bolge"], baslik=r["baslik"], alinan=r["alinan"],
                   satilan=r["satilan"], kasa_bas=r["kasa_bas"], kasa_son=r["kasa_son"], aksilik=r["aksilik"],
                   ipucu=r["ipucu"], son=r["son"], hazir=r["no"] in yazili) for r in ROTA],
        bolumler=yazili,
        karakterler=[dict(ad=ad, isim=isim, alt=alt, ozet=ozet, tarif=tarif(ad),
                          referans=referans_prompt(ad) if ad in K else None)
                     for ad, isim, alt, ozet in KARAKTER_TR if ad in K or ad in YAN],
        profil=dict(kullanici="kervan.dizi", ad="Kervan", biyo_ig=BIYO,
                    biyo_tt="\n".join(BIYO.split("\n")[:2]), foto=sablonlar.profil_prompt()),
    )


def main():
    tam = "kismi" not in sys.argv
    eps = bolumler.yukle()
    hatalar = model.denetle(eps, tam=tam)
    if hatalar:
        print("DENETİM BAŞARISIZ:")
        for h in hatalar:
            print("  - " + h)
        return 1
    with io.open(SABLON, encoding="utf-8") as fh:
        html = fh.read()
    with io.open(MOTOR, encoding="utf-8") as fh:
        motor = fh.read()
    js = json.dumps(veri(eps), ensure_ascii=False, indent=1).replace("</", "<\\/").replace("<!--", "\\u003c!--")
    html = html.replace("/*__VERI__*/", js).replace("/*__KASA_MOTOR__*/", motor)
    os.makedirs(os.path.dirname(CIKTI), exist_ok=True)
    with io.open(CIKTI, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("yazıldı: %s (%d bölüm, %.0f KB)" % (os.path.relpath(CIKTI, HERE), len(eps), len(html.encode()) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
