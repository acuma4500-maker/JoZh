# -*- coding: utf-8 -*-
"""Mert ile Ali: bölüm montaj aracı.

Klasör düzeni (girdi/):
    girdi/bolum-01/kapak.png      bölümün kapak fotoğrafı (jpg/png/webp olabilir)
    girdi/bolum-01/01.mp4         Flow'dan gelen sahneler, dosya adına göre sıralanır
    girdi/bolum-01/02.mp4 ...
    girdi/bolum-02/kapak.png      bir sonraki bölümün kapağı "pek yakında" kartında kullanılır

Her bölüm için cikti/mert-ali-bolum-01.mp4 üretilir:
    [kapak + "BÖLÜM 1" yazısı, 1.2 sn] -> [sahneler arka arkaya] -> [sonraki bölümün kapağı + "BÖLÜM 2 · PEK YAKINDA", 3 sn]

Kullanım:
    python3 montaj.py            # girdi/ içindeki tüm bölümler
    python3 montaj.py 3          # sadece bölüm 3
    python3 montaj.py 1-20       # 1'den 20'ye
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

KOK = Path(__file__).resolve().parent
GIRDI = KOK / "girdi"
CIKTI = KOK / "cikti"

DIZI_ADI = "MERT İLE ALİ"
W, H, FPS = 1080, 1920, 30
KAPAK_SN = 1.2          # başta kapak ne kadar kalsın (uzun tutma, Reels'te izleyici kaçar)
YAKINDA_SN = 3.0        # sondaki "pek yakında" kartı
SON_BOLUM = None        # son bölümün numarası belliyse yaz; o bölümde "pek yakında" kartı "SEZON FİNALİ" olur

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
RESIM = (".png", ".jpg", ".jpeg", ".webp")
VIDEO = (".mp4", ".mov", ".m4v", ".webm")

# Tüm parçalar aynı biçime getirilir ki birleştirme sorunsuz olsun.
NORMAL = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"setsar=1,fps={FPS},format=yuv420p")
KOD = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


def calistir(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args])
    if r.returncode:
        sys.exit(f"ffmpeg hata verdi: {' '.join(args)}")


def ses_var_mi(dosya):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                        "stream=index", "-of", "csv=p=0", str(dosya)], capture_output=True, text=True)
    return bool(r.stdout.strip())


def yazi(metin, boyut, y, renk="white"):
    metin = metin.replace(":", r"\:").replace("'", "’")
    return (f"drawtext=fontfile={FONT}:text='{metin}':fontsize={boyut}:fontcolor={renk}:"
            f"x=(w-text_w)/2:y={y}:borderw=6:bordercolor=black@0.85:shadowx=0:shadowy=4:shadowcolor=black@0.6")


def kapak_bul(klasor):
    if not klasor.is_dir():
        return None
    for d in sorted(klasor.iterdir()):
        if d.suffix.lower() in RESIM and d.stem.lower().startswith("kapak"):
            return d
    return None


def resimden_klip(resim, sure, filtre, hedef):
    """Fotoğraftan sessiz, hafif yakınlaşan bir klip üretir."""
    kare = int(sure * FPS)
    zoom = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='1+0.04*on/{kare}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={kare}:s={W}x{H}:fps={FPS}")
    calistir(["-loop", "1", "-i", str(resim), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
              "-t", f"{sure}", "-vf", f"{zoom},{filtre},setsar=1,format=yuv420p", *KOD, "-shortest", str(hedef)])


def sahne_normalle(video, hedef):
    if ses_var_mi(video):
        calistir(["-i", str(video), "-vf", NORMAL, *KOD, str(hedef)])
    else:
        calistir(["-i", str(video), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                  "-vf", NORMAL, *KOD, "-shortest", str(hedef)])


def bolum_yap(n):
    klasor = GIRDI / f"bolum-{n:02d}"
    sahneler = sorted(d for d in klasor.iterdir() if d.suffix.lower() in VIDEO)
    if not sahneler:
        print(f"Bölüm {n}: video yok, atlandı.")
        return
    kapak = kapak_bul(klasor)
    sonraki = kapak_bul(GIRDI / f"bolum-{n+1:02d}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        parcalar = []

        if kapak:
            p = tmp / "00_kapak.mp4"
            resimden_klip(kapak, KAPAK_SN,
                          yazi(DIZI_ADI, 86, "h*0.07") + "," + yazi(f"BÖLÜM {n}", 120, "h*0.07+120", "#FFD23F"), p)
            parcalar.append(p)
        else:
            print(f"Bölüm {n}: kapak.png yok, kapaksız birleştiriliyor.")

        for i, s in enumerate(sahneler, 1):
            p = tmp / f"{i:02d}_sahne.mp4"
            sahne_normalle(s, p)
            parcalar.append(p)

        # Sonraki bölümün kapağı varsa onu, yoksa bu bölümün kapağını karartıp kullan.
        arka = sonraki or kapak
        if arka:
            p = tmp / "99_yakinda.mp4"
            if SON_BOLUM and n >= SON_BOLUM:
                ust, alt = "SEZON FİNALİ", "İZLEDİĞİNİZ İÇİN TEŞEKKÜRLER"
            else:
                ust, alt = f"BÖLÜM {n+1}", "PEK YAKINDA"
            karart = "eq=brightness=-0.18:saturation=0.85" if sonraki else "gblur=sigma=18,eq=brightness=-0.3"
            resimden_klip(arka, YAKINDA_SN,
                          f"{karart},fade=t=in:st=0:d=0.4,"
                          + yazi(ust, 130, "h*0.40", "#FFD23F") + "," + yazi(alt, 96, "h*0.40+160")
                          + "," + yazi("Takipte kal", 58, "h*0.40+300"), p)
            parcalar.append(p)

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
        sys.exit(f"{GIRDI} klasörü yok. Videoları girdi/bolum-01/ gibi klasörlere koy.")
    for n in secim(sys.argv[1] if len(sys.argv) > 1 else ""):
        bolum_yap(n)
