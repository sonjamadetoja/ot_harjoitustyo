# Sovellus

Sovelluksen tarkoitus on tulojen ja menojen seuraaminen ja se on tarkoitettu yksityishenkilön käyttöön. Sovellukseen voi tallentaa itse tulo- ja meno-tietoja sekä antaa pankista saadun cvs-tiedoston, jossa on tilitapahtumat tiedot, ja laittaa sen tietokantaan. Tuloja ja menoja voi luokitella, ja niistä voi katsella yhteenvetoja numeromuodossa tai graafeina. Tulo- ja menotietoja voi myös poistaa. Sovelluksessa on yksi käyttäjärooli.

## Huomio python-versiosta

Sovelluksen toiminta on testattu Python-versiolla ```3.8.```

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Release 1](https://github.com/sonjamadetoja/ot_harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/sonjamadetoja/ot_harjoitustyo/releases/tag/viikko6)

[Käyttöohje](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Asennus

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

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```
Raportti muodostuu *htmlcov*-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Tapahtumien lisääminen tiedostosta

Tiedostonluku-toimintoa varten on data-kansioon lisätty tiedosto 'testitili.csv', jota voi halutessaan käyttää tähän tarkoitukseen.
