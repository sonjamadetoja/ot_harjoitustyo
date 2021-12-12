class User:
    """Tallentaa sisäänkirjautuneen käyttäjän
    käyttäjätunnuksen ja tietokannan tunnusnumeron.

    Attributes:
        user_name (string): käyttäjätunnus
        user_id (integer): tunnusnumero
    """

    def __init__(self, user_name, user_id):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            user_name (string): käyttäjätunnus
            user_id (integer): tunnusnumero
        """
        self.user_name = user_name
        self.user_id = user_id

    def get_user_id(self):
        """Palauttaa kirjautuneena olevan käyttäjän käyttäjätunnuksen.

        Returns:
            string: Käyttäjätunnus.
        """
        return self.user_id
