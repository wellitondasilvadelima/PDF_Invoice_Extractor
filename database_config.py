import os

# config.py
DB_CONFIG = {
    "DB_HOST" : "localhost",
    "DB_USER" : os.getenv('DB_USER'),
    "DB_PASSWORD" : os.getenv('DB_PASSWORD'),
    "DB_NAME" : "database_invoices"
}