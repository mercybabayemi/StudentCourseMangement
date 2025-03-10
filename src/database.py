import os

import bcrypt


class Database:
    def __init__(self,file_name):
        self.__file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                pass

    @property
    def file_name(self):
        return self.__file_name


    def save_to_file(self,first_name, last_name, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with open(self.__file_name, 'a') as file:
            file.write(f'{first_name}:{last_name}:{email}:{hashed_password}\n')



    def load_from_file(self, email, password):
        with open(self.__file_name, 'r') as file:
            for line in file:
                data = line.strip().split(':')
                stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                if email == stored_email:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        return [stored_firstname, stored_lastname, stored_email, stored_password],True
                    else:
                        print("Invalid password or email")
                        return False


            print("Email doesn't exist")
            return False

    def verify_email_exist(self,email):
        with open(self.__file_name, 'r') as file:
            for line in file:
                data = line.strip().split(':')
                stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                if stored_email == email:
                    return True
                else:
                    return False

    def save_to_file_grades(self,course_name,student_email,grade,grade_type):
        with open(self.__file_name, 'a') as file:
            file.write(f"{course_name}:{student_email}:{grade}:{grade_type}\n")


    def load_from_file_grades(self):
        with open(self.__file_name, 'r') as file:
            for line in file:
                data = line.strip().split(':')
                course_name, student_email, grade, grade_type = data[0], data[1], data[2], data[3]
                return [course_name, student_email, grade, grade_type]

