from repositories.user_repository import user_repository

class DataBase:

    def __init__(self, connection):
        self._connection = connection

    def create_tables(self):
        cursor = self._connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, date TIMESTAMP, deposits INTEGER, user_id INTEGER REFERENCES users, title TEXT, category TEXT);
            ''')
        return True

    def insert_test_user(self):
        cursor = self._connection.cursor()
        find_user = user_repository.find_user('Testaaja')
        if find_user is False:
            cursor.execute('''
                INSERT INTO users (username) VALUES ('Testaaja');
                ''')
            self._connection.commit()

    def initialize_database(self):
        connection = self._connection
        self.create_tables()
        self.insert_test_user()
