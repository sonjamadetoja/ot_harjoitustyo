import unittest
from services.service import service

class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_login_with_valid_username(self):
        response = service.login("Testaaja")

        self.assertEqual(response, "login")

    def test_login_with_invalid_username(self):
        response = service.login("Testaja")

        self.assertEqual(response, None)

    # def test_register_creates_a_new_username(self):
    #     pass
    #    self.assertEqual(response, "register")

    def test_register_does_not_create_if_username_exists(self):
        response = service.register("Testaaja")

        self.assertEqual(response, False)
