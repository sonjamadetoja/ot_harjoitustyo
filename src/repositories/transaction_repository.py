
from database_connection import get_database_connection

class TransactionRepository:
    """Tapahtumiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: tietokantayhteys.
        """
        self._connection = connection

    def add_deposit(self, date, amount, user_id, title, category):
        """Tallentaa tapahtuman tietokantaan.

        Args:
            date: päivämäärä
            amount: summa (positiivinen tai negatiivinen tapahtumasta riippuen)
            user: kirjautuneena oleva käyttäjä
            title: tapahtuman otsikko
            category: tapahtuman luokittelu
        """
        cursor = self._connection.cursor()
        cursor.execute('''
        INSERT INTO transactions (date, deposits, user_id, title, category) VALUES (?,?,?,?,?)
        ''', (date,amount,user_id,title,category))
        self._connection.commit()

    def find_all_deposits(self, user_id):
        """Hakee kaikki käyttäjän tapahtumat tietokannasta.

        Args:
            user_id (integer): käyttäjän tunnusnumero tietokannassa.

        Returns:
            lista: lista tapahtumista
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE user_id=? ORDER BY date', (user_id,))
        all_transactions = cursor.fetchall()
        if not all_transactions:
            return None
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def find_deposit_by_year(self, user_id, year):
        """Hakee kaikki käyttäjän tapahtumat tietokannasta yhden vuoden ajalta.

        Args:
            user_id (integer): käyttäjän tunnusnumero tietokannassa.
            year (integer): vuosi

        Returns:
            lista: lista tapahtumista
        """
        cursor = self._connection.cursor()
        date = str(year + '%')
        cursor.execute('''
        SELECT * FROM transactions WHERE user_id=? AND date LIKE ? ORDER BY date
        ''', (user_id,date))
        all_transactions = cursor.fetchall()
        if not all_transactions:
            return None
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def find_deposit_by_month(self, user_id, year, month):
        """Hakee kaikki käyttäjän tapahtumat tietokannasta yhden kuukauden ajalta.

        Args:
            user_id (integer): käyttäjän tunnusnumero tietokannassa.
            year (integer): vuosi
            monts (integer): kuukausi

        Returns:
            lista: lista tapahtumista
        """
        cursor = self._connection.cursor()
        date = str(year + '-' + month + '%')
        cursor.execute('''
        SELECT * FROM transactions WHERE user_id=? AND date LIKE ? ORDER BY date
        ''', (user_id,date))
        all_transactions = cursor.fetchall()
        if not all_transactions:
            return None
        deposits = []
        for row in all_transactions:
            tpl = row[0], row[1], row[2], row[4], row[5]
            deposits.append(tpl)
        return deposits

    def remove_deposit(self, id_number):
        """Poistaa tapahtuman tietokannasta.

        Args:
            id_number (integer): tapahtuman tunnusnumero tietokannassa.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE id=?', (id_number,))
        self._connection.commit()

    def remove_all_deposits(self, user_id):
        """Poistaa kaikki kirjautuneen käyttäjän tapahtumat tietokannasta.

        Args:
            user_id (integer): käyttäjän tunnusnumero tietokannassa.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM transactions WHERE id=?', (user_id,))
        self._connection.commit()

transaction_repository = TransactionRepository(get_database_connection())
