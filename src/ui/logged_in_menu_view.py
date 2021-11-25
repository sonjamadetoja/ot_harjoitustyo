
from repositories.transaction_repository import transaction_repository

class MenuView:

    def show_menu(self):
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
