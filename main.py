from init_db import init_db
from students import add_student, add_course, add_grade
from analytics import get_top_students, get_course_difficulty, get_student_gpa

def menu():
    print("\n--- Student Analytics System ---")
    print("1. Add student")
    print("2. Add course")
    print("3. Add grade")
    print("4. Show top students")
    print("5. Show course difficulty")
    print("6. Get student GPA")
    print("0. Exit")

def main():
    init_db()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Name: ")
            major = input("Major: ")
            year = int(input("Year: "))
            add_student(name, major, year)

        elif choice == "2":
            course = input("Course name: ")
            credits = int(input("Credits: "))
            add_course(course, credits)

        elif choice == "3":
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            grade = float(input("Grade: "))
            add_grade(sid, cid, grade)

        elif choice == "4":
            print(get_top_students())

        elif choice == "5":
            print(get_course_difficulty())

        elif choice == "6":
            sid = int(input("Student ID: "))
            print("GPA:", get_student_gpa(sid))

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
