import tkinter as tk

class TableCopy:
    def __init__(self, root, copies):
        headers = ["id_copy", "id_book"]

        numRows = len(copies)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=25, pady=5)
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = copies[i].id_copy
                else:
                    cellValue = copies[i].id_book
                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=25, pady=5)