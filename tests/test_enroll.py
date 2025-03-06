import unittest
from enroll import Enrollment
from course import Course

class TestEnrollment(unittest.TestCase):

    def setUp(self):
        self.enrollment = Enrollment()
        self.enrollment.course = Course()

    def test_that_can_enroll_valid_course(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        self.enrollment.enroll("python")
        self.assertIn("python", self.enrollment.view_enroll_courses())

    def test_that_enroll_invalid_course_raise_exception(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        with self.assertRaises(Exception):
            self.enrollment.enroll("jango")

    def test_that_enrolled_courses_should_remove_after_un_enrolled(self):
        self.enrollment.enrolled_courses = ["python"]
        self.enrollment.un_enroll("python")
        self.assertNotIn("python", self.enrollment.view_enroll_courses())

    def test_that_can_view_enrolled_courses(self):
        self.enrollment.enrolled_courses = ["python"]
        self.assertEqual(self.enrollment.view_enroll_courses(), ["python"])

if __name__ == "__main__":
    unittest.main()
