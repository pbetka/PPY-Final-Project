import tkinter as tk

class TableClient:
    def __init__(self, root, clients):
        headers = ["id_client", "first_name", "last_name", "phone_number"]

        numRows = len(clients)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=5, pady=5)
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = clients[i].id_client
                elif j == 1:
                    cellValue = clients[i].first_name
                elif j == 2:
                    cellValue = clients[i].last_name
                else:
                    cellValue = clients[i].phone_number

                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=5, pady=5)