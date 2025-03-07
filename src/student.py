import bcrypt
import authentication
import file_saver
from user import User

class Student(User):
    def __init__(self,first_name,last_name,email,password):
        super().__init__(first_name,last_name, email, password)
        self.enrolled_courses = []
        self.grades = {}
        self.is_logged_in = False


    def register(self,first_name,last_name,email,password):
        try:
            self.first_name = authentication.validate_name(first_name)
            self.last_name = authentication.validate_name(last_name)
            self.email = authentication.validate_email(email)
            self.password = authentication.validate_password(password)
            file_saver.save_to_file_for_student(self.first_name,self.last_name,self.email,self.password)
        except ValueError as e:
            print(f"Error during registration: {e}")

    def log_in_state(self):
        return self.is_logged_in


    def login(self, email, password):
        if email == self.email and password == self.password:
            self.is_logged_in = True
            return True

    def log_out(self):
        self.is_logged_in = False


    def register_for_course(self, course_name):
        try:
            if course_name not in self.enrolled_courses:
                self.enrolled_courses.append(course_name)
                print(f"Successfully enrolled in {course_name}.")
            else:
                raise ValueError (f"You are already enrolled in {course_name}.")
        except Exception as e:
            print(e)

    def view_courses(self):
        if not self.enrolled_courses:
            print("You are not enrolled in any courses.")
        else:
            print("Your enrolled courses:")
            for course in self.enrolled_courses:
                print(f"- {course}")

    def view_course_grade(self, course_name):
        if course_name in self.grades:
            print(f"Your grade for {course_name} is {self.grades[course_name]}.")
        else:
            print(f"No grade found for {course_name}.")








