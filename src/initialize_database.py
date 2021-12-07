from repositories.user_repository import user_repository

class DataBase:

    def __init__(self, connection, user_repository):
        self._connection = connection
        self._user_repository = user_repository

    def create_tables(self):
        cursor = self._connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, date TIMESTAMP, deposits INTEGER, user_id INTEGER REFERENCES users, title TEXT, category TEXT);
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_transactions (id INTEGER PRIMARY KEY, date TIMESTAMP, deposits INTEGER, user_id INTEGER REFERENCES users, title TEXT, category TEXT);
            ''')
        return True

    def insert_test_user(self):
        cursor = self._connection.cursor()
        find_user = self._user_repository.find_user('Testaaja')
        if find_user is False:
            cursor.execute('''
                INSERT INTO users (username) VALUES ('Testaaja');
                ''')
            self._connection.commit()
            cursor.execute('''
                INSERT INTO test_users (username) VALUES ('Testaaja');
                ''')
            self._connection.commit()
            return True
        return False

    def drop_tables(self):
        cursor = self._connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS users;''')
        self._connection.commit()
        cursor.execute('''DROP TABLE IF EXISTS transactions;''')
        self._connection.commit()
        cursor.execute('''DROP TABLE IF EXISTS test_users;''')
        self._connection.commit()
        cursor.execute('''DROP TABLE IF EXISTS test_transactions;''')
        self._connection.commit()
        return True

    def initialize_database(self):
        self.create_tables()
        self.insert_test_user()
