class Course:
    def __init__(self):
        self.courses = {}
        self.course_id = 1
        self.load_courses_from_file()


    def save_courses_to_file(self):
        with open("courses.txt", "a") as file:
            for course_id, course_name in self.courses.items():
                file.write(f"{course_id}:{course_name}\n")

    def add_course(self, course):
        if course not in self.courses.values():
            self.courses[self.course_id] = course
            print(f"Here is your course id:{self.course_id}")
            self.save_courses_to_file()
            self.course_id += 1
        else:
            raise Exception(f"Course {course} already exists")

    def load_courses_from_file(self):
        try:
            with open("courses.txt", "r") as file:
                for line in file:
                    course_id, course_name = line.strip().split(":", 1)
                    self.courses[int(course_id)] = course_name
                    self.course_id += max(self.courses.keys()) + 1
        except FileNotFoundError:
            self.courses = {}
        except IOError as e:
            print(f"Error loading courses from file: {e}")

    def remove_course(self, input_course):
        course_id_to_remove = None
        for course_id, course_name in self.courses.items():
            if course_name == input_course:
                course_id_to_remove = course_id
                break

        if course_id_to_remove is not None:
            del self.courses[course_id_to_remove]
            self.save_courses_to_file()
        else:
            raise Exception(f"Course '{input_course}' not found")

    def remove_using_id(self, id_number):
        if id_number in self.courses:
            del self.courses[id_number]

    def view_course(self):
        return self.courses

    def find_course_using_id(self, id_number):
        if id_number in self.courses:
            return self.courses.get(id_number)
        raise Exception(f"{id_number} not not found")

    def find_id_by_course(self, course):
        for course_id, course_name in self.courses.items():
            if course_name == course:
                return course_id
        raise Exception(f"Course '{course}' not found")