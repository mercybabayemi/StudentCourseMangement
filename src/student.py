import bcrypt

from user import User

class Student(User):

    def register(self,password):
        while True:
            try:
                self.collect_user_firstname()
                self.collect_user_lastname()
                self.collect_user_email()

                self.save_to_file(self.hashed_password(password))
                print("User registered successfully")
            except ValueError:
                print("Invalid Input.")
            except FileNotFoundError:
                print("File not found.")


    def collect_user_firstname(self):
        while True:
            try:
                firstname_input = input("""
                    Your firstname cannot be an empty space or contain space character
                    Enter your firstname:
                 """)

                firstname = self.validate_user_firstname(firstname_input)
                self.first_name(firstname)
            except ValueError:
                print("Invalid firstname.")

    def collect_user_lastname(self):
        while True:
            try:
                lastname_input = input("""
                    Your lastname cannot be an empty space or contain space character
                    Enter your lastname:
                """)
                lastname = self.validate_user_lastname(lastname_input)
                self.last_name(lastname)
            except ValueError:
                print("Invalid lastname.")

    def collect_user_email(self):
        while True:
            try:
                email_input = input("""
                    Enter a valid email address:
                """)
                email = self.validate_user_email(email_input)
                self.email(email)
            except ValueError:
                print("Invalid email.")

    def save_to_file(self, hashed_pass):
        with open("student_details.txt", 'a') as file:
            file.write(f'{self.first_name}:{self.last_name}:{self.email}:{hashed_pass.decode('utf-8')}')

    def load_to_file(self, password):
        try:
            with open("student_details.txt", 'r') as file:
                for line in file:
                    data = file.read().strip().split(':')
                    stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                    if self.passage == stored_password:
                        return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
        except FileNotFoundError:
            print("File not found.")
        except ValueError:
            print("Invalid email or password")

    def login(self):
        pass

    def register_for_course(self):
        pass

    def view_courses(self):
        pass

    def view_course_grade(self):
        pass