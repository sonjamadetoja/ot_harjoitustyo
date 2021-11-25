from repositories.user_repository import user_repository

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
            find_user = user_repository.find_user(user_name)
            if find_user is True:
                return "login"
            else:
                print("Tällaista käyttäjää ei ole. Ohjelma päättyy.")
                # Note to self: Lisää tähän return niin että se palaa alkuun tms
        elif choice == 2:
            add_user_name = input("Keksi käyttäjätunnus: ")
            # Note to self: Lisää tähän joku vaatimus pituudesta ja tarkistus sille
            find_user = user_repository.find_user(add_user_name)
            if find_user is True:
                print("Tämä käyttäjänimi on jo olemassa. Ohjelma päättyy.")
                # Note to self: Lisää tähän return niin että se palaa alkuun tms
            else:
                user_repository.add_user(add_user_name)
                return "register"
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")
