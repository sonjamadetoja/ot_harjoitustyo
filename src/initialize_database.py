class DataBase:
    """Tietokannasta vastaava luokka.
    """

    def __init__(self, connection, user_repository):
        """Luokan konstruktori.

        Args:
            connection: tietokantayhteys
            user_repository: Tietokannan käyttäjätoiminnoista vastaava olio.
        """
        self._connection = connection
        self._user_repository = user_repository

    def create_tables(self):
        """Luo sekä varsinaiset tietokantataulut että testitietokantataulut, jos niitä ei vielä ole.

        Returns:
            True.
        """
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
        """Lisää tietokantatauluihin testikäyttäjän nimellä "Testaaja", jos sellaista ei vielä ole.

        Returns:
            True, jos lisäys onnistuu.
            False, jos lisäystä ei tehdä.
        """
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
        """Poistaa kaikki olemassaolevat tietokantataulut.

        Returns:
            True.
        """
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
        """Alustaa tietokannan kutsumalla taulut luovaa funktiota
        ja testikäyttäjän luovaa funktiota.
        """
        self.create_tables()
        self.insert_test_user()
