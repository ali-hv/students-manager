# add students
# view students
# delete students
# update students

from files import load_json_file, save_students
from manager import add_student, view_students, update_student, delete_student

FILE_NAME = "students.json"
students = load_json_file(FILE_NAME)

while True:
    user_input = input("Enter you option(add, view, delete, update, exit): ")
    match user_input:
        case 'add':
            name = input("Enter name: ")
            age = input("Enter age: ")
            class_name = input("Enter class_name: ")
            add_student(students, name, age, class_name)
        case 'view':
            view_students(students)
        case 'update':
            student_name = input("Enter the name of student you want to update: ")
            update_field_name = input("Enter field name you want to update: ")
            if update_field_name not in ["name", "age", "class_name"]:
                print("The field name can only be name, age or class_name")
            else:
                new_value = input("Enter the new value to replace: ")
                is_updated = update_student(
                    students, student_name, update_field_name, new_value
                )
                if is_updated:
                    print("The student updated.")
                else:
                    print("No student found with the given name.")
        case 'delete':
            student_name = input("Enter the name of student you want to update: ")
            is_deleted = delete_student(students, student_name)
            if is_deleted:
                print("The student deleted.")
            else:
                print("No student found with the given name.")
        case 'exit':
            save_students(FILE_NAME, students)
            break
        case _:
            print('Your input can only be add, view, update or delete')
