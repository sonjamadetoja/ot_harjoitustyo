import unittest
from services.service import Service
from entities.user import User
from repositories.transaction_repository import TransactionRepository
from repositories.user_repository import UserRepository
from initialize_database import DataBase
from database_connection import get_database_connection_test

class TestService(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection_test())
        self.transaction_repository = TransactionRepository(get_database_connection_test())
        database = DataBase(get_database_connection_test(), self.user_repository)
        database.initialize_database()
        self.user = User("Testaaja", 1)
        self.service = Service(self.user_repository, self.transaction_repository)
        self.service.register("Testaaja")

    def test_login_with_valid_username(self):
        response = self.service.login("Testaaja")
        validity = isinstance(response, User)

        self.assertEqual(validity, True)

    def test_login_with_invalid_username(self):
        response = self.service.login("Testaja")

        self.assertEqual(response, None)

    def test_logout(self):
        tester = User("Tester", 2)
        response = self.service.logout(tester)
        self.assertEqual(response, None)

    def test_register_creates_a_new_username(self):
        response = self.service.register("Testikäyttäjä")
        user = self.service.login("Testikäyttäjä")
        self.service.delete_user(user)
        self.assertEqual(response, True)

    def test_register_does_not_create_if_username_exists(self):
        response = self.service.register("Testaaja")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_long(self):
        response = self.service.register("xxxxxxxxxxxxxxxxxxxxxxxxx")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_short(self):
        response = self.service.register("")

        self.assertEqual(response, False)

    def test_add_transaction(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("21-11-11", 550, user, "testi1", "testi")
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id = added_transaction[0]
        title = added_transaction[3]
        self.service.remove_transaction(id)
        self.assertEqual(title, "testi1")

    def test_find_transactions(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("2021-11-11", 1500, user, "testi4", "testi")
        self.service.add_transaction("2021-11-11", 1500, user, "testi5", "testi")
        deposits = self.service.find_transactions(user)
        print(deposits)
        response = False
        if len(deposits) == 2:
            response = True
        self.assertEqual(response, True)
        # Lisättyjen tapahtumien poistaminen
        first_transaction = deposits[-2]
        second_transaction = deposits[-1]
        id_first = first_transaction[0]
        id_second = second_transaction[0]
        self.service.remove_transaction(id_first)
        self.service.remove_transaction(id_second)

    def test_find_transactions_if_none(self):
        user = self.service.login("Testaaja")
        user_id = user.get_user_id()
        self.transaction_repository.remove_all_deposits(user_id)
        deposits = self.service.find_transactions(user)
        response = False
        if not deposits:
            response = True
        self.assertEqual(response, True)

    # def test_find_transaction_by_year(self):
    #     user = self.service.login("Testaaja")
    #     self.service.add_transaction("2020-11-11", 1500, user, "testi6", "testi")
    #     self.service.add_transaction("2019-11-11", 1500, user, "testi9", "testi")
    #     deposits = self.service.find_transaction_by_year(user, "2020")
    #     print(deposits)

    #     deposits = self.service.find_transactions(user)
    #     print(deposits)

    #     response = False
    #     if len(deposits) == 1:
    #         response = True
    #     self.assertEqual(response, True)
    #     # Lisättyjen tapahtumien poistaminen
    #     first_transaction = deposits[-2]
    #     second_transaction = deposits[-1]
    #     id_first = first_transaction[0]
    #     id_second = second_transaction[0]
    #     self.service.remove_transaction(id_first)
    #     self.service.remove_transaction(id_second)

    # def test_find_transaction_by_year_if_none(self):
    #     user = self.service.login("Testaaja")
    #     user_id = user.get_user_id()
    #     self.transaction_repository.remove_all_deposits(user_id)
    #     self.service.add_transaction("2018-11-11", 1500, user, "testi10", "testi")
    #     self.service.add_transaction("2019-11-11", 1500, user, "testi11", "testi")
    #     deposits = self.service.find_transaction_by_year(user, "2019")
    #     print(deposits)
    #     response = False
    #     if not deposits:
    #         response = True
    #     user_id = user.get_user_id()
    #     self.transaction_repository.remove_all_deposits(user_id)
    #     self.assertEqual(response, False)
    #     # Lisättyjen tapahtumien poistaminen
    #     first_transaction = deposits[-2]
    #     second_transaction = deposits[-1]
    #     id_first = first_transaction[0]
    #     id_second = second_transaction[0]
    #     self.service.remove_transaction(id_first)
    #     self.service.remove_transaction(id_second)

    # def test_find_transaction_by_month(self):
    #     user = self.service.login("Testaaja")
    #     self.service.add_transaction("2020-11-11", 1500, user, "testi12", "testi")
    #     self.service.add_transaction("2020-12-11", 1500, user, "testi13", "testi")
    #     self.service.add_transaction("2019-11-11", 1500, user, "testi14", "testi")
    #     self.service.add_transaction("2019-12-11", 1500, user, "testi15", "testi")
    #     deposits = self.service.find_transaction_by_month(user, "2020", "11")
    #     print(deposits)

    #     deposits = self.service.find_transactions(user)
    #     print(deposits)

    #     response = False
    #     if len(deposits) == 1:
    #         response = True
    #     self.assertEqual(response, True)
    #     user_id = user.get_user_id()
    #     self.transaction_repository.remove_all_deposits(user_id)

    # def test_find_transaction_by_month_if_none(self):
    #     user = self.service.login("Testaaja")
    #     user_id = user.get_user_id()
    #     self.transaction_repository.remove_all_deposits(user_id)
    #     self.service.add_transaction("2018-11-11", 1500, user, "testi16", "testi")
    #     self.service.add_transaction("2018-12-11", 1500, user, "testi17", "testi")
    #     self.service.add_transaction("2019-11-11", 1500, user, "testi18", "testi")
    #     self.service.add_transaction("2019-12-11", 1500, user, "testi19", "testi")
    #     deposits = self.service.find_transaction_by_month(user, "2019", "11")
    #     print(deposits)
    #     response = False
    #     if not deposits:
    #         response = True
    #     user_id = user.get_user_id()
    #     self.transaction_repository.remove_all_deposits(user_id)
    #     self.assertEqual(response, False)

    def test_remove_transaction(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("2021-11-11", 1000, user, "testi3a", "testi")
        self.service.add_transaction("2021-11-11", 1000, user, "testi3b", "testi")
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id1 = added_transaction[0]
        self.service.remove_transaction(id1)
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id2 = added_transaction[0]
        self.service.remove_transaction(id2)
        self.assertEqual(id2, (id1-1))

    # def test_add_file(self) TEKEMÄTTÄ: miten?