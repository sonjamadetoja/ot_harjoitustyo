from repositories.user_repository import user_repository
from repositories.transaction_repository import transaction_repository
from entities.user import User

class UserService:
    """Luokka, jonka avulla toteutetaan käyttäjiin liittyvä sovelluslogiikka.

    Attributes:
        user_repository: UserRepository-olion UserRepository-luokasta
        transaction_repository: TransactionRepository-olion TransactionRepository-luokasta
    """
    def __init__(self, user_repository, transaction_repository):
        """Luokan konstruktori, joka luo uuden Service-olion.
        Argumenttina annettava repositoriot tuodaan niiden omista luokista.

        Args:
            user_repository: user_repository
            transaction_repository: transaction_repository
        """
        self.user_repository = user_repository
        self.transaction_repository = transaction_repository

    def login(self, user_name):
        """Tämä funktio huolehtii käyttäjän sisäänkirjautumisesta.

        Args:
            user_name (string): Käyttäjän käyttäjänimi.

        Returns:
            Palauttaa käyttäjän, jos sisäänkirjautuminen onnistui.
            Palauttaa merkkijonon "no_username", jos sisäänkirjautuminen ei onnistunut,
            koska kyseistä käyttäjää ei löydy tietokannasta.
        """
        find_user = self.user_repository.find_user(user_name)
        if find_user is True:
            user_id = self.user_repository.find_user_id(user_name)
            user = User(user_name, user_id)
            return user
        return None

    def logout(self, user):
        """Tämä funktio huolehtii käyttäjän uloskirjautumisesta.

        Args:
            user: käyttäjä

        Returns:
            string: "logout"
        """
        user = None
        return user

    def register(self, add_user_name):
        """Tämä funktio huolehtii uuden käyttäjänimen rekisteröinnistä.

        Args:
            add_user_name (string): tallennettava käyttäjänimi.

        Returns:
            Jos rekisteröinti onnistuu, palauttaa merkkijonon "register".
            Jos rekisteröinti epäonnistuu, palauttaa False.
        """
        find_user = self.user_repository.find_user(add_user_name)
        if find_user is True:
            return False
        if add_user_name == "":
            return False
        if len(add_user_name) > 20:
            return False
        self.user_repository.add_user(add_user_name)
        return True

    def delete_user(self, user):
        """Poistaa käyttäjän tietokannoista.

        Args:
            user: poistettava käyttäjä, joka on kirjautuneena.
        """
        user_id = user.get_user_id()
        self.transaction_repository.remove_all_deposits(user_id)
        self.user_repository.remove_user(user_id)

user_service = UserService(user_repository, transaction_repository)