# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on tulojen ja menojen seuraaminen ja se on tarkoitettu yksityishenkilön käyttöön. Sovellukseen voi tallentaa itse tulo- ja meno-tietoja sekä antaa pankista saadun cvs-tiedoston, jossa on tilitapahtumat tiedot, ja laittaa sen tietokantaan. Tuloja ja menoja voi luokitella, ja niistä voi katsella yhteenvetoja numeromuodossa tai graafeina. Tulo- ja menotietoja voi myös poistaa. Sovelluksessa on yksi käyttäjärooli.

## Käyttöliittymäluonnos

Ensimmäinen näkymä on kirjautumisnäkymä, josta pääsee tunnuksenluomisnäkymään tai kirjautuneen käyttäjän näkymään. Kirjautuneen käyttäjän näkymästä pääsee lisäämään tapahtumia, katsomaan tapahtumia tai poistamaan tunnuksen. Tapahtumien lisäämisnäkymässä joko lisätään yhden tapahtuman tiedot tai haetaan tiedot tiedostosta. Tapahtumien katsomisnäkymässä valitaan kuukausi tai vuosi, jolloin sovellus hakee tapahtumatiedot ja näyttää niistä graafin.

<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/kayttoliittymaluonnos_budjettisovellus.jpeg" width="750">

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Tunnuksen luominen -tehty
- Sisäänkirjautuminen -tehty

### Kirjautuneena
- tapahtumien lisääminen (rahan lisäys/poisto, nimi, pvm, luokittelu) -tehty kokonaan
- tapahtuman poistaminen -tehty
- saldon näkeminen (omistuksessa olevan rahan määrä tällä hetkellä) -tehty
- kuukausittaisten tai vuosittaisten yhteenvetojen katseleminen tuloista ja menoista luokittain -tehty
- graafien katseleminen -tehty
- tunnuksen poistaminen -tehty
- uloskirjautuminen -tehty

## Jatkokehitysideoita
- salasana
- useat tilit
- tiedot voi viedä exceliin
