import os
import time
import pandas as pd
from reader import pdf_reader
from movefiles import move_allfiles
from openpyxl import load_workbook


# Function that obtains files from the input folder and performs the reading to obtain the data and saves it in an XLSX file.

path_input   =  './input'
path_data    =  './data'
path_error   =  './dataerror'
path_output  =  './output'

def nfe_reader(path_input, path_data,path_error):
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

                move_okay = pdf_reader(invoice_name,rows) 

                if (move_okay == True):
                    move_allfiles(path_input,path_data, invoice_name)
                else:
                    move_allfiles(path_input,path_error, invoice_name)
            else:
               move_allfiles(path_input,path_error, invoice_name)
               cols.append(" "," ",invoice_name," ","Exeception","It's not a PDF File.")

        # Checks to create a message informing the user
        file_log = "./output/logs.xlsx"
        if(rows != []):
            # table = pd.DataFrame(columns=cols,data=rows)
            # table.to_excel(file_log,index=False)
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
        else:
            msg_return = ("Output file LOG CANNOT be generated")

    else:
        msg_return = "The input folder is empty!"
    
    return msg_return

nfe_reader(path_input, path_data,path_error)
print("OK")