# Käyttöohje

## Ohjelman käynnistäminen

1. Asenna riippuvuudet komennolla:

    ```bash
    poetry install
    ```

2. Käynnistä sovellus komennolla:

    ```bash
    poetry run invoke start
    ```

## Uudenkäyttäjän luominen

Käynnistä ohjelma. Valitse "Luo käyttäjätunnus". Anna haluamasi käyttäjätunnus. Se voi olla korkeintaan 20 merkkiä pitkä.

## Sisäänkirjautuminen

Käynnistä ohjelma. Valitse "Kirjaudu". Anna käyttäjätunnuksesi.

## Uuden tapahtuman lisääminen

Sisäänkirjautuneena valitse "Lisää tapahtuma". Anna tapahtuman summa numerona. Jos kyseessä on meno, laita summan eteen miinusmerkki. Anna päivämäärä muodossa yyyy-mm-dd, missä yyyy on vuosi (esim. 2021), mm on kuukausi (esim. 01) ja dd on päivä (esim. 30). Jos jätät kohdan tyhjäksi, tapahtumalle laitetaan automaattisesti päivämääräksi kirjauspäivä. Anna tapahtumalle otsikko (esim. mitä ostit). Anna tapahtumalle luokittelu.

## Tapahtumien lisääminen tiedostosta

Sisäänkirjautuneena valitse "Lisää tapahtumia csv-tiedostosta". Anna tiedoston nimi. Tiedoston tulee sijaita data-kansiossa.

## Tapahtumien katseleminen

Sisäänkirjautuneena valitse "Katso tapahtumia". Valitse joku seuraavista vaihtoehdoista:
1 Hae kaikki tapahtumat
2 Hae yhden vuoden tapahtumat
3 Hae yhden kuukauden tapahtumat
Anna vuosi ja kuukausi numerona (esimerkiksi joulukuu on 12).

## Tapahtumien poistaminen

Sisäänkirjautuneena valitse "Poista tapahtuma". Näet listan tapahtumistasi. Katso listasta, mikä on sen tapahtuman id-numero, jonka haluat poistaa, ja syötä kyseinen id-numero.

Poistamisen jälkeen tapahtumaa voi palauttaa.

## Käyttäjätunnuksen poistaminen 

Sisäänkirjautuneena valitse "Poista käyttäjätunnus". Ohjelma pyytää sinua vielä varmistamaan, haluatko todella poistaa tunnuksesi ja kaikki tietosi. Kirjoita "kyllä" tai "ei".

Tämä toiminto poistaa kaikki tietosi tietokannasta, eikä niitä voi enää palauttaa.
