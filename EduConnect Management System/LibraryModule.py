from db_connection import get_connection

def add_book():
    conn = get_connection()
    cursor = conn.cursor()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    quantity = input("Enter quantity: ")

    cursor.execute(
        "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
        (title, author, quantity)
    )
    conn.commit()
    conn.close()
    print("Book added successfully!")


def show_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    print("\n--- All Books in Library ---")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | Quantity: {row[3]}")
    conn.close()


def issue_book():
    conn = get_connection()
    cursor = conn.cursor()
    roll_no = input("Enter student Roll No: ")
    book_id = input("Enter book ID: ")

    # Check if student exists
    cursor.execute("SELECT student_id FROM students WHERE roll_no = ?", (roll_no))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        conn.close()
        return

    # Check if book is available
    cursor.execute("SELECT quantity FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book and book[0] > 0:
        # Issue the book
        cursor.execute(
            "INSERT INTO issued_books (student_id, book_id, issue_date) VALUES (?, ?, GETDATE())",
            (student[0], book_id)
        )
        # Reduce quantity
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))
        conn.commit()
        print("Book issued successfully!")
    else:
        print("Book not available.")

    conn.close()


def return_book():
    conn = get_connection()
    cursor = conn.cursor()
    roll_no = input("Enter student Roll No: ")
    book_id = input("Enter book ID: ")

    # Check student existence
    cursor.execute("SELECT id FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        conn.close()
        return

    # Find issued book that hasn't been returned
    cursor.execute(
        "SELECT issue_id FROM issued_books WHERE student_id = ? AND book_id = ? AND return_date IS NULL",
        (student[0], book_id)
    )
    issue = cursor.fetchone()

    if issue:
        # Update return date and increase book quantity
        cursor.execute("UPDATE issued_books SET return_date = GETDATE() WHERE issue_id = ?", (issue[0],))
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (book_id,))
        conn.commit()
        print("Book returned successfully!")
    else:
        print("No issued book found for this student and book.")

    conn.close()
