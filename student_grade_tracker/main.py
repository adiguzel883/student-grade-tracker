from roster import add_student, add_course, enroll_student
from storage import load_state, save_state

BASE = "data"

def main():
    students, courses = load_state(BASE)

    while True:
        print("\n--- Student Grade Tracker ---")
        print("1) Add student")
        print("2) Add course")
        print("3) Enroll student to course")
        print("4) Show students")
        print("5) Show courses")
        print("0) Save & Exit")

        choice = input("Select: ")

        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            add_student(students, {"id": sid, "name": name})
            print("Student added.")

        elif choice == "2":
            cid = input("Course ID: ")
            title = input("Course Title: ")
            add_course(courses, {"id": cid, "title": title})
            print("Course added.")

        elif choice == "3":
            cid = input("Course ID: ")
            sid = input("Student ID: ")

            for c in courses:
                if c["id"] == cid:
                    enroll_student(c, sid)
                    print("Enrolled.")
                    break

        elif choice == "4":
            print(students)

        elif choice == "5":
            print(courses)

        elif choice == "0":
            save_state(BASE, students, courses)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
