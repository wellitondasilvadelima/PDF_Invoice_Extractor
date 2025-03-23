import pymysql
from database_config import DB_CONFIG
from database_connect import connect

def savedata_Invoices(invoice_number,issue_date,due_date,customer_name,customer_address,po_number,subtotal,tax,total_due,payment_status):

    #connection = pymysql.connect(**DB_CONFIG)
    connection = connect()
    cursor = connection.cursor()

    try:
        # Verifica se o PDF já foi inserido
        cursor.execute("SELECT COUNT(*) FROM Invoices WHERE invoice_number = ?", (str(invoice_number),))
        resultado = cursor.fetchone()

        if(resultado[0] > 0):
            # Atualiza o registro existente
            cursor.execute("""
                            UPDATE Invoices 
                            SET issue_date= ?,
                            due_date= ?,
                            customer_name= ?,
                            customer_address= ?, 
                            po_number= ?,
                            subtotal= ?,
                            tax=?,
                            total_due= ?,
                            payment_status= ? 
                            WHERE invoice_number = ?
                            """, (issue_date,due_date,customer_name,customer_address,po_number,subtotal,tax,total_due,payment_status,invoice_number)
                         )
            print("PDF atualizado com sucesso!")
            connection.commit()
        else:
            # Insere um novo registro
           cursor.execute("""
                            INSERT INTO Invoices 
                            (invoice_number, issue_date, due_date, customer_name, customer_address, po_number, subtotal, tax, total_due, payment_status) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """, (invoice_number, issue_date, due_date, customer_name, customer_address, po_number, subtotal, tax, total_due, payment_status)
                        )
        print("PDF inserido com sucesso!")

        connection.commit()
    
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")
    
    finally:
        cursor.close()
        connection.close()

def savedata_Invoice_Items(invoice_number,item_description,quantity,unit_price,total_price):
    #connection = pymysql.connect(**DB_CONFIG)
    connection = connect()
    cursor = connection.cursor()

    try:
        # Verifica se o PDF já foi inserido
        cursor.execute("SELECT COUNT(*) FROM Invoice_Items WHERE invoice_number = ?", (invoice_number,))
        resultado = cursor.fetchone()

        if resultado[0] > 0:
            # Atualiza o registro existente
            cursor.execute("""
                            UPDATE Invoice_Items 
                            SET item_description= ?,
                                quantity= ?,
                                unit_price= ?,
                                total_price= ?
                            WHERE invoice_number = ?
                                """, (item_description,quantity,unit_price,total_price,invoice_number)
                        )
            print("PDF atualizado com sucesso!")
            connection.commit()
        else:
            # Insere um novo registro
            cursor.execute("""
                    INSERT INTO Invoice_Items (invoice_number,item_description,quantity,unit_price,total_price)
                    VALUES (?, ?, ?,?,?)
                    """, (invoice_number,item_description,quantity,unit_price,total_price)
                    )
            print("PDF inserido com sucesso!")

        connection.commit()
    
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")
    
    finally:
        cursor.close()
        connection.close()

def savedata_Payments(invoice_number,payment_date,payment_amount,payment_status):
    #connection = pymysql.connect(**DB_CONFIG)
    connection = connect()
    cursor = connection.cursor()

    try:
        # Verifica se o PDF já foi inserido
        cursor.execute("SELECT COUNT(*) FROM Payments WHERE invoice_number = ?", (invoice_number,))
        resultado = cursor.fetchone()

        if resultado[0] > 0:
            # Atualiza o registro existente
            cursor.execute("""
                UPDATE Payments 
                SET payment_date= ?,
                    payment_amount= ?,
                    payment_status= ?
                WHERE invoice_number = ?
                """, (payment_date,payment_amount,payment_status,invoice_number)
            )
            print("PDF atualizado com sucesso!")
        else:
            # Insere um novo registro
            cursor.execute("""
                            INSERT INTO Payments (payment_date,payment_amount,payment_status,invoice_number)
                            VALUES (?, ?, ?, ?)
                            """, (payment_date,payment_amount,payment_status,invoice_number)
                            )
            print("PDF inserido com sucesso!")

        connection.commit()
    
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")
    
    finally:
        cursor.close()
        connection.close()

