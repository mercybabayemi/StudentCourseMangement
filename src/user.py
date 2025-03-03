import re

import bcrypt


class User:
    def __init__(self):
        self.__email = "email"
        self.__password = "password"
        self.__first_name = "first_name"
        self.__last_name = "last_name"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, name):
        self.__first_name = name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, name):
        self.__last_name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def hashed_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register(self):
        validate_process_one = True

        while validate_process_one:
            firstname_input = input("""
                                Your first name cannot be an empty space or contain space character
                                Enter your first:
                    """)
            try:
                self.validate_user_firstname(firstname_input)
                validate_process_one = False
            except ValueError:
                print("Invalid Input.")

        validate_process_two = True

        while validate_process_two:
            password_input = input("""
                                Username must contain capital letters
                                Username must contain small letters
                                Username must contain at least 1 number, at least 1 punctuation and must be 8 alphanumeric - symbol long
                                Enter your password:
                    """)
            try:
                self.validate_user_password(password_input)
                validate_process_one = False
            except ValueError:
                print("Invalid Input.")


    def validate_user_password(self, password):
        password_is_correct = password is not None and re.fullmatch('[A-Za-z0-9-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/]{8}')

        if not password_is_correct:
            raise ValueError("Invalid password.")


    def validate_user_firstname(self, firstname):
        firstname_is_correct = firstname is not None and re.fullmatch('\S+')