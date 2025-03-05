import bcrypt

import course
from user import User


class Professor(User):
    def __init__(self, password):
        super().__init__(password)
        self.courses = course.Course()
        #

    def register(self,password):
        try:
            firstname_collected = self.collect_user_firstname()
            self.first_name = firstname_collected
            lastname_collected = self.collect_user_lastname()
            self.last_name = lastname_collected
            email_collected = self.collect_user_email()
            self.email = email_collected
            self.save_to_file(self.hashed_password(password))
            print("Professor registered successfully")
        except ValueError as e:
            print(f"Error during registration: {e}")
        except FileNotFoundError:
            print("File not found.")

    def add_course(self, input_course):
        try:
            self.courses.add_course(input_course)
            return f"Course '{input_course}' added successfully."
        except Exception as e:
            return str(e)

    def remove_course(self, input_course):
        try:
            self.courses.remove_course(input_course)
            return f"Course '{input_course}' removed successfully."
        except Exception as e:
            return str(e)

    def view_courses(self):
        if not self.courses.courses:
            print("You are not teaching any courses.")
        else:
            print("Your teaching courses:")
            for particular_course in self.courses.courses.values():
                print(f"- {particular_course}")

    def login(self):
        email = self.collect_user_email()
        password = self.collect_user_password()

        if self.load_from_file(password, email):
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False

    def save_to_file(self, hashed_pass):
        with open("professor_details.txt", 'a') as file:
            file.write(f'{self.first_name}:{self.last_name}:{self.email}:{hashed_pass.decode("utf-8")}\n')

    def load_from_file(self, password, email):
        try:
            with open("professor_details.txt", 'r') as file:
                for line in file:
                    data = line.strip().split(':')
                    stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                    if self.email == stored_email:
                        if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                            self.first_name = stored_firstname
                            self.last_name = stored_lastname
                            return True
        except FileNotFoundError:
            print("File not found.")
        except ValueError:
            print("Invalid email or password is incorrect.")
        return False