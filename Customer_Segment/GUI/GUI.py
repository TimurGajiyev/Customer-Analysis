"""
Upload the file by identifing its extension while saving it
Find missing values and point them out
Ask user to proceed further in a new pop-up window 
"""

## Imports
import tkinter as tk
from tkinter import filedialog
import json
import os
import openpyxl
import pandas as pd

## Functions
def on_submit():
    # Retrieve text from entry widgets
    name1 = name.get()
    surname1 = surname.get()
    mail1 = mail.get()
    file_path = entry_file.get()

    file_extension = os.path.splitext(file_path)[1]
    file_type = "Unknown"
    if file_extension:
        file_type = file_extension[1: ].lower()

    if file_path and file_type == "xlsx":
        workbook =  openpyxl.load_workbook(file_path) # Using factory method?

        sheet = workbook.active
        data = sheet.values
        
        try:
            columns = next(data) # Assumes if the first rows contain heads
            file_content = pd.DataFrame(data, columns=columns)
        except StopIteration:
            file_content = pd.DataFrame(columns=[])
        
        workbook.close()

        # Rough approach
        # for row in sheet.iter_rows():
        #     for cell in row:
        #         print(cell.value, end="/t")
        #     print()
    else:
        file_content = None

    data = {
        "Name" : name1,
        "Surname" : surname1,
        "Mail" : mail1,
        "FilePath" : file_path,
        "FileType" : file_type,
        "FileContent" : None if file_content is None else file_content.to_dict(orient='records')
    }

    json_data = json.dumps(data, indent=2)

    print("Collected data in JSON format")
    print(json_data)
    print(file_content)


def file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)
    

# Main Window
root = tk.Tk()
root.title("Data Extraction")


# Entry widgets
name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
name = tk.Entry(root)
name.grid(row=0, column=1, padx=10, pady=10)

surname_label = tk.Label(root, text="Surname")
surname_label.grid(row=1, column=0, padx=10, pady=10)
surname = tk.Entry(root)
surname.grid(row=1, column=1, padx=10, pady=10)

mail_label = tk.Label(root, text="Mail")
mail_label.grid(row=2, column=0, padx=10, pady=10)
mail = tk.Entry(root)
mail.grid(row=2, column=1, padx=10, pady=10)

file_label = tk.Label(root, text="File Path:")
file_label.grid(row=3, column=0, padx=10, pady=10)
entry_file = tk.Entry(root, width=30)
entry_file.grid(row=3, column=1, padx=10, pady=10)


# Buttons
browse_button1 = tk.Button(root, text="Browse", command=file)
browse_button1.grid(row=3, column=2, pady=10)

submit_button1 = tk.Button(root, text="Submit", command=on_submit)
submit_button1.grid(row=4, column=0, columnspan=2, pady=10)


## Callings
root.mainloop()