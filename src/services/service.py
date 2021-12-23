import os
from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class Service:
    """Luokka, jonka avulla toteutetaan sovelluslogiikka.

    Attributes:
        user_repository: UserRepository-olion UserRepository-luokasta
        transaction_repository: TransactionRepository-olion TransactionRepository-luokasta
    """
    def __init__(self, user_repository, transaction_repository):
        """Luokan konstruktori, joka luo uuden Service-olion.
        Argumenttina annettava repositoriot tuodaan niiden omista luokista.

        Args:
            user_repository: user_repository
            transaction_repository: transaction_repository
        """
        self.user_repository = user_repository
        self.transaction_repository = transaction_repository

    def login(self, user_name):
        """Tämä funktio huolehtii käyttäjän sisäänkirjautumisesta.

        Args:
            user_name (string): Käyttäjän käyttäjänimi.

        Returns:
            Palauttaa käyttäjän, jos sisäänkirjautuminen onnistui.
            Palauttaa merkkijonon "no_username", jos sisäänkirjautuminen ei onnistunut,
            koska kyseistä käyttäjää ei löydy tietokannasta.
        """
        find_user = self.user_repository.find_user(user_name)
        if find_user is True:
            user_id = self.user_repository.find_user_id(user_name)
            user = User(user_name, user_id)
            return user
        return None

    def logout(self, user):
        """Tämä funktio huolehtii käyttäjän uloskirjautumisesta.

        Args:
            user: käyttäjä

        Returns:
            string: "logout"
        """
        user = None
        return user

    def register(self, add_user_name):
        """Tämä funktio huolehtii uuden käyttäjänimen rekisteröinnistä.

        Args:
            add_user_name (string): tallennettava käyttäjänimi.

        Returns:
            Jos rekisteröinti onnistuu, palauttaa merkkijonon "register".
            Jos rekisteröinti epäonnistuu, palauttaa False.
        """
        find_user = self.user_repository.find_user(add_user_name)
        if find_user is True:
            return False
        if add_user_name == "":
            return False
        if len(add_user_name) > 20:
            return False
        self.user_repository.add_user(add_user_name)
        return True

    def delete_user(self, user):
        """Poistaa käyttäjän tietokannoista.

        Args:
            user: poistettava käyttäjä, joka on kirjautuneena.
        """
        user_id = user.get_user_id()
        self.transaction_repository.remove_all_deposits(user_id)
        self.user_repository.remove_user(user_id)

    def add_transaction(self, date, amount, user, title, category):
        """Lisää tapahtuman tietokantaan.

        Args:
            date: päivämäärä
            amount: summa (positiivinen tai negatiivinen tapahtumasta riippuen)
            user: kirjautuneena oleva käyttäjä
            title: tapahtuman otsikko
            category: tapahtuman luokittelu

        Returns:
            True
        """
        user_id = user.get_user_id()
        self.transaction_repository.add_deposit(date, amount, user_id, title, category)
        return True

    def find_transactions(self, user):
        """Hakee tapahtumat tietokannasta. Näyttää kaavion ja piirakan tapahtumista.

        Args:
            user: kirjautuneena oleva käyttäjä.

        Returns:
            Lista käyttäjän tapahtumista.
        """
        user_id = user.get_user_id()
        deposits = self.transaction_repository.find_all_deposits(user_id)
        if not deposits:
            return None
        return deposits

    def find_transaction_by_year(self, user, year):
        """Hakee kaikki käyttäjän tapahtuman annetun vuoden ajalta.
        Näyttää kaavion ja piirakan tapahtumista.

        Args:
            user: kirjautuneena oleva käyttäjä.
            year: annettu vuosi

        Returns:
            Lista käyttäjän tapahtumista.
        """
        user_id = user.get_user_id()
        deposits = transaction_repository.find_deposit_by_year(user_id, year)
        if not deposits:
            return None
        return deposits

    def find_transaction_by_month(self, user, year, month):
        """Hakee kaikki käyttäjän tapahtuman annetun kuukauden ajalta.
        Näyttää kaavion ja piirakan tapahtumista.

        Args:
            user: kirjautuneena oleva käyttäjä.
            year: annettu vuosi
            month: annettu kuukausi

        Returns:
            Lista käyttäjän tapahtumista.
        """
        user_id = user.get_user_id()
        deposits = transaction_repository.find_deposit_by_month(user_id, year, month)
        if not deposits:
            return None
        return deposits

    def remove_transaction(self, id_number):
        """Poistaa tapahtuman tietokannasta.

        Args:
            id (integer): tapahtuman tunnusnumero tietokannassa.
        """
        self.transaction_repository.remove_deposit(id_number)

    def add_file(self, user, filename):
        """Lisää tietokantaan tapahtumia csv-tiedostolta.

        Args:
            user: kirjautuneena oleva käyttäjä.
            filename: tiedoston nimi.

        Returns:
            True, jos onnistuu.
            False, jos epäonnistuu.
        """
        user_id = user.get_user_id()
        dirname = os.path.dirname(__file__)
        new_path = os.path.join(dirname, "..", "..", "data", filename)
        try:
            open(new_path, "r")
        except FileNotFoundError:
            return False
        with open(new_path, "r") as file_x:
            file_x = iter(file_x)
            next(file_x)
            for line in file_x:
                edit = line.split(";")
                for item in edit:
                    item.strip()
                date = self._fix_date(edit[0])
                amount = str(edit[1]).replace(",", ".")
                title = edit[5]
                category = "tilitapahtuma"
                self.transaction_repository.add_deposit(date, amount, user_id, title, category)
        return True

    def _fix_date(self, date):
        date = date.strip()
        date = date.split(".")
        date = date[2]+"-"+date[1]+"-"+date[0]
        return date

service = Service(user_repository, transaction_repository)
