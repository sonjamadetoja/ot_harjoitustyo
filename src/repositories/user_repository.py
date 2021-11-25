from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row is None:
            return False
        return row[1] == username

    def add_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
