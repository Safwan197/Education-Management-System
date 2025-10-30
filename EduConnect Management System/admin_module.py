from db_connection import get_connection

def admin_login():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    data = cursor.fetchone()
    conn.close()
    if data:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials.")
        return False


def change_admin_credentials():
    conn = get_connection()
    cursor = conn.cursor()

    current_username = input("Enter current admin username: ")
    current_password = input("Enter current admin password: ")

    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", 
                   (current_username, current_password))
    row = cursor.fetchone()

    if row:
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        cursor.execute("UPDATE admin SET username=?, password=? WHERE username=? AND password=?",
                       (new_username, new_password, current_username, current_password))
        conn.commit()
        print("Admin credentials updated successfully!")
    else:
        print("Current credentials are incorrect.")

    conn.close()
