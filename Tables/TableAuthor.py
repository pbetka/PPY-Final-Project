import tkinter as tk

# Table displaying Authors

class TableAuthor:
    def __init__(self, root, authors):

        # Add headers to table

        headers = ["id_author", "first_name", "last_name"]

        numRows = len(authors)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=5, pady=5)

        # Populate table with given data
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = authors[i].id_author
                elif j == 1:
                    cellValue = authors[i].first_name
                else:
                    cellValue = authors[i].last_name

                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=5, pady=5)