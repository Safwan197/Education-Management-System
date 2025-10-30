from db_connection import get_connection

def add_course():
    conn = get_connection()
    cursor = conn.cursor()
    name = input("Enter course name: ")
    cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print("Course added successfully!")

def register_course():
    conn = get_connection()
    cursor = conn.cursor()

    roll_no = input("Enter your Roll No: ")
    course_id = input("Enter course ID to register: ")

    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return

    cursor.execute("INSERT INTO  student_courses (student_id, course_id) VALUES (?, ?)", (student[0], course_id))
    conn.commit()
    conn.close()
    print("Course registered successfully!")
