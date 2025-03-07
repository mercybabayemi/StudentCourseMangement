import authentication


class User:
    def __init__(self, first_name,last_name,email,password):
        self.__email = authentication.validate_email(email)
        self.__password = authentication.validate_password(password)
        self.__first_name = authentication.validate_name(first_name)
        self.__last_name = authentication.validate_name(last_name)
        self.__is_logged_in = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = authentication.validate_name(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = authentication.validate_name(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = authentication.validate_email(value)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = authentication.validate_password(value)

    def register(self,first_name,last_name,email, password):
        raise NotImplementedError("Subclass must implement register method.")

    def login(self,email,password):
        raise NotImplementedError("Subclass must implement login method.")


    def view_courses(self):
        raise NotImplementedError("Subclass must implement view courses method.")




