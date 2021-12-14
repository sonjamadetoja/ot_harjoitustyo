from services.service import service

class LoginView:
    def __init__(self):
        pass

    def show(self):
        while True:
            print("Valitse toiminto numerolla:")
            print("1 Kirjaudu")
            print("2 Luo käyttäjätunnus")
            print("3 Lopeta ohjelma")
            choice = input("Valintani: ")
            if choice == "1":
                user_name = input("Anna käyttäjätunnus: ")
                return service.login(user_name)
            elif choice == "2":
                add_user_name = input("Keksi käyttäjätunnus: (max 20 merkkiä): ")
                return service.register(add_user_name)
            elif choice == "3":
                print("Ohjelma päättyy.")
                break
            else:
                print("Virheellinen valinta.")
