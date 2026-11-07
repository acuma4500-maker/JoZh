# -*- coding: utf-8 -*-
"""Yazılmış bölümleri yükler: bolumler/b01.py … b50.py (varsa). Her dosya BOLUMLER listesi verir."""
import importlib
import os
import re

_DIR = os.path.dirname(os.path.abspath(__file__))


def yukle():
    eps = []
    for ad in sorted(os.listdir(_DIR)):
        if re.fullmatch(r"b\d{2}\.py", ad):
            eps.extend(importlib.import_module("bolumler." + ad[:-3]).BOLUMLER)
    return sorted(eps, key=lambda e: e["no"])
