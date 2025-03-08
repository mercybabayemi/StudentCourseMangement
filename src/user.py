from authentication import Authentication

class User:
    def __init__(self, first_name,last_name,email,password):
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def __first_name(self):
        return self.first_name

    @__first_name.setter
    def __first_name(self, value):
        self.first_name = value

    @property
    def __last_name(self):
        return self.last_name

    @__last_name.setter
    def __last_name(self, value):
        self.last_name = value

    @property
    def __email(self):
        return self.email

    @__email.setter
    def __email(self, value):
        self.email = value

    @property
    def __password(self):
        return self.password

    @__password.setter
    def __password(self, value):
        self.password = value

    def register(self,first_name,last_name,email, password):
        raise NotImplementedError("Subclass must implement register method.")

    def login(self,email,password):
        raise NotImplementedError("Subclass must implement login method.")

    def view_courses(self):
        raise NotImplementedError("Subclass must implement view courses method.")




