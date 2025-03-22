import unittest

from course import Course
from grade import Grade
from grade_type import GradeType
from student import Student


class TestGrade(unittest.TestCase):
    def setUp(self):
        self.course = Course()
        self.grade = Grade()
        self.student = Student("Abdul", "Azeez", "azeez233@gmail.com", "lase")

    def test_that_can_creates_a_Grade_object_with_a_numeric_grade_of_85(self):
        self.grade.set_numeric_grade("maths", "azeez233@gmail.com", 85.9)
        expected = GradeType.convert_score_to_grade_type(85.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_can_set_a_grade_object_with_70_then_updates_it_to_90(self):
        self.grade.set_numeric_grade("physics", "azeez233@gmail.com", 90.0)
        expected = GradeType.convert_score_to_grade_type(90.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_for_grade_conversion(self):
        test_cases = [
            (95.0, "A"),
            (80.0, "B"),
            (70.0, "C"),
            (50.0, "F"),
            (89.9, "B"),
            (79.9, "C"),
            (69.9, "D"),
            (0.0, "F"),
        ]

        for score, expected in test_cases:
            with self.subTest(score=score):
                self.grade.set_numeric_grade("physics", "azeez233@gmail.com", score)
                actual = self.grade.letter_grade.name
                self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_negative_grade_input_should_return_lowest_possible_grade(self):
        self.grade.set_numeric_grade("python", "azeez233@gmail.com", -5.0)
        expected = GradeType.convert_score_to_grade_type(-5.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_numeric_grade_above_100(self):
        self.grade.set_numeric_grade("javaScript", "azeez233@gmail.com", 105.0)
        expected = GradeType.convert_score_to_grade_type(105.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_for_zero_numeric_grade(self):
        self.grade.set_numeric_grade("Datas-science", "azeez233@gmail.com", 0.0)
        expected = GradeType.convert_score_to_grade_type(0.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_non_numeric_grade_input_raises_exception(self):
        with self.assertRaises(TypeError):
            self.grade.set_numeric_grade("java", "azeez233@gmail.com", "fourteen")

    def test_for_large_negative_numeric_grade(self):
        self.grade.set_numeric_grade("python", "azeez233@gmail.com", -100.0)
        expected = GradeType.convert_score_to_grade_type(-100.0).name
        actual = self.grade.letter_grade.name
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

if __name__ == "__main__":
    unittest.main()