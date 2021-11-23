
from database_connection import get_database_connection

class DataBase:

    def create_tables(self,connection):
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);
            ''')
        return True

    def insert_test_user(self,connection):
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO users (username) VALUES ('Testaaja');
            ''')

    def initialize_database(self):
        connection = get_database_connection()
        self.create_tables(connection)
        self.insert_test_user(connection)

db = DataBase()
db.initialize_database()