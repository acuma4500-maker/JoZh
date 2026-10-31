# -*- coding: utf-8 -*-
"""Kasa Prompt Aracı sayfasını üretir: kasa-prompt.sablon.html + kasa-motor.js -> kasa-prompt.html

Motor (kasa-motor.js) tek kaynaktır; Dedemin Defteri sayfası da flow/build.py ile aynı dosyayı içine alır.
Kullanım: python3 kasa/kasa_uret.py
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def uret():
    with io.open(os.path.join(HERE, "kasa-motor.js"), encoding="utf-8") as fh:
        motor = fh.read().strip("\n")
    with io.open(os.path.join(HERE, "kasa-prompt.sablon.html"), encoding="utf-8") as fh:
        sablon = fh.read()
    assert "/*__KASA_MOTOR__*/" in sablon, "şablonda motor yer tutucusu yok"
    html = sablon.replace("/*__KASA_MOTOR__*/", motor)
    with io.open(os.path.join(HERE, "kasa-prompt.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("yazıldı: kasa/kasa-prompt.html (%.0f KB)" % (len(html.encode("utf-8")) / 1024))


if __name__ == "__main__":
    uret()
