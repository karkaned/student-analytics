from db import get_connection

def get_top_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, AVG(grade) as avg_grade
        FROM grades
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 5
    """)

    results = cursor.fetchall()
    conn.close()
    return results


def get_course_difficulty():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT course_id, AVG(grade) as avg_grade
        FROM grades
        GROUP BY course_id
        ORDER BY avg_grade ASC
    """)

    results = cursor.fetchall()
    conn.close()
    return results


def get_student_gpa(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(grade)
        FROM grades
        WHERE student_id = ?
    """, (student_id,))

    result = cursor.fetchone()
    conn.close()
    return result[0]