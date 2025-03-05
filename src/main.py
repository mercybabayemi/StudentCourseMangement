from studentmanagement import StudentManagementSystem

def print_menu():
    print("""
                ---WELCOME TO MEA PROGRAMMING INSTITUTE---
        Where Passion for Code Transforms into Innovation.
        --- Main Menu ---
        1. Register Student
        2. Register Professor
        3. Login
        4. Exit""")
def student_menu():
    manager = StudentManagementSystem()
    while True:
        print("""
            --- Student Menu ---
            1. View courses
            2. Enroll in a course
            3. View Grade
            4. Log out
        """)
        choice = input("Enter your choice 1- 4: ").strip()

        match choice:
            case '1':
                manager.view_course()
            case '2':
                course = input("Enter course name to enroll: ")
                print(f"Enrolling in {course}...")
            case '3':
                print("Fetching grades...")  # Replace with actual logic
            case '4':
                print("Logging out...\n")
                break  # Exit student menu
            case _:
                print("Invalid option. Please select a valid option (1-4).")
                choice = input("Enter your choice 1-4: ").strip()



def teacher_menu():
    manger = StudentManagementSystem()
    while True:
        print("""
            --- Teacher Menu ---
            1. Add course
            2. Remove course
            3. 
            4. Log out
        """)
        choice = input("Enter your choice 1- 4: ").strip()
        match choice:
            case '1':
                course = input("Enter course name: ")
                manger.add_course(course)
            case '2':
                course = input("Enter course name: ")
                manger.remove_course(course)



def main():
    student_grade = StudentManagementSystem()
    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-4): ").strip()

            while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("Invalid menu option. Please select a valid option (1-9).")
                choice = input("Enter your choice (1-9): ").strip()

            match choice:
                case '1':
                    print("-- Register Student --")
                    first_name = input("Enter first Name: ")
                    last_name = input("Enter last name: ")
                    email = input("Email: ")
                    password = input("Password: ")
                    #student_id = input("Student ID: ")
                    student_grade.register_student(first_name, last_name, email, password)

                case '2':
                    print("-- Register Professor --")
                    first_name = input("Enter first Name: ")
                    last_name = input("Enter last name: ")
                    email = input("Email: ")
                    password = input("Password: ")
                    #student_id = input("Student ID: ")
                    try:
                       student_grade.register_professor(first_name, last_name, email, password)
                       print(f"Professor {first_name} {last_name} registered successfully.")
                    except Exception as e:
                        print(e)


                case '3':
                    print("\n-- Login --")
                    email = input("Enter your Email: ")
                    password = input("Password: ")
                    try:
                        student_grade.login_in_student(email, password)
                        holder = student_grade.verify_role(password, email)
                        print("Login successful.")
                        if holder is True:
                            student_menu()
                            
                        else:
                            teacher_menu()
                        
                    except Exception as e:
                        print("Error:", e)


                case '4':
                    print("Exiting... Goodbye!\nThanks for using this app")
                    return

                case _:
                    print("Invalid option. Please select a valid option (1-4).")
                    choice = input("Enter your choice (1-4): ").strip()

        except Exception as e:
            print(e)




if __name__ == "__main__":
    main()
