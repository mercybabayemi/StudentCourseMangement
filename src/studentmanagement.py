import authentication
from rich import print
import professor_view
import student_view
from database import Database
from professor import Professor
from student import Student


class StudentManagementSystem:
    def __init__(self):
        pass


    def register_student(self, first_name, last_name, email, password):
        try:
            first_name = authentication.Authentication.validate_name(first_name,"first name")
            last_name = authentication.Authentication.validate_name(last_name,"last name")
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            student = Student(first_name, last_name, email, password)
            student.register(first_name, last_name, email, password)
            print(f"Registered Student {first_name} {last_name} successfully!")
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')

    def register_professor(self, first_name, last_name, email, password):
        try:
            first_name = authentication.Authentication.validate_name(first_name,"first name")
            last_name = authentication.Authentication.validate_name(last_name,"last name")
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            professor = Professor(first_name, last_name, email, password)
            professor.register(first_name, last_name, email, password)
            print(f"Registered Professor {first_name} {last_name} successfully!")
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')

    def log_in_professor(self, email, password):
        try:
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            holder_tuple = Database("professor_details.txt").load_from_file(email,password)
            holder = holder_tuple[0]
            if holder_tuple[1]:
                stored_first_name,stored_last_name,stored_email,stored_password = holder[0],holder[1],holder[2],holder[3]
                professor = Professor(stored_first_name, stored_last_name, stored_email, stored_password)
                professor.login(stored_email,stored_password)
                choice = ""
                while choice != '6':
                    choice = professor_view.display(professor,stored_first_name,stored_last_name)
            else:
                print(f'\033[1;31mInvalid email or password\033[0m')
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')

    def log_in_student(self, email, password):
        try:
            email = authentication.Authentication.validate_email(email)
            holder_tuple = Database("student_details.txt").load_from_file(email,password)
            holder = holder_tuple[0]
            if holder_tuple[1]:
                stored_first_name,stored_last_name,stored_email,stored_password = holder[0],holder[1],holder[2],holder[3]
                student = Student(stored_first_name, stored_last_name, stored_email, stored_password)
                student.login(stored_email,stored_password)
                choice = ""
                while choice != "8":
                    choice = student_view.display(student,stored_first_name,stored_last_name,stored_email)
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')






