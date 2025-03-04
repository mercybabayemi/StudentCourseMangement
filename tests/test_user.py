import unittest

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

if __name__ == '__main__':
    unittest.main()
