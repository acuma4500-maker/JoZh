# -*- coding: utf-8 -*-
"""Bütün sayfaları sırayla üretir: Kasa Prompt Aracı, Dedemin Defteri sayfası, GitHub Pages kopyaları.

Kullanım: python3 icerik/dedemin-defteri/uret.py
"""
import os
import subprocess
import sys

KOK = os.path.dirname(os.path.abspath(__file__))
ADIMLAR = [
    ("kasa", "kasa_uret.py"),
    ("flow", "build.py"),
    (".", "yayin_hazirla.py"),
]

for dizin, betik in ADIMLAR:
    print("==", os.path.join(dizin, betik) if dizin != "." else betik)
    subprocess.check_call([sys.executable, betik], cwd=os.path.join(KOK, dizin))
