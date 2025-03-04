import re

import bcrypt

from email_validator import validate_email, EmailNotValidError

class User:
    def __init__(self, password):
        self.__email = "email"
        self.___password = password
        self.__first_name = "first_name"
        self.__last_name = "last_name"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.validate_user_firstname(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.validate_user_lastname(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = self.validate_user_email(value)

    @property
    def passage(self):
        return self.___password

    def register(self, password):
        raise NotImplementedError("Subclass must implement register method.")

    def login(self):
        raise NotImplementedError("Subclass must implement login method.")

    def view_courses(self):
        raise NotImplementedError("Subclass must implement view courses method.")

    def hashed_password(self, password):
        while True:
            try:
                password_input = self.validate_user_password(password)
                return bcrypt.hashpw(password_input.encode('utf-8'), bcrypt.gensalt())
            except ValueError:
                print("Invalid input.")
                password_input = input("""
                    Username must contain capital letters
                    Username must contain small letters
                    Username must contain at least 1 number, at least 1 punctuation and must be 8 to 16 alphanumeric - symbol long
                    Enter your password:
                """)
        
    def validate_user_password(self, password):
        if password is None or not re.fullmatch('[A-Za-z0-9-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/]{8,16}', password):
            raise ValueError("Invalid password.")
        return password
    
    def validate_user_firstname(self, firstname):
        if firstname is None or not re.fullmatch('[a-zA-Z]+', firstname):
            raise  ValueError("Invalid firstname.")
        return firstname

    def validate_user_lastname(self, lastname):
        if lastname is None or not re.fullmatch('[a-zA-Z]+', lastname):
            raise ValueError("Invalid lastname.")
        return lastname

    def validate_user_email(self, value):
            email = validate_email(value)
            if not email:
                raise EmailNotValidError("Email not valid.")
            return email

    def save_to_file(self, hashed_pass):
        raise NotImplementedError("Subclass must implement save to file method.")

    def load_to_file(self, password):
        raise NotImplementedError("Subclass must implement load to file method.")