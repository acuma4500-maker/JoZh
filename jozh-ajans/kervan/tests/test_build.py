# -*- coding: utf-8 -*-
import io
import os
import subprocess
import sys
import unittest

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CIKTI = os.path.join(KOK, "yayin", "kervan.html")


def calistir(*arg):
    return subprocess.run([sys.executable, "build.py"] + list(arg), cwd=KOK, capture_output=True, text=True)


class Build(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sonuc = calistir("kismi")
        with io.open(CIKTI, encoding="utf-8") as fh:
            cls.html = fh.read()

    def test_build_kismi(self):
        self.assertEqual(self.sonuc.returncode, 0, self.sonuc.stdout + self.sonuc.stderr)

    def test_sayfa_icerik(self):
        for parca in ("const KasaMotor", "B01-S15", "kervan.dizi", "PEK YAKINDA", "200.000", "İstanbul",
                      "<title>Kervan</title>", "Üç genç, tek bir hayal"):
            self.assertIn(parca, self.html, parca)

    def test_script_kapanmiyor(self):
        govde = self.html.split('<script id="veri" type="application/json">', 1)[1].split("</script>", 1)[0]
        self.assertNotIn("<!--", govde)
        self.assertIn('"no": 1', govde)

    def test_build_tam_eksik(self):
        import bolumler
        if len(bolumler.yukle()) == 50:
            self.skipTest("50 bölüm tamam")
        self.assertEqual(calistir().returncode, 1)


if __name__ == "__main__":
    unittest.main()
