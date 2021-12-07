
from database_connection import get_database_connection

class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_deposit(self, date, amount, user_id, title, category):
        cursor = self._connection.cursor()
        cursor.execute('''
        INSERT INTO transactions (date, deposits, user_id, title, category) VALUES (?,?,?,?,?)
        ''', (date,amount,user_id,title,category))
        self._connection.commit()

    def find_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE user_id=?', (user_id,))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4]
            deposits.append(tpl)
        sum_transactions = 0
        for item in deposits:
            item_string = "id: "+str(item[0])+", "+item[1]+", "+str(item[2])+", "+item[3]
            print(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)
        return deposits

    def find_deposit_by_year(self, user_id, year):
        cursor = self._connection.cursor()
        date = str(year + '%') 
        cursor.execute('SELECT * FROM transactions WHERE user_id=? AND date LIKE ?', (user_id,date))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4]
            deposits.append(tpl)
        sum_transactions = 0
        for item in deposits:
            item_string = "id: "+str(item[0])+", "+item[1]+", "+str(item[2])+", "+item[3]
            print(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)
        return deposits

    def find_deposit_by_month(self, user_id, year, month):
        cursor = self._connection.cursor()
        date = str(year + '-' + month + '%') 
        cursor.execute('SELECT * FROM transactions WHERE user_id=? AND date LIKE ?', (user_id,date))
        all_transactions = cursor.fetchall()
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4]
            deposits.append(tpl)
        sum_transactions = 0
        for item in deposits:
            item_string = "id: "+str(item[0])+", "+item[1]+", "+str(item[2])+", "+item[3]
            print(item_string)
            item = int(item[2])
            sum_transactions = sum_transactions+item
        print("Saldo: ", sum_transactions)
        return deposits

    def remove_deposit(self, id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE id=?', (id,))
        self._connection.commit()

    def remove_all_deposits(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE user_id=?', (user_id,))
        self._connection.commit()


transaction_repository = TransactionRepository(get_database_connection())
