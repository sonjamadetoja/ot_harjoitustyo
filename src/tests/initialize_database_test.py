import unittest
from initialize_database import DataBase
from database_connection import get_database_connection_test
from repositories.fake_user_repository import fake_user_repository

class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase(get_database_connection_test(), fake_user_repository)

    def test_create_tables(self):
        self.db.drop_tables()
        response = self.db.create_tables()
        self.assertEqual(response, True)
        self.db.initialize_database()

    def test_drop_tables(self):
        response = self.db.drop_tables()
        self.assertEqual(response, True)
        self.db.initialize_database()

    def test_insert_test_user_successful(self):
        self.db.drop_tables()
        self.db.create_tables()
        response = self.db.insert_test_user()
        self.db.drop_tables()
        self.db.initialize_database()
        self.assertEqual(response, True)

    def test_insert_test_user_unsuccessful(self):
        self.db.drop_tables()
        self.db.create_tables()
        self.db.insert_test_user()
        response = self.db.insert_test_user()
        self.db.drop_tables()
        self.db.initialize_database()
        self.assertEqual(response, False)
