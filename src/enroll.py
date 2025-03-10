from course import Course


class Enrollment:

    def __init__(self):
        self.course = Course()
        self.__enrolled_courses = []
        self.load_enrolled_courses()

    def enroll(self, course):
        available_courses = self.course.view_course()
        if course in available_courses.values():
            if course in self.__enrolled_courses:
                raise ValueError("Course already enrolled")
            self.__enrolled_courses.append(course)
            print(f"You are already enrolled in {course}.")
            self.save_enrolled_courses()
        else:
            raise Exception("Invalid course . Please select a valid course.")


    def un_enroll(self,course):
        if course in self.__enrolled_courses:
            self.__enrolled_courses.remove(course)
            self.save_enrolled_courses()



    def save_enrolled_courses(self):
        with open("__enrolled_courses.txt", "a") as file:
            for course in self.__enrolled_courses:
                file.write(f"{course}\n")


    def load_enrolled_courses(self):
        try:
            with open("__enrolled_courses.txt", "r") as file:
                self.__enrolled_courses = [line.strip() for line in file]
        except FileNotFoundError:
            Enrollment.enrolled_courses = []

    def view_enroll_courses(self):
        return self.__enrolled_courses

