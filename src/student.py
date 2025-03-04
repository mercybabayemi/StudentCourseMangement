from user import User

class Student(User):

    def register(self):
        validate_process_one = True
        firstname = ""
        lastname = ""
        password = ""
        email = ""

        while validate_process_one:
            firstname_input = input("""
                                Your firstname cannot be an empty space or contain space character
                                Enter your firstname:
                    """)
            try:
                firstname = self.validate_user_firstname(firstname_input)
                validate_process_one = False
            except ValueError:
                print("Invalid Input.")

        validate_process_two = True

        while validate_process_two:
            lastname_input = input("""
                                Your lastname cannot be an empty space or contain space character
                                Enter your lastname:
                    """)
            try:
                lastname = self.validate_user_lastname(lastname_input)
                validate_process_one = False
            except ValueError:
                print("Invalid Input.")

        validate_process_three = True

        while validate_process_three:
            password_input = input("""
                                Username must contain capital letters
                                Username must contain small letters
                                Username must contain at least 1 number, at least 1 punctuation and must be 8 to 16 alphanumeric - symbol long
                                Enter your password:
                    """)
            try:
                password = self.validate_user_password(password_input)
                validate_process_three = False
            except ValueError:
                print("Invalid Input.")