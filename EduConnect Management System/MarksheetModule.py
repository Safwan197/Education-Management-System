from db_connection import get_connection

def view_marksheet():
    conn = get_connection()
    cursor = conn.cursor()

    roll_no = input("Enter your Roll No: ")

    try:
        cursor.execute("""
            SELECT s.full_name, c.course_name, m.marks_obtained
            FROM marks m
            JOIN students s ON m.student_id = s.student_id
            JOIN courses c ON m.course_id = c.course_id
            WHERE s.roll_no = ?
        """, (roll_no,))
        
        rows = cursor.fetchall()

        if not rows:
            print("No record found.")
            return

        total = 0
        count = 0

        print(f"\nMarksheet for Roll No: {roll_no}")
        print("-" * 40)

        for row in rows:
            print("Course:", row[1], "| Marks:", row[2])
            total += int(row[2])
            count += 1

        print("-" * 40)
        print("Total Marks:", total, "| Average:", total / count)

    except Exception as e:
        print("Database Error:", e)
    finally:
        conn.close()
