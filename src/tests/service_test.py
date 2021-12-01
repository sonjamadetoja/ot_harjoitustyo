import unittest
from services.service import service
from entities.user import User

class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_login_with_valid_username(self):
        response = service.login("Testaaja")
        validity = isinstance(response, User)

        self.assertEqual(validity, True)

    def test_login_with_invalid_username(self):
        response = service.login("Testaja")

        self.assertEqual(response, "no_username")

    # def test_register_creates_a_new_username(self):
    #     pass
    #    self.assertEqual(response, "register")

    def test_register_does_not_create_if_username_exists(self):
        response = service.register("Testaaja")

        self.assertEqual(response, False)
