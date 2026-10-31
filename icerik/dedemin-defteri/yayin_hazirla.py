# -*- coding: utf-8 -*-
"""GitHub Pages için yayın sayfasını hazırlar.

Artifact biçimindeki sayfa (title, meta, style, içerik, script) tam HTML iskeleti taşımaz;
Artifact bunu yayınlarken ekler. GitHub'dan doğrudan açılınca telefonda küçük görünmesin diye
bu betik aynı sayfayı tam HTML iskeletiyle yayin/index.html olarak yazar. Tek sayfa vardır:
Dedemin Defteri (sahne promptları, kasa promptları ve Kasa aracı sekmesi içinde).
Eski adresler (dedemin-defteri.html, kasa-prompt.html) küçük yönlendirme sayfalarıdır.

Kullanım: python3 icerik/dedemin-defteri/uret.py   (build.py'den sonra bunu da çalıştırır)
"""
import os
import re

KOK = os.path.dirname(os.path.abspath(__file__))
KAYNAK = "flow/dedemin-defteri-flow.html"
HEDEF = "yayin/index.html"
# eski adres -> (yönlendirme hedefi, betik)
YONLENDIR = {
    "yayin/dedemin-defteri.html": ("./index.html", 'location.replace("./index.html" + location.hash);'),
    "yayin/kasa-prompt.html": ("./index.html#kasa", 'location.replace("./index.html#kasa");'),
}

# Parçanın başındaki title/meta/link/style blokları head'e, geri kalanı body'ye gider.
BASLIK = re.compile(r"\s*(<title>.*?</title>|<meta\b[^>]*>|<link\b[^>]*>|<style\b[^>]*>.*?</style>)", re.S)

ISKELET = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
@@HEAD@@
</head>
<body>
@@BODY@@
</body>
</html>
"""

YONLENDIRME = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta http-equiv="refresh" content="0; url=@@HEDEF@@">
<title>Dedemin Defteri</title>
</head>
<body>
<p><a href="@@HEDEF@@">Dedemin Defteri sayfasına git</a></p>
<script>@@JS@@</script>
</body>
</html>
"""


def sar(parca):
    konum, bas = 0, []
    while True:
        m = BASLIK.match(parca, konum)
        if not m:
            break
        bas.append(m.group(1))
        konum = m.end()
    head = "\n".join(bas)
    assert "<title>" in head, "parçanın başında <title> yok"
    return head, parca[konum:].lstrip("\n")


def main():
    os.makedirs(os.path.join(KOK, "yayin"), exist_ok=True)
    with open(os.path.join(KOK, KAYNAK), encoding="utf-8") as f:
        head, body = sar(f.read())
    with open(os.path.join(KOK, HEDEF), "w", encoding="utf-8") as f:
        f.write(ISKELET.replace("@@HEAD@@", head).replace("@@BODY@@", body))
    print("yazıldı:", HEDEF)
    for yol, (hedef, js) in YONLENDIR.items():
        with open(os.path.join(KOK, yol), "w", encoding="utf-8") as f:
            f.write(YONLENDIRME.replace("@@HEDEF@@", hedef).replace("@@JS@@", js))
        print("yazıldı:", yol, "->", hedef)


if __name__ == "__main__":
    main()
