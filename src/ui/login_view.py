from services.service import service

class LoginView:
    def __init__(self):
        pass

    def show(self):
        print("Valitse toiminto numerolla:")
        print("1 Kirjaudu")
        print("2 Luo käyttäjätunnus")
        choice = int(input("Valintani: "))
        # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
        if choice == 1:
            user_name = input("Anna käyttäjätunnus: ")
            # Note to self: Lisää tsekkaus esim. tyhjälle kentälle
            return service.login(user_name)
        elif choice == 2:
            add_user_name = input("Keksi käyttäjätunnus: ")
            # Note to self: Lisää tähän joku vaatimus pituudesta ja tarkistus sille
            return service.register(add_user_name)
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
