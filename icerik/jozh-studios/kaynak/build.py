# -*- coding: utf-8 -*-
"""JOZH STUDIOS · 81 Şehir içeriklerini doğrular ve panelin veri dosyasını (../js/data.js) üretir.

Kullanım:  python3 jozh-studios/kaynak/build.py

Kontroller (biri bile tutmazsa derleme durur):
  - 87 bölüm (6 başlangıç + 81 il), her bölümde 6 sahne
  - 81 ilin her biri tam bir kez, doğru bölgede, sezon sırası bölge sırasıyla aynı
  - sahnede konuşan herkes sahnede, sahne saatleri ileri gidiyor, diyalog 10 saniyeye sığıyor
  - kasa hiçbir anda eksiye düşmüyor, borç taksitleri toplamı 800.000 TL
  - her para etiketi ({tx}, {adet}, {fiyat}) karşılığı olan bir işlemle kullanılıyor
"""
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from karakterler import K, NESNE  # noqa: E402
from ortak import (EPS, BOLGELER, ILLER, ILLER_AD, TIPLER, faz_of, tr_sayi, nokta_sayi)  # noqa: E402
import bible  # noqa: E402

MODULLER = ["v_baslangic", "s1_dogu", "s2_guneydogu", "s3_akdeniz", "s4_ege", "s5_marmara", "s6_karadeniz", "s7_icanadolu"]
KISMI = "kismi" in sys.argv
for _ad in MODULLER:
    try:
        importlib.import_module(_ad)
    except ModuleNotFoundError as e:
        if e.name != _ad or not KISMI:
            raise

BASLANGIC_KASA = 100000
BORC = 800000

# ---------------------------------------------------------------- sabit prompt parçaları (İngilizce)
SABIT = dict(
    format="Vertical 9:16 video, 1080x1920, 10 seconds, one continuous shot with no cuts.",
    stil=("Semi-realistic stylized 3D animation with Pixar-like proportions but realistic human anatomy; realistic skin, hair and fabric "
          "textures; highly detailed 3D characters placed in a photorealistic, cinematic real-world environment with realistic streets, "
          "buildings, materials and nature; film-quality cinematic lighting and lens work, shallow depth of field. A modern animated "
          "feature film look combined with real cinema. NOT a childish cartoon, no exaggerated cartoon physics."),
    background=("Simple and uncluttered with a clear foreground subject. Any other people stay few (at most three), far away and softly "
                "out of focus; no crowds of identical faces"),
    physics=("Natural human motion with realistic weight and balance, feet stay planted on the ground, hands grip objects firmly and hold "
             "one object at a time, boxes, crates, bags, money and glasses move with realistic weight, inertia and contact, cloth and hair "
             "react naturally, no sudden speed changes, no objects passing through bodies"),
    lipsync=("All speech is in natural, fluent Turkish. Exact lip synchronization with the spoken Turkish words; only the character who is "
             "speaking moves his or her mouth, everyone else keeps the mouth closed while listening. Off-screen voices move no visible lips. "
             "Lines are short, clear and unhurried"),
    avoid=("distorted or morphing faces, face changing between frames, extra or missing fingers, deformed hands, floating or duplicated "
           "objects, characters changing clothes or hairstyle, flickering light, sudden lighting changes, shaky camera, jump cuts, "
           "subtitles, captions, on-screen text, watermarks, logos, brand names, childish cartoon style"),
    kapak_stil=("Social media video cover image for TikTok and Instagram Reels, vertical 9:16, 1080x1920. Semi-realistic stylized 3D animation "
                "still with Pixar-like proportions, realistic skin, hair and fabric, photorealistic cinematic real-world background, dramatic "
                "cinematic lighting, rich but natural colors, very high detail, eye-catching. Keep faces and the main action inside the "
                "central square so the image still works when cropped to 1:1 or 4:5 in the profile grid. Leave the top 22% as clean, calm "
                "background for a title added later in editing. No text, no letters, no numbers, no logos, no watermark."),
    yakinda_stil=("'Coming soon' teaser poster image for TikTok and Instagram, vertical 9:16, 1080x1920. Semi-realistic stylized 3D animation "
                  "still with Pixar-like proportions, realistic textures and a photorealistic cinematic background. Mysterious, high-contrast "
                  "teaser mood: the key moment is only HINTED, partly hidden in shadow, backlight or silhouette, with a strong single light "
                  "source and a slightly darker color grade. Keep the faces recognizable and inside the central square. Leave the bottom 25% as "
                  "dark, clean, uncluttered space for the words 'PEK YAKINDA' added later in editing. No text, no letters, no numbers, "
                  "no logos, no watermark."),
)

FAZ = {
    "şafak": "Dawn, around {c}. The sun is just rising at the horizon, soft pink-orange light, long soft shadows, cool blue shade",
    "sabah": "Morning, around {c}. Clean bright sunlight at a low angle from camera-left, fresh morning air",
    "öğle": "Midday, around {c}. High sun, bright even daylight, short crisp shadows",
    "ikindi": "Afternoon, around {c}. Warm sunlight at a lowering angle from camera-right",
    "gün batımı": "Sunset, around {c}. Warm orange golden-hour light, long shadows, glowing sky",
    "akşam": "Early evening, around {c}. Deep blue dusk sky, street lamps and windows just lit, warm practical lights",
    "gece": "Night, around {c}. Dark sky, warm pools of light from lamps and windows, soft cool moonlight",
    "iç-gündüz": "Interior during the day, around {c}. Soft daylight through a window, warm ambient interior tones",
    "iç-gece": "Interior in the evening, around {c}. Warm lamp light, dark windows, soft natural shadows",
    "anı-gündüz": "Memory flashback in daytime. Warm, slightly golden, soft-focus look with a gentle faded film feel",
}
HAVA = {
    "açık": "Clear sky, crisp clean air",
    "sıcak": "Hot dry summer day, very bright sun, faint heat shimmer far in the distance, skin slightly glistening",
    "nemli": "Hot humid Mediterranean summer air, hazy bright sky",
    "ılık": "Mild sunny weather with a gentle breeze",
    "serin": "Cool fresh highland air, a few white clouds, light breeze",
    "bulutlu": "Overcast sky, soft diffused light, no hard shadows",
    "yağmur": "Light steady rain, wet ground reflecting the light, overcast sky",
    "sis": "Low mist drifting through the scene, soft diffused light",
    "rüzgar": "Windy, hair and clothes moving in the breeze",
    "kar": "Light snow falling, snow on the ground and rooftops, soft overcast light, visible breath in the cold air",
}
HAVA_TR = {"açık": "açık", "sıcak": "sıcak", "nemli": "nemli sıcak", "ılık": "ılık", "serin": "serin", "bulutlu": "bulutlu",
           "yağmur": "yağmurlu", "sis": "sisli", "rüzgar": "rüzgârlı", "kar": "karlı"}


# ---------------------------------------------------------------- yardımcılar
def tr_upper(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


def kelime(s):
    return len(re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîûÂÎÛ0-9]+", s))


def saat_dk(z):
    m = re.match(r"(\d\d):(\d\d)", z)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def doldur(s, T, mod, yer=""):
    def f(m):
        k = m.group(1)
        if k not in T or T[k] is None:
            raise KeyError("%s: {%s} için işlem yok" % (yer, k))
        v = T[k]
        if mod == "words":
            w = tr_sayi(v)
            onceki = m.string[:m.start()].rstrip()
            if (not onceki) or (onceki[-1] in ".!?" and not onceki.endswith("...")):
                w = tr_upper(w[0]) + w[1:]
            return w
        if mod == "en":
            return "{:,}".format(v)
        return nokta_sayi(v)
    return re.sub(r"\{(tx|adet|fiyat|tx2)\}", f, s)


def sahne_T(s):
    tx = s["tx"]
    T = dict(tx=None, adet=None, fiyat=None, tx2=None)
    if tx:
        T["tx"] = tx[0]["tutar"]
        T["adet"] = tx[0]["adet"]
        T["fiyat"] = tx[0]["fiyat"]
    if len(tx) > 1:
        T["tx2"] = tx[1]["tutar"]
    return T


def karakter_var(ep, cid):
    return cid in K or cid in ep["misafir"]


# ---------------------------------------------------------------- derleme
def derle():
    nolar = sorted(EPS)
    if not KISMI:
        assert nolar == list(range(1, 88)), "Eksik ya da fazla bölüm: %s" % sorted(set(range(1, 88)) ^ set(nolar))
    # --- il ve bölge kontrolü
    gorulen = {}
    for no in nolar:
        il = EPS[no]["sehir"]
        if il is None:
            assert no <= 6, "Bölüm %d: şehir bölümünde il yok" % no
            continue
        assert no >= 7, "Bölüm %d: başlangıç videosuna il bağlanmış" % no
        assert il not in gorulen, "%s iki kez: Bölüm %d ve %d" % (il, gorulen[il], no)
        gorulen[il] = no
    if not KISMI:
        assert len(gorulen) == 81, "81 il yerine %d il" % len(gorulen)
    # sezon/bölge sırası
    sezon_rota = {}
    for sz in bible.SEZONLAR:
        if sz["bolge"] is None:
            continue
        rota = sz["rota"]
        for il in rota:
            assert ILLER[ILLER_AD[il]][1] == sz["bolge"], "%s %s bölgesinde değil" % (il, sz["bolge"])
        sezon_rota[sz["bolge"]] = rota
    tum_rota = [il for b in [x[0] for x in BOLGELER] for il in sezon_rota.get(b, [])]
    if not KISMI:
        assert len(tum_rota) == 81 and len(set(tum_rota)) == 81
        sirali = [EPS[n]["sehir"] for n in range(7, 88)]
        assert sirali == [il for sz in bible.SEZONLAR if sz["bolge"] for il in sz["rota"]], "Bölüm sırası rota sırasıyla aynı değil"
    for b, rota in sezon_rota.items():
        n = sum(1 for il, (_, bb) in [(v[0], v) for v in ILLER.values()] if bb == b)
        assert len(rota) == n, "%s: rota %d il, bölgede %d il" % (b, len(rota), n)

    # --- bölümler
    kasa = None  # kasa Bölüm 4 sahne 6'da açılır
    borc_odenen = 0
    uyari = []
    bolumler = []
    for no in nolar:
        ep = EPS[no]
        yer = "Bölüm %d" % no
        son_dk = -1
        sahneler = []
        acilis = kasa
        for i, s in enumerate(ep["sahneler"]):
            yer_s = "%s sahne %d" % (yer, i + 1)
            # karakterler
            gor = [c for c in s["kim"] if not c.startswith("~")]
            ses = [c[1:] for c in s["kim"] if c.startswith("~")]
            for c in gor + ses:
                assert karakter_var(ep, c), "%s: bilinmeyen karakter %s" % (yer_s, c)
            for d in s["dlg"]:
                assert d[0] in gor or d[0] in ses, "%s: konuşan %s sahnede yok" % (yer_s, d[0])
            if len(gor) > 3:
                uyari.append("%s: %d görünür karakter" % (yer_s, len(gor)))
            # saat
            dk = saat_dk(s["z"])
            if not s["fb"] and dk is not None:
                assert dk >= son_dk, "%s: saat geriye gidiyor (%s)" % (yer_s, s["z"])
                son_dk = dk
            # para
            T = sahne_T(s)
            dlg = []
            for d in s["dlg"]:
                metin = doldur(d[1], T, "words", yer_s)
                dlg.append([d[0], metin, d[2] if len(d) > 2 else ""])
            toplam = sum(kelime(d[1]) for d in dlg)
            assert toplam <= 30, "%s: diyalog 10 saniyeye sığmaz (%d kelime)" % (yer_s, toplam)
            if toplam > 25:
                uyari.append("%s: diyalog %d kelime" % (yer_s, toplam))
            tx = []
            for t in s["tx"]:
                if t["tip"] == "acilis":
                    assert kasa is None, "%s: kasa iki kez açılıyor" % yer_s
                    assert t["tutar"] == BASLANGIC_KASA
                    kasa = 0
                assert kasa is not None, "%s: kasa açılmadan işlem var" % yer_s
                onceki = kasa
                kasa += TIPLER[t["tip"]][1] * t["tutar"]
                assert kasa >= 0, "%s: kasa eksiye düştü (%d)" % (yer_s, kasa)
                if t["tip"] == "borc":
                    borc_odenen += t["tutar"]
                tx.append(dict(t, aciklama=doldur(t["aciklama"], dict(tx=t["tutar"], adet=t["adet"], fiyat=t["fiyat"], tx2=None), "tr", yer_s), onceki=onceki, sonraki=kasa))
            sahneler.append(dict(
                n=i + 1, ad=s["ad"], z=s["z"], saat=(re.match(r"(\d\d:\d\d)", s["z"]).group(1) if dk is not None else ""),
                faz=faz_of(s["z"]), h=s["h"], yer=s["yer"], kim=s["kim"],
                tr=doldur(s["tr"], T, "tr", yer_s), en=doldur(s["en"], T, "en", yer_s),
                dlg=dlg, kam=s["kam"], tx=tx, kurgu=s["kurgu"], fb=s["fb"], kasa=kasa))
        il = ep["sehir"]
        plaka = ILLER_AD[il] if il else None
        bolge = ILLER[plaka][1] if il else None
        sezon = next(sz["id"] for sz in bible.SEZONLAR if (il in sz["rota"] if il else sz["bolge"] is None))
        bolumler.append(dict(
            no=no, sehir=il, plaka=plaka, bolge=bolge, sezon=sezon, baslik=ep["baslik"], ozet=ep["ozet"], hikaye=ep["hikaye"],
            ay=ep["ay"], hava=ep["hava"], hava_tr=HAVA_TR[ep["hava"]], kiyafet=ep["kiyafet"],
            yerler={k: list(v) for k, v in ep["yerler"].items()},
            misafir={k: list(v) for k, v in ep["misafir"].items()},
            kapak=list(ep["kapak"]), yakinda=list(ep["yakinda"]),
            tiktok=ep["tiktok"], ig=ep["ig"], tags=ep["tags"], son=ep["son"], teaser=ep["teaser"], sponsor=ep["sponsor"], urun=ep["urun"],
            sahneler=sahneler, kasa_acilis=acilis, kasa_kapanis=kasa))
        for k in (ep["kapak"], ep["yakinda"]):
            for c in k[1]:
                assert karakter_var(ep, c), "%s kapak: bilinmeyen karakter %s" % (yer, c)
    if not KISMI:
        assert borc_odenen == BORC, "Borç taksitleri toplamı %d, olması gereken %d" % (borc_odenen, BORC)

    karakterler = [dict(id=k["id"], ad=k["ad"], yas=k["yas"], ilk=k["ilk"], rol=k["rol"], tr=k["tr"], gecmis=k["gecmis"],
                        en=k["en"], ses=k["ses"], kiyafet=k["kiyafet"], ana=k["ana"]) for k in K.values()]
    sehirler = [dict(plaka=p, ad=v[0], bolge=v[1]) for p, v in sorted(ILLER.items())]
    data = dict(
        surum=1, baslangic_kasa=BASLANGIC_KASA, borc=BORC,
        sabit=SABIT, faz=FAZ, hava=HAVA, tipler={k: dict(ad=v[0], isaret=v[1], grup=v[2]) for k, v in TIPLER.items()},
        karakterler=karakterler, nesne=NESNE,
        bolgeler=[dict(id=b[0], ad=b[1], sezon=b[2]) for b in BOLGELER], sehirler=sehirler,
        sezonlar=bible.SEZONLAR, biblio=bible.BIBLIO,
        bolumler=bolumler)
    return data, uyari, kasa, borc_odenen


if __name__ == "__main__":
    data, uyari, kasa, borc = derle()
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = os.path.join(HERE, "..", "js", "data.js")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("/* JOZH STUDIOS · 81 Şehir. BU DOSYA ÜRETİLİR: kaynak/build.py. Elle düzenleme. */\n")
        fh.write("window.JOZH_DATA = " + js + ";\n")
    n = sum(len(b["sahneler"]) for b in data["bolumler"])
    print("Bölüm: %d  Sahne: %d  Boyut: %.0f KB" % (len(data["bolumler"]), n, os.path.getsize(out) / 1024))
    print("Senaryo kasası (son): %s TL   Ödenen borç: %s TL" % (nokta_sayi(kasa or 0), nokta_sayi(borc)))
    if "-v" in sys.argv:
        for b in data["bolumler"]:
            print("%3d %-16s %10s -> %10s" % (b["no"], b["sehir"] or "-", nokta_sayi(b["kasa_acilis"] or 0), nokta_sayi(b["kasa_kapanis"] or 0)))
    for u in uyari:
        print("UYARI:", u)
