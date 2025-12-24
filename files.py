import json
import os


def load_json_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    return []

def save_students(file_name, students):
    with open(file_name, 'w') as f:
        json.dump(students, f, indent=4)
