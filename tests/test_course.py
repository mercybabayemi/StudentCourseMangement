import unittest
import os
from course import Course

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course_manager = Course()
        self.test_file = "courses.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_course(self):
        self.course_manager.add_course("Mathematics")
        self.assertIn("Mathematics", self.course_manager.courses.values())

    def test_add_duplicate_course(self):
        self.course_manager.add_course("Physics")
        with self.assertRaises(Exception) as context:
            self.course_manager.add_course("Physics")
        self.assertEqual(str(context.exception), "Course Physics already exists")

    def test_remove_course(self):
        self.course_manager.add_course("Computer Science")
        self.course_manager.remove_course("Computer Science")
        self.assertNotIn("Computer Science", self.course_manager.courses.values())

    def test_that_when_i_remove_nonexistent_course_it_throws_error(self):
        with self.assertRaises(Exception) as context:
            self.course_manager.remove_course("Biology")
        self.assertEqual(str(context.exception), "Course 'Biology' not found")

    def test_that_the_save_courses_to_file_is_working_well(self):
        self.course_manager.add_course("Mathematics")
        self.course_manager.add_course("Physics")
        self.course_manager.save_courses_to_file()

        with open(self.test_file, "r") as file:
            lines = file.readlines()
            self.assertIn("1:Mathematics\n", lines)
            self.assertIn("2:Physics\n", lines)

    def test_that_courses_is_loaded_from_file(self):
        with open(self.test_file, "w") as file:
            file.write("1:Mathematics\n")
            file.write("2:Physics\n")

        self.course_manager.load_courses_from_file()
        self.assertIn("Mathematics", self.course_manager.courses.values())
        self.assertIn("Physics", self.course_manager.courses.values())

    def test_that_when_the_file_is_empty_it_prints_out_an_empty_list(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.course_manager.load_courses_from_file()
        self.assertEqual(self.course_manager.courses, {})

    def test_that_courses_can_be_viewed(self):
        self.course_manager.add_course("Computer Science")
        self.course_manager.add_course("English")

        expected_courses = {1: "Computer Science", 2: "English"}
        self.assertEqual(expected_courses, self.course_manager.view_course())



