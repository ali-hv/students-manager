# add students
# view students
# delete students
# update students

from files import load_json_file, save_students
from manager import add_student, view_students

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
            print('update')
        case 'delete':
            print('delete')
        case 'exit':
            save_students(FILE_NAME, students)
            break
        case _:
            print('Your input can only be add, view, update or delete')
