import os
from repositories.transaction_repository import transaction_repository

class TransactionService:
    """Luokka, jonka avulla toteutetaan tapahtumiin liittyvä sovelluslogiikka.

    Attributes:
        transaction_repository: TransactionRepository-olion TransactionRepository-luokasta
    """
    def __init__(self, transaction_repository):
        """Luokan konstruktori, joka luo uuden Service-olion.
        Argumenttina annettava repositoriot tuodaan niiden omista luokista.

        Args:
            transaction_repository: transaction_repository
        """
        self.transaction_repository = transaction_repository

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

transaction_service = TransactionService(transaction_repository)
