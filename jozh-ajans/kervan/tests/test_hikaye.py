# -*- coding: utf-8 -*-
import unittest

from karakterler import K, referans_prompt
from rota import ROTA

BOLGELER = {"Marmara", "Ege", "Akdeniz", "İç Anadolu", "Karadeniz", "Doğu Anadolu", "Güneydoğu Anadolu"}


class Hikaye(unittest.TestCase):
    def test_elli_bolum(self):
        self.assertEqual(len(ROTA), 50)
        self.assertEqual([b["no"] for b in ROTA], list(range(1, 51)))

    def test_kasa_baslangic(self):
        self.assertEqual(ROTA[0]["kasa_bas"], 200_000)

    def test_kasa_zinciri(self):
        for onceki, b in zip(ROTA, ROTA[1:]):
            self.assertEqual(b["kasa_bas"], onceki["kasa_son"], "B%02d" % b["no"])

    def test_kasa_hedef(self):
        self.assertTrue(2_700_000 <= ROTA[-1]["kasa_son"] <= 3_300_000)

    def test_kasa_pozitif(self):
        for b in ROTA:
            self.assertGreater(b["kasa_son"], 0)

    def test_kayiplar_var(self):
        self.assertGreaterEqual(sum(b["kasa_son"] < b["kasa_bas"] for b in ROTA), 6)

    def test_bolgeler(self):
        for b in ROTA:
            self.assertIn(b["bolge"], BOLGELER, "B%02d" % b["no"])
        for bolge in BOLGELER:
            self.assertGreaterEqual(sum(b["bolge"] == bolge for b in ROTA), 7, bolge)

    def test_yerler_farkli(self):
        self.assertEqual(len({b["sehir"] for b in ROTA}), 50)

    def test_ilk_sehir(self):
        self.assertEqual(ROTA[0]["sehir"], "İstanbul")

    def test_bos_alan_yok(self):
        for b in ROTA:
            for k, v in b.items():
                if isinstance(v, str):
                    self.assertTrue(v.strip(), "B%02d %s boş" % (b["no"], k))

    def test_karakterler(self):
        self.assertEqual(set(K), {"kerem", "defne", "kaan"})
        for ad, tarif in K.items():
            n = len(tarif.split())
            self.assertTrue(60 <= n <= 110, "%s: %d kelime" % (ad, n))
        self.assertIn("20", K["kerem"])
        self.assertIn("19", K["defne"])
        self.assertIn("18", K["kaan"])

    def test_referans_prompt(self):
        for ad in K:
            p = referans_prompt(ad)
            self.assertIn(K[ad], p)
            self.assertIn("No text", p)


if __name__ == "__main__":
    unittest.main()
