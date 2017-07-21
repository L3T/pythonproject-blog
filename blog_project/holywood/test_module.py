import unittest
from security.models import UserInfo

class UserModeTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = UserInfo(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = UserInfo(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = UserInfo(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertTrue(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = UserInfo(password='cat')
        u2 = UserInfo(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
