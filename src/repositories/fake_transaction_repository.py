
from database_connection import get_database_connection_test

class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_deposit(self, date, amount, user_id, title, category):
        cursor = self._connection.cursor()
        cursor.execute('''
        INSERT INTO test_transactions (date, deposits, user_id, title, category) VALUES (?,?,?,?,?)
        ''', (date,amount,user_id,title,category))
        self._connection.commit()

    def find_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM test_transactions WHERE user_id=?', (user_id,))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def find_deposit_by_year(self, user_id, year):
        cursor = self._connection.cursor()
        date = str(year + '%')
        cursor.execute('''
        SELECT * FROM test_transactions WHERE user_id=? AND date LIKE ? ORDER BY date
        ''', (user_id,date))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def find_deposit_by_month(self, user_id, year, month):
        cursor = self._connection.cursor()
        date = str(year + '-' + month + '%')
        cursor.execute('''
        SELECT * FROM test_transactions WHERE user_id=? AND date LIKE ? ORDER BY date
        ''', (user_id,date))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def remove_deposit(self, id_number):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM test_transactions WHERE id=?', (id_number,))
        self._connection.commit()

    def remove_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM test_transactions WHERE user_id=?', (user_id,))
        self._connection.commit()

fake_transaction_repository = TransactionRepository(get_database_connection_test())
