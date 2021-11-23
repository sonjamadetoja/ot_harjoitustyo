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
            userName = input("Anna käyttäjätunnus:")
            bool = user_repository.find_user(userName)
            if bool == True:
                return "login"
            else:
                print("Tällaista käyttäjää ei ole. Ohjelma päättyy.")
        elif choice == 2:
            addUserName = input("Keksi käyttäjätunnus:")
            # Note to self: Lisää tähän joku vaatimus pituudesta ja tarkistus sille
            print("Tähän tulee kutsu tietokantatoimintoon, ei vielä valmis")
            return "register"
        else:
            print("Virheellinen valinta. Ohjelma päättyy.")