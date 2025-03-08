import os
import unittest
from unittest.mock import patch

import file_saver
from student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Mercy","Babayemi","mercy@gmail.com","Password1.")
        self.test_file = "student_details.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_register(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com"]):
            self.student1.register("Mercy","Babayemi","mercy.babayemi@example.com","Password1.")
            self.assertTrue(os.path.exists(self.test_file))

    def test_login_success(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com","jonathan"]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com","jonathan")

        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com","jonathan"]):
            self.assertTrue(self.student1.login("mercy.babayemi@example.com", "jonathan" ))

    def test_login_state_success(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com","Jonathan"]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com","Jonathan")

        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com","Jonathan"]):
            self.assertTrue(self.student1.login("mercy.babayemi@example.com", "Jonathan" ))

        self.assertTrue(self.student1.login_state())

    def test_login_state_failure(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1."]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1.")

        with patch('builtins.input', side_effect=["mercy.babayemi@example.com", "WrongPassword"]):
            self.assertFalse(self.student1.login("mercy.babayemi@example.com", "wrongPassword"))

        self.assertFalse(self.student1.login_state())

    def test_login_failure(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1."]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1.")

        with patch('builtins.input', side_effect=["mercy.babayemi@example.com", "WrongPassword"]):
            self.assertFalse(self.student1.login("mercy.babayemi@example.com", "wrongPassword"))

    def test_register_for_course(self):
        self.student1.register_for_course("Mathematics")
        self.assertIn("Mathematics", self.student1.get_enrolled_courses())

    def test_view_courses(self):
        self.student1.register_for_course("Mathematics")
        self.student1.register_for_course("Physics")
        with patch('builtins.print') as mock_print:
            self.student1.view_courses()
            mock_print.assert_any_call("Your enrolled courses:")
            mock_print.assert_any_call("- Mathematics")
            mock_print.assert_any_call("- Physics")


    # def test_view_course_grade(self):
    #     self.student1.get_grades["Mathematics"] = "A"
    #     with patch('builtins.print') as mock_print:
    #         self.student1.view_course_grade("Mathematics")
    #         mock_print.assert_called_with("Your grade for Mathematics is A.")


if __name__ == '__main__':
    unittest.main()
