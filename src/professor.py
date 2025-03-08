import grade_type
from database import Database
from course import Course
from user import User


class Professor(User):
    def __init__(self, first_name,last_name,email, password):
        super().__init__(first_name,last_name,email,password)
        self.__grades = {}
        self.__courses = Course()
        self.__is_logged_in = False

    def get_courses(self):
        return self.__courses.courses

    def get_course(self, course_id):
        return self.__courses.courses.get(course_id, None)

    def get_grades(self):
        return self.__grades

    def register(self,first_name,last_name,email,password):
        try:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__email = email
            self.__password = password
            Database.save_to_file(self.__first_name,self.__last_name,self.__email,self.__password)
        except ValueError as e:
            print(f"Error during registration: {e}")


    def add_course(self, input_course):
        try:
            self.__courses.add_course(input_course)
            return f"Course '{input_course}' added successfully."
        except Exception as e:
            return str(e)

    def remove_course(self, input_course):
        try:
            self.__courses.remove_course(input_course)
            return f"Course '{input_course}' removed successfully."
        except Exception as e:
            return str(e)

    def view_courses(self):
        if not self.__courses.courses:
            print("You are not teaching any course yet.")
        else:
            print("Teaching course/courses:")
            for particular_course in self.__courses.courses.values():
                print(f"- {particular_course}")

    def login_state(self):
        return self.__is_logged_in

    def login(self,email,password):
        try:
            if Database.load_from_file(password, email):
                self.__is_logged_in = True
                print("You are logged in.")
            return self.__is_logged_in
        except Exception as e:
            print(e)

    def logout(self):
        self.__is_logged_in = False

    def assign_grade(self, course_input, numeric_value):
        if course_input in self.__courses.courses:
            grade = grade_type.GradeType.from_numeric(numeric_value)
            self.__grades[course_input] = grade
