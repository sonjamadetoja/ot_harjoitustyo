
from services.service import service

class SearchView:
    def __init__(self):
        pass

    def show_search_options(self, user):
        while True:
            print("Valitse toiminto numerolla:")
            print("1 Hae kaikki tapahtumat")
            print("2 Hae yhden vuoden tapahtumat")
            print("3 Hae yhden kuukauden tapahtumat")
            print("4 Palaa edelliseen valikkoon")
            choice = input("Valintani: ")
            # Note to self: Tähän lisättävä joku ratkaisu siihen jos input ei ole numero
            if choice == "1":
                service.find_transactions(user)
                return "again"
            elif choice == "2":
                year = input("Anna vuosi: ")
                service.find_transaction_by_year(user, year)
                return "again"
            elif choice == "3":
                year = input("Anna vuosi: ")
                month = input("Anna kuukausi: ")
                service.find_transaction_by_month(user, year, month)
                return "again"
            elif choice == "4":
                return "return"
            else:
                print("Virheellinen valinta.")
