# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on kolmitasoinen: ui-kansio sisältää käyttöliittymäkoodin, services-kansio sovelluslogiikan, ja repositories-kansio tietokantatoiminnot. Entities-kansio sisältää käyttäjäluokan, jota muut luokat käyttävät.

## Käyttöliittymä

Käyttöliittymä sisältää seuraavat näkymät: kirjautuminen, rekisteröityminen, toiminnan valinta, tietojen haku. Jokainen on toteutettu omana luokkanaan.

## Sovelluslogiikka

Luokkakaavio: 
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.jpg">

Sovelluksen toiminnasta vastaa Service-luokka. Se sisältää fuktiot tärkeimmille toiminnoille. Se käyttää UserRepository- ja TransactionRepository-luokkien tietokantatoimintoja tietojen tallennukseen ja poistamiseen. User-luokkaa se käyttää kirjautuneen käyttäjän tallentamiseen.

## Tietojen tallennus

Tiedot käyttäjistä ja tapahtumista tallennetaan sqlite3-tietokantaan. Tietoja voi tallentaa yksitellen, jolloin ohjelma pyytää antamaan tallennettavat tiedot, tai tietoja voi tallentaa isomman määrän csv-tiedostosta, jonka tiedot ohjelma lukee ja tallentaa automaattisesti.

Tietojen tallentamisesta huolehtivat UserRepository- ja TransactionRepository-luokat.

## Päätoiminnallisuudet

### Sisäänkirjautuminen

Login-toiminnon sekvenssikaavio:
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/loginsequencediagram.png">

### Rekisteröityminen
### Uloskirjautuminen
### Tapahtuman lisääminen
### Tapahtumien lisääminen tiedostosta
### Tapahtuman poistaminen
### Käyttäjän poistaminen
### Tietojen katsominen

## Ohjelman rakenteeseen jääneet heikkoudet
