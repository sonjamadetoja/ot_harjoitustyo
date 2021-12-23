# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on kolmitasoinen: ui-kansio sisältää käyttöliittymäkoodin, services-kansio sovelluslogiikan, ja repositories-kansio tietokantatoiminnot. Entities-kansio sisältää käyttäjäluokan, jota muut luokat käyttävät.

## Käyttöliittymä

Käyttöliittymä sisältää seuraavat näkymät: kirjautuminen, rekisteröityminen, toiminnan valinta, tietojen haku, tapahtumien lisääminen. Jokainen on toteutettu omana luokkanaan.

## Sovelluslogiikka

Luokkakaavio: 
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.jpg">

Sovelluksen toiminnasta vastaa Service-luokka. Se sisältää fuktiot tärkeimmille toiminnoille. Se käyttää UserRepository- ja TransactionRepository-luokkien tietokantatoimintoja tietojen tallennukseen ja poistamiseen. User-luokkaa se käyttää kirjautuneen käyttäjän tallentamiseen.

## Tietojen tallennus

Tiedot käyttäjistä ja tapahtumista tallennetaan sqlite3-tietokantaan. Tietoja voi tallentaa yksitellen, jolloin ohjelma pyytää antamaan tallennettavat tiedot, tai tietoja voi tallentaa isomman määrän csv-tiedostosta, jonka tiedot ohjelma lukee ja tallentaa automaattisesti.

Tietojen tallentamisesta huolehtivat UserRepository- ja TransactionRepository-luokat.

## Päätoiminnallisuudet

### Sisäänkirjautuminen

Painikkeen painamisen jälkeen käyttöliittymä kutsuu Service-luokan login-toimintoa, joka puolestaan kutsuun UserRepository-luokan find_user-toimintoa, joka palauttaa True, jos käyttäjätunnus on olemassa. Sen jälkeen Service-luokka kutsuu luokan UserRepository find_user_id-toimintoa, joka hakee käyttäjätunnuksen id-numeron tietokannasta. Tämän jälkeen Service-luokka kutsuu User-luokan create_user-toimintoa, joka luo käyttäjän kirjautuneena olemisen ajaksi. Service-luokka palauttaa käyttäjän käyttöliittymälle.

Login-toiminnon sekvenssikaavio:
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/loginsequencediagram.png">

### Rekisteröityminen

Painikkeen painamisen jälkeen käyttöliittymä kutsuu Service-luokan register-toimintoa, joka puolestaan kutsuun UserRepository-luokan find_user-toimintoa, joka palauttaa False, jos käyttäjätunnusta ei ole olemassa. Sen jälkeen Service-luokka kutsuu luokan UserRepository add_user-toimintoa, joka lisää käyttäjän tietokantaan. 

### Tapahtuman lisääminen

Service-luokan add_transaction-toiminto kutsuu ensin User-luokan get_user_id-toimintoa, joka palauttaa id-numeron Service-luokalle. Sen jälkeen se kutsuu TransactionRepository-luokan add_deposit-toimintoa, joka tallentaa tiedot tietokantaan.

Tapahtuman lisäämisen sekvenssikaavio:
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/addtransactionsequencediagram.png">

### Tapahtumien lisääminen tiedostosta

Service-luokan add_file-toiminto lukee ja muokkaa annetun tiedoston tiedot, ja muuten toimii samalla tavalla kuin yksittäisen tapahtuman lisääminen, se vain lisää jokaisen tiedostossa olevan tapahtuman erikseen.

### Tapahtuman poistaminen

Service-luokan remove_transaction-toiminto saa käyttöliittymältä käyttäjän antaman tapahtuma-id:n, jonka se antaa kutsumalleen TransactionRepository-luokan remove_deposit-toiminnolle, joka poistaa tapahtuman tietokannasta.

### Käyttäjän poistaminen

Service-luokan delete_user-toiminto kutsuu ensin User-luokan get_user_id-toimintoa, joka palauttaa id-numeron Service-luokalle. Sen jälkeen se välittää käyttäjän id-numeron seuraaville toiminoille: se kutsuu TransactionRepository-luokan remove_all_deposits-toimintoa, joka poistaa kaikki käyttäjän tapahtumat, sekä UserRepository-luokan remove_user-toimintoa, joka poistaa käyttäjän tietokannasta.

### Tietojen katsominen

Tietojen katsomisen sekvenssikaavio:
<img src="https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/viewtransactionssequencediagram.png">

Service-luokan find_transactions-toiminto kutsuu ensin User-luokan get_user_id-toimintoa, joka palauttaa id-numeron Service-luokalle. Sen jälkeen se kutsuu TransactionRepository-luokan find_all_deposits-toimintoa, ja välittää id-numeron sille, jolloin se palauttaa Service-luokalle kaikki tapahtumat. Service-luokka palauttaa tapahtumat edelleen käyttöliittymälle, tai jos tapahtumia ei ole, se palauttaa None. find_transaction_by_year ja find_transaction_by_month toimivat samaan tapaan, mutta ne saavat käyttöliittymältä ja välittävät TransactionRepository-luokan toiminnoille find_deposit_by_year ja find_deposit_by_month myös tiedon halutusta ajankohdasta.
