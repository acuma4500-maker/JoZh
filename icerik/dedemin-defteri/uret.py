# -*- coding: utf-8 -*-
"""Sayfayı baştan üretir: Dedemin Defteri sayfası (kasa motoru içinde), sonra GitHub Pages kopyası.

Kullanım: python3 icerik/dedemin-defteri/uret.py
"""
import os
import subprocess
import sys

KOK = os.path.dirname(os.path.abspath(__file__))
ADIMLAR = [
    ("flow", "build.py"),
    (".", "yayin_hazirla.py"),
]

for dizin, betik in ADIMLAR:
    print("==", os.path.join(dizin, betik) if dizin != "." else betik)
    subprocess.check_call([sys.executable, betik], cwd=os.path.join(KOK, dizin))
