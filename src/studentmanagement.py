import student
from grade import Grade
from student import Student
from professor import Professor
from course import Course
from enroll import Enrollment

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = Course()
        self.grades = []
        self.roll = Enrollment()

    def get_students(self):
        return self.students


    def register_student(self, first_name, last_name, email, password):
        try:
            student = Student(password)
            if not student.verify_email(email):
                student.register(first_name, last_name, email, password)
                self.students.append(student)
                print(f'Student {first_name} {last_name} registered')
            else:
                raise ValueError("Email already exists")
        except Exception as e:
            print(e)


    def enroll_course(self,course):
        try:
            self.roll.enroll(course)
        except Exception as e:
            print(e)


    def register_professor(self, first_name, last_name, email, password):
        try:
            students = Student(password)
            if not students.verify_email(email):
                professor = Professor(password)
                if not professor.verify_email(email):
                    professor.register(first_name, last_name, email, password)
                    self.professors.append(professor)
            else:
                raise ValueError("Email already exists")
        except Exception as e:
            print(e)

    def create_course(self, course_name):
        try:
            if not self.professors:
                print("No professors available to create a course.")
                return
            professor = self.professors[0]
            professor.add_course(course_name)
            print(f"Course {course_name} created successfully.")
        except Exception as e:
            print(e)



    def view_student_grades(self, student_email):
        student_grades = [grade for grade in self.grades if grade.student == student_email]
        if not student_grades:
            print("No grades found for this student.")
            return
        for grade in student_grades:
            print(grade)

    def view_course(self):
        try:
            if not self.courses:
                print("No courses available.")
                return

            courses = self.courses.view_course()

            if not courses:
                print("No courses found.")
                return

            for course_id,course in courses.items():
                print(f"- Here is the course id:{course_id} and course:{course}")
        except Exception as e:
            print(e)

    def login_in_student(self,email,password):
        try:
            student = Student(password)
            student.login(email,password)
        except Exception as e:
            print(e)


    def add_course(self,course_name):
        try:
            self.courses.add_course(course_name)
        except Exception as e:
            print(e)

    def remove_course(self, course):
        try:
            self.courses.remove_course(course)
        except Exception as e:
            print(e)

    def find_course_id(self,id_number):
        try:
            return self.courses.find_course_using_id(id_number)
        except Exception as e:
            print(e)

    def view_enrolled_courses(self):
        try:
            enrolled_courses = self.roll.view_enroll_courses()
            for course in enrolled_courses:
                print(f"- {course}")
        except Exception as e:
            print(e)

    def grade_student(self,course,student,grade):
        grades = Grade(course,student, grade)

    def verify_student_role(self, password, email):
        try:
            student = Student(password)
            return student.verify_email_in_file(email, password)
        except Exception as e:
            print(e)

    def verify_teacher_role(self, password, email):
        try:
            professor = Professor(password)
            return professor.verify_email_in_file(email, password)
        except Exception as e:
            print(e)

    def login_in_teacher(self,email,password):
        try:
            professor = Professor(password)
            professor.login(email,password)
        except Exception as e:
            print(e)

    def view_grade(self):
        pass

    def find_course_by_id(self, id_number):
        course = self.courses.find_course_using_id(id_number)
        return course





    def view_course_grade(self, course_name, professor):
        if professor.get_grades():
            for course_name,grade in professor.get_grades().items():
                if course_name in self.__enrolled_courses:
                    print(f"Your grade for {course_name} is {grade}.")
                else:
                    print(f"No grade found for {course_name}.")

    def assign_grade(self, student, course_input, numeric_value):
        if course_input in self.get_courses():
            if course_input in student.get_enrolled_courses():
                grade = grade_type.GradeType.from_numeric(numeric_value)
                student.professor_grade_setter(course_input, grade)
                self.__grades[course_input] = grade
                print(f"Grade {grade} assigned for {course_input}.")
            else:
                    raise ValueError(f"Student is not enrolled in {course_input}.")

        else:
            raise ValueError(f"Course '{course_input}' is not taught by this professor.")

