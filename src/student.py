import professor
from database import Database
from professor import Professor
from user import User

class Student(User):
    def __init__(self,first_name,last_name,email,password):
        super().__init__(first_name,last_name, email, password)
        self.__grades = {}
        self.__enrolled_courses = []
        self.__is_logged_in = False

    def get_enrolled_courses(self):
        return self.__enrolled_courses

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

    def login_state(self):
        return self.__is_logged_in

    def login(self, email, password):
        try:
            if Database.load_from_file(password, email):
                self.__is_logged_in = True
                print("You are logged in.")
            return self.__is_logged_in
        except Exception as e:
            print(e)

    def log_out(self):
        self.__is_logged_in = False

    def register_for_course(self, course_name):
        try:
            if course_name not in self.__enrolled_courses:
                self.__enrolled_courses.append(course_name)
                print(f"Successfully enrolled in {course_name}.")
            else:
                raise ValueError (f"You are already enrolled in {course_name}.")
        except Exception as e:
            print(e)

    def view_courses(self):
        if not self.get_enrolled_courses():
            print("You are not enrolled in any course.")
        else:
            print("Your enrolled courses:")
            for course in self.get_enrolled_courses():
                print(f"- {course}")


    def view_course_grade(self, course_name):
        if course_name in self.__grades:
            print(f"Your grade for {course_name} is {self.__grades[course_name]}.")
        else:
            print(f"No grade found for {course_name}.")








