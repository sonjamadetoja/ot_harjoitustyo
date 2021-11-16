import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kp = Kassapaate()
        self.mk = Maksukortti(1000)

    def test_luotu_paate_rahamaara_oikea(self):
        raha = self.kp.kassassa_rahaa

        self.assertEqual(raha, 100000)

    def test_luotu_paate_myytyjen_lounaiden_maara_oikea(self):
        ed = self.kp.edulliset

        self.assertEqual(ed, 0)

    def test_syo_edullisesti_kateisella_riittava_maksu_rahamaara_kasvaa(self):
        self.kp.syo_edullisesti_kateisella(240)
        raha = self.kp.kassassa_rahaa

        self.assertEqual(raha, 100240)

    def test_syo_edullisesti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        palautus = self.kp.syo_edullisesti_kateisella(300)

        self.assertEqual(palautus, 60)

    def test_syo_edullisesti_kateisella_riittava_maksu_lounaiden_maara_kasvaa(self):
        self.kp.syo_edullisesti_kateisella(240)
        ed = self.kp.edulliset

        self.assertEqual(ed, 1)

    def test_syo_edullisesti_kateisella_ei_riittava_maksu_rahamaara_ei_kasva(self):
        self.kp.syo_edullisesti_kateisella(200)
        raha = self.kp.kassassa_rahaa

        self.assertEqual(raha, 100000)
    
    def test_syo_edullisesti_kateisella_ei_riittava_maksu_kaikki_rahat_palautetaan(self):
        palautus = self.kp.syo_edullisesti_kateisella(200)

        self.assertEqual(palautus, 200)

    def test_syo_edullisesti_kateisella_ei_riittava_maksu_lounaiden_maara_ei_kasva(self):
        self.kp.syo_edullisesti_kateisella(200)
        ed = self.kp.edulliset

        self.assertEqual(ed, 0)

    def test_syo_maukkaasti_kateisella_riittava_maksu_rahamaara_kasvaa(self):
        self.kp.syo_maukkaasti_kateisella(400)
        raha = self.kp.kassassa_rahaa

        self.assertEqual(raha, 100400)
   
    def test_syo_maukkaasti_kateisella_riittava_maksu_vaihtoraha_oikein(self):
        palautus = self.kp.syo_maukkaasti_kateisella(500)

        self.assertEqual(palautus, 100)
        
    def test_syo_maukkaasti_kateisella_riittava_maksu_lounaiden_maara_kasvaa(self):
        self.kp.syo_maukkaasti_kateisella(400)
        ma = self.kp.maukkaat

        self.assertEqual(ma, 1)

    def test_syo_maukkaasti_kateisella_ei_riittava_maksu_rahamaara_ei_kasva(self):
        self.kp.syo_maukkaasti_kateisella(300)
        raha = self.kp.kassassa_rahaa

        self.assertEqual(raha, 100000)
    
    def test_syo_maukkaasti_kateisella_ei_riittava_maksu_kaikki_rahat_palautetaan(self):
        palautus = self.kp.syo_maukkaasti_kateisella(300)

        self.assertEqual(palautus, 300)

    def test_syo_maukkaasti_kateisella_ei_riittava_maksu_lounaiden_maara_ei_kasva(self):
        self.kp.syo_maukkaasti_kateisella(300)
        ma = self.kp.maukkaat

        self.assertEqual(ma, 0)

    def test_kortilla_tarpeeksi_rahaa_veloitetaan_summa_kortilta_ja_palautetaan_true(self):
        ed_bool = self.kp.syo_edullisesti_kortilla(self.mk)
        ma_bool = self.kp.syo_maukkaasti_kortilla(self.mk)
        # kortilla aluksi 10 e joten nyt pitäisi olla 10-2.4-4=3.6
        self.assertEqual(str(self.mk), "saldo: 3.6")
        self.assertEqual(ed_bool, True)
        self.assertEqual(ma_bool, True)

    def test_kortilla_tarpeeksi_rahaa_myytyjen_lounaiden_maara_kasvaa(self):
        self.kp.syo_edullisesti_kortilla(self.mk)
        self.kp.syo_maukkaasti_kortilla(self.mk)
        
        ma = self.kp.maukkaat
        self.assertEqual(ma, 1)

        ed = self.kp.edulliset
        self.assertEqual(ed, 1)

    def test_kortilla_ei_tarpeeksi_rahaa(self):
        # testataan, että kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
        self.kp.syo_edullisesti_kortilla(self.mk)
        self.kp.syo_maukkaasti_kortilla(self.mk)
        # kortilla aluksi 10 e joten nyt pitäisi olla 10-2.4-4=3.6 joka ei riitä maukkaaseen
        ma_bool = self.kp.syo_maukkaasti_kortilla(self.mk) # pitäisi olla False
        ma = self.kp.maukkaat # pitäisi olla 1
        self.assertEqual(ma, 1)
        self.assertEqual(ma_bool, False)
        self.assertEqual(str(self.mk), "saldo: 3.6")
        self.kp.syo_edullisesti_kortilla(self.mk)
        # kortin saldo nyt 1.2 e, ed lounaita myyty 2
        ed_bool = self.kp.syo_edullisesti_kortilla(self.mk) # pitäisi olla False
        ed = self.kp.edulliset # pitäisi olla 2
        self.assertEqual(ed, 2)
        self.assertEqual(ed_bool, False)
        self.assertEqual(str(self.mk), "saldo: 1.2")

    def test_korttimaksu_kassan_rahamaara_ei_muutu(self):
        self.kp.syo_maukkaasti_kortilla(self.mk)
        raha = self.kp.kassassa_rahaa
        self.assertEqual(raha, 100000)
        self.kp.syo_edullisesti_kortilla(self.mk)
        raha = self.kp.kassassa_rahaa
        self.assertEqual(raha, 100000)

    def test_ladattaessa_kortinsaldo_muuttuu_ja_kassan_rahamaara_kasvaa(self):
        self.kp.lataa_rahaa_kortille(self.mk, 1000)
        raha = self.kp.kassassa_rahaa
        self.assertEqual(raha, 101000)
        self.assertEqual(str(self.mk), "saldo: 20.0")

    def test_lataa_neg_summa_kortille_kortin_saldo_ja_kassan_rahamaara_pysyvat_samana(self):
        self.kp.lataa_rahaa_kortille(self.mk, -1000)
        raha = self.kp.kassassa_rahaa
        self.assertEqual(raha, 100000)
        self.assertEqual(str(self.mk), "saldo: 10.0")