import pyodbc
import os

def  db_connection():
    drivers = pyodbc.drivers()
    mysql_driver = next((d for d in drivers if "MySQL ODBC" in d and "ANSI Driver" in d), None)
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    
    dataconnection = (
        f"Driver={mysql_driver};"
        "Server=127.0.0.1;"
        "Database=database_invoices;"
        f"User={db_user};"
        f"Password={db_password};"
        "charset=utf8mb4;"
    )

    try:
        connection = pyodbc.connect(dataconnection)
        return True, ("Successful database connection!")
    except pyodbc.Error as e:
        return False, (f"Error connecting to database: {e}")
    finally:
        connection.close()


if __name__ == '__main__':
    db_connection()
