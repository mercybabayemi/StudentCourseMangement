import course
from user import User

class Professor(User):
    def __init__(self, first_name, last_name, email,password):
        super().__init__(first_name, last_name, email, password)
        self.courses = course.Course()

    def add_course(self, input_course):
        try:
            self.courses.add_course(input_course)
        except Exception as e:
            return str(e)

    def remove_course(self, input_course):
        try:
            self.courses.remove_course(input_course)
        except Exception as e:
            return str(e)

