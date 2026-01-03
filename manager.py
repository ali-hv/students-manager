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


def update_student(students, student_name, update_field_name, new_value):
    for student in students:
        if student["name"] == student_name:
            student[update_field_name] = new_value
            return True
    return False


def delete_student(students, student_name):
    for student in students:
        if student["name"] == student_name:
            students.remove(student)
            return True
    return False
