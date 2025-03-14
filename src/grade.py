from grade_type import GradeType

class Grade:
    def __init__(self):
        self.course = "course"
        self.student = "student"
        self.numeric_grade = 0.0
        self.letter_grade = GradeType.convert_score_to_grade_type(self.numeric_grade)

    def set_numeric_grade(self, course, student, score: float):
        # self.numeric_grade = score
        self.letter_grade = GradeType.convert_score_to_grade_type(score)
        self.course = course
        self.student = student

    def view_grade(self):
        print(f"{self.course.course_name}: {self.numeric_grade} ({self.letter_grade.name})")

