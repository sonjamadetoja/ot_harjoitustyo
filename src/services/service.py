import os
import pandas as pd
import plotly.express as px
from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class Service:
    def __init__(self, user_repository, transaction_repository):
        self.user_repository = user_repository
        self.transaction_repository = transaction_repository

    def login(self, user_name):
        find_user = self.user_repository.find_user(user_name)
        if find_user is True:
            user_id = self.user_repository.find_user_id(user_name)
            user = User(user_name, user_id)
            return user
        return "no_username"

    def logout(self, user):
        user = None
        return "logout"

    def register(self, add_user_name):
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
        user_id = user.get_user_id()
        self.transaction_repository.remove_all_deposits(user_id)
        self.user_repository.remove_user(user_id)

    def add_transaction(self, date, amount, user, title, category):
        user_id = user.get_user_id()
        self.transaction_repository.add_deposit(date, amount, user_id, title, category)
        return True

    def find_transactions(self, user):
        user_id = user.get_user_id()
        deposits = self.transaction_repository.find_all_deposits(user_id)
        self.print_search_results(deposits)
        self.show_graph(deposits)
        return deposits

    def find_transaction_by_year(self, user, year):
        user_id = user.get_user_id()
        deposits = transaction_repository.find_deposit_by_year(user_id, year)
        self.print_search_results(deposits)
        return deposits

    def find_transaction_by_month(self, user, year, month):
        user_id = user.get_user_id()
        deposits = transaction_repository.find_deposit_by_month(user_id, year, month)
        self.print_search_results(deposits)
        return deposits

    def print_search_results(self, deposits):
        sum_transactions = 0
        for item in deposits:
            item_string = "id: "+str(item[0])+", "+item[1]+", "+str(item[2])+", "+item[3]+", "+str(item[4])
            print(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)

    def show_graph(self, deposits):
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

    def remove_transaction(self, id):
        self.transaction_repository.remove_deposit(id)

    def add_file(self, user, filename):
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
