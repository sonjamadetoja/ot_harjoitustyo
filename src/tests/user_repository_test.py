import unittest
from initialize_database import DataBase
from repositories.user_repository import UserRepository
from database_connection import get_database_connection_test


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection_test())
        database = DataBase(get_database_connection_test(), self.user_repository)
        database.initialize_database()

    def test_find_user_when_exists(self):
        response = self.user_repository.find_user("Testaaja")

        self.assertEqual(response, True)
    
    def test_find_user_when_doesnt_exist(self):
        response = self.user_repository.find_user("Sonja")

        self.assertEqual(response, False)

    def test_find_user_id_successful(self):
        response = self.user_repository.find_user_id("Testaaja")

        self.assertEqual(response, 1)

    def test_add_user(self):
        self.user_repository.add_user("Maaria")
        response = self.user_repository.find_user("Maaria")
        id = self.user_repository.find_user_id("Maaria")
        self.user_repository.remove_user(id)

        self.assertEqual(response, True)

    def test_remove_user(self):
        self.user_repository.add_user("Maria")
        id = self.user_repository.find_user_id("Maria")
        self.user_repository.remove_user(id)
        response = self.user_repository.find_user("Maria")

        self.assertEqual(response, False)