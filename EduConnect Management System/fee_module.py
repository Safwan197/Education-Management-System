from db_connection import get_connection
from datetime import datetime


def add_fee_record():
    conn = get_connection()
    cursor = conn.cursor()

    roll_no = input("Enter student roll number: ")
    total_fee = float(input("Enter total fee amount: "))

    cursor.execute("SELECT student_id FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()

    if not student:
        print("Student not found!")
        conn.close()
        return

    student_id = student[0]

    cursor.execute("""
        INSERT INTO fees (student_id, total_fee, paid_amount, due_amount, status)
        VALUES (?, ?, ?, ?, ?)
    """, (student_id, total_fee, 0, total_fee, 'Unpaid'))

    conn.commit()
    conn.close()
    print("Fee record added successfully!")

def update_payment():
    conn = get_connection()
    cursor = conn.cursor()

    roll_no = input("Enter student roll number: ")
    payment = float(input("Enter payment amount: "))

    cursor.execute("SELECT student_id FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()

    if not student:
        print("Student not found!")
        conn.close()
        return

    student_id = student[0]

    cursor.execute("SELECT paid_amount, due_amount FROM fees WHERE student_id = ?", (student_id,))
    fee = cursor.fetchone()

    if not fee:
        print("Fee record not found for this student!")
        conn.close()
        return

    paid_amount, due_amount = fee
    new_paid = paid_amount + payment
    new_due = max(due_amount - payment, 0)

    if new_due == 0:
        status = 'Paid'
    elif new_due < due_amount:
        status = 'Partial'
    else:
        status = 'Unpaid'

    payment_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        UPDATE fees
        SET paid_amount = ?, due_amount = ?, status = ?, payment_date = ?
        WHERE student_id = ?
    """, (new_paid, new_due, status, payment_date, student_id))

    conn.commit()
    conn.close()
    print("Payment updated successfully!")


def view_fee_details():
    conn = get_connection()
    cursor = conn.cursor()


    roll_no = input("Enter student roll number: ")

    cursor.execute("""
        SELECT s.full_name, f.total_fee, f.paid_amount, f.due_amount, f.status
        FROM fees f
        JOIN students s ON f.student_id = s.student_id
        WHERE s.roll_no = ?
    """, (roll_no,))

    record = cursor.fetchone()

    if not record:
        print("No fee record found for this student.")
    else:
        print("\n--- FEE DETAILS ---")
        print(f"Student Name : {record[0]}")
        print(f"Total Fee    : {record[1]}")
        print(f"Paid Amount  : {record[2]}")
        print(f"Due Amount   : {record[3]}")
        print(f"Status       : {record[4]}")

        conn.close()

