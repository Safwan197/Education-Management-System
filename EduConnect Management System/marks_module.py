from db_connection import get_connection

def add_marks():
    conn = get_connection()
    cursor = conn.cursor()

    roll_no = input("Enter student roll number: ")
    course_id = input("Enter course ID: ")
    marks = input("Enter marks: ")

    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return

    cursor.execute("INSERT INTO marks (student_id, course_id, marks) VALUES (?, ?, ?)", (student[0], course_id, marks))
    conn.commit()
    conn.close()
    print("Marks added successfully!")
