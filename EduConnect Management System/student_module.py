import random
from db_connection import get_connection

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter student name: ")
    email = input("Enter student email: ")
    roll_no = random.randint(1000, 9999)

    cursor.execute("INSERT INTO students (full_name, email, roll_no) VALUES (?, ?, ?)", (name, email, roll_no))
    conn.commit()
    conn.close()
    print("Student added successfully with Roll No:", roll_no)

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    roll_no = input("Enter roll number to delete: ")

    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No student found with roll number {roll_no}.")
    else:
        print("Student deleted successfully.")

    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | FULL NAME: {row[1]} | ROLL NO: {row[2]} | PASS: {row[3]} | EMAIL: {row[4]}")
    conn.close()

def student_login():
    name = input("Enter Full Name: ")
    roll = input("Enter Roll No: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_id FROM students WHERE full_name=? AND roll_no=?", (name, roll))
    s = cursor.fetchone()
    conn.close()
    if s:
        print("Login Successful!")
        return s[0]
    else:
        print("Invalid Name or Roll No.")
        return None
