import unittest
from unittest.mock import patch

from email_validator import EmailNotValidError

from user import User

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.user_class = User("Mercy","Babayemi","mercy@gmail.com","Password1.")


    def test_that_user_class_return_error_if_name_is_empty(self):
        with self.assertRaises(ValueError):
            User("", "Babayemi", "mercy@gmail.com", "Password1.")



    def test_that_user_class_return_error_if_last_name_is_empty(self):
        with self.assertRaises(ValueError):
            User("Mercy", "", "mercy@gmail.com", "Password1.")

    def test_that_user_class_return_error_if_given_password_that_is_not_up_to_eight_or_more_characters(self):
        with self.assertRaises(ValueError):
            User("Mercy", "Babayemi", "mercy@gmail.com", "jojo")

    def test_that_user_email_given_is_a_correct_value_when_registering(self):
        self.assertEqual("mercy@gmail.com", self.user_class.email)

    def test_that_when_user_given_invalid_email_raise_exception(self):
        with self.assertRaises(ValueError):
            User("Mercy", "Babayemi", "mercygml.com", "password")


if __name__ == '__main__':
    unittest.main()
