from studentmanagement import StudentManagementSystem


def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Register Student")
        print("2. Register Professor")
        print("3. Create Course")
        print("4. Assign Grade")
        print("5. View Student Grades")
        print("6. View Course Students")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            password = input("Enter student's password: ")
            sms.register_student(first_name, last_name, email, password)

        elif choice == "2":
            first_name = input("Enter professor's first name: ")
            last_name = input("Enter professor's last name: ")
            email = input("Enter professor's email: ")
            password = input("Enter professor's password: ")
            sms.register_professor(first_name, last_name, email, password)

        elif choice == "3":
            course_name = input("Enter course name: ")
            sms.create_course(course_name)

        elif choice == "4":
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")
            grade = input("Enter grade: ")
            sms.assign_grade(student_email, course_name, grade)

        elif choice == "5":
            student_email = input("Enter student's email: ")
            sms.view_student_grades(student_email)

        elif choice == "6":
            course_name = input("Enter course name: ")
            sms.view_course_students(course_name)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()