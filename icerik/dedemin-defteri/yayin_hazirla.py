# -*- coding: utf-8 -*-
"""GitHub Pages için yayın sayfalarını hazırlar.

Artifact biçimindeki sayfalar (title, meta, style, içerik, script) tam HTML iskeleti taşımaz;
Artifact bunu yayınlarken ekler. GitHub'dan doğrudan açılınca telefonda küçük görünmesin diye
bu betik aynı sayfaları tam HTML iskeletiyle yayin/ klasörüne yazar ve bir bağlantı sayfası ekler.

Kullanım: önce flow/build.py ile dedemin-defteri-flow.html'i üret, sonra
    python3 yayin_hazirla.py
"""
import os
import re

KOK = os.path.dirname(os.path.abspath(__file__))
SAYFALAR = [
    ("flow/dedemin-defteri-flow.html", "yayin/dedemin-defteri.html"),
    ("kasa/kasa-prompt.html", "yayin/kasa-prompt.html"),
]

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

BAGLANTI = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>Dedemin Defteri</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:wght@700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{color-scheme:light;--paper:#f5f6f1;--sheet:#ffffff;--ink:#1d2433;--ink-soft:#5b6372;--rule:#d9dccf;--up:#2f6f62;
  --f-display:"Alegreya",Georgia,serif;--f-body:"Source Sans 3","Segoe UI",system-ui,sans-serif;--f-mono:"JetBrains Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme: dark){:root{color-scheme:dark;--paper:#141922;--sheet:#1b212c;--ink:#e7e9e2;--ink-soft:#a3a9b4;--rule:#2e3644;--up:#6fbfad}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f-body);font-size:16px;line-height:1.55}
main{max-width:560px;margin:0 auto;padding:32px max(16px,env(safe-area-inset-right,0px)) calc(48px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));display:grid;gap:14px}
.eyebrow{font-family:var(--f-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--up)}
h1{font-family:var(--f-display);font-weight:800;font-size:clamp(34px,9vw,48px);line-height:1.03;margin:0}
.lede{margin:0 0 8px;color:var(--ink-soft)}
a.kart{display:grid;gap:4px;padding:18px;background:var(--sheet);border:1px solid var(--rule);border-radius:12px;color:inherit;text-decoration:none;min-height:88px}
a.kart:hover{border-color:var(--ink-soft)}
a.kart:focus-visible{outline:2px solid var(--up);outline-offset:2px}
.k{font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft)}
.ad{font-family:var(--f-display);font-weight:700;font-size:24px;line-height:1.15}
.ac{color:var(--ink-soft)}
</style>
</head>
<body>
<main>
  <span class="eyebrow">Instagram Reels · AI animasyon · Sezon 1</span>
  <h1>Dedemin Defteri</h1>
  <p class="lede">Flow için sahne promptları ve kasa aracı.</p>
  <a class="kart" href="dedemin-defteri.html"><span class="k">100 bölüm · 600 sahne</span><span class="ad">Sahne promptları</span><span class="ac">Saat, yer, ışık, kamera ve kasa videosu. Her sahnenin kopyala düğmesi var.</span></a>
  <a class="kart" href="kasa-prompt.html"><span class="k">Sabit prompt</span><span class="ad">Kasa Prompt Aracı</span><span class="ac">Bakiye değişimini yaz, kasa videosunun promptunu kopyala.</span></a>
</main>
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
    for kaynak, hedef in SAYFALAR:
        with open(os.path.join(KOK, kaynak), encoding="utf-8") as f:
            head, body = sar(f.read())
        with open(os.path.join(KOK, hedef), "w", encoding="utf-8") as f:
            f.write(ISKELET.replace("@@HEAD@@", head).replace("@@BODY@@", body))
        print("yazıldı:", hedef)
    with open(os.path.join(KOK, "yayin/index.html"), "w", encoding="utf-8") as f:
        f.write(BAGLANTI)
    print("yazıldı: yayin/index.html")


if __name__ == "__main__":
    main()
