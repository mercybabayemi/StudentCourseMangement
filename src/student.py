import enroll
from course import Course
from database import Database
from user import User

class Student(User):
    def __init__(self,first_name,last_name,email,password):
        super().__init__(first_name,last_name, email, password)
        self.__email = email
        self.__first_name = first_name
        self.__grades = {}
        self.__is_logged_in = False
        self.__enrolled_courses = enroll.Enrollment()
        self.__student_course = Course()

    def get_enrolled_courses(self):
        return self.__enrolled_courses.view_enrolled_courses()

    def get_grades(self):
        return self.__grades

    def enroll(self, course_name):
        try:
            self.__enrolled_courses.enroll(self.__email,course_name)
        except ValueError as e:
            print(e)

    def un_enroll(self, course_name):
        try:
            self.__enrolled_courses.un_enroll(self.__email,course_name)
        except ValueError as e:
            print(e)

    def student_grade_setter(self, course_input, grade):
        self.__grades[course_input] = grade

    def register(self, first_name, last_name, email, password):
        if not Database("student_details.txt").verify_email_exist(email) and not Database("professor_details.txt").verify_email_exist(email):
            self.__first_name = first_name
            self.__last_name = last_name
            self.__email = email
            self.__password = password
            Database("student_details.txt").save_to_file(self.__first_name, self.__last_name, self.__email,self.__password)
        else:
            raise ValueError("Email already registered")

    def login_state(self):
        return self.__is_logged_in

    def login(self, email, password):
        try:
            data = Database("student_details.txt").load_from_file(email, password)
            if data[1]:
                self.__is_logged_in = True
                print("You are logged in.")
                return self.__is_logged_in
            else:
                return self.__is_logged_in
        except Exception as e:
            print(e)


    def log_out(self):
        self.__is_logged_in = False

    def register_for_course(self, course_name):
        try:
            if course_name in self.__student_course.get_courses().values():
                raise ValueError("Course already registered")
            else:
                self.__enrolled_courses.enroll(self.__email,course_name)
                print(f"Successfully enrolled in {course_name}.")
        except Exception as e:
            print(e)

    def view_courses(self):
        if not self.get_enrolled_courses():
            print("You are not enrolled in any course.")
        else:
            print("Your enrolled courses:")
            for course in self.get_enrolled_courses():
                print(f"- {course}")

    def view_course_grades(self,course_name):
        if course_name not in self.get_enrolled_courses() or not self.__student_course.view_course():
            print("You are not enrolled in any course.")
        else:
            holder = Database("grade_details.txt").load_from_file_grades()
            if self.__email == holder[1]:
                print(f"Your grades in {holder[0]} is: {holder[2]}: {holder[3]}")