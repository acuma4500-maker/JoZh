# -*- coding: utf-8 -*-
import io
import os
import re
import unittest

from karakterler import K, SOGUK
import sablonlar as s

SPEC = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "superpowers", "specs",
                    "2026-11-05-kervan-design.md")


def spec_blogu(baslik):
    """Spec'te verilen başlıktan sonraki ilk ``` kod bloğu."""
    with io.open(SPEC, encoding="utf-8") as fh:
        metin = fh.read()
    sonra = metin[metin.index(baslik):]
    return re.search(r"```\n(.*?)\n```", sonra, re.S).group(1)


def sabit_satirlar(blok):
    return [l for l in blok.split("\n") if l.strip() and "[" not in l]


def sirali_icerir(test, satirlar, metin):
    yer = 0
    for l in satirlar:
        i = metin.find(l, yer)
        test.assertNotEqual(i, -1, "eksik/yer değiştirmiş satır: %r" % l)
        yer = i + len(l)


KAPAK = dict(no=5, baslik="FIRTINA", ana="kerem", yanlar=["defne", "kaan"],
             mekan="Çanakkale ferry port at dusk.", kompozisyon="Kerem in front holding the notebook.",
             duygu="Tense, stormy.")
SAHNE = dict(no=3, rol="TRADE", kimler=["defne", "kaan"], mekan="Edirne bazaar, morning.",
             aksiyon=("Defne opens a box.", "Kaan sniffs the soap.", "The seller frowns."),
             kamera="Fast push-in.", replik=("Defne", "Bu fiyata olmaz, abi."), ses="Bazaar noise.",
             duygu="Playful tension.")
PARANTEZ = re.compile(r"\[[A-ZÇĞİÖŞÜÂ ]{3,}")


class Sablonlar(unittest.TestCase):
    def test_kapak1_birebir(self):
        out = s.kapak1(**KAPAK)
        sirali_icerir(self, sabit_satirlar(spec_blogu("### 4.1")), out)
        self.assertIn("“BÖLÜM 5”", out)
        self.assertIn("“FIRTINA”", out)
        self.assertIn("Episode 5 of", out)

    def test_kapak1_karakterler(self):
        out = s.kapak1(**KAPAK)
        for ad in ("kerem", "defne", "kaan"):
            self.assertIn(K[ad], out)
        self.assertLess(out.index(K["kerem"]), out.index(K["defne"]))

    def test_kapak2_pek_yakinda(self):
        out = s.kapak2(**KAPAK)
        k1 = sabit_satirlar(spec_blogu("### 4.1"))
        kapanis = k1.index("The ONLY permitted text elements are:")
        sirali_icerir(self, k1[:kapanis], out)
        sirali_icerir(self, sabit_satirlar(spec_blogu("### 4.2")), out)
        self.assertEqual(out.count("The ONLY permitted text elements are:"), 1)
        self.assertTrue(out.rstrip().endswith("“PEK YAKINDA”"))

    def test_senaryo_birebir(self):
        out = s.senaryo(**SAHNE)
        sirali_icerir(self, sabit_satirlar(spec_blogu("### 4.3")), out)
        self.assertIn("SCENE 3 OF 15 — ROLE: TRADE", out)
        self.assertIn('DEFNE: "Bu fiyata olmaz, abi."', out)
        self.assertIn(K["defne"], out)
        self.assertNotIn(K["kerem"], out)

    def test_parantez_kalmadi(self):
        for out in (s.kapak1(**KAPAK), s.kapak2(**KAPAK), s.senaryo(**SAHNE)):
            self.assertIsNone(PARANTEZ.search(out), PARANTEZ.search(out))

    def test_replik_yok(self):
        out = s.senaryo(**dict(SAHNE, replik=None))
        self.assertIn("DIALOGUE: No dialogue.", out)
        self.assertNotIn("LIP-SYNCED", out)

    def test_replik_siniri(self):
        with self.assertRaises(ValueError):
            s.senaryo(**dict(SAHNE, replik=("Kaan", "bir iki üç dört beş altı yedi sekiz dokuz")))

    def test_bilinmeyen_rol(self):
        with self.assertRaises(ValueError):
            s.senaryo(**dict(SAHNE, rol="DANCE"))

    def test_soguk(self):
        self.assertIn(SOGUK, s.senaryo(**dict(SAHNE, soguk=True)))
        self.assertIn(SOGUK, s.kapak1(**dict(KAPAK, soguk=True)))
        self.assertNotIn(SOGUK, s.senaryo(**SAHNE))

    def test_profil(self):
        out = s.profil_prompt()
        self.assertTrue(out.startswith("Square profile picture"))
        self.assertIn("No text", out)
        self.assertNotIn("```", out)


if __name__ == "__main__":
    unittest.main()
