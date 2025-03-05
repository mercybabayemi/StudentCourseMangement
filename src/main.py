from studentmanagement import StudentManagementSystem


def main():
    choice = input("""
        Welcome to AEM Student Management System

        1. Register
        2. Login

        Please enter your choice (1 or 2): """)

    match choice:
        case "1":
            role = input("""
                Enter 1 for Student
                Enter 2 for Teacher

                Please enter your role (1 or 2): """)

            match role:
                case "1":
                    student_system = StudentManagementSystem()

                    while True:
                        try:
                            first_name = input("Enter your first name: ")
                            last_name = input("Enter your last name: ")
                            email = input("Enter your email: ")
                            password = input("Enter your password: ")

                            student_system.register_student(first_name, last_name, email, password)
                            print("Student registered successfully!")
                            break  # Exit the loop if registration is successful
                        except ValueError as error:
                            print(f"Error: {error}")
                            print("Please try again.")
                        except Exception as error:
                            print(f"An unexpected error occurred: {error}")
                            break

                case "2":
                    print("Teacher registration is not implemented yet.")
                case _:
                    print("Invalid role. Please enter 1 for Student or 2 for Teacher.")

        case "2":
            role = input("""
                Enter 1 for Student
                Enter 2 for Teacher

                Please enter your role (1 or 2): """)

            match role:
                case "1":
                    student_system = StudentManagementSystem()

                    email = input("Enter your email: ")
                    password = input("Enter your password: ")

                    if student_system.login_student(email, password):
                        print("Login successful!")
                    else:
                        print("Invalid email or password.")

                case "2":
                    print("Teacher login is not implemented yet.")
                case _:
                    print("Invalid role. Please enter 1 for Student or 2 for Teacher.")

        case _:
            print("Invalid choice. Please enter 1 for Register or 2 for Login.")


if __name__ == "__main__":
    main()