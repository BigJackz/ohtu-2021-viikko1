import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 77)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uutta_varastoa_ei_voi_luoda_negatiivisella_tilavuudella(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_varaston_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
    def test_alku_saldo_ei_voi_olla_negatiivinen(self):
        varasto = Varasto(10, -5)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_yli_saldon_lisaa_maksimikapasiteettiin(self):
	    self.varasto.lisaa_varastoon(20)

	    self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_arvon_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-4)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_yli_saldon_ottaa_kaiken_mahdollisen_ei_enempää(self):
        self.varasto.lisaa_varastoon(7)
        
        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(saatu_maara, 7)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
