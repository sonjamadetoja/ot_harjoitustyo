
from database_connection import get_database_connection

class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_deposit(self, amount):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO transactions (deposits) VALUES (?)', (amount,))
        self._connection.commit()

    def find_all_deposits(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions')
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[1]
            deposits.append(tpl)
        sum_transactions = 0
        for item in deposits:
            print(item)
            sum_transactions = sum_transactions+item
        print("Yhteensä: ", sum_transactions)

transaction_repository = TransactionRepository(get_database_connection())
