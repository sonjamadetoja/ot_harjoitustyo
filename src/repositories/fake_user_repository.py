from database_connection import get_database_connection_test

class FakeUserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM test_users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row is None:
            return False
        user_id = row[0]
        return row[1] == username

    def find_user_id(self, username):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id FROM test_users WHERE username=?', (username,))
        row = cursor.fetchone()
        user_id = row[0]
        return user_id

    def add_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO test_users (username) VALUES (?)', (username,))
        self._connection.commit()

    def remove_user(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM test_users WHERE username=?', (user_id,))
        self._connection.commit()

fake_user_repository = FakeUserRepository(get_database_connection_test())
