import unittest
from unittest.mock import patch

from email_validator import EmailNotValidError

from user import User

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.user_class = User("Password1.")

    def test_validate_user_firstname_given_correct_value_when_registering(self):
        self.assertEqual("Mercy", self.user_class.validate_user_firstname("Mercy"))

    def test_validate_user_firstname_given_invalid_input_raise_exception(self):
        with self.assertRaises(ValueError):
            self.user_class.validate_user_firstname("M Er")

    def test_validate_user_lastname_given_correct_value_when_registering(self):
        self.assertEqual("Babayemi", self.user_class.validate_user_lastname("Babayemi"))

    def test_validate_user_lastname_given_invalid_input_raise_exception(self):
        with self.assertRaises(ValueError):
            self.user_class.validate_user_firstname(" ")

    def test_validate_user_password_success_given_correct_value_when_registering_user(self):
        self.assertEqual("Password1.", self.user_class.validate_user_password("Password1."))

    def test_validate_user_password_given_invalid_input_raise_exception(self):
        with self.assertRaises(ValueError):
            self.user_class.validate_user_password("pass")

    def test_validate_user_email_given_correct_value_when_registering(self):
        self.assertEqual("mercy@gmail.com", self.user_class.validate_user_email("mercy@gmail.com"))

    def test_validate_user_email_given_invalid_input_raise_exception(self):
        with self.assertRaises(ValueError):
            self.user_class.validate_user_email("mercy@gm")

    def test_invalid_email(self):
        email = "invalid-email"
        with self.assertRaises(ValueError):
            self.user_class.validate_user_email(email)

    def test_that_collect_user_firstname_returns_correct_value_when_given_valid_input(self):
        with unittest.mock.patch('builtins.input', return_value="Mercy"):
            firstname = self.user_class.collect_user_firstname()
            self.assertEqual("Mercy", firstname)

    def test_that_collect_user_firstname_except_exception_when_given_invalid_input(self):
        with patch('builtins.input', return_value=" "):
            self.assertEqual(None ,self.user_class.collect_user_firstname())

    def test_that_collect_user_lastname_returns_correct_value_when_given_valid_input(self):
        with unittest.mock.patch('builtins.input', return_value="Babayemi"):
            lastname = self.user_class.collect_user_lastname()
            self.assertEqual("Babayemi", lastname)

    def test_that_collect_user_lastname_except_exception_when_given_invalid_input(self):
        with patch('builtins.input', return_value=" "):
            self.assertEqual(None ,self.user_class.collect_user_firstname())

    def test_that_collect_user_email_returns_correct_value_when_given_valid_input(self):
        with unittest.mock.patch('builtins.input', return_value="mercy@gmail.com"):
            email = self.user_class.collect_user_email()
            self.assertEqual("mercy@gmail.com", email)

    def test_that_collect_user_email_except_exception_when_given_invalid_input(self):
        with patch('builtins.input', return_value=" "):
            self.assertEqual(None ,self.user_class.collect_user_firstname())

    def test_that_collect_user_password_returns_correct_value_when_given_valid_input(self):
        with unittest.mock.patch('builtins.input', return_value="Password1."):
            password = self.user_class.collect_user_password()
            self.assertEqual("Password1.", password)

    def test_hashed_password(self):
        hashed_pass = self.user_class.hashed_password("Password1.")
        self.assertIsNotNone(hashed_pass)
        self.assertTrue(isinstance(hashed_pass, bytes))


if __name__ == '__main__':
    unittest.main()
