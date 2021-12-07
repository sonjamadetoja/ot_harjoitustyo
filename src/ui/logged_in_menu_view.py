
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
        print("6 Lisää tapahtumia cvs-tiedostosta")
        print("7 Poista tapahtuma")
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            amount = int(input("Anna summa: "))
            date = input("Anna päivämäärä (muodossa yyyy-mm-dd): ")
            title = input("Anna otsikko: ")
            # Note to self: lisää tähän jokin varmistus, että syöte on sopiva
            service.add_transaction(date, amount, user, title)
        elif choice == 2:
            service.find_transactions(user)
        elif choice == 3:
            print("Tapahtumien poistamista ei ole vielä toteutettu.")
        elif choice == 4:
            service.logout(user)
        elif choice == 5:
            print("HUOM: Kaikki tietosi poistuvat.")
            # Note to self: Lisää tähän vielä varmistus siitä, haluaako käyttäjä jatkaa.
            service.delete_user(user)
            service.logout(user)
        elif choice == 6:
            filename = input("Anna tiedoston nimi: ")
            ret = service.add_file(user, filename)
            if ret == False:
                print("Virheellinen tiedostonimi.")
                return "again"
            elif ret == True:
                print("Tiedot lisätty.")
                return "again"
        elif choice == 7:
            deposits = service.find_transactions(user)
            id = int(input("Anna poistettavan tapahtuman id: "))
            service.remove_transaction(id)
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
