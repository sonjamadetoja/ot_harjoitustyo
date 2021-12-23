import unittest
from initialize_database import DataBase
from repositories.transaction_repository import TransactionRepository
from repositories.user_repository import UserRepository
from database_connection import get_database_connection_test

class TestTransactionRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection_test())
        self.transaction_repository = TransactionRepository(get_database_connection_test())
        database = DataBase(get_database_connection_test(), self.user_repository)
        database.initialize_database()

    def test_add_deposit(self):
        self.transaction_repository.add_deposit("2021-12-12", -30, 10, "puhelinlasku", "menot")
        cursor = get_database_connection_test().cursor()
        cursor.execute('SELECT id FROM transactions WHERE user_id=10 AND date="2021-12-12" AND deposits=-30 AND title="puhelinlasku" AND category="menot"')
        result = cursor.fetchall()
        if not result:
            response = False
        else:
            response = True
        id = result[0][0]
        self.transaction_repository.remove_deposit(id)
        self.assertEqual(response, True)

    def test_find_all_deposits(self):
        self.transaction_repository.add_deposit("2021-12-12", -30, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2021-12-12", -40, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2021-12-12", -50, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2021-12-12", -60, 10, "puhelinlasku", "menot")
        result = self.transaction_repository.find_all_deposits(10)
        response = False
        if len(result) == 4:
            response = True
        self.assertEqual(response, True)

    def test_find_deposit_by_year(self):
        self.transaction_repository.add_deposit("2018-12-12", -30, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2019-12-12", -40, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2020-12-12", -50, 10, "puhelinlasku", "menot")
        result = self.transaction_repository.find_deposit_by_year(10, "2018")
        response = False
        if len(result) == 1:
            response = True
        self.assertEqual(response, True)

    def test_find_deposit_by_year_if_none(self):
        result = self.transaction_repository.find_deposit_by_year(10, "2000")
        response = False
        if result == None:
            response = True
        self.assertEqual(response, True)

    def test_find_deposit_by_month(self):
        self.transaction_repository.add_deposit("2017-08-12", -30, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2017-09-12", -40, 10, "puhelinlasku", "menot")
        self.transaction_repository.add_deposit("2017-10-12", -50, 10, "puhelinlasku", "menot")
        result = self.transaction_repository.find_deposit_by_month(10, "2017", "10")
        response = False
        if len(result) == 1:
            response = True
        self.assertEqual(response, True)

    def test_find_deposit_by_month_if_none(self):
        self.transaction_repository.add_deposit("2017-11-12", -60, 10, "puhelinlasku", "menot")
        result = self.transaction_repository.find_deposit_by_month(10, "2017", "12")
        response = False
        if result == None:
            response = True
        self.assertEqual(response, True)

    def test_remove_deposit(self):
        self.transaction_repository.add_deposit("2021-12-12", -70, 10, "puhelinlasku", "menot")
        cursor = get_database_connection_test().cursor()
        cursor.execute('SELECT id FROM transactions WHERE user_id=10 AND date="2021-12-12" AND deposits=-70 AND title="puhelinlasku" AND category="menot"')
        id = cursor.fetchall()[0][0]
        self.transaction_repository.remove_deposit(id)
        cursor.execute('SELECT id FROM transactions WHERE id=?', (id,))
        result = cursor.fetchall()
        response = True
        if not result:
            response = False
        self.assertEqual(response, False)

    def test_remove_all_deposits(self):
        self.transaction_repository.add_deposit("2010-08-12", -30, 10, "puhelinlasku", "menot")
        self.transaction_repository.remove_all_deposits(10)
        cursor = get_database_connection_test().cursor()
        cursor.execute('SELECT id FROM transactions WHERE user_id=10')
        result = cursor.fetchall()
        response = True
        if not result:
            response = False
        self.assertEqual(response, False)
