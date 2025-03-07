import bcrypt

from student import Student


def load_from_file_student(password, email):
    try:
        with open("student_details.txt", 'r') as file:
            for line in file:
                data = line.strip().split(':')
                stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                if email == stored_email:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        student = Student(stored_firstname, stored_lastname, stored_email, stored_password)
                        return student
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print("Invalid password or email")
        return False


def verify_email_in_file_student(email):
    with open("student_details.txt", 'r') as file:
        for line in file:
            data = line.strip().split(':')
            stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
            if email == stored_email:
                return True

    raise ValueError("Email already exists")