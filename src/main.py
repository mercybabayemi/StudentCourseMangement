from studentmanagement import StudentManagementSystem
def main():
    choice = input("""
                    You are welcome to AEM Student Management System 
                    
                    
                    
                    1. Register
                    2. login in :""")

    match choice:
        case "1":
            role = input("""
            Enter 1 for Student
            Enter 2 for Teacher
            Please enter your role: """)

            match role:
                case "1":
                    student = StudentManagementSystem()
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    try:
                        student.register_student(first_name, last_name, email, password)
                    except Exception as error:
                        print(str(error))
