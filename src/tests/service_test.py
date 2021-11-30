import unittest
from services.service import Service

class TestService:
    def setUp(self):
        self.service = Service()

    def test_login_with_valid_username(self):
        response = self.service.login("Testaaja")

        self.AssertEqual(response, "login")

    def test_login_with_invalid_username(self):
        response = self.service.login("Testaja")

        self.AssertEqual(response, None)

    # def test_register_creates_a_new_username(self):
    #     pass

    def test_register_does_not_create_if_username_exists(self):
        response = self.service.register("Testaaja")

        self.AssertEqual(response, False)
