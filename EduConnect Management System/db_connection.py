import pyodbc

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=libraryDB;"
        "UID=sa;"
        "PWD=safwan12345;"
    )

conn = get_connection()
print("Connection successful!")
conn.close()
