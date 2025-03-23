import os
import time
import pandas as pd
from reader import pdf_reader
from movefiles import move_allfiles
from database_commit import savedata_Invoice_Items,savedata_Invoices,savedata_Payments

#from openpyxl import load_workbook

# path_input   =  './input'
# path_data    =  './data'
# path_error   =  './dataerror'
# path_output  =  './output'

def Data_Log(cols,rows,path_output):
    file_log = path_output+"/logs.xlsx"

    new_data = pd.DataFrame(columns=cols,data=rows)
    if not os.path.exists(file_log):
        new_data.to_excel(file_log, index=False)
        print("Arquivo criado com sucesso!")
    else:
        # Se existir, adiciona os novos dados sem apagar os antigos
        with pd.ExcelWriter(file_log, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            df_exists = pd.read_excel(file_log)  # Lê os dados existentes
            new_data.to_excel(writer, index=False, header=False, startrow=len(df_exists) + 1)
        print("Novos dados adicionados com sucesso!")

def process_reader(path_input, path_data,path_error,path_output):
    # -------|    Variable declaration   |-------
    msg_return = ""
    move_okay  = False
    # -------| END Variable declaration |-------

    list_invoice = os.listdir(path_input) # Get the files contained in the directory

    if (list_invoice != []):

        cols = ["Date_process","Hour_process","File_Name","invoice_number","Status","Messege"]
        rows = []
        for invoice_name in list_invoice:
            if(".pdf" == os.path.splitext(invoice_name)[1]): # Checks if files have the correct extension
                save, data = pdf_reader(invoice_name,rows) 

                if (save == True):
                    print(invoice_name)
                    savedata_Invoices(data["invoice_number"],data["issue_date"],data["due_date"],data["customer_name"],data["customer_address"],data["po_number"],data["subtotal"],data["salestax"],data["total_due"], data["payment_status"])
            
                    savedata_Payments(data["invoice_number"],data["payment_date"], data["payment_amount"],data["payment_status"])

                    for product in data["products"]:
                        savedata_Invoice_Items(data["invoice_number"],product["description"],product["quantity"],product["unitprice"],product["total"])

                    move_allfiles(path_input,path_data, invoice_name)
                else:
                    move_allfiles(path_input,path_error, invoice_name)
            else:
               move_allfiles(path_input,path_error, invoice_name)
               rows.append(" "," ",invoice_name," ","Exeception","It's not a PDF File.")

        # Checks to create a message informing the user
        
        if(rows != []):
           Data_Log(cols,rows,path_output)
        else:
            msg_return = ("Output file LOG CANNOT be generated")
    else:
        msg_return = "The input folder is empty!"
    
    return msg_return
