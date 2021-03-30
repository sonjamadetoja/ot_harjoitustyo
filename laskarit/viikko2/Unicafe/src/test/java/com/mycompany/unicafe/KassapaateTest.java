/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author smadetoj
 */
public class KassapaateTest {
    
    Kassapaate kassa;
    Maksukortti kortti;
    
    @Before
    public void setUp() {
        kassa = new Kassapaate();
        kortti = new Maksukortti(1000);
    }
    
    @Test
    public void onkoKassassaOikeaRahamaara() {
        int vastaus = kassa.kassassaRahaa();
        
        assertEquals(100000, vastaus);
    }
    
    @Test
    public void myytyjenLounaidenMaaraEdulliset() {
        int vastaus = kassa.edullisiaLounaitaMyyty();
        
        assertEquals(0, vastaus);
    }
    
    
    @Test
    public void myytyjenLounaidenMaaraMaukkaat() {
        int vastaus = kassa.maukkaitaLounaitaMyyty();
        
        assertEquals(0, vastaus);
    }
    
    @Test 
    public void kateisostoToimiiJosRiittavastiRahaaEdullisestiRahamaaraOikea() {
        kassa.syoEdullisesti(240);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000+240;
        assertEquals(odotettu, vastaus);
    }
    
    @Test 
    public void kateisostoToimiiJosRiittavastiRahaaEdullisestiLounaidenMaaraOikea() {
        kassa.syoEdullisesti(240);
        int vastaus = kassa.edullisiaLounaitaMyyty();
        assertEquals(1, vastaus);
    }
    
    @Test 
    public void kateisostoToimiiJosRiittavastiRahaaMaukkaastiRahamaaraOikea() {
        kassa.syoMaukkaasti(400);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000+400;
        assertEquals(odotettu, vastaus);
    }
    
    @Test 
    public void kateisostoToimiiJosRiittavastiRahaaMaukkaastiLounaidenMaaraOikea() {
        kassa.syoMaukkaasti(400);
        int vastaus = kassa.maukkaitaLounaitaMyyty();
        assertEquals(1, vastaus);
    }
    
        @Test
    public void kateisostoToimiiJosRiittavastiRahaaEdullisestiRahanPalautus() {
        int vastaus = kassa.syoEdullisesti(300);

        assertEquals(60, vastaus);
    }
    
    @Test
    public void kateisostoToimiiJJosRiittavastiRahaaMaukkaastiRahanPalautus() {
        int vastaus = kassa.syoMaukkaasti(500);

        assertEquals(100, vastaus);        
    }
    
    
    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaEdullisestiKassanRahamaara() {
        kassa.syoEdullisesti(100);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000;
        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaMaukkaastiKassanRahamaara() {
        kassa.syoMaukkaasti(100);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000;
        assertEquals(odotettu, vastaus);
    }

    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaEdullisestiRahanPalautus() {
        int vastaus = kassa.syoEdullisesti(100);

        assertEquals(100, vastaus);
    }
    
    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaMaukkaastiRahanPalautus() {
        int vastaus = kassa.syoMaukkaasti(100);

        assertEquals(100, vastaus);        
    }
    
    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaEdullisestiMyytyjenLounaidenMaara() {
        kassa.syoEdullisesti(100);
        int vastaus = kassa.edullisiaLounaitaMyyty();
        assertEquals(0, vastaus);
    }
    
    @Test
    public void kateisostoToimiiJosMaksuEiRiittavaMaukkaastiMyytyjenLounaidenMaara() {
        kassa.syoMaukkaasti(100);
        int vastaus = kassa.maukkaitaLounaitaMyyty();
        assertEquals(0, vastaus);
    }
    
    @Test
    public void korttiostoToimiiEdullisestiTarpeeksiRahaaVeloitetaanSumma() {
        kassa.syoEdullisesti(kortti);
        int vastaus = kortti.saldo();
        int odotettu = 1000 - 240;

        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void korttiostoToimiiMaukkaastiTarpeeksiRahaaVeloitetaanSumma() {
        kassa.syoMaukkaasti(kortti);
        int vastaus = kortti.saldo();
        int odotettu = 1000 - 400;

        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void korttiostoToimiiEdullisestiTarpeeksiRahaaBooleanTrue() {
        boolean vastaus = kassa.syoEdullisesti(kortti);
        assertEquals(true, vastaus);
    }
    
    @Test
    public void korttiostoToimiiMaukkaastiTarpeeksiRahaaBooleanTrue() {
        boolean vastaus = kassa.syoMaukkaasti(kortti);
        assertEquals(true, vastaus);
    }
    
    @Test
    public void korttiostoToimiiEdullisestiTarpeeksiRahaaMyydytLounaatKasvaa() {
        kassa.syoEdullisesti(kortti);
        int vastaus = kassa.edullisiaLounaitaMyyty();
        assertEquals(1, vastaus);
    }
    
    @Test
    public void korttiostoToimiiMaukkaastiTarpeeksiRahaaMyydytLounaatKasvaa() {
        kassa.syoMaukkaasti(kortti);
        int vastaus = kassa.maukkaitaLounaitaMyyty();
        assertEquals(1, vastaus);
    }
    
    
    @Test
    public void korttiostoToimiiEdullisestiEiTarpeeksiRahaaKortinRahamaaraEiMuutu() {
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        int vastaus = kortti.saldo();
        assertEquals(40, vastaus);
    }  
    
    @Test
    public void korttiostoToimiiMaukkaastiEiTarpeeksiRahaaKortinRahamaaraEiMuutu() {
        kassa.syoMaukkaasti(kortti);
        kassa.syoMaukkaasti(kortti);
        kassa.syoMaukkaasti(kortti);
        int vastaus = kortti.saldo();
        assertEquals(200, vastaus);
    }
    
    
    @Test
    public void korttiostoToimiiEdullisestiEiTarpeeksiRahaaMyydytLounaatEiMuutu() {
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        int vastaus = kassa.edullisiaLounaitaMyyty();
        int odotettu = 4;
        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void korttiostoToimiiMaukkaastiEiTarpeeksiRahaaMyydytLounaatEiMuutu() {
        kassa.syoMaukkaasti(kortti);
        kassa.syoMaukkaasti(kortti);
        kassa.syoMaukkaasti(kortti);
        int vastaus = kassa.maukkaitaLounaitaMyyty();
        int odotettu = 2;
        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void korttiostoToimiiEdullisestiEiTarpeeksiRahaaBooleanFalse() {
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        kassa.syoEdullisesti(kortti);
        boolean vastaus = kassa.syoEdullisesti(kortti);
        assertEquals(false, vastaus);
    }
    
    @Test
    public void korttiostoToimiiMaukkaastiEiTarpeeksiRahaaBooleanFalse() {
        kassa.syoMaukkaasti(kortti);
        kassa.syoMaukkaasti(kortti);
        boolean vastaus = kassa.syoMaukkaasti(kortti);
        assertEquals(false, vastaus);
    }
    
    @Test
    public void korttiostoToimiiEdullisestiKassaEiMuutu() {
        int odotettu = kassa.kassassaRahaa();
        kassa.syoEdullisesti(kortti);
        int vastaus = kassa.kassassaRahaa();
        assertEquals(odotettu, vastaus);
    }

    @Test
    public void korttiostoToimiiMaukkaastiKassaEiMuutu() {
        int odotettu = kassa.kassassaRahaa();
        kassa.syoMaukkaasti(kortti);
        int vastaus = kassa.kassassaRahaa();
        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void ladattaessaKortinRahamaaraMuuttuu() {
        kassa.lataaRahaaKortille(kortti, 200);
        int vastaus = kortti.saldo();
    
        assertEquals(1200, vastaus);
    }
    
    @Test
    public void ladattaessaKassanRahamaaraMuuttuu() {
        kassa.lataaRahaaKortille(kortti, 200);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000+200;
    
        assertEquals(odotettu, vastaus);
    }
    
    @Test
    public void ladattaessaMortilleNegatiivistaSummaaEiToimiSaldo() {
        kassa.lataaRahaaKortille(kortti, -200);
        int vastaus = kortti.saldo();
    
        assertEquals(1000, vastaus);
    }
    
    @Test
    public void ladattaessaMortilleNegatiivistaSummaaEiToimiKassa() {
        kassa.lataaRahaaKortille(kortti, -200);
        int vastaus = kassa.kassassaRahaa();
        int odotettu = 100000;
    
        assertEquals(odotettu, vastaus);
    }
    
}
