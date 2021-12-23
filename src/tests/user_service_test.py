import unittest
from services.user_service import UserService
from entities.user import User
from repositories.transaction_repository import TransactionRepository
from repositories.user_repository import UserRepository
from initialize_database import DataBase
from database_connection import get_database_connection_test

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection_test())
        self.transaction_repository = TransactionRepository(get_database_connection_test())
        database = DataBase(get_database_connection_test(), self.user_repository)
        database.initialize_database()
        self.user = User("Testaaja", 1)
        self.user_service = UserService(self.user_repository, self.transaction_repository)
        self.user_service.register("Testaaja")

    def test_login_with_valid_username(self):
        response = self.user_service.login("Testaaja")
        validity = isinstance(response, User)

        self.assertEqual(validity, True)

    def test_login_with_invalid_username(self):
        response = self.user_service.login("Testaja")

        self.assertEqual(response, None)

    def test_logout(self):
        tester = User("Tester", 2)
        response = self.user_service.logout(tester)
        self.assertEqual(response, None)

    def test_register_creates_a_new_username(self):
        response = self.user_service.register("Testikäyttäjä")
        user = self.user_service.login("Testikäyttäjä")
        self.user_service.delete_user(user)
        self.assertEqual(response, True)

    def test_register_does_not_create_if_username_exists(self):
        response = self.user_service.register("Testaaja")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_long(self):
        response = self.user_service.register("xxxxxxxxxxxxxxxxxxxxxxxxx")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_short(self):
        response = self.user_service.register("")

        self.assertEqual(response, False)