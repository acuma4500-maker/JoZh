# -*- coding: utf-8 -*-
"""Flow sahne prompt'larını birleştirip tek HTML sayfası üretir.

Kullanım:  python3 build.py   ->  dedemin-defteri-flow.html
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

import sezon1  # noqa: E402  kasa hesabı ve bölüm başlıkları
from karakterler import K, STIL  # noqa: E402
from ortak import EPS  # noqa: E402
import sahne_01_03, sahne_04_20, sahne_21_40, sahne_41_60, sahne_61_80, sahne_81_100  # noqa: E402,F401
from aciklama import ACIKLAMA  # noqa: E402
from kapak import KAPAK, KAPAK_STIL  # noqa: E402

KAM_TEK = [
    "medium tracking shot following the character, eye level",
    "wide establishing shot that slowly pushes in",
    "medium close-up, slow dolly",
    "close-up with gentle handheld movement",
    "medium shot, slow dolly",
    "slow dramatic push-in to a close-up",
]
KAM_COK = [
    "medium tracking shot following the characters, eye level",
    "wide establishing shot that slowly pushes in to a two-shot",
    "over-the-shoulder shot alternating between speakers, shallow depth of field",
    "close-up reaction shots with gentle handheld movement",
    "medium two-shot, slow dolly",
    "slow dramatic push-in to a close-up",
]

SEZONLAR = [
    ("b1-20", "Bölüm 1–20", 1, 20, "Londra'dan Gaziantep'e"),
    ("b21-40", "Bölüm 21–40", 21, 40, "Kahramanmaraş'tan Erzincan'a"),
    ("b41-60", "Bölüm 41–60", 41, 60, "Erzurum'dan Zonguldak'a"),
    ("b61-100", "Bölüm 61–100", 61, 100, "Düzce'den Kayseri'ye, final"),
]


def etiket(desc):
    return desc.split(",")[0].strip()


def kasa_akisi(r, sahneler):
    si = next((i for i, s in enumerate(sahneler) if s["k"] == "s"), 2)
    ai = next((i for i, s in enumerate(sahneler) if s["k"] == "a"), 4)
    mi = min(si + 1, 5)
    v = r["acilis"]
    out, parts = [], []
    for i in range(6):
        p = []
        if i == 1 and r["yol"]:
            v -= r["yol"]
            p.append(("yol (otobüs)", -r["yol"]))
        if i == si and r["satis_t"]:
            v += r["satis_t"]
            p.append(("satış", r["satis_t"]))
        if i == mi and r["masraf_t"]:
            v -= r["masraf_t"]
            p.append(("masraf", -r["masraf_t"]))
        if i == ai and r["alis_t"]:
            v -= r["alis_t"]
            p.append(("alış (mal)", -r["alis_t"]))
        assert v >= 0, "Bölüm %d sahne %d: kasa eksi" % (r["no"], i + 1)
        out.append(v)
        parts.append(p)
    assert out[-1] == r["kapanis"], "Bölüm %d: kasa akışı kapanışı tutmuyor" % r["no"]
    return out, parts


def tl(n):
    return "{:,}".format(n).replace(",", ".") + " ₺"


def isaretli(n):
    return ("+" if n > 0 else "−") + tl(abs(n))


KV_ORTAK = ("Vertical 9:16 video, 8 seconds, PURE SOLID BLACK background (#000000) filling the entire frame, "
            "made to be layered over another video with a Screen / Lighten blend mode. "
            "Absolutely nothing else in the frame: no scene, no characters, no gradient, no vignette, no texture, "
            "no glow spilling across the screen, locked static camera, no camera movement, no sound, no music.\n\n"
            "LAYOUT: only in the TOP RIGHT corner (about 6% from the top edge and 5% from the right edge) sits one compact "
            "cash counter widget: a small flat banknote icon, the small label \"KASA\", and under it a large bold "
            "odometer-style number followed by the Turkish lira sign. The widget is at most 38% of the frame width and 9% "
            "of the frame height. All the rest of the frame stays pure black.\n\n")


def kasa_video(onceki, simdi, parts, no):
    fark = simdi - onceki
    if fark == 0:
        tip = "sabit"
        anim = ("ANIMATION: the counter stays perfectly still for all 8 seconds showing exactly \"%s\" in clean white-gold "
                "glowing digits, with only a very faint soft pulse of light. The digits never change." % tl(simdi))
    else:
        yon = "increasing" if fark > 0 else "decreasing"
        renk = "bright green" if fark > 0 else "bright red"
        tip = "artis" if fark > 0 else "azalis"
        efekt = ("a few small gold coins and banknotes sparkle and fly into the widget" if fark > 0
                 else "a few banknotes slide out of the widget and fade away")
        anim = ("ANIMATION: seconds 0 to 1: the counter holds still on exactly \"%s\" in white-gold digits. "
                "Seconds 1 to 5.5: the digits roll smoothly like a mechanical odometer, the value %s continuously through "
                "intermediate values, the glow turns %s, and %s. At about second 5.5 the number lands exactly on \"%s\". "
                "Seconds 5.5 to 8: the counter holds still on exactly \"%s\", glow returns to white-gold. "
                "A tiny change label \"%s\" appears under the number from second 1 and fades out at second 6." % (
                    tl(onceki), yon, renk, efekt, tl(simdi), tl(simdi), isaretli(fark)))
    son = ("\n\nTEXT RULES: the only characters allowed in the whole video are \"KASA\", the numbers and the ₺ sign shown above; "
           "digits must be sharp, perfectly legible, evenly spaced and never distorted or morphing into other characters.")
    return dict(onceki=onceki, simdi=simdi, fark=fark, tip=tip, no=no,
                neden=[a + " " + isaretli(d) for a, d in parts], prompt=KV_ORTAK + anim + son)


def prompt_kur(ep, s, i):
    mis = ep["misafir"]
    gorunen, sesli = [], []
    for c in s["kim"]:
        (sesli if c.startswith("~") else gorunen).append(c.lstrip("~"))
    for sp, _ in s["dlg"]:
        if sp not in gorunen and sp not in sesli:
            gorunen.append(sp)

    def bilgi(cid):
        if cid in K:
            return K[cid]["en"], K[cid]["ses"]
        if cid in mis:
            return mis[cid][1], mis[cid][2]
        raise KeyError("Bölüm %d: bilinmeyen karakter '%s'" % (ep["no"], cid))

    satir = []
    for cid in gorunen:
        en, ses = bilgi(cid)
        satir.append("- %s. Voice: %s." % (en, ses))
    for cid in sesli:
        en, ses = bilgi(cid)
        satir.append("- %s (NOT visible on screen; only the voice is heard, through a phone or as voice-over). Voice: %s." % (etiket(en), ses))

    yer_tr, yer_en = ep["yerler"][s["yer"]]
    kam = s["kam"] or (KAM_TEK if len(gorunen) <= 1 else KAM_COK)[i]
    dlg = "\n".join('%s: "%s"' % (etiket(bilgi(sp)[0]), line) for sp, line in s["dlg"])
    ses = ("natural ambient sound of the location, a subtle suspense music sting in the last second"
           if i == 5 else "natural ambient sound of the location, no background music")
    p = (STIL + "\n\n"
         "CHARACTERS (keep appearance exactly the same in every shot):\n" + "\n".join(satir) + "\n\n"
         "SETTING: " + yer_en + ".\n\n"
         "ACTION: " + s["en"] + "\n\n"
         "DIALOGUE (spoken in Turkish, natural lip-sync, short lines that fit 8 seconds):\n" + dlg + "\n\n"
         "CAMERA: " + kam + ".\n"
         "AUDIO: " + ses + ".")
    return p, yer_tr, [etiket(bilgi(c)[0]) for c in gorunen], [etiket(bilgi(c)[0]) for c in sesli]


def kapak_kur(ep, r):
    yer, kim, en, tr = KAPAK[ep["no"]]
    mis = ep["misafir"]
    satir = []
    for cid in kim:
        if cid in K:
            satir.append("- " + K[cid]["en"] + ".")
        elif cid in mis:
            satir.append("- " + mis[cid][1] + ".")
        else:
            raise KeyError("Kapak %d: bilinmeyen karakter '%s'" % (ep["no"], cid))
    p = (KAPAK_STIL + "\n\n"
         "CHARACTERS (same fixed design as in the episode):\n" + "\n".join(satir) + "\n\n"
         "SETTING: " + ep["yerler"][yer][1] + ".\n\n"
         "COMPOSITION: " + en + " Expressive faces, strong depth, dramatic rim light, "
         "the scene feels like a frozen moment just before something big happens.")
    yazi = ["BÖLÜM %d" % ep["no"], r["baslik"], r["il"]]
    if ep["no"] >= 4:
        yazi.append("KASA: " + tl(r["kapanis"]))
    return dict(tr=tr, yer=ep["yerler"][yer][0], prompt=p, yazi=yazi)


def aciklama_kur(no, r):
    if no not in ACIKLAMA:
        return None
    metin, tags = ACIKLAMA[no]
    assert len(tags) == 4 and all(t.startswith("#") for t in tags), "Bölüm %d: tam 4 hashtag olmalı" % no
    assert "#" not in metin, "Bölüm %d: hashtag sadece etiket listesinde olmalı" % no
    if "{kasa}" in metin:
        metin = metin.replace("{kasa}", tl(r["kapanis"]))
    return dict(metin=metin, etiketler=tags, tam=metin + "\n\n" + " ".join(tags))


def ad_tr(ep, cid):
    if cid in K:
        return K[cid]["ad"]
    return ep["misafir"][cid][0]


def derle():
    rows = {r["no"]: r for r in sezon1.hesapla()}
    sezon1.kontrol(list(rows.values()))
    assert sorted(EPS) == list(range(1, 101)), "Eksik bölüm: %s" % sorted(set(range(1, 101)) - set(EPS))
    bolumler = []
    for no in range(1, 101):
        ep = EPS[no]
        r = rows.get(no) or sahne_01_03.META[no]
        akis, parcalar = kasa_akisi(r, ep["sahneler"]) if no >= 4 else ([None] * 6, [None] * 6)
        sahneler = []
        for i, s in enumerate(ep["sahneler"]):
            prompt, yer_tr, gor, ses = prompt_kur(ep, s, i)
            sahneler.append(dict(
                n=i + 1, yer=yer_tr, olay=s["tr"],
                dlg=[[ad_tr(ep, sp), line] for sp, line in s["dlg"]],
                kasa=akis[i], kurgu=s["kurgu"], prompt=prompt,
                kv=(kasa_video(r["acilis"] if i == 0 else akis[i - 1], akis[i], parcalar[i], i + 1) if no >= 4 else None)))
        bolumler.append(dict(
            no=no, il=r["il"], baslik=r["baslik"], ozet=r["hikaye"], son=r["son"],
            satilan=r["satilan"], alinan=r["alinan"],
            kasa=(dict(acilis=r["acilis"], yol=r["yol"], masraf=r["masraf_t"], satis=r["satis_t"],
                       alis=r["alis_t"], kapanis=r["kapanis"]) if no >= 4 else None),
            aciklama=aciklama_kur(no, r),
            konuk=[dict(ad=v[0], en=v[1], ses=v[2]) for v in ep["misafir"].values()],
            kapak=kapak_kur(ep, r),
            sahneler=sahneler))
    karakterler = [dict(id=k["id"], ad=k["ad"], yas=k["yas"], ilk=k["ilk"], rol=k["rol"], tr=k["tr"],
                        en=k["en"], ses=k["ses"], ana=k["ana"]) for k in K.values()]
    assert sorted(KAPAK) == list(range(1, 101)), "Eksik kapak"
    return dict(stil=STIL, kapak_stil=KAPAK_STIL, karakterler=karakterler, sezonlar=[
        dict(id=a, ad=b, ilk=c, son=d, alt=e) for a, b, c, d, e in SEZONLAR], bolumler=bolumler)


if __name__ == "__main__":
    data = derle()
    with io.open(os.path.join(HERE, "sablon.html"), encoding="utf-8") as fh:
        html = fh.read()
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = html.replace("/*__DATA__*/null", js)
    out = os.path.join(HERE, "dedemin-defteri-flow.html")
    with io.open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    n = sum(len(b["sahneler"]) for b in data["bolumler"])
    print("Bölüm:", len(data["bolumler"]), " Sahne:", n, " Boyut: %.0f KB" % (len(html.encode("utf-8")) / 1024))
