import os
import unittest

from student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Password1.")
        self.test_file = "student_details.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_register(self):
        self.student1.first_name = "John"
        self.student1.last_name = "Doe"
        self.student1.email = "mercyjanet013@gmail.com"
        self.student1.register("Password1.")
        self.assertTrue(os.path.exists(self.test_file))


if __name__ == '__main__':
    unittest.main()
