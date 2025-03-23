from database_connect import connect
from process import process_reader
from getpath import check_path
from database_create import create_database,create_tables

def main():
    create_database()
    create_tables()
    try:
        connection = connect()
        database = True
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        database = False
    finally:
        connection.close()

    okay, path_input, path_data, path_error, path_output = check_path()

    if(database and not okay):
        process_reader(path_input, path_data,path_error,path_output)
    elif (okay):
        print("Diretórios criados")
    else:
        print("Erro na conexão com a database")


if __name__ == '__main__':
    main()
