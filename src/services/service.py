from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class Service:
    def __init__(self):
        pass

    def login(self, user_name):
        find_user = user_repository.find_user(user_name)
        if find_user is True:
            user_id = user_repository.find_user_id(user_name)
            user = User(user_name, user_id)
            return user
        else:
            return "no_username"

    def logout(self, user):
        user = None
        return "logout"

    def register(self, add_user_name):
        find_user = user_repository.find_user(add_user_name)
        if find_user is True:
            return False
        else:
            user_repository.add_user(add_user_name)
            return "register"

    def add_transaction(self, amount, user):
        user_id = user.get_user_id()
        transaction_repository.add_deposit(amount, user_id)

    def find_transactions(self, user):
        user_id = user.get_user_id()
        transaction_repository.find_all_deposits(user_id)

service = Service()
