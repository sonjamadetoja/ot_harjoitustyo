package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void saldoAlussaOikein() {
        int vastaus = kortti.saldo();
        
        assertEquals(10, vastaus);
    }
    
    @Test
    public void lataaRahaaKasvattaaSaldoaOikein() {
        kortti.lataaRahaa(25);
        int vastaus = kortti.saldo();
        
        assertEquals(35, vastaus);
    }
    
    @Test
    public void otaRahaaToimiiKunSaldoRiittaa() {
        kortti.otaRahaa(5);
        int vastaus = kortti.saldo();
        
        assertEquals(5, vastaus);
    }
    
    @Test
    public void otaRahaaToimiiKunSaldoEiRiita() {
        kortti.otaRahaa(15);
        int vastaus = kortti.saldo();
        
        assertEquals(10, vastaus);
    }
    
    @Test
    public void otaRahaaBooleanFalseKunSaldoEiRiita() {
        boolean vastaus = kortti.otaRahaa(15);
        
        assertEquals(false, vastaus);
    }
    
    
    @Test
    public void otaRahaaBooleanTrueKunSaldoRiittaa() {
        boolean vastaus = kortti.otaRahaa(5);
        
        assertEquals(true, vastaus);
    }
    
    @Test
    public void toimiikoToString() {
        String vastaus = kortti.toString();
        
        assertEquals("saldo: 0.10", vastaus);
    }
}
