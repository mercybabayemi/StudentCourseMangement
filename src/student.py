from user import User

class Student(User):
    def register(self):
        while True:
            try:
                firstname_input = input("""
                                Your firstname cannot be an empty space or contain space character
                                Enter your firstname:
                    """)

                firstname = self.validate_user_firstname(firstname_input)
                self.first_name(firstname)
                lastname_input = input("""
                                                Your lastname cannot be an empty space or contain space character
                                                Enter your lastname:
                                    """)
                lastname = self.validate_user_lastname(lastname_input)
                self.last_name(lastname)
                password_input = input("""
                                                Username must contain capital letters
                                                Username must contain small letters
                                                Username must contain at least 1 number, at least 1 punctuation and must be 8 to 16 alphanumeric - symbol long
                                                Enter your password:
                                    """)
                self.__
            except ValueError:
                print("Invalid Input.")

    def save_to_file(self):
        pass

    def load_to_file(self):
        pass

    def login(self):
        pass

    def register_for_course(self):
        pass

    def view_courses(self):
        pass

    def view_course_grade(self):
        pass