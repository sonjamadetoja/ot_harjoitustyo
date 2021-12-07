import os
import datetime
from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class Service:
    def __init__(self, user_repository, transaction_repository):
        self.user_repository = user_repository
        self.transaction_reporitory = transaction_repository

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
        self.user_repository.add_user(add_user_name)
        return "register"

    def delete_user(self, user):
        user_id = user.get_user_id()
        self.transaction_reporitory.remove_all_deposits(user_id)
        self.user_repository.remove_user(user_id)

    def add_transaction(self, date, amount, user, title):
        user_id = user.get_user_id()
        self.transaction_reporitory.add_deposit(date, amount, user_id, title)

    def find_transactions(self, user):
        user_id = user.get_user_id()
        deposits = self.transaction_reporitory.find_all_deposits(user_id)
        return deposits

    def remove_transaction(self, id):
        self.transaction_reporitory.remove_deposit(id)

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
                self.transaction_reporitory.add_deposit(date, amount, user_id, title)
        return True

service = Service(user_repository, transaction_repository)
