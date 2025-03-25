import os
import pyodbc

drivers = pyodbc.drivers()
mysql_driver = next((d for d in drivers if "MySQL ODBC" in d and "ANSI Driver" in d), None)

# config.py
DB_CONFIG = {
    "DB_HOST" : "localhost",
    "DB_USER" : os.getenv('DB_USER'),
    "DB_PASSWORD" : os.getenv('DB_PASSWORD'),
    "DB_NAME" : "database_invoices",
    "DB_DRIVER": mysql_driver
}