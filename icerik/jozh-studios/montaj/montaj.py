# -*- coding: utf-8 -*-
"""JOZH STUDIOS · Mert ile Ali: bölüm montaj aracı.

Klasör düzeni (girdi/):
    girdi/bolum-07/kapak.png     bölümün kapağı (yazılı: "BÖLÜM 7 / KAYISININ BAŞKENTİ")
    girdi/bolum-07/yakinda.png   bölümün "pek yakında" kapağı (yazılı: "... PEK YAKINDA")
    girdi/bolum-07/1.mp4 ... 6.mp4   Flow'dan gelen sahneler; dosya adındaki ilk sayı = sahne numarası

Her bölüm için cikti/mert-ali-bolum-07.mp4 üretilir:
    [bu bölümün kapağı, 1.2 sn]
    -> [sahneler arka arkaya; kasa açıldıysa sağ üstte KASA sayacı, rakamlar panelin kasa defterinden]
    -> [SONRAKİ bölümün "pek yakında" kapağı, 3 sn]

Sonraki bölümün yakinda.png'si yoksa: onun kapak.png'si (ya da bu bölümün kapağı) karartılıp
üstüne "BÖLÜM 8 / PEK YAKINDA" yazısı montajda eklenir.

Kullanım:
    python3 montaj.py            # girdi/ içindeki tüm bölümler
    python3 montaj.py 7          # sadece bölüm 7
    python3 montaj.py 1-20       # 1'den 20'ye
    python3 montaj.py 1-20 --kasasiz   # kasa sayacı çizilmez
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

KOK = Path(__file__).resolve().parent
GIRDI = KOK / "girdi"
CIKTI = KOK / "cikti"
DATA_JS = KOK.parent / "js" / "data.js"

W, H, FPS = 1080, 1920, 30
KAPAK_SN = 1.2          # başta kapak (uzun tutma, Reels'te izleyici kaçar)
YAKINDA_SN = 3.0        # sondaki "pek yakında" kapağı

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
RESIM = (".png", ".jpg", ".jpeg", ".webp")
VIDEO = (".mp4", ".mov", ".m4v", ".webm")

NORMAL = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"setsar=1,fps={FPS},format=yuv420p")
KOD = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


# ------------------------------------------------------------------ yardımcılar
def calistir(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args])
    if r.returncode:
        sys.exit("ffmpeg hata verdi.")


def ses_var_mi(dosya):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                        "stream=index", "-of", "csv=p=0", str(dosya)], capture_output=True, text=True)
    return bool(r.stdout.strip())


def para(n):
    return "{:,}".format(abs(int(n))).replace(",", ".") + " TL"


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


# ------------------------------------------------------------------ kasa (panelin kasa defteriyle aynı hesap)
def veri_oku():
    s = DATA_JS.read_text(encoding="utf-8")
    return json.loads(s[s.index("{"):s.rstrip().rstrip(";").rindex("}") + 1])


def sahne_bakiyeleri(D):
    """{(bölüm, sahne): (önceki, sonraki)}; kasa açılmadan önceki sahneler yok."""
    T = D["tipler"]
    out, bal = {}, None
    for b in D["bolumler"]:
        for s in b["sahneler"]:
            bas, acilis = bal, False
            for t in s["tx"]:
                if t["tip"] == "acilis":
                    bal, acilis = 0, True
                bal = (bal or 0) + T[t["tip"]]["isaret"] * t["tutar"]
            if bal is not None:
                out[(b["no"], s["n"])] = (0 if acilis else bas, bal)
    return out


def kasa_kareleri(once, sonra, klasor):
    """Sağ üst köşe için şeffaf PNG kareleri: 0-1 sn eski bakiye, 1-1.4 değişim satırı belirir,
    1.4-3.4 sayaç akar, sonra son kare donar (overlay son kareyi tekrar eder)."""
    klasor.mkdir()
    fb = ImageFont.truetype(FONT_MONO, 62)
    fk = ImageFont.truetype(FONT, 28)
    fd = ImageFont.truetype(FONT_MONO, 42)
    fark = sonra - once
    renk = (0, 230, 118) if fark > 0 else (255, 23, 68)
    degisim = ("+" if fark > 0 else "−") + para(fark)
    BW, BH = 560, 200
    kare_say = 1 if fark == 0 else int(3.4 * FPS) + 1

    def ciz(t):
        im = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        if fark == 0 or t >= 3.4:
            deger, alfa = sonra, 1.0
        else:
            ilerle = min(max((t - 1.4) / 2.0, 0), 1)
            ilerle = ilerle * ilerle * (3 - 2 * ilerle)          # yumuşak başla, yumuşak dur
            deger = round(once + fark * ilerle)
            alfa = min(max((t - 1.0) / 0.4, 0), 1)
        satirlar = [("KASA", fk, (210, 210, 210, 255), 0), (para(deger), fb, (255, 255, 255, 255), 38)]
        if fark != 0 and alfa > 0:
            satirlar.append((degisim, fd, renk + (int(255 * alfa),), 112))
        for metin, f, c, y in satirlar:
            x = BW - d.textlength(metin, font=f)
            d.text((x, y), metin, font=f, fill=c, stroke_width=5, stroke_fill=(0, 0, 0, int(c[3] * 0.75)))
        return im

    for i in range(kare_say):
        ciz(i / FPS).save(klasor / f"{i:04d}.png")
    return BW


# ------------------------------------------------------------------ parçalar
def resimden_klip(resim, sure, filtre, hedef):
    kare = int(sure * FPS)
    zoom = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='1+0.03*on/{kare}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={kare}:s={W}x{H}:fps={FPS}")
    vf = zoom + ("," + filtre if filtre else "") + ",setsar=1,format=yuv420p"
    calistir(["-loop", "1", "-i", str(resim), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
              "-t", f"{sure}", "-vf", vf, *KOD, "-shortest", str(hedef)])


def sahne_yap(video, kasa_klasor, bw, hedef):
    girdiler = ["-i", str(video)]
    ses = ses_var_mi(video)
    if not ses:
        girdiler += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
    if kasa_klasor:
        k = 1 if ses else 2
        girdiler += ["-framerate", str(FPS), "-i", str(kasa_klasor / "%04d.png")]
        fc = (f"[0:v]{NORMAL}[v];[v][{k}:v]overlay=x={W - bw - 54}:y={int(H * 0.06)}:eof_action=repeat:shortest=0,"
              f"format=yuv420p[o]")
        harita = ["-filter_complex", fc, "-map", "[o]", "-map", "0:a" if ses else "1:a"]
    else:
        harita = ["-vf", NORMAL, "-map", "0:v", "-map", "0:a" if ses else "1:a"]
    sure = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
                          capture_output=True, text=True).stdout.strip()
    calistir([*girdiler, *harita, *KOD, "-t", sure, str(hedef)])


def bolum_yap(n, D, SB, kasali):
    klasor = GIRDI / f"bolum-{n:02d}"
    sahneler = []
    for d in klasor.iterdir():
        sayilar = re.findall(r"\d+", d.stem)        # "3.mp4" ya da "1.3.mp4" → sahne 3 (son sayı)
        if d.suffix.lower() in VIDEO and sayilar:
            sahneler.append((int(sayilar[-1]), d.name, d))
    sahneler.sort()
    if not sahneler:
        print(f"Bölüm {n}: video yok, atlandı.")
        return
    kapak = resim_bul(klasor, "kapak")
    sonraki_klasor = GIRDI / f"bolum-{n + 1:02d}"
    yakinda = resim_bul(sonraki_klasor, "yakinda")
    ep = {b["no"]: b for b in D["bolumler"]}

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
            kk, bw = None, 0
            if kasali and (n, sn) in SB:
                once, sonra = SB[(n, sn)]
                kk = tmp / f"kasa_{i}"
                bw = kasa_kareleri(once, sonra, kk)
            p = tmp / f"{i + 1:03d}_sahne.mp4"
            sahne_yap(video, kk, bw, p)
            parcalar.append(p)

        p = tmp / "999_yakinda.mp4"
        if yakinda:
            resimden_klip(yakinda, YAKINDA_SN, "fade=t=in:st=0:d=0.3", p)
            parcalar.append(p)
        else:
            arka = resim_bul(sonraki_klasor, "kapak") or kapak
            if not arka:                                   # hiç kapak yoksa: son sahnenin son karesi
                arka = tmp / "son_kare.png"
                calistir(["-sseof", "-0.2", "-i", str(sahneler[-1][2]), "-frames:v", "1", "-update", "1", str(arka)])
            if (n + 1) in ep:
                ad = tr_upper(ep[n + 1]["baslik"])
                resimden_klip(arka, YAKINDA_SN,
                              "gblur=sigma=14,eq=brightness=-0.28,fade=t=in:st=0:d=0.3,"
                              + yazi(f"BÖLÜM {n + 1}", 84, "h*0.10", "#FFD23F") + "," + yazi(ad, 74, "h*0.10+110")
                              + "," + yazi("PEK YAKINDA", 130, "h*0.45", "#FFD23F"), p)
                parcalar.append(p)
                print(f"Bölüm {n}: {n + 1}. bölümün yakinda.png'si yok, yazılı yedek kart kullanıldı.")

        liste = tmp / "liste.txt"
        liste.write_text("".join(f"file '{p}'\n" for p in parcalar), encoding="utf-8")
        CIKTI.mkdir(exist_ok=True)
        hedef = CIKTI / f"mert-ali-bolum-{n:02d}.mp4"
        calistir(["-f", "concat", "-safe", "0", "-i", str(liste), "-c", "copy", "-movflags", "+faststart", str(hedef)])
    print(f"Bölüm {n}: {len(sahneler)} sahne -> {hedef.relative_to(KOK)}")


def secim(arg):
    var = sorted(int(d.name.split("-")[1]) for d in GIRDI.glob("bolum-*") if d.name.split("-")[1].isdigit())
    if not arg:
        return var
    if "-" in arg:
        a, b = map(int, arg.split("-"))
        return [n for n in var if a <= n <= b]
    return [int(arg)]


if __name__ == "__main__":
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg kurulu değil.")
    if not GIRDI.is_dir():
        sys.exit(f"{GIRDI} klasörü yok. Videoları girdi/bolum-07/ gibi klasörlere koy.")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    D = veri_oku()
    SB = sahne_bakiyeleri(D)
    for n in secim(args[0] if args else ""):
        bolum_yap(n, D, SB, "--kasasiz" not in sys.argv)
