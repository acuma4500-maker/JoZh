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
import sahne_04_20, sahne_21_40, sahne_41_60, sahne_61_80, sahne_81_100  # noqa: E402,F401

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
    ("b4-20", "Bölüm 4–20", 4, 20, "Kayseri'den Gaziantep'e"),
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
    out = []
    for i in range(6):
        if i == 1:
            v -= r["yol"]
        if i == si:
            v += r["satis_t"]
        if i == mi:
            v -= r["masraf_t"]
        if i == ai:
            v -= r["alis_t"]
        assert v >= 0, "Bölüm %d sahne %d: kasa eksi" % (r["no"], i + 1)
        out.append(v)
    assert out[-1] == r["kapanis"], "Bölüm %d: kasa akışı kapanışı tutmuyor" % r["no"]
    return out


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


def ad_tr(ep, cid):
    if cid in K:
        return K[cid]["ad"]
    return ep["misafir"][cid][0]


def derle():
    rows = {r["no"]: r for r in sezon1.hesapla()}
    sezon1.kontrol(list(rows.values()))
    assert sorted(EPS) == list(range(4, 101)), "Eksik bölüm: %s" % sorted(set(range(4, 101)) - set(EPS))
    bolumler = []
    for no in range(4, 101):
        ep, r = EPS[no], rows[no]
        akis = kasa_akisi(r, ep["sahneler"])
        sahneler = []
        for i, s in enumerate(ep["sahneler"]):
            prompt, yer_tr, gor, ses = prompt_kur(ep, s, i)
            sahneler.append(dict(
                n=i + 1, yer=yer_tr, olay=s["tr"],
                dlg=[[ad_tr(ep, sp), line] for sp, line in s["dlg"]],
                kasa=akis[i], kurgu=s["kurgu"], prompt=prompt))
        bolumler.append(dict(
            no=no, il=r["il"], baslik=r["baslik"], ozet=r["hikaye"], son=r["son"],
            satilan=r["satilan"], alinan=r["alinan"],
            kasa=dict(acilis=r["acilis"], yol=r["yol"], masraf=r["masraf_t"], satis=r["satis_t"],
                      alis=r["alis_t"], kapanis=r["kapanis"]),
            konuk=[dict(ad=v[0], en=v[1], ses=v[2]) for v in ep["misafir"].values()],
            sahneler=sahneler))
    karakterler = [dict(id=k["id"], ad=k["ad"], yas=k["yas"], ilk=k["ilk"], rol=k["rol"], tr=k["tr"],
                        en=k["en"], ses=k["ses"], ana=k["ana"]) for k in K.values()]
    return dict(stil=STIL, karakterler=karakterler, sezonlar=[
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
