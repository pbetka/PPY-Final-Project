import tkinter as tk

class TableRent:
    def __init__(self, root, rents):
        headers = ["id_rent", "id_client", "rent_date", "due_date", "given_back", "id_employee", "id_copy"]

        numRows = len(rents)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=5, pady=5)
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = rents[i].id_rent
                elif j == 1:
                    cellValue = rents[i].id_client
                elif j == 2:
                    cellValue = rents[i].rent_date
                elif j == 3:
                    cellValue = rents[i].due_date
                elif j == 4:
                    cellValue = rents[i].given_back
                elif j == 5:
                    cellValue = rents[i].id_employee
                else:
                    cellValue = rents[i].id_copy

                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=5, pady=5)