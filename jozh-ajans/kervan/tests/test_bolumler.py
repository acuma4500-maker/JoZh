# -*- coding: utf-8 -*-
import json
import os
import subprocess
import unittest

import bolumler
import model
from rota import ROTA

MOTOR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "icerik", "dedemin-defteri", "kasa", "kasa-motor.js")
EPS = bolumler.yukle()


def _sahte(n_senaryo=15):
    b = ROTA[0]
    sc = [model.S("HOOK" if i == 0 else ("CLIFFHANGER" if i == n_senaryo - 1 else "TRADE"),
                  ["kerem"], "x", ("a", "b", "c"), "k", "s", "d") for i in range(n_senaryo)]
    sc[1]["kasa"] = (b["kasa_bas"], b["kasa_son"])
    return model.EP(1, "açıklama", ["#Kervan"], dict(ana="kerem", yanlar=["defne", "kaan"], mekan="m",
                    kompozisyon="k", duygu="d"), sc)


class Bolumler(unittest.TestCase):
    def test_en_az_bir_bolum(self):
        self.assertGreaterEqual(len(EPS), 1)
        self.assertEqual([e["no"] for e in EPS], list(range(1, len(EPS) + 1)))

    def test_denetle_temiz(self):
        self.assertEqual(model.denetle(EPS, tam=False), [])

    def test_on_bes_senaryo(self):
        for e in EPS:
            self.assertEqual(len(e["senaryolar"]), 15, "B%02d" % e["no"])

    def test_rol_sirasi(self):
        for e in EPS:
            self.assertEqual(e["senaryolar"][0]["rol"], "HOOK")
            self.assertEqual(e["senaryolar"][-1]["rol"], "CLIFFHANGER")

    def test_kasa_bolum_ici(self):
        for e in EPS:
            olaylar = [s["kasa"] for s in e["senaryolar"] if s["kasa"]]
            self.assertTrue(olaylar, "B%02d kasa olayı yok" % e["no"])
            self.assertEqual(olaylar[0][0], e["kasa_bas"])
            self.assertEqual(olaylar[-1][1], e["kasa_son"])
            for a, b in zip(olaylar, olaylar[1:]):
                self.assertEqual(b[0], a[1])

    def test_kasa_zinciri_dosyalar_arasi(self):
        for a, b in zip(EPS, EPS[1:]):
            self.assertEqual(b["kasa_bas"], a["kasa_son"])

    def test_sabit_kasalar(self):
        e = EPS[0]
        sabit = model.sabit_kasalar(e)
        kapsanan = sorted(n for _, nolar in sabit for n in nolar)
        degisen = [i + 1 for i, s in enumerate(e["senaryolar"]) if s["kasa"]]
        gizli = list(range(1, e["kasa_baslar"]))
        self.assertEqual(sorted(kapsanan + degisen + gizli), list(range(1, 16)))
        self.assertEqual(sabit[0][0], e["kasa_bas"])

    def test_aciklama(self):
        for e in EPS:
            self.assertLessEqual(len(e["aciklama"]), 2200)
            self.assertIn("#Kervan", e["etiketler"])

    def test_promptlar_uretiliyor(self):
        for e in EPS:
            p = model.promptlar(e)
            self.assertEqual(len(p["senaryolar"]), 15)
            self.assertIn("“BÖLÜM %d”" % e["no"], p["kapak1"])
            self.assertIn("PEK YAKINDA", p["kapak2"])

    def test_kasa_motoru(self):
        satirlar = ["%s → %s" % (model.para(a), model.para(b))
                    for e in EPS for s in e["senaryolar"] if s["kasa"] for a, b in [s["kasa"]]]
        js = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
              "vm.runInContext(fs.readFileSync(process.argv[1],'utf8')+';this.KM=KasaMotor;',c);"
              "const r=JSON.parse(process.argv[2]).map(l=>{const o=c.KM.parseLine(l);"
              "return o&&o.ok?'ok':l+': '+(o?o.msg:'boş')});console.log(JSON.stringify(r));")
        out = subprocess.run(["node", "-e", js, MOTOR, json.dumps(satirlar)], capture_output=True, text=True, check=True)
        self.assertEqual([r for r in json.loads(out.stdout) if r != "ok"], [])

    def test_denetle_hata_yakalar(self):
        self.assertEqual(model.denetle([_sahte()], tam=False), [])
        self.assertTrue(model.denetle([_sahte(14)], tam=False))
        self.assertTrue(model.denetle([_sahte()], tam=True))  # tam: 50 bölüm ister


if __name__ == "__main__":
    unittest.main()
