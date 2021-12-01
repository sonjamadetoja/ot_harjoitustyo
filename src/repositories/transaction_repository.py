
from database_connection import get_database_connection

class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_deposit(self, amount, user_id):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO transactions (deposits, user_id) VALUES (?,?)', (amount,user_id))
        self._connection.commit()

    def find_all_deposits(self ,user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE user_id=?', (user_id,))
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
