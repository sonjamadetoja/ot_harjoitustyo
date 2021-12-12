import os
import pandas as pd
import plotly.express as px
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
        return "no_username"

    def logout(self, user):
        """Tämä funktio huolehtii käyttäjän uloskirjautumisesta.

        Args:
            user: käyttäjä

        Returns:
            string: "logout"
        """
        user = None
        return "logout"

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
        return "register"

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
        self.print_search_results(deposits)
        self.show_graph(deposits)
        self.show_pie(deposits)
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
        self.print_search_results(deposits)
        self.show_graph(deposits)
        self.show_pie(deposits)
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
        self.print_search_results(deposits)
        self.show_graph(deposits)
        self.show_pie(deposits)
        return deposits

    def print_search_results(self, deposits):
        """Tulostaa hakutulokset ruudulle.

        Args:
            deposits (list): Lista tapahtumista.
        """
        sum_transactions = 0
        for item in deposits:
            item_string = f"id: {str(item[0])}, {item[1]}, {str(item[2])}, {item[3]}, {str(item[4])}"
            print(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)

    def show_graph(self, deposits):
        """Piirtää kaavion tapahtumista.

        Args:
            deposits (list): Lista tapahtumista.
        """
        balance = []
        dates = []
        previous = 0
        # Miten tähän sais aiemman saldon aloitussummaksi?
        for item in deposits:
            dep = previous + float(item[2])
            dep = round(dep, 2)
            balance.append(dep)
            previous = dep
            date = item[1]
            dates.append(date)
        fig = px.line(x=dates, y=balance, title="Tilin saldon muutos")
        fig.show()

    def show_pie(self, deposits):
        """Piirtää piirakkakaavion tapahtumista.

        Args:
            deposits (list): Lista tapahtumista.
        """
        data_frame = self.make_dataframe(deposits)
        df_income = data_frame[data_frame.deposits > 0]
        df_expense = data_frame[data_frame.deposits < 0]
        df_expense.deposits = abs(df_expense.deposits)
        fig = px.pie(df_income, values='deposits', names='category', title="Tulot",
        color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()
        fig = px.pie(df_expense, values='deposits', names='category', title="Menot",
        color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()

    def make_dataframe(self, deposits):
        """Muodostaa tapahtumalistasta dataframe-taulukon.

        Args:
            deposits (list): Lista tapahtumista.

        Returns:
            DataFrame: Taulukko tapahtumista.
        """
        data_frame = pd.DataFrame(deposits, columns=["id", "date", "deposits", "title", "category"])
        return data_frame

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
                edit[0] = edit[0].strip()
                # Tää alla oleva ei toimi jostain syystä
                # -> siksi ekan rivin skippaus ennen loopin alkua
                # if edit[0] == "Kirjauspäivä":
                #     continue
                date = edit[0]
                date = date.split(".")
                date = date[2]+"-"+date[1]+"-"+date[0]
                amount = str(edit[1])
                amount = amount.replace(",", ".")
                title = edit[5]
                category = "tilitapahtuma"
                self.transaction_repository.add_deposit(date, amount, user_id, title, category)
        return True

service = Service(user_repository, transaction_repository)
