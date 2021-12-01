
from services.service import service
from entities.user import User

class MenuView:
    def __init__(self):
        pass

    def show_menu(self, user):
        print("Valitse toiminto numerolla:")
        print("1 Lisää tapahtuma")
        print("2 Katso tapahtumia") 
        print("3 Poista tapahtumia")
        print("4 Kirjaudu ulos") # Ei toteutettu
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            amount = int(input("Anna summa: "))
            # Note to self: lisää tähän jokin varmistus, että syöte on sopiva
            service.add_transaction(amount, user)
        elif choice == 2:
            service.find_transactions()
        elif choice == 3:
            print("Tapahtumien poistamista ei ole vielä toteutettu.")
        elif choice == 4:
            service.logout()
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
