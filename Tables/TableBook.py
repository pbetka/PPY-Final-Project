import tkinter as tk

class TableBook:
    def __init__(self, root, books):
        headers = ["id_book", "name", "id_author"]

        numRows = len(books)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=5, pady=5)
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = books[i].id_book
                elif j == 1:
                    cellValue = books[i].name
                else:
                    cellValue = books[i].id_author

                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=5, pady=5)