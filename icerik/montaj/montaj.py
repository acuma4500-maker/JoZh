# -*- coding: utf-8 -*-
"""Bölüm montaj aracı: Mert ile Ali (JOZH STUDIOS) ve Dedemin Defteri.

Klasör düzeni:
    girdi/<dizi>/bolum-07/kapak.png       bölümün kapağı (yazısı görselin içinde)
    girdi/<dizi>/bolum-07/yakinda.png     bölümün "pek yakında" kapağı
    girdi/<dizi>/bolum-07/7.1.mp4 … 7.6.mp4   sahneler (dosya adındaki SON sayı = sahne numarası; 1.mp4 de olur)
    <dizi> = mert-ali | dedemin-defteri

Her bölüm için cikti/<dizi>/<dizi>-bolum-07.mp4:
    [bu bölümün kapağı, 1.2 sn]
    -> [sahneler; kasa açıldıysa sağ üstte KASA sayacı, rakamlar dizinin kendi kasa hesabından]
       (Dedemin Defteri: sahne notundaki yer-zaman yazısı da altta belirir, ör. "KAYSERİ · GÜN 4 · 09:40")
    -> [SONRAKİ bölümün "pek yakında" kapağı, 3 sn]
Sonraki bölümün yakinda.png'si yoksa: onun kapağı / bu bölümün kapağı / son sahnenin son karesi
karartılıp üstüne "BÖLÜM 8 / adı / PEK YAKINDA" yazılır.

Kullanım:
    python3 montaj.py mert-ali 1-20
    python3 montaj.py dedemin-defteri 7
    seçenekler: --kasasiz (sayaç yok)  --yazisiz (yer-zaman yazısı yok)
"""
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

KOK = Path(__file__).resolve().parent
ICERIK = KOK.parent

W, H, FPS = 1080, 1920, 30
KAPAK_SN = 1.2
YAKINDA_SN = 3.0
YAZI_SN = 3.0           # yer-zaman yazısı ekranda kalma süresi

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_TL = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"   # ₺ işareti için (DejaVu'da yok)
RESIM = (".png", ".jpg", ".jpeg", ".webp")
VIDEO = (".mp4", ".mov", ".m4v", ".webm")

NORMAL = (f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},"
          f"setsar=1,fps={FPS},format=yuv420p")
KOD = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


# ------------------------------------------------------------------ diziler
def mert_ali():
    s = (ICERIK / "jozh-studios" / "js" / "data.js").read_text(encoding="utf-8")
    D = json.loads(s[s.index("{"):s.rstrip().rstrip(";").rindex("}") + 1])
    T = D["tipler"]
    out, bal = {}, None
    for b in D["bolumler"]:
        kasa = {}
        for sc in b["sahneler"]:
            bas, acilis = bal, False
            for t in sc["tx"]:
                if t["tip"] == "acilis":
                    bal, acilis = 0, True
                bal = (bal or 0) + T[t["tip"]]["isaret"] * t["tutar"]
            if bal is not None:
                kasa[sc["n"]] = (0 if acilis else bas, bal)
        out[b["no"]] = dict(baslik=b["baslik"], kasa=kasa, yazi={})
    return out, "TL"


def dedemin_defteri():
    flow = ICERIK / "dedemin-defteri" / "flow"
    sys.path.insert(0, str(flow))
    build = importlib.import_module("build")
    D, _ = build.derle()
    out = {}
    on = "Ekrana yazı ekle (kurguda): "
    for b in D["bolumler"]:
        kasa = {s["n"]: (s["kv"]["onceki"], s["kv"]["simdi"]) for s in b["sahneler"] if s["kv"]}
        yazi = {s["n"]: k[len(on):] for s in b["sahneler"] for k in s["kurgu"] if k.startswith(on)}
        out[b["no"]] = dict(baslik=b["baslik"], kasa=kasa, yazi=yazi)
    return out, "₺"


DIZILER = {"mert-ali": mert_ali, "dedemin-defteri": dedemin_defteri}


# ------------------------------------------------------------------ yardımcılar
def calistir(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args])
    if r.returncode:
        sys.exit("ffmpeg hata verdi.")


def ses_var_mi(dosya):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                        "stream=index", "-of", "csv=p=0", str(dosya)], capture_output=True, text=True)
    return bool(r.stdout.strip())


def sayi(n):
    return "{:,}".format(abs(int(n))).replace(",", ".")


def tr_upper(s):
    return s.replace("i", "İ").replace("ı", "I").upper()


def yazi(metin, boyut, y, renk="white"):
    metin = metin.replace("\\", "").replace(":", r"\:").replace("'", "’").replace("%", r"\%")
    return (f"drawtext=fontfile={FONT}:text='{metin}':fontsize={boyut}:fontcolor={renk}:"
            f"x=(w-text_w)/2:y={y}:borderw=6:bordercolor=black@0.85:shadowx=0:shadowy=4:shadowcolor=black@0.6")


def resim_bul(klasor, ad):
    if not klasor.is_dir():
        return None
    for d in sorted(klasor.iterdir()):
        if d.suffix.lower() in RESIM and d.stem.lower() == ad:
            return d
    return None


# ------------------------------------------------------------------ katmanlar (şeffaf PNG kareleri)
def metin_ciz(d, x_sag, y, parcalar):
    """parcalar: [(metin, font, renk)] sağa yaslı tek satır."""
    gen = sum(d.textlength(m, font=f) for m, f, _ in parcalar)
    x = x_sag - gen
    for m, f, c in parcalar:
        d.text((x, y), m, font=f, fill=c, stroke_width=5, stroke_fill=(0, 0, 0, int(c[3] * 0.75)))
        x += d.textlength(m, font=f)


def kasa_kareleri(once, sonra, birim, klasor):
    """0-1 sn eski bakiye, 1-1.4 değişim satırı belirir, 1.4-3.4 sayaç akar, sonra son kare donar."""
    klasor.mkdir()
    fb, fk, fd = ImageFont.truetype(FONT_MONO, 62), ImageFont.truetype(FONT, 28), ImageFont.truetype(FONT_MONO, 42)
    tlb = ImageFont.truetype(FONT_TL, 62) if birim == "₺" else fb
    tld = ImageFont.truetype(FONT_TL, 42) if birim == "₺" else fd
    fark = sonra - once
    renk = (0, 230, 118) if fark > 0 else (255, 23, 68)
    BW, BH = 560, 200
    kare_say = 1 if fark == 0 else int(3.4 * FPS) + 1

    def ciz(t):
        im = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        if fark == 0 or t >= 3.4:
            deger, alfa = sonra, 1.0
        else:
            k = min(max((t - 1.4) / 2.0, 0), 1)
            deger = round(once + fark * k * k * (3 - 2 * k))
            alfa = min(max((t - 1.0) / 0.4, 0), 1)
        beyaz = (255, 255, 255, 255)
        metin_ciz(d, BW, 0, [("KASA", fk, (210, 210, 210, 255))])
        metin_ciz(d, BW, 38, [(sayi(deger) + " ", fb, beyaz), (birim, tlb, beyaz)])
        if fark != 0 and alfa > 0:
            c = renk + (int(255 * alfa),)
            metin_ciz(d, BW, 112, [(("+" if fark > 0 else "−") + sayi(fark) + " ", fd, c), (birim, tld, c)])
        return im

    for i in range(kare_say):
        ciz(i / FPS).save(klasor / f"{i:04d}.png")
    return BW


def yazi_kareleri(metin, klasor):
    """Alt bölümde sola yaslı yer-zaman yazısı: 0.3 sn belirir, YAZI_SN'de 0.4 sn'de kaybolur."""
    klasor.mkdir()
    f = ImageFont.truetype(FONT, 46)
    gen = int(ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(metin, font=f)) + 40
    BW = min(gen, W - 100)
    while f.size > 24 and ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(metin, font=f) > BW - 30:
        f = ImageFont.truetype(FONT, f.size - 2)
    son = int((YAZI_SN + 0.4) * FPS)
    for i in range(son + 1):
        t = i / FPS
        a = min(t / 0.3, 1) if t < YAZI_SN else max(1 - (t - YAZI_SN) / 0.4, 0)
        im = Image.new("RGBA", (BW, 80), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 8, 8, 70), fill=(255, 210, 63, int(255 * a)))
        d.text((24, 12), metin, font=f, fill=(255, 255, 255, int(255 * a)),
               stroke_width=4, stroke_fill=(0, 0, 0, int(190 * a)))
        im.save(klasor / f"{i:04d}.png")
    return BW


# ------------------------------------------------------------------ parçalar
def resimden_klip(resim, sure, filtre, hedef):
    kare = int(sure * FPS)
    zoom = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='1+0.03*on/{kare}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={kare}:s={W}x{H}:fps={FPS}")
    vf = zoom + ("," + filtre if filtre else "") + ",setsar=1,format=yuv420p"
    calistir(["-loop", "1", "-i", str(resim), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
              "-t", f"{sure}", "-vf", vf, *KOD, "-shortest", str(hedef)])


def sahne_yap(video, katmanlar, hedef):
    """katmanlar: [(png_klasörü, x, y, son_kareyi_tut)]"""
    girdiler = ["-i", str(video)]
    ses = ses_var_mi(video)
    if not ses:
        girdiler += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
    ilk = 1 if ses else 2
    fc, son = [f"[0:v]{NORMAL}[v0]"], "v0"
    for i, (kl, x, y, tut) in enumerate(katmanlar):
        girdiler += ["-framerate", str(FPS), "-i", str(kl / "%04d.png")]
        eof = "repeat" if tut else "pass"
        fc.append(f"[{son}][{ilk + i}:v]overlay=x={x}:y={y}:eof_action={eof}:shortest=0[v{i + 1}]")
        son = f"v{i + 1}"
    sure = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
                          capture_output=True, text=True).stdout.strip()
    calistir([*girdiler, "-filter_complex", ";".join(fc) + f";[{son}]format=yuv420p[o]",
              "-map", "[o]", "-map", "0:a" if ses else "1:a", *KOD, "-t", sure, str(hedef)])


def bolum_yap(dizi, n, EP, birim, kasali, yazili):
    girdi = KOK / "girdi" / dizi
    klasor = girdi / f"bolum-{n:02d}"
    sahneler = []
    for d in klasor.iterdir():
        sayilar = re.findall(r"\d+", d.stem)
        if d.suffix.lower() in VIDEO and sayilar:
            sahneler.append((int(sayilar[-1]), d.name, d))
    sahneler.sort()
    if not sahneler:
        print(f"Bölüm {n}: video yok, atlandı.")
        return
    ep = EP.get(n, dict(kasa={}, yazi={}))
    kapak = resim_bul(klasor, "kapak")
    sonraki_klasor = girdi / f"bolum-{n + 1:02d}"
    yakinda = resim_bul(sonraki_klasor, "yakinda")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        parcalar = []
        if kapak:
            p = tmp / "000_kapak.mp4"
            resimden_klip(kapak, KAPAK_SN, "", p)
            parcalar.append(p)
        else:
            print(f"Bölüm {n}: kapak.png yok, kapaksız birleştiriliyor.")

        for i, (sn, _, video) in enumerate(sahneler):
            kat = []
            if kasali and sn in ep["kasa"]:
                once, sonra = ep["kasa"][sn]
                bw = kasa_kareleri(once, sonra, birim, tmp / f"kasa_{i}")
                kat.append((tmp / f"kasa_{i}", W - bw - 54, int(H * 0.06), True))
            if yazili and sn in ep["yazi"]:
                yazi_kareleri(ep["yazi"][sn], tmp / f"yazi_{i}")
                kat.append((tmp / f"yazi_{i}", 50, int(H * 0.80), False))
            p = tmp / f"{i + 1:03d}_sahne.mp4"
            sahne_yap(video, kat, p)
            parcalar.append(p)

        p = tmp / "999_yakinda.mp4"
        if yakinda:
            resimden_klip(yakinda, YAKINDA_SN, "fade=t=in:st=0:d=0.3", p)
            parcalar.append(p)
        elif (n + 1) in EP:
            arka = resim_bul(sonraki_klasor, "kapak") or kapak
            if not arka:
                arka = tmp / "son_kare.png"
                calistir(["-sseof", "-0.2", "-i", str(sahneler[-1][2]), "-frames:v", "1", "-update", "1", str(arka)])
            ad = tr_upper(EP[n + 1]["baslik"])
            resimden_klip(arka, YAKINDA_SN,
                          "gblur=sigma=14,eq=brightness=-0.28,fade=t=in:st=0:d=0.3,"
                          + yazi(f"BÖLÜM {n + 1}", 84, "h*0.10", "#FFD23F") + "," + yazi(ad, 74, "h*0.10+110")
                          + "," + yazi("PEK YAKINDA", 130, "h*0.45", "#FFD23F"), p)
            parcalar.append(p)
            print(f"Bölüm {n}: {n + 1}. bölümün yakinda.png'si yok, yazılı yedek kart kullanıldı.")

        liste = tmp / "liste.txt"
        liste.write_text("".join(f"file '{p}'\n" for p in parcalar), encoding="utf-8")
        cikti = KOK / "cikti" / dizi
        cikti.mkdir(parents=True, exist_ok=True)
        hedef = cikti / f"{dizi}-bolum-{n:02d}.mp4"
        calistir(["-f", "concat", "-safe", "0", "-i", str(liste), "-c", "copy", "-movflags", "+faststart", str(hedef)])
    print(f"Bölüm {n}: {len(sahneler)} sahne -> {hedef.relative_to(KOK)}")


def secim(girdi, arg):
    var = sorted(int(d.name.split("-")[1]) for d in girdi.glob("bolum-*") if d.name.split("-")[1].isdigit())
    if not arg:
        return var
    if "-" in arg:
        a, b = map(int, arg.split("-"))
        return [n for n in var if a <= n <= b]
    return [int(arg)]


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or args[0] not in DIZILER:
        sys.exit("Kullanım: python3 montaj.py <" + "|".join(DIZILER) + "> [bölüm ya da 1-20]")
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg kurulu değil.")
    dizi = args[0]
    girdi = KOK / "girdi" / dizi
    if not girdi.is_dir():
        sys.exit(f"{girdi} klasörü yok. Videoları girdi/{dizi}/bolum-01/ gibi klasörlere koy.")
    EP, birim = DIZILER[dizi]()
    for n in secim(girdi, args[1] if len(args) > 1 else ""):
        bolum_yap(dizi, n, EP, birim, "--kasasiz" not in sys.argv, "--yazisiz" not in sys.argv)
