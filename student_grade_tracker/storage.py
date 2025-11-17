import json
import os

def load_state(base_dir):
    with open(os.path.join(base_dir, "students.json")) as f:
        students = json.load(f)

    with open(os.path.join(base_dir, "courses.json")) as f:
        courses = json.load(f)

    return students, courses

def save_state(base_dir, students, courses):
    with open(os.path.join(base_dir, "students.json"), "w") as f:
        json.dump(students, f, indent=2)

    with open(os.path.join(base_dir, "courses.json"), "w") as f:
        json.dump(courses, f, indent=2)
