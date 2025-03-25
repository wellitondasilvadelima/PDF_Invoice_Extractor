import pyodbc
import os

def connect():
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

    return pyodbc.connect(dataconnection)
