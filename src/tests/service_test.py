import unittest
from services.service import Service
from entities.user import User
from repositories.fake_transaction_repository import fake_transaction_repository
from repositories.fake_user_repository import fake_user_repository

class TestService(unittest.TestCase):
    def setUp(self):
        self.user = User("Testaaja", 1)
        self.service = Service(fake_user_repository, fake_transaction_repository)
        self.service.register("Testaaja")

    def test_login_with_valid_username(self):
        response = self.service.login("Testaaja")
        validity = isinstance(response, User)

        self.assertEqual(validity, True)

    def test_login_with_invalid_username(self):
        response = self.service.login("Testaja")

        self.assertEqual(response, "no_username")

    # def test_logout(self):
    #     tester = User("Tester", 2)
    #     response = self.service.logout(tester)
    #     self.assertEqual(tester, None)
    # EI TOIMI

    # def test_register_creates_a_new_username(self):
    #     response = self.service.register("Testikäyttäjä")
    #     user = self.service.login("Testikäyttäjä")
    #     self.service.delete_user(user)
    #     self.assertEqual(response, "register")
    # ONGELMA: käyttäjän poistaminen ei onnistu

    def test_register_does_not_create_if_username_exists(self):
        response = self.service.register("Testaaja")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_long(self):
        response = self.service.register("xxxxxxxxxxxxxxxxxxxxxxxxx")

        self.assertEqual(response, False)

    def test_register_does_not_create_if_username_too_short(self):
        response = self.service.register("")

        self.assertEqual(response, False)

    def test_add_transaction(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("21-11-11", 550, user, "testi1", "testi")
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id = added_transaction[0]
        title = added_transaction[3]
        self.service.remove_transaction(id)
        self.assertEqual(title, "testi1")

    # Tämä ei varmaan oo oikein testattu (alla), koska on täysin sama kuin ylläoleva,
    # mutta en oo vielä keksinyt miten pitäis tehdä
    def test_find_transactions(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("2021-11-11", 1500, user, "testi2", "testi")
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id = added_transaction[0]
        title = added_transaction[3]
        self.service.remove_transaction(id)
        self.assertEqual(title, "testi2")

    def test_remove_transaction(self):
        user = self.service.login("Testaaja")
        self.service.add_transaction("2021-11-11", 1000, user, "testi3a", "testi")
        self.service.add_transaction("2021-11-11", 1000, user, "testi3b", "testi")
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id1 = added_transaction[0]
        self.service.remove_transaction(id1)
        deposits = self.service.find_transactions(user)
        added_transaction = deposits[-1]
        id2 = added_transaction[0]
        self.service.remove_transaction(id2)
        self.assertEqual(id2, (id1-1))

    # def test_add_file(self) TEKEMÄTTÄ: miten?