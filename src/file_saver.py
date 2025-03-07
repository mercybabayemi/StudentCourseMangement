import bcrypt


def save_to_file_for_student(first_name,last_name,email,password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    with open("student_details.txt", 'a') as file:
        file.write(f'{first_name}:{last_name}:{email}:{hashed_password}\n')