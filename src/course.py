class Course:
    def __init__(self):
        self.load_courses_from_file()
        self.courses = []


    def save_courses_to_file(self):
        with open("courses.txt", "a") as file:
            for course in self.courses:
                file.write(f"{course}\n")

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.save_courses_to_file()
        else:
            raise Exception(f"Course {course} already exists")

    def load_courses_from_file(self):
        try:
            with open("courses.txt", "r") as file:
                self.courses = [line.strip() for line in file.readlines()]
            print("Courses loaded from file.")
        except FileNotFoundError:
            print("No courses file found. Starting with an empty list.")
            self.courses = []
        except IOError as e:
            print(f"Error loading courses from file: {e}")


    def remove_course(self, input_course):
        if input_course in self.courses:
            self.courses.remove(input_course)
            self.save_courses_to_file()
        else:
            raise Exception(f"Course '{input_course}' not found")

    def view_course(self):
        return self.courses

