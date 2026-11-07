# -*- coding: utf-8 -*-
"""Yazılmış bölümleri yükler: b01_10 … b41_50 (varsa)."""
import importlib


def yukle():
    eps = []
    for a in range(1, 51, 10):
        ad = "bolumler.b%02d_%02d" % (a, a + 9)
        try:
            mod = importlib.import_module(ad)
        except ModuleNotFoundError as ex:
            if ex.name != ad:
                raise
            continue
        eps.extend(mod.BOLUMLER)
    return sorted(eps, key=lambda e: e["no"])
