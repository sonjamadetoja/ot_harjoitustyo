import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def test_get_user_id(self):
        test_user = User("tester", 5)
        id = test_user.get_user_id()

        self.assertEqual(id, 5)