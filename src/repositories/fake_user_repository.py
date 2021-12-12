from database_connection import get_database_connection_test

class FakeUserRepository:
    """Käyttäjiin liittyvistä testitietokantaoperaatioista vastaava luokka,
    joka on tehty service-luokan testaamista varten.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: tietokantayhteys.
        """
        self._connection = connection

    def find_user(self, username):
        """Hakee käyttäjän tiedot tietokannasta käyttäjänimen perusteella,
        ja tarkistaa siten, että käyttäjä on olemassa.

        Args:
            username (string): käyttäjänimi.

        Returns:
            True, jos käyttäjä löytyy.
            False, jos käyttäjää ei löydy.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM test_users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row is None:
            return False
        return row[1] == username

    def find_user_id(self, username):
        """Hakee käyttäjän tunnusnumeron tietokannasta käyttäjätunnuksen perusteella.

        Args:
            username (string): käyttäjätunnus.

        Returns:
            integer: käyttäjän tunnusnumero.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT id FROM test_users WHERE username=?', (username,))
        row = cursor.fetchone()
        user_id = row[0]
        return user_id

    def add_user(self, username):
        """Lisää käyttäjän tietokantaan.

        Args:
            username (string): käyttäjätunnus.
        """
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO test_users (username) VALUES (?)', (username,))
        self._connection.commit()

    def remove_user(self, user_id):
        """Poistaa käyttäjän tietokannasta.

        Args:
            username (string): käyttäjätunnus.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM test_users WHERE username=?', (user_id,))
        self._connection.commit()

fake_user_repository = FakeUserRepository(get_database_connection_test())
