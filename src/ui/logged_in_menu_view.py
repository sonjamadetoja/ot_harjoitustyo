
from services.service import service
from entities.user import User

class MenuView:
    def __init__(self):
        pass

    def show_menu(self, user):
        print("Valitse toiminto numerolla:")
        print("1 Lisää tapahtuma")
        print("2 Katso tapahtumia") 
        print("3 Poista tapahtuma")
        print("4 Kirjaudu ulos")
        print("5 Poista käyttäjätunnus")
        print("6 Lisää tapahtumia cvs-tiedostosta")
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            amount = int(input("Anna summa: "))
            date = input("Anna päivämäärä (muodossa yyyy-mm-dd): ")
            title = input("Anna otsikko: ")
            category = input("Luokittele tapahtuma: ") 
            # Note to self: Tähän voisi tulla graafisessa käyttöliittymässä myös drop down valikko
            # Note to self: lisää tähän jokin varmistus, että syötteet ovat sopivia
            ret = service.add_transaction(date, amount, user, title, category)
            if ret == True:
                print("Tapahtuma on lisätty.")
            return "again"
        elif choice == 2:
            return "search"
        elif choice == 3:
            deposits = service.find_transactions(user)
            id = int(input("Anna poistettavan tapahtuman id: "))
            # Note to self: lisää tähän jotain siltä varalta, että syöte ei ole sopiva
            service.remove_transaction(id)
            return "again"
        elif choice == 4:
            service.logout(user)
        elif choice == 5:
            print("HUOM: Kaikki tietosi poistuvat.")
            action = input("Haluatko varmasti jatkaa? Vastaa \"kyllä\" tai \"ei\": ")
            if action == "kyllä":
                service.delete_user(user)
                service.logout(user)
                print("Käyttäjätunnuksesi on poistettu. Ohjelma päättyy.")
            elif action == "ei":
                return "again"
            else:
                print("Vastaus oli virheellinen.")
                return "again"
        elif choice == 6:
            filename = input("Anna tiedoston nimi: ")
            ret = service.add_file(user, filename)
            if ret == False:
                print("Virheellinen tiedostonimi.")
                return "again"
            elif ret == True:
                print("Tiedot lisätty.")
                return "again"
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
