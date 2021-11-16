import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "saldo: 11.0")

    def test_rahan_ottaminen_saldo_vahenee_jos_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_rahan_ottaminen_saldo_ei_vahene_jos_summa_liian_suuri(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_ottaminen_true_jos_saldo_vaheni(self):
        boolean = self.maksukortti.ota_rahaa(500)
        self.assertEqual(boolean, True)

    def test_rahan_ottaminen_false_jos_saldo_ei_vahentynyt(self):
        boolean = self.maksukortti.ota_rahaa(1100)
        self.assertEqual(boolean, False)