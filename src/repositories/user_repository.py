
from sqlite3.dbapi2 import connect
from database_connection import get_database_connection

class UserRepository:
    def _init_(self, connection):
        self._connection = connection

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row[1] == username:
            return True
        else:
            return False

user_repository = UserRepository(get_database_connection())