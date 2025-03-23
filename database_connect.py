import pyodbc
import os
    # Acessar as variáveis de ambiente
def connect():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    dataconnection = (
        "Driver={MySQL ODBC 9.2 ANSI Driver};"
        "Server=127.0.0.1;"
        "Database=database_invoices;"
        f"User={db_user};"
        f"Password={db_password};"
        "charset=utf8mb4;"
    )

    return pyodbc.connect(dataconnection)

# try:
#     connection = pyodbc.connect(dataconnection)
#     print("Conexão bem-sucedida!")
# except pyodbc.Error as e:
#     print(f"Erro ao conectar: {e}")
# finally:
#     connection.close()
