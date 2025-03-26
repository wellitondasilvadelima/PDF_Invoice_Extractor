from database_config import DB_CONFIG
from database_connect import connect

def savedata_Invoices(invoice_number,
                      issue_date,
                      due_date,
                      customer_name,
                      customer_address,
                      customerphone,
                      suppliercompany,
                      suppliercompanyadress,
                      phonecompany,
                      ordernumber,
                      po_number,
                      subtotal,
                      tax,
                      total_due,
                      payment_terms,
):
    connection = connect()
    cursor = connection.cursor()

    # Inserts a new record
    cursor.execute("SELECT COUNT(*) FROM Invoices WHERE invoice_number = ?", (str(invoice_number),))
    resultado = cursor.fetchone()

    if(resultado[0] > 0):
        # Updates existing record
        cursor.execute("""
                        UPDATE Invoices 
                        SET issue_date= ?,
                        due_date= ?,
                        customer_name= ?,
                        customer_address= ?, 
                        customerphone= ?,
                        suppliercompany= ?,
                        suppliercompanyadress= ?,
                        phonecompany= ?,
                        ordernumber= ?,
                        po_number= ?,
                        subtotal= ?,
                        tax= ?,
                        total_due= ?,
                        payment_terms= ? 
                        WHERE invoice_number= ?
                        """, (issue_date,
                                due_date,
                                customer_name,
                                customer_address,
                                customerphone,
                                suppliercompany,
                                suppliercompanyadress,
                                phonecompany,
                                ordernumber,
                                po_number,
                                subtotal,
                                tax,
                                total_due,
                                payment_terms,
                                invoice_number)
                        )
        connection.commit()
    else:
        # Inserts a new record
        cursor.execute("""
                        INSERT INTO Invoices 
                        (invoice_number,
                         issue_date,
                         due_date,
                         customer_name,
                         customer_address,
                         customerphone,
                         suppliercompany,
                         suppliercompanyadress,
                         phonecompany,
                         ordernumber,
                         po_number,
                         subtotal,
                         tax,
                         total_due,
                         payment_terms) 
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                         """, ( invoice_number,
                                issue_date,
                                due_date,
                                customer_name,
                                customer_address,
                                customerphone,
                                suppliercompany,
                                suppliercompanyadress,
                                phonecompany,
                                ordernumber,
                                po_number,
                                subtotal,
                                tax,
                                total_due,
                                payment_terms)
                    )
    connection.commit()
    cursor.close()
    connection.close()

def savedata_Invoice_Items(invoice_number,ordernumber,item_description,quantity,unit_price,total_price):
    connection = connect()
    cursor = connection.cursor()

    # Checks if the invoice has already been entered
    cursor.execute("SELECT COUNT(*) FROM Invoice_Items WHERE invoice_number = ?", (invoice_number,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        # Updates existing record
        cursor.execute("""
                        UPDATE Invoice_Items 
                        SET ordernumber = ?,
                            item_description= ?,
                            quantity= ?,
                            unit_price= ?,
                            total_price= ?
                        WHERE invoice_number = ?
                        """, (ordernumber,
                            item_description,
                            quantity,
                            unit_price,
                            total_price,
                            invoice_number))
        msg = ("PDF atualizado com sucesso!")
        connection.commit()
    else:
        # Inserts a new record
        cursor.execute("""
                INSERT INTO Invoice_Items (invoice_number,
                                            ordernumber,
                                            item_description,
                                            quantity,
                                            unit_price,
                                            total_price)
                                            VALUES (?,?,?,?,?,?)
                                            """, (invoice_number,
                                                    ordernumber,
                                                    item_description,
                                                    quantity,
                                                    unit_price,
                                                    total_price)
                )

    connection.commit()
    cursor.close()
    connection.close()


def savedata_Payments(invoice_number,
                      payment_date,
                      payment_terms,
                      payment_amount,
                      payment_shipping_handling):
    
    connection = connect()
    cursor = connection.cursor()

    # Checks if the invoice has already been entered
    cursor.execute("SELECT COUNT(*) FROM Payments WHERE invoice_number = ?", (invoice_number,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        # Updates existing record
        cursor.execute("""
            UPDATE Payments 
            SET payment_date= ?,
                payment_terms= ?,
                payment_amount= ?,
                payment_shipping_handling =?
            WHERE invoice_number = ?
            """, (payment_date,
                    payment_terms,
                    payment_amount,
                    payment_shipping_handling,
                    invoice_number)
        )
        msg = ("PDF atualizado com sucesso!")
    else:
        # Inserts a new record
        cursor.execute("""
                        INSERT INTO Payments ( payment_date,
                                               payment_terms,
                                               payment_amount,
                                               payment_shipping_handling,
                                               invoice_number)
                                               VALUES (?, ?, ?, ?, ?)
                                               """, ( payment_date,
                                                      payment_terms,
                                                      payment_amount,
                                                      payment_shipping_handling,
                                                      invoice_number))

    connection.commit()
    cursor.close()
    connection.close()