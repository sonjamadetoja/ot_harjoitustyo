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
        user_id = row[0]
        return row[1] == username

    def find_user_id(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        user_id = row[0]
        return user_id

    def add_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
