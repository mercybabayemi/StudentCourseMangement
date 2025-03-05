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

def main():
    student_grade = StudentManagementSystem()
    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-9): ").strip()

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
                    print(f"Student {first_name} {last_name} registered successfully.")

                case '2':
                    print("-- Register Professor --")
                    first_name = input("Enter first Name: ")
                    last_name = input("Enter last name: ")
                    email = input("Email: ")
                    password = input("Password: ")
                    #student_id = input("Student ID: ")
                    try:
                       student_grade.register_professor(first_name, last_name, email, password)
                    except Exception as e:
                        print(e)
                    print(f"Professor {first_name} {last_name} registered successfully.")

                case '3':
                    print("\n-- Login --")
                    email = input("Email: ")
                    password = input("Password: ")
                    try:
                        logged_in_user = student_grade.login_user(email, password)
                        print("Login successful. Welcome,", logged_in_user.name + "!")
                    except Exception as e:
                        print("Error:", e)


                case '4':
                    print("Exiting... Goodbye!\nThanks for using this app")
                    break




if __name__ == "_main_":
    main()
