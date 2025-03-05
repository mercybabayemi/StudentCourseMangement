from student import Student
from professor import Professor
from course import Course
from grade import Grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = Course()
        self.grades = []

    def register_student(self, first_name, last_name, email, password):
        student = Student(password)
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.register(password)
        self.students.append(student)
        print(f"Student {first_name} {last_name} registered successfully.")

    def register_professor(self, first_name, last_name, email, password):
        professor = Professor(password)
        professor.first_name = first_name
        professor.last_name = last_name
        professor.email = email
        professor.register(password)
        self.professors.append(professor)
        print(f"Professor {first_name} {last_name} registered successfully.")

    def create_course(self, course_name):
        if not self.professors:
            print("No professors available to create a course.")
            return
        professor = self.professors[0]
        professor.add_course(course_name)
        print(f"Course {course_name} created successfully.")

    def assign_grade(self, student_email, course_name, grade):
        student = next((student for student in self.students if student.email == student_email), None)
        if not student:
            print("Student not found.")
            return
        if course_name not in self.courses.courses:
            print("Course not found.")
            return
        # self.grades.append(Grade(student_email, course_name, grade))
        # print(f"Grade {grade} assigned to {student_email} for {course_name}.")

    def view_student_grades(self, student_email):
        student_grades = [g for g in self.grades if g.student == student_email]
        if not student_grades:
            print("No grades found for this student.")
            return
        for grade in student_grades:
            print(grade)

    def view_course_students(self, course_name):
        if course_name not in self.courses.courses:
            print("Course not found.")
            return
        students_in_course = [s for s in self.students if course_name in s.enrolledCourses]
        if not students_in_course:
            print("No students enrolled in this course.")
            return
        for student in students_in_course:
            print(f"Student: {student.first_name} {student.last_name}, Email: {student.email}")