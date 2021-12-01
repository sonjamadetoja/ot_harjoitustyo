
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
        print("4 Kirjaudu ulos")
        print("5 Poista käyttäjätunnus")
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            amount = int(input("Anna summa: "))
            # Note to self: lisää tähän jokin varmistus, että syöte on sopiva
            service.add_transaction(amount, user)
        elif choice == 2:
            service.find_transactions(user)
        elif choice == 3:
            print("Tapahtumien poistamista ei ole vielä toteutettu.")
        elif choice == 4:
            service.logout(user)
        elif choice == 5:
            print("HUOM: Kaikki tietosi poistuvat.")
            # Lisää tähän vielä varmistus siitä, haluaako käyttäjä jatkaa.
            service.delete_user(user)
            service.logout(user)
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
