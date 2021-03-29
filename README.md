# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voi pelata tetris-peliä. Pelissä on alue, jolla liikku palikoita alaspäin. Pelaaja voi kääntää palikoita tai siirtää niitä alaspäin. Tarkoitus on saada alue täytettyä jokaisella rivillä laidalta toiselle. Täytetyt rivit häviävät, ja niistä saa pisteitä. Peli päättyy, kun alue täyttyy pystysuunnassa. Sovelluksessa on vain yksikäyttäjärooli.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä näkymästä. Ensimmäinen on kirjautumisnäkymä, josta pääsee tunnuksenluomisnäkymään tai kirjautuneen käyttäjän näkymään. Kirjautuneen käyttäjän näkymästä pääsee pelinäkymään. Kun peli päättyy, ohjelma palaa automaattisesti kirjautuneen käyttäjän näkymään.
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/OHTE_kayttoliittymaluonnos1.jpg" width="750">

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Tunnuksen luominen
- Sisäänkirjautuminen

### Kirjautuneena
- pelin aloittaminen
- pelaaminen:
  - palikoiden kääntäminen näppäimistöllä
  - palikoiden siirtäminen sivusuunnassa näppäimistöllä
  - 7 erilaista palikkaa
  - värimaailma soveltuu värisokeille
- pistemäärän tallentuminen
- omien pistetulosten katselu
- tunnuksen poistaminen
- uloskirjautuminen

## Jatkokehitysideoita

- parhaiden tulosten lista
- salasana
- pelinopeuden valinta
- keskeytä peli
- valitse värimaailma
- omien tulosten järjestäminen ajan tai pistemäärän mukaan
- äänitehosteet
