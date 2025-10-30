# from LibraryModule import *
# from MarksheetModule import *




# # LIBRARY:2


# #add_book()

# issue_book()
# show_books()
# view_marksheet()




from admin_module import *
from student_module import *
from course_module import *
from marks_module import *
from fee_module import *
from LibraryModule import *
from MarksheetModule import *
from chatbot import *
def fee_management_menu():
    while True:
        print("\n--- FEE MANAGEMENT ---")
        print("1. Add Fee Record")
        print("2. Update Payment")
        print("3. View Fee Details")
        print("4. Back to Admin Menu")
        ch = input("Enter choice: ")

        if ch == '1':
            add_fee_record()
        elif ch == '2':
            update_payment()
        elif ch == '3':
            view_fee_details()
        elif ch == '4':
            break
        else:
            print("Invalid choice.")

# def admin_menu():
#     while True:
#         print("\n--- ADMIN MENU ---")
#         print("1. Add Student")
#         print("2. Delete Student")
#         print("3. View Students")
#         print("4. Add Course")
#         print("5. Add Marks")
#         print("6. Add Book")
#         print("7. Fee Management")
#         print("8. Logout")
#         ch = input("Enter choice: ")

#         if ch == '1':
#             add_student()
#         elif ch == '2':
#             delete_student()
#         elif ch == '3':
#             view_students()
#         elif ch == '4':
#             add_course()
#         elif ch == '5':
#             add_marks()
#         elif ch == '6':
#             add_book()
#         elif ch == '7':
#             fee_management_menu()  
#         elif ch == '8':
#             print("Logging out...")
#             break
#         else:
#             print("Invalid option.")

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Students")
        print("4. Add Course")
        print("5. Add Marks")
        print("6. Add Book")
        print("7. Fee Management")
        print("8. Change Admin Credentials")  
        print("9. Logout")
        ch = input("Enter choice: ")

        if ch == '1':
            add_student()
        elif ch == '2':
            delete_student()
        elif ch == '3':
            view_students()
        elif ch == '4':
            add_course()
        elif ch == '5':
            add_marks()
        elif ch == '6':
            add_book()
        elif ch == '7':
            fee_management_menu()  
        elif ch == '8':
            change_admin_credentials() 
        elif ch == '9':
            print("Logging out...")
            break
        else:
            print("Invalid option.")


def student_menu(student_id):
    while True:
        print("\n--- STUDENT MENU ---")
        print("1. Register Course")
        print("2. View Marksheet")
        print("3. Show Books")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Use AI Chatbot")
        print("7. Logout")
        ch = input("Enter choice: ")

        if ch == '1':
            register_course()
        elif ch == '2':
            view_marksheet()
        elif ch == '3':
            show_books()
        elif ch == '4':
            issue_book()
        elif ch == '5':
            return_book()
        elif ch == '6':
            ai_generate_questions()
        elif ch == '7':
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n==============================")
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("   BY EDUCONNECT ")
        print("==============================")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            if admin_login():
                admin_menu()
        elif ch == '2':
            student_id = student_login()
            if student_id:
                student_menu(student_id)
        elif ch == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input!")

main_menu()
