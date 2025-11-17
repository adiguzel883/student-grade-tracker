def add_student(students, student_data):
    students.append(student_data)
    return student_data

def update_student(students, student_id, updates):
    for s in students:
        if s["id"] == student_id:
            s.update(updates)
            return s
    return None

def add_course(courses, course_data):
    courses.append(course_data)
    return course_data

def enroll_student(course, student_id):
    course.setdefault("students", [])
    if student_id not in course["students"]:
        course["students"].append(student_id)
    return course
