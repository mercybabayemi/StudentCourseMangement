from grade_type import GradeType

class Grade:
    def __init__(self):
        self.course = "course"
        self.student = "student"
        self.numeric_grade = 0.0
        self.letter_grade = GradeType.from_numeric(self.numeric_grade)

    def set_numeric_grade(self, course, student, numeric_grade: float):
        self.numeric_grade = numeric_grade
        self.letter_grade = GradeType.from_numeric(numeric_grade)
        self.course = course
        self.student = student

    def view_grade(self):
        print(f"{self.course.course_name}: {self.numeric_grade} ({self.letter_grade.name})")

