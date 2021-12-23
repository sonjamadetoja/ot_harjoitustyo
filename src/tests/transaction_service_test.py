import unittest
from services.transaction_service import TransactionService
from services.user_service import UserService
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
        self.user_service = UserService(self.user_repository, self.transaction_repository)
        self.transaction_service = TransactionService(self.transaction_repository)
        self.user_service.register("Testaaja")

    def test_add_transaction(self):
        user = self.user_service.login("Testaaja")
        self.transaction_service.add_transaction("21-11-11", 550, user, "testi1", "testi")
        deposits = self.transaction_service.find_transactions(user)
        added_transaction = deposits[-1]
        id = added_transaction[0]
        title = added_transaction[3]
        self.transaction_service.remove_transaction(id)
        self.assertEqual(title, "testi1")

    def test_find_transactions(self):
        user = self.user_service.login("Testaaja")
        self.transaction_service.add_transaction("2021-11-11", 1500, user, "testi4", "testi")
        self.transaction_service.add_transaction("2021-11-11", 1500, user, "testi5", "testi")
        deposits = self.transaction_service.find_transactions(user)
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
        self.transaction_service.remove_transaction(id_first)
        self.transaction_service.remove_transaction(id_second)

    def test_find_transactions_if_none(self):
        user = self.user_service.login("Testaaja")
        user_id = user.get_user_id()
        self.transaction_repository.remove_all_deposits(user_id)
        deposits = self.transaction_service.find_transactions(user)
        response = False
        if not deposits:
            response = True
        self.assertEqual(response, True)

    def test_remove_transaction(self):
        user = self.user_service.login("Testaaja")
        self.transaction_service.add_transaction("2021-11-11", 1000, user, "testi3a", "testi")
        self.transaction_service.add_transaction("2021-11-11", 1000, user, "testi3b", "testi")
        deposits = self.transaction_service.find_transactions(user)
        added_transaction = deposits[-1]
        id1 = added_transaction[0]
        self.transaction_service.remove_transaction(id1)
        deposits = self.transaction_service.find_transactions(user)
        added_transaction = deposits[-1]
        id2 = added_transaction[0]
        self.transaction_service.remove_transaction(id2)
        self.assertEqual(id2, (id1-1))
