# Käyttöohje

## Ohjelman käynnistäminen

1. Asenna riippuvuudet komennolla:

    ```bash
    poetry install
    ```

2. Asenna Kaleido joko pipillä:

    ```bash
    pip install -U kaleido
    ```

    tai condalla:

    ```bash
    conda install -c plotly python-kaleido 
    ```

3. Käynnistä sovellus komennolla:

    ```bash
    poetry run invoke start
    ```

## Uudenkäyttäjän luominen

Käynnistä ohjelma. Valitse "Rekisteröidy". Anna haluamasi käyttäjätunnus. Se voi olla korkeintaan 20 merkkiä pitkä. Valitse "Tallenna käyttäjätunnus".

## Sisäänkirjautuminen

Käynnistä ohjelma. Syötä käyttäjätunnuksesi. Valitse "Kirjaudu sisään".

## Uuden tapahtuman lisääminen

Sisäänkirjautuneena valitse "Lisää tapahtumia yksittäin tai tiedostosta". Anna päivämäärä muodossa yyyy-mm-dd, missä yyyy on vuosi (esim. 2021), mm on kuukausi (esim. 01) ja dd on päivä (esim. 30). Jos jätät kohdan tyhjäksi, tapahtumalle laitetaan automaattisesti päivämääräksi kirjauspäivä. Anna tapahtuman summa numerona. Jos kyseessä on meno, laita summan eteen miinusmerkki. Anna tapahtumalle otsikko (esim. mitä ostit). Anna tapahtumalle luokittelu. Valitse "Lisää tapahtuma".

### Tapahtumien lisääminen tiedostosta

Anna tiedoston nimi. Tiedoston tulee sijaita data-kansiossa. Valitse "Lisää tapahtumia csv-tiedostosta".

## Tapahtumien katseleminen

Sisäänkirjautuneena valitse "Katso tai poista tapahtumia".

### Tapahtumien katseleminen

Valitse joku seuraavista vaihtoehdoista:
-"Hae kaikki tapahtumat"
-"Hae yhden vuoden tapahtumat". Anna ensin vuosi neljänä numerona.
-"Hae yhden kuukauden tapahtumat". Anna ensin vuosi ja kuukausi numerona (esimerkiksi joulukuu on 12, vuosi ilmoitetaan neljänä numerona).

### Tapahtumien poistaminen

Anna poistettavan tapahtuman id-numero. Jos et tiedä numeroa, etsi tapahtuma hakutoiminnolla numeron nähdäksesi. Id-numeron annettuasi valitse "Poista tapahtuma". Poisto on lopullinen.

## Käyttäjätunnuksen poistaminen 

Sisäänkirjautuneena valitse "Poista käyttäjätunnus". Tämä toiminto poistaa kaikki tietosi tietokannasta, eikä niitä voi enää palauttaa.

## Ohjelman sulkeminen

Valitse ensin "Kirjaudu ulos" ja sen jälkeen "Lopeta ohjelma".
