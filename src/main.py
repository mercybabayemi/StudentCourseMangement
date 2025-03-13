import sys

from studentmanagement import StudentManagementSystem


def display_menu():
    print("""
            Welcome to MEA Institute Application 
            
            Here  are our menu:
            1. Register as Student
            2. Register as Professor
            3. Login as Professor
            4. Login as Student
            5. Exit""")

    choice = input("Enter your choice: ").strip()
    while choice not in ["1", "2", "3", "4", "5"]:
        print(f'\033[1;31mInvalid Input\nTry Again!!!\033[0m')
        choice = input("Enter your choice: ").strip()
    cases(choice)


def cases(choice):
    match choice:
        case "1":
            try:
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                StudentManagementSystem().register_student(first_name, last_name, email, password)
            except Exception as e:
                print(e)

        case "2":
            try:
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                StudentManagementSystem().register_professor(first_name, last_name, email, password)
            except Exception as e:
                print(e)


        case "3":
            try:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                StudentManagementSystem().log_in_professor(email, password)
            except Exception as e:
                print(e)

        case "4":
            try:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                StudentManagementSystem().log_in_student(email, password)
            except Exception as e:
                print(e)
        case "5":
            print(f"\033[1;32mThank you for using our application\033[32m")
            sys.exit()

def main():
    while True:
        display_menu()


if __name__ == "__main__":
    main()
