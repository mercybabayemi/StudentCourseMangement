import re

import bcrypt

from email_validator import validate_email, EmailNotValidError

class User:
    def __init__(self):
        self.__email = "email"
        self.__hashed_password = self.__hashed_password("password")
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

    def register(self):
        raise NotImplementedError("Subclass must implement register method.")

    def login(self):
        raise NotImplementedError("Subclass must implement login method.")

    def view_courses(self):
        raise NotImplementedError("Subclass must implement view courses method.")

    def __hashed_password(self, password):
        while True:
            try:
                password_input = self.validate_user_password(password)
                return bcrypt.hashpw(password_input.encode('utf-8'), bcrypt.gensalt())
            except ValueError:
                print("Invalid input.")
        
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
        try:
            email = validate_email(value)
            return email
        except EmailNotValidError as e:
            print("Email not valid.")