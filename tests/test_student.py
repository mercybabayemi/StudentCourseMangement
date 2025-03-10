import os
import unittest

from professor import Professor
from student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Mercy","Babayemi","mercy@gmail.com","Password1.")
        self.test_file = "student_details.txt"
        professor = Professor("Mercy", "Babayemi", "mercy@gmail.com", "Password1.")
        professor.add_course("Mathematics")
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
        if os.path.isfile("professor_details.txt"):
            os.remove("professor_details.txt")


    def tearDown(self):
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
        if os.path.isfile("professor_details.txt"):
            os.remove("professor_details.txt")
#

    def test_that_when_i_register_the_file_exists(self):
            self.student1.register("Mercy","Babayemi","mercy.babayemi@example.com","Password1.")
            self.assertTrue(os.path.exists(self.test_file))

    def test_that_i_can_login_successfully(self):
            self.student1.register("Mercy","Babayemi","mercy@gmail.com","Password1.")
            self.assertTrue(self.student1.login("mercy@gmail.com","Password1."))

    def test_login_state_success(self):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com","Jonathan")
            self.assertTrue(self.student1.login("mercy.babayemi@example.com", "Jonathan" ))
            self.assertTrue(self.student1.login_state())


    def test_login_state_failure(self):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1.")
            self.assertFalse(self.student1.login("mercy.babayemi@example.com", "wrongPassword"))
            self.assertFalse(self.student1.login_state())

    def test_login_failure(self):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1.")
            self.assertFalse(self.student1.login("mercy.babayemi@example.com", "wrongPassword"))

    def test_register_for_course(self):
        self.student1.register_for_course("Mathematics")
        self.assertEqual(["Mathematics"], self.student1.get_enrolled_courses())
        if os.path.isfile("courses.txt"):
            os.remove("courses.txt")
        if os.path.isfile("__enrolled_courses.txt"):
            os.remove("__enrolled_courses.txt")

if __name__ == '__main__':
    unittest.main()
