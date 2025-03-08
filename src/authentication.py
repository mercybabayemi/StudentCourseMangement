import re

class Authentication:

    @staticmethod
    def validate_name(name):
        if name is None or not re.fullmatch('[a-zA-Z]+', name):
            raise ValueError("Invalid firstname.")
        return name

    @staticmethod
    def validate_email(email):
        if email is None or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email")
        return email

    @staticmethod
    def validate_password(password):
        if password is None or not re.fullmatch(r'[A-Za-z0-9\-!$%^&*()_+|~=`{}\[\]:";\'<>?,.]{8,16}', password):
            raise ValueError("Invalid password.\nYour password must contain at least 8 characters.  ")
        return password