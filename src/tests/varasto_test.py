import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):

    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_saldo_pieni = Varasto(10, -1)
        self.varasto_saldo_suuri = Varasto(10, 11)
        self.varasto_tilavuus_pieni = Varasto(-1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_saldo_alle_nolla(self):
        self.assertAlmostEqual(self.varasto_saldo_pieni.saldo, 0)

    def test_uudella_varastolla_saldo_yli_tilavuus(self):
        self.assertAlmostEqual(self.varasto_saldo_suuri.saldo, 10)

    def test_uudella_varastolla_tilavuus_alle_nolla(self):
        self.assertAlmostEqual(self.varasto_tilavuus_pieni.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_alle_nolla_saldoa(self):
        self.varasto.lisaa_varastoon(-1)

        #Vapaata tilaa pitäisi olla nolla
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    
    def test_lisays_lisaa_enemmän_saldoa_kuin_tilaa(self):
        self.varasto.lisaa_varastoon(11)

        #Vapaata tilaa pitäisi olla alkuperäinen 10
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_ottaminen_palauttaa_nolla_kun_otetaan_alle_nolla(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara=self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8)


    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    

    def test_printtaus(self):
        vastaus = str(self.varasto)
        self.assertEqual(vastaus, "saldo = 0, vielä tilaa 10")
