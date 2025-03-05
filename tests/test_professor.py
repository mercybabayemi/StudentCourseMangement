import os
import unittest
from unittest.mock import patch
from professor import Professor

class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.professor1 = Professor("Password1.")
        self.test_file = "professor_detail.txt"
        self.test_file_two = "courses.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            if os.path.exists(self.test_file_two):
                os.remove(self.test_file_two)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_file_two):
            os.remove(self.test_file_two)

    def test_add_course_success(self):
        self.professor1.add_course("Mathematics")
        self.assertIn(1, self.professor1.courses.courses)
        self.assertEqual(self.professor1.courses.courses[1], "Mathematics")

    def test_add_course_duplicate(self):
        self.professor1.add_course("Physics")
        result = self.professor1.add_course("Physics")
        self.assertEqual(result, "Course Physics already exists")

    def test_remove_course_success(self):
        self.professor1.add_course("Computer Science")
        result = self.professor1.remove_course("Computer Science")
        self.assertEqual(result, "Course 'Computer Science' removed successfully.")
        self.assertNotIn("Computer Science", self.professor1.courses.courses)


    def test_remove_course_not_found(self):
       result = self.professor1.remove_course("Biology")
       self.assertEqual(result, "Course 'Biology' not found")

    def test_view_courses(self):
        self.professor1.add_course("Mathematics")
        self.professor1.add_course("Physics")
        with patch('builtins.print') as mock_print:
            self.professor1.view_courses()
            mock_print.assert_any_call("Your teaching courses:")
            mock_print.assert_any_call("- Mathematics")
            mock_print.assert_any_call("- Physics")

