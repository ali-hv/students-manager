def add_student(students, name, age, class_name):
    students.append(
        {
            'name': name,
            'age': age,
            'class_name': class_name,
        }
    )


def view_students(students):
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Class name: {student['class_name']}")
