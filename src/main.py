from studentmanagement import StudentManagementSystem
from student import Student
from professor import Professor
from exception import UserNotFoundException, CourseNotFoundException, GradeOutOfRangeException

class InvalidMenuChoice(Exception):
    pass

def print_menu():
    print("\n---WELCOME TO MEA PROGRAMMING INSTITUTE---")
    print("\nWhere Passion for Code Transforms into Innovation.")
    print("\n--- Main Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Login")
    print("4. Create Course")
    print("5. Enroll Student in Course")
    print("6. Assign Grade")
    print("7. View User Details")
    print("8. View All Registered Students")
    print("9. Exit")

def main():
    mgmt = StudentManagementSystem()
    logged_in_user = None

    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-9): ").strip()

            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                raise InvalidMenuChoice("Invalid menu option. Please select a valid option (1-9).")

            if choice == '1':
                print("\n-- Register Student --")
                email = input("Email: ")
                password = input("Password: ")
                name = input("Name: ")
                student_id = input("Student ID: ")
                student = Student(email, password, name, student_id)
                mgmt.register_user(student)
                print("Student", name, "registered successfully.")

            elif choice == '2':
                print("\n-- Register Professor --")
                email = input("Email: ")
                password = input("Password: ")
                name = input("Name: ")
                professor_id = input("Professor ID: ")
                professor = Professor(email, password, name, professor_id)
                mgmt.register_user(professor)
                print("Professor", name, "registered successfully.")

            elif choice == '3':
                print("\n-- Login --")
                email = input("Email: ")
                password = input("Password: ")
                try:
                    logged_in_user = mgmt.login_user(email, password)
                    print("Login successful. Welcome,", logged_in_user.name + "!")
                except UserNotFoundException as e:
                    print("Error:", e)

            elif choice == '4':
                print("\n-- Create Course --")
                if logged_in_user is None or not hasattr(logged_in_user, 'professor_id'):
                    print("Only a logged in professor can create a course.")
                else:
                    course_id = input("Course ID: ")
                    course_name = input("Course Name: ")
                    try:
                        mgmt.create_course(course_id, course_name, logged_in_user.email)
                        print("Course", course_name, "created successfully.")
                    except UserNotFoundException as e:
                        print("Error:", e)

            elif choice == '5':
                print("\n-- Enroll Student in Course --")
                student_email = input("Student Email: ")
                course_id = input("Course ID: ")
                try:
                    mgmt.enroll_student_in_course(student_email, course_id)
                    print("Student", student_email, "enrolled in course", course_id, "successfully.")
                except (UserNotFoundException, CourseNotFoundException) as e:
                    print("Error:", e)

            elif choice == '6':
                print("\n-- Assign Grade --")
                if logged_in_user is None or not hasattr(logged_in_user, 'professor_id'):
                    print("Only a logged in professor can assign grades.")
                else:
                    student_email = input("Student Email: ")
                    course_id = input("Course ID: ")
                    try:
                        numeric_grade = float(input("Numeric Grade (0-100): "))
                        mgmt.assign_grade(logged_in_user.email, student_email, course_id, numeric_grade)
                    except ValueError:
                        print("Please enter a valid number for the grade.")
                    except (UserNotFoundException, CourseNotFoundException, GradeOutOfRangeException) as e:
                        print("Error:", e)

            elif choice == '7':
                print("\n-- View User Details --")
                email = input("Enter user email to view details: ")
                found = None
                for user in mgmt.users:
                    if user.email == email:
                        found = user
                        break
                if found:
                    print("Name:", found.name)
                    print("Email:", found.email)
                    if hasattr(found, 'student_id'):
                        print("Student ID:", found.student_id)
                        found.view_courses()
                        found.view_grades()
                    elif hasattr(found, 'professor_id'):
                        print("Professor ID:", found.professor_id)
                        found.view_courses()
                else:
                    print("User not found.")

            elif choice == '8':
                print("\n-- All Registered Students --")
                student_found = False
                for user in mgmt.users:
                    if hasattr(user, 'student_id'):
                        print("Name:", user.name, "| Email:", user.email, "| Student ID:", user.student_id)
                        student_found = True
                if not student_found:
                    print("No students have been registered yet.")

            elif choice == '9':
                print("Exiting... Goodbye!")
                break

        except InvalidMenuChoice as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
