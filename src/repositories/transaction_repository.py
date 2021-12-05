
from database_connection import get_database_connection

class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_deposit(self, date, amount, user_id, title):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO transactions (date, deposits, user_id, title) VALUES (?,?,?,?)', (date,amount,user_id,title))
        self._connection.commit()

    def find_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE user_id=?', (user_id,))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[1], row[2], row[4]
            deposits.append(tpl)
        sum_transactions = 0
        for item in deposits:
            item_string = item[0]+", "+str(item[1])+", "+item[2]
            print(item_string)
            item = int(item[1])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)

    def remove_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE user_id=?', (user_id,))
        self._connection.commit()


transaction_repository = TransactionRepository(get_database_connection())
