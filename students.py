from db import get_connection

def add_student(name, major, year):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, major, year) VALUES (?, ?, ?)",
        (name, major, year)
    )

    conn.commit()
    conn.close()

def add_course(course_name, credits):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (course_name, credits) VALUES (?, ?)",
        (course_name, credits)
    )

    conn.commit()
    conn.close()

def add_grade(student_id, course_id, grade):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)",
        (student_id, course_id, grade)
    )

    conn.commit()
    conn.close()