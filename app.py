from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return {"message": "Student Analytics API"}


@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    result = []
    for s in students:
        result.append({
            "id": s["id"],
            "name": s["name"],
            "grade": s["grade"]
        })

    return jsonify(result)


@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    name = data["name"]
    grade = data["grade"]

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name, grade) VALUES (?, ?)",
        (name, grade)
    )
    conn.commit()
    conn.close()

    return {"message": "Student added successfully"}


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return {"message": "Student deleted"}


if __name__ == "__main__":
    app.run(debug=True)