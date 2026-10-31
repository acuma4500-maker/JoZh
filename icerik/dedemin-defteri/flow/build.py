# -*- coding: utf-8 -*-
"""Flow sahne prompt'larını birleştirip tek HTML sayfası üretir.

Kullanım:
  python3 build.py          tüm bölümler (1-100) tanımlı olmalı
  python3 build.py kismi    sadece yazılmış bölümleri derler (geliştirme sırasında)
"""
import importlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

import sezon1  # noqa: E402
from karakterler import K, STIL  # noqa: E402
from kapak import KAPAK_STIL  # noqa: E402
from ortak import EPS, faz_of  # noqa: E402
from aciklama import ACIKLAMA  # noqa: E402

KISMI = "kismi" in sys.argv
META = {}
for _ad in ["sahne_%03d_%03d" % (a, a + 9) for a in range(1, 100, 10)]:
    try:
        _mod = importlib.import_module(_ad)
    except ModuleNotFoundError as e:
        if e.name != _ad:
            raise
        continue
    META.update(getattr(_mod, "META", {}))

# ---------------------------------------------------------------- ışık, hava
FAZ = {
    "şafak": "Dawn, around {c}. The sun is just rising at the horizon, soft pink-orange light, long soft shadows, cool blue shade",
    "sabah": "Morning, around {c}. Bright clean sunlight at a low angle from camera-left",
    "öğle": "Midday, around {c}. High sun, bright even light, short crisp shadows",
    "ikindi": "Afternoon, around {c}. Warm sunlight at a lowering angle from camera-right",
    "gün batımı": "Sunset, around {c}. Warm orange golden-hour light, long shadows, glowing sky",
    "akşam": "Early evening, around {c}. Deep blue dusk sky, street lamps and shop windows just lit, warm practical lights",
    "gece": "Night, around {c}. Dark sky, warm pools of light from lamps and windows, soft cool moonlight",
    "iç-gündüz": "Interior during the day, around {c}. Soft daylight coming through a window, warm ambient interior tones",
    "iç-gece": "Interior at night, around {c}. Warm lamp light, dark windows, soft shadows",
    "anı-gündüz": "Flashback scene in daytime. Warm, slightly golden, soft-focus look with a faded film feel",
    "anı-gece": "Flashback scene at night. Warm practical lights and deep shadows with a faded 1970s film look",
}
HAVA = {
    "açık": "Clear sky, crisp air",
    "ılık": "Mild sunny weather, gentle breeze",
    "bulutlu": "Overcast sky, soft diffused light, no hard shadows",
    "yağmur": "Light rain falling, wet ground reflecting the light, overcast",
    "kar": "Light snow falling, snow covering the ground and rooftops, overcast soft light, visible breath in the cold air",
    "tipi": "Heavy blowing snow, strong wind, low visibility",
    "sis": "Low mist drifting through the scene, soft diffused light",
    "rüzgar": "Windy, coats and hair moving gently in the breeze",
}
HAVA_TR = {"açık": "açık", "ılık": "ılık, güneşli", "bulutlu": "bulutlu", "yağmur": "yağmurlu", "kar": "karlı",
           "tipi": "tipi", "sis": "sisli", "rüzgar": "rüzgârlı"}

BACKGROUND = ("Simple and uncluttered, with a clear foreground subject. If other people appear behind, only two or three, "
              "far away and softly out of focus")
PHYSICS = ("Natural human motion with realistic weight and balance, feet stay on the ground, objects such as boxes, "
           "money and tea glasses move with realistic weight and inertia, hands hold one simple object at a time, "
           "no sudden speed changes")
AVOID = ("distorted or morphing faces, extra or missing fingers, deformed hands, floating or duplicated objects, "
         "characters changing clothes, flickering light, shaky camera, text, subtitles, watermarks, logos, "
         "cartoon exaggeration, crowds of identical people")
LIPSYNC = ("All speech is in Turkish with a natural accent. Lips sync exactly to the spoken words and only the speaking "
           "character's mouth moves. Each line is short and clear")


def mevsim(no):
    return "Kış" if no <= 60 else ("Kış sonu" if no <= 80 else "İlkbahar")


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


def tl(n):
    return "{:,}".format(n).replace(",", ".") + " ₺"


def isaretli(n):
    return ("+" if n > 0 else "−") + tl(abs(n))


def doldur(s, T, mod):
    def f(m):
        k = m.group(1)
        if k not in T:
            raise KeyError("bilinmeyen para etiketi {%s}" % k)
        v = T[k]
        if mod == "words":
            w = tr_sayi(v)
            onceki = m.string[:m.start()].rstrip()
            if (not onceki) or (onceki[-1] in ".!?" and not onceki.endswith("...")):
                w = tr_upper(w[0]) + w[1:]
            return w
        if mod == "en":
            return "{:,}".format(v)
        return "{:,}".format(v).replace(",", ".")
    return re.sub(r"\{(\w+)\}", f, s)


def tr_upper(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


def kelime(s):
    return len(re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîûÂÎÛ0-9]+", s))


def saat_dk(z):
    m = re.match(r"(\d\d):(\d\d)", z)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def saat_goster(z):
    m = re.match(r"(\d\d):(\d\d)", z)
    return "%02d:%02d" % (int(m.group(1)) % 24, int(m.group(2))) if m else ""


# ---------------------------------------------------------------- kasa
# Kasa prompt'u sayfada, ../kasa/kasa-motor.js ile üretilir (ayarlara göre). Burada yalnızca kasa olayı kaydedilir.
def kasa_video(onceki, simdi, parts, no):
    fark = simdi - onceki
    tip = "sabit" if fark == 0 else ("artis" if fark > 0 else "azalis")
    return dict(onceki=onceki, simdi=simdi, fark=fark, tip=tip, no=no,
                neden=[a + " " + isaretli(d) for a, d in parts])


def kasa_akisi(r, ep):
    f = dict(y=0, s=1, m=2, a=4)
    f.update(ep["kasa"])
    baslar = ep["kasa_baslar"]
    v = 0 if baslar else r["acilis"]
    out, parts = [], []
    for i in range(6):
        p = []
        if i < baslar:
            out.append(None)
            parts.append(p)
            continue
        if baslar and i == baslar:
            v = r["acilis"]
            p.append(("sermaye", r["acilis"]))
        if i == f["y"] and r["yol"]:
            v -= r["yol"]
            p.append(("yol (otobüs)", -r["yol"]))
        if i == f["s"] and r["satis_t"]:
            v += r["satis_t"]
            p.append(("satış", r["satis_t"]))
        if i == f["m"] and r["masraf_t"]:
            v -= r["masraf_t"]
            p.append(("masraf", -r["masraf_t"]))
        if i == f["a"] and r["alis_t"]:
            v -= r["alis_t"]
            p.append(("alış (mal)", -r["alis_t"]))
        assert v >= 0, "Bölüm %d sahne %d: kasa eksi" % (r["no"], i + 1)
        out.append(v)
        parts.append(p)
    assert out[-1] == r["kapanis"], "Bölüm %d: kasa akışı kapanışı tutmuyor" % r["no"]
    return out, parts, f


# ---------------------------------------------------------------- prompt
def etiket(look):
    return look.split(",")[0].strip()


def nokta(s):
    return s.rstrip().rstrip(".") + "."


def parcalar(ep, s, T, no, n):
    mis = ep["misafir"]

    def bilgi(cid):
        if cid in K:
            return K[cid]["en"], K[cid]["ses"]
        if cid in mis:
            return mis[cid][1], mis[cid][2]
        raise KeyError("Bölüm %d sahne %d: bilinmeyen karakter '%s'" % (no, n, cid))

    gor, ses = [], []
    for c in s["kim"]:
        (ses if c.startswith("~") else gor).append(c.lstrip("~"))
    for d in s["dlg"]:
        assert d[0] in gor or d[0] in ses, "Bölüm %d sahne %d: konuşan '%s' kim listesinde yok" % (no, n, d[0])
    sat_gor, sat_ses = [], []
    for cid in gor:
        look, v = bilgi(cid)
        sat_gor.append("- %s Voice: %s." % (nokta(look), v.rstrip(".")))
    for cid in ses:
        look, v = bilgi(cid)
        sat_ses.append("- %s: off-screen voice only, NOT visible in the shot (heard from a phone speaker or from outside the frame). "
                       "Voice: %s." % (etiket(look), v.rstrip(".")))
    satirlar = sat_gor + sat_ses
    dlg = []
    for d in s["dlg"]:
        ad = etiket(bilgi(d[0])[0])
        ton = d[2] if len(d) > 2 else None
        text = doldur(d[1], T, "words")
        ad_tr = K[d[0]]["ad"] if d[0] in K else mis[d[0]][0]
        dlg.append((d[0], ad, ton, text, d[0] in ses, ad_tr))
    faz = faz_of(s["z"])
    saat = saat_goster(s["z"])
    base = FAZ[faz]
    isik = base.replace("{c}", saat) if saat else base.replace(", around {c}", "")
    if faz.startswith("iç"):
        hv = ("Through the window: " + HAVA[s["h"]]) if s["h"] else ""
    elif faz.startswith("anı"):
        hv = ""
    else:
        hv = HAVA[s["h"] or ep["hava"]]
    isik = nokta(isik) + (" " + nokta(hv) if hv else "") + " The light stays exactly the same for the whole shot, with no flicker."
    return dict(gor=gor, ses=ses, satirlar=satirlar, sat_gor=sat_gor, sat_ses=sat_ses, dlg=dlg, isik=isik,
                yer_en=ep["yerler"][s["yer"]][1], en=doldur(s["en"], T, "en"), kam=s["kam"],
                saat=saat, faz=faz, bilgi=bilgi)


def dlg_blok(dlg):
    if not dlg:
        return "DIALOGUE: none. Nobody speaks."
    satir = []
    for _, ad, ton, text, off, _t in dlg:
        etiket_ = ad + (" (off-screen, from the phone speaker)" if off else "") + (" [" + ton + "]" if ton else "")
        satir.append('%s: "%s"' % (etiket_, text))
    return "DIALOGUE (spoken in Turkish):\n" + "\n".join(satir) + "\nLIP SYNC: " + nokta(LIPSYNC)


def prompt_kur(ep, s, i, T, no):
    p = parcalar(ep, s, T, no, i + 1)
    ses = ("Clear Turkish speech over the natural room tone and ambient sound of the location, no background music"
           if p["dlg"] else "No speech. Natural ambient sound of the location only, no background music")
    if i == 5:
        ses += ", and one single low suspense note in the final second"
    txt = (STIL + "\n\n"
           "CHARACTERS (identical appearance in every shot, same outfit every time):\n" + "\n".join(p["satirlar"]) + "\n\n"
           "LOCATION: " + nokta(p["yer_en"]) + "\n"
           "TIME AND LIGHT: " + p["isik"] + "\n"
           "BACKGROUND: " + nokta(BACKGROUND) + "\n\n"
           "ACTION (one continuous 8-second shot): " + nokta(p["en"]) + "\n"
           "CAMERA: " + nokta(p["kam"]) + "\n\n"
           + dlg_blok(p["dlg"]) + "\n\n"
           "PHYSICS: " + nokta(PHYSICS) + "\n"
           "AUDIO: " + nokta(ses) + "\n"
           "AVOID: " + nokta(AVOID))
    return txt, p


def basit_kur(ep, s, p, T):
    eylem = doldur(s["basit"], T, "en") if s["basit"] else re.split(r"(?<=[.!?])\s+", p["en"])[0]
    ilk = p["dlg"][:1]
    satirlar = p["sat_gor"][:2] + (p["sat_ses"] if ilk and ilk[0][4] else [])
    parts = [STIL, "",
             "CHARACTERS (at most two visible, identical appearance in every shot):\n" + "\n".join(satirlar),
             "LOCATION: " + nokta(p["yer_en"]),
             "TIME AND LIGHT: " + p["isik"],
             "BACKGROUND: empty and simple, no other people",
             "ACTION (one simple action): " + nokta(eylem),
             "CAMERA: static locked-off medium shot at eye level on a tripod, no camera movement", "",
             dlg_blok(ilk), "",
             "PHYSICS: " + nokta(PHYSICS),
             "AVOID: " + nokta(AVOID)]
    return "\n".join(parts)


# ---------------------------------------------------------------- kapak
def kapak_kur(ep, r, T):
    yer, kim, en, tr = ep["kapak"]
    mis = ep["misafir"]
    satir = []
    for cid in kim:
        if cid in K:
            satir.append("- " + nokta(K[cid]["en"]))
        elif cid in mis:
            satir.append("- " + nokta(mis[cid][1]))
        else:
            raise KeyError("Kapak %d: bilinmeyen karakter '%s'" % (ep["no"], cid))
    p = (KAPAK_STIL + "\n\n"
         "CHARACTERS (same fixed design as in the episode):\n" + "\n".join(satir) + "\n\n"
         "SETTING: " + nokta(ep["yerler"][yer][1]) + "\n\n"
         "COMPOSITION: " + nokta(doldur(en, T, "en")) + " Expressive faces, strong depth, dramatic rim light, "
         "the scene feels like a frozen moment just before something big happens.")
    yazi = ["BÖLÜM %d" % ep["no"], r["baslik"], r["il"]]
    if ep["no"] >= 4:
        yazi.append("KASA: " + tl(r["kapanis"]))
    return dict(tr=doldur(tr, T, "tr"), yer=ep["yerler"][yer][0], prompt=p, yazi=yazi)


def aciklama_kur(no, r):
    if no not in ACIKLAMA:
        return None
    metin, tags = ACIKLAMA[no]
    assert len(tags) == 4 and all(t.startswith("#") for t in tags), "Bölüm %d: tam 4 hashtag olmalı" % no
    assert "#" not in metin, "Bölüm %d: hashtag sadece etiket listesinde olmalı" % no
    if "{kasa}" in metin:
        metin = metin.replace("{kasa}", tl(r["kapanis"]))
    return dict(metin=metin, etiketler=tags, tam=metin + "\n\n" + " ".join(tags))


# ---------------------------------------------------------------- derleme
def derle():
    rows = {r["no"]: r for r in sezon1.hesapla()}
    sezon1.kontrol(list(rows.values()))
    tum = list(range(1, 101))
    if not KISMI:
        eksik = sorted(set(tum) - set(EPS))
        assert not eksik, "Eksik bölüm: %s" % eksik
    nolar = [n for n in tum if n in EPS]
    uyari = []
    bolumler = []
    for no in nolar:
        ep = EPS[no]
        r = rows.get(no) or dict(META[no], satis=None, alis_t=0)
        onceki = rows.get(no - 1) or META.get(no - 1)
        onceki_son = onceki["son"] if onceki else None
        # --- kasa
        if no >= 4:
            akis, parcal, f = kasa_akisi(r, ep)
            prev = rows.get(no - 1)
            stok = prev["alis_t"] if (prev and r["satis"] is None) else 0
            T = dict(acilis=r["acilis"], yol=r["yol"], satis=r["satis_t"], masraf=r["masraf_t"], alis=r["alis_t"],
                     kapanis=r["kapanis"], stok=stok, kar=max(r["satis_t"] - stok, 0),
                     kasa_s=akis[f["s"]] if akis[f["s"]] is not None else 0,
                     kasa_m=akis[f["m"]] if akis[f["m"]] is not None else 0,
                     kasa_a=akis[f["a"]] if akis[f["a"]] is not None else 0)
        else:
            akis, parcal, f, T = [None] * 6, [[] for _ in range(6)], {}, {}
        # --- saat sırası
        son_dk = -1
        for i, s in enumerate(ep["sahneler"]):
            dk = saat_dk(s["z"])
            if s["fb"] or dk is None:
                continue
            assert dk >= son_dk, "Bölüm %d sahne %d: saat geriye gidiyor (%s)" % (no, i + 1, s["z"])
            son_dk = dk
        sahneler, plan = [], []
        for i, s in enumerate(ep["sahneler"]):
            prompt, p = prompt_kur(ep, s, i, T, no)
            basit = basit_kur(ep, s, p, T)
            toplam = sum(kelime(d[3]) for d in p["dlg"])
            if toplam > 24:
                raise AssertionError("Bölüm %d sahne %d: diyalog çok uzun (%d kelime)" % (no, i + 1, toplam))
            if toplam > 18:
                uyari.append("B%d S%d diyalog %d kelime" % (no, i + 1, toplam))
            if len([c for c in p["gor"]]) > 3:
                uyari.append("B%d S%d %d görünür karakter" % (no, i + 1, len(p["gor"])))
            yer_tr = ep["yerler"][s["yer"]][0]
            saat, faz = p["saat"], p["faz"]
            notlar = []
            if not s["fb"] and (i == 0 or s["et"]):
                ad = s["et"] or r["il"]
                head = tr_upper(ad) + (" · GÜN %d" % no if i == 0 else "") + (" · " + saat if saat else "")
                notlar.append("Ekrana yazı ekle (kurguda): " + head)
            if s["kurgu"]:
                notlar.append(doldur(s["kurgu"], T, "tr"))
            kv = None
            if akis[i] is not None:
                onc = 0 if (ep["kasa_baslar"] and i == ep["kasa_baslar"]) else (r["acilis"] if i == 0 else akis[i - 1])
                kv = kasa_video(onc, akis[i], parcal[i], i + 1)
            sahneler.append(dict(
                n=i + 1, saat=saat, faz=faz, yer=yer_tr, tr=doldur(s["tr"], T, "tr"),
                dlg=[[d[5], d[3], d[2] or ""] for d in p["dlg"]],
                kasa=akis[i], kv=kv, kurgu=notlar, prompt=prompt, basit=basit, fb=s["fb"]))
            if not s["fb"]:
                plan.append((saat + " " + yer_tr).strip())
        bolumler.append(dict(
            no=no, gun=no, mevsim=mevsim(no), hava=HAVA_TR[ep["hava"]], il=r["il"], baslik=r["baslik"],
            ozet=doldur(r["hikaye"], T, "tr"), son=ep["son"] or r["son"], onceki_son=onceki_son,
            satilan=r["satilan"], alinan=r["alinan"],
            kasa=(dict(acilis=r["acilis"], yol=r["yol"], masraf=r["masraf_t"], satis=r["satis_t"],
                       alis=r["alis_t"], kapanis=r["kapanis"]) if no >= 4 else None),
            konuk=[dict(ad=v[0], en=v[1], ses=v[2]) for v in ep["misafir"].values()],
            kapak=kapak_kur(ep, r, T), aciklama=aciklama_kur(no, r), plan=plan, sahneler=sahneler))
    karakterler = [dict(id=k["id"], ad=k["ad"], yas=k["yas"], ilk=k["ilk"], rol=k["rol"], tr=k["tr"],
                        en=k["en"], ses=k["ses"], ana=k["ana"]) for k in K.values()]
    sezonlar = [("b1-20", "Bölüm 1–20", 1, 20, "Londra'dan Gaziantep'e"),
                ("b21-40", "Bölüm 21–40", 21, 40, "Kahramanmaraş'tan Erzincan'a"),
                ("b41-60", "Bölüm 41–60", 41, 60, "Erzurum'dan Zonguldak'a"),
                ("b61-100", "Bölüm 61–100", 61, 100, "Düzce'den Kayseri'ye, final")]
    data = dict(stil=STIL, kapak_stil=KAPAK_STIL, karakterler=karakterler,
                sezonlar=[dict(id=a, ad=b, ilk=c, son=d, alt=e) for a, b, c, d, e in sezonlar], bolumler=bolumler)
    return data, uyari


if __name__ == "__main__":
    data, uyari = derle()
    with io.open(os.path.join(HERE, "sablon.html"), encoding="utf-8") as fh:
        html = fh.read()
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    assert "/*__DATA__*/null" in html
    html = html.replace("/*__DATA__*/null", js)
    with io.open(os.path.join(HERE, "..", "kasa", "kasa-motor.js"), encoding="utf-8") as fh:
        motor = fh.read().strip("\n")
    assert "/*__KASA_MOTOR__*/" in html
    html = html.replace("/*__KASA_MOTOR__*/", motor)
    out = os.path.join(HERE, "dedemin-defteri-flow.html")
    with io.open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    n = sum(len(b["sahneler"]) for b in data["bolumler"])
    print("Bölüm:", len(data["bolumler"]), " Sahne:", n, " Boyut: %.0f KB" % (len(html.encode("utf-8")) / 1024))
    for u in uyari:
        print("UYARI:", u)
