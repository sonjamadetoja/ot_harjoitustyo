from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class Service:
    def __init__(self):
        pass

    def login(self, user_name):
        find_user = user_repository.find_user(user_name)
        if find_user is True:
            user = User(user_name)
            return "login"
        else:
            return "no_username"

    def logout():
        return "logout"

    def register(self, add_user_name):
        find_user = user_repository.find_user(add_user_name)
        if find_user is True:
            return False
        else:
            user_repository.add_user(add_user_name)
            return "register"

    def add_transaction(self, amount):
        transaction_repository.add_deposit(amount)

    def find_transactions(self):
        transaction_repository.find_all_deposits()

service = Service()
