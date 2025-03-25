"""
=================================================================================
Project: Invoice_PDFReader
File: main.py
Description: Script to read and extract information from Invoice PDF
Author: Welliton Lima
Creation Date: 23/03/2025
Last Modified: 23/03/2025
Version: 1.0
License: MIT License
=================================================================================
"""
from process import process_reader
from getpath import check_path
from database_create import create_database,create_tables
from test_dbconnection import db_connection
import customtkinter as ctk
import re

def clear():
    progress.set(0)
    label_msg.configure(text="",font=("Segoe UI", 14))

def open_popup(msg):
    def set_value(value):
        response.set(value)  # Sets the selected value
        popup.destroy()      # Close the pop-up

    popup = ctk.CTkToplevel()
    popup.title("Notification")
    response = ctk.StringVar()

    center_window(popup,250,250) # to position the window in the center of the screen

    ctk.CTkLabel(popup, text=msg,font=("Segoe UI", 14),wraplength=150).pack(pady=10,fill="both", expand=True)
    ctk.CTkButton(popup, text="OK", command=lambda: set_value(True),width=100, height=50).pack(pady=20)
    
    popup.transient(mainwindow)    # Makes the window stay on top of the main one
    popup.grab_set()               # Blocks interaction with the main
    mainwindow.wait_window(popup)  # Wait for the pop-up to close

def start():
    check_database = False
    
    create_database()
    create_tables()
    
    check_database, msg_db = db_connection()
    okay, path_input, path_data, path_error, path_output = check_path()

    if(check_database and not okay):
        msg = process_reader(path_input=path_input,
                       path_data=path_data,
                       path_error=path_error,
                       path_output=path_output,
                       progress=progress,
                       mainwindow=mainwindow)
        msg = msg_db + "\n\n" + msg
    elif (okay):
        msg = ("Diretórios criados")
    open_popup(msg)
    label_msg.configure(text= msg,font=("Segoe UI", 14))

def center_window(window,width,height):
     # Gets the screen size
    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()

    # Calculates x and y position to center
    pos_x = (width_screen // 2) - (width // 2)
    pos_y = (height_screen // 2) - (height // 2)

    # Defines centered geometry
    window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

# -------| END Function |-------

# -------| MainWindow |-------

def main():
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue") 
    global mainwindow, label_msg, progress

    mainwindow = ctk.CTk()
    mainwindow.title("NF-e Read")

    center_window(mainwindow,380,380)

    label_title = ctk.CTkLabel(mainwindow, text="PDF INVOICE READER: ",font=("Segoe UI", 14),text_color="white")
    label_title.pack()

    button_start = ctk.CTkButton(mainwindow,text="START",command=start,width=150, height=50)
    button_start.pack(pady=20)

    button_clear = ctk.CTkButton(mainwindow,text="Clear",command=clear,width=150, height=50)
    button_clear.pack(pady=5)

    label_msg = ctk.CTkLabel(mainwindow, text="", font=("Segoe UI", 10), text_color="white",wraplength=250)
    label_msg.pack(pady=5,fill="both", expand=True)

    
    progress = ctk.CTkProgressBar(mainwindow, width=300)
    progress.set(0)
    progress.pack(pady=5)

    mainwindow.mainloop()

# -----| END MainWindow |-----

if __name__ == '__main__':
    main()
