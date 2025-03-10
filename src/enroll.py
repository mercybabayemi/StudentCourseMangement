import os
from course import Course


class Enrollment:
    def __init__(self):
        self.course = Course()
        self.__enrolled_courses = {}
        self.ensure_file_exists()
        self.load_enrolled_courses()

    def ensure_file_exists(self):
        if not os.path.exists("enrolled_courses.txt"):
            with open("enrolled_courses.txt", "w") as file:
                pass

    def enroll(self, student_email, course_name):
        available_courses = self.course.view_course()
        if course_name not in available_courses.values():
            raise ValueError(f"Course '{course_name}' does not exist.")

        if course_name not in self.__enrolled_courses:
            self.__enrolled_courses[student_email] = course_name
            print(f"Student '{student_email}' enrolled in '{course_name}'.")
            self.save_enrolled_courses()

        if student_email in self.__enrolled_courses[student_email]:
            raise ValueError(f"Student '{student_email}' is already enrolled in '{course_name}'.")





    def un_enroll(self, student_email, course_name):
        if course_name in self.__enrolled_courses[student_email] and student_email in self.__enrolled_courses:
            del self.__enrolled_courses[student_email]
            print(f"Student '{student_email}' unenrolled from '{course_name}'.")
            self.save_enrolled_courses()
        else:
            raise ValueError(f"Student '{student_email}' is not enrolled in '{course_name}'.")

    def save_enrolled_courses(self):
        with open("enrolled_courses.txt", "a")as file:
            for course_name, student_emails in self.__enrolled_courses.items():
                for student_email in student_emails:
                    file.write(f"{student_email}:{course_name}\n")

    def load_enrolled_courses(self):
        try:
            with open("enrolled_courses.txt", "r") as file:
                for line in file:
                    student_email, course_name = line.strip().split(":")
                    if course_name not in self.__enrolled_courses:
                        self.__enrolled_courses[course_name] = []
                    self.__enrolled_courses[course_name].append(student_email)
        except Exception as e:
            print(f"Error loading enrollments: {e}")

    def view_enrollments(self):
        enrolled_students = []
        if not self.__enrolled_courses:
            print("No enrollments found.")
        else:
            for course_name, student_emails in self.__enrolled_courses.items():
                for student_email in student_emails:
                    enrolled_students.append(student_email)
        return enrolled_students

    def view_students_in_course(self, course_name):
        if course_name in self.__enrolled_courses:
            print(f"Students enrolled in '{course_name}':")
            for student_email in self.__enrolled_courses[course_name]:
                print(f"- {student_email}")
        else:
            print(f"No students enrolled in '{course_name}'.")

    def view_enrolled_courses(self):
        enrolled_course = []
        for email, course in self.__enrolled_courses.items():
            enrolled_course.append(course)
        return enrolled_course