from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository

class Service:
    def __init__(self):
        pass

    def login(self, user_name):
            find_user = user_repository.find_user(user_name)
            if find_user is True:
                return "login"
            else:
                return None

    def register(self, add_user_name):
            find_user = user_repository.find_user(add_user_name)
            if find_user is True:
                return False
            else:
                user_repository.add_user(add_user_name)
                return "register"

    def transaction(self):
        print("Valitse toiminto numerolla:")
        print("1 Lisää tapahtuma") # Kesken
        print("2 Katso tapahtumia") # Ei toteutettu
        print("3 Kirjaudu ulos") # Ei toteutettu
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            amount = int(input("Anna summa: "))
            # Note to self: lisää tähän jokin varmistus, että syöte on sopiva
            transaction_repository.add_deposit(amount)
        elif choice == 2:
            transaction_repository.find_all_deposits()

service = Service()
