# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

UserService-luokka on testattu [TestUserService](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/user_service_test.py)-luokalla. Sille alustetaan tietokantayhteys testitietokantaan, User-luokka sekä UserRepository-luokka.

TransactionService-luokka on testattu [TestTransactionService](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/transaction_service_test.py)-luokalla. Sille alustetaan tietokantayhteys testitietokantaan, User-luokka sekä TransactionRepository-luokka. 

Alustuksen yhteydessä molemmille luodaan testikäyttäjä.

### Repositorio-luokat

UserRepository-luokka on testattu [TestUserRepository](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/user_repository_test.py)-luokalla. Sille alustetaan tietokantayhteys testitietokantaan.

TransactionRepository-luokka on testattu [TestTransactionRepository](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/transaction_repository_test.py)-luokalla. Sille alustetaan tietokantayhteys testitietokantaan sekä UserRepository-luokka.

### Muut luokat

User-luokka on testattu [TestUser](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/user_test.py)-luokalla, sekä Database-luokka [TestDataBase](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/src/tests/initialize_database_test.py)-luokalla, jolle on alustettu tietokantayhteys testitietokantaan.

### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 84 %. 

![](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kuvat/Testauskattavuus.png)

Testaamatta jäivät TransactionService-luokan toiminnot tietojen lisääminen tiedostosta, tietojen hakeminen vuoden perusteella sekä tietojen hakeminen kuukauden perusteella. Nämä toiminnot on testattu manuaalisesti.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti. Sovellus on haettu ja sitä on testattu [käyttöohjeen](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) kuvaamalla tavalla vain Linux-ympäristössä. Kaikki [vaatimusmäärittelyn](https://github.com/sonjamadetoja/ot_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen ilmoittamat toiminnot on käyty testattu. Kaikkien toimintojen yhteydessä on syötekentät yritetty täyttää myös virheellisillä arvoilla kuten tyhjillä.
