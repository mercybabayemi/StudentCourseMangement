class Course:
    def __init__(self):
        self.courses = {}
        self.course_id = 1
        self.load_courses_from_file()

    def get_courses(self):
        return self.courses



    def add_course(self, course):
        if course not in self.courses.values():
            self.courses[self.course_id] = course
            print(f"Here is your course id:{self.course_id}")
            self.save_courses_to_file()
            self.course_id += 1
        else:
            raise Exception(f"Course {course} already exists")


    def save_courses_to_file(self):
        with open("courses.txt", "a") as file:
            for course_id, course_name in self.courses.items():
                file.write(f"{course_id}:{course_name}\n")

    def load_courses_from_file(self):
        try:
            with open("courses.txt", "r") as file:
                for line in file:
                    data =  [line.strip().split(":")]
                    course_id, course_name = data[0] , data[1]
                    self.courses[int(course_id)] = course_name
                    self.course_id = max(self.courses.keys()) + 1
        except FileNotFoundError:
            self.courses = {}

    def remove_course(self, input_course):
        course_removed = False

        for id_number, course_name in list(self.courses.items()):
            if course_name == input_course:
                del self.courses[id_number]
                course_removed = True

        if course_removed:
            self.save_courses_to_file()
            print(f"Course '{input_course}' has been removed.")
        else:
            raise Exception(f"Course '{input_course}' not found.")

    def remove_using_id(self, id_number):
        if id_number in self.courses:
            del self.courses[id_number]

    def view_course(self):
        course = []
        for id_number,course_name in self.courses.items():
            course.append(course_name)
        return course


    def find_course_using_id(self, id_number):
        if id_number in self.courses:
            return self.courses.get(id_number)
        raise Exception(f"{id_number} not not found")

    def find_id_by_course(self, course):
        for course_id, course_name in self.courses.items():
            if course_name == course:
                return course_id
        raise Exception(f"Course '{course}' not found")