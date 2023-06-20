import tkinter as tk

# Table displaying Employees

class TableEmployee:
    def __init__(self, root, employees):

        # Add headers to table

        headers = ["id_employee", "first_name", "last_name", "salary"]

        numRows = len(employees)
        numColumns = len(headers)

        for j in range(numColumns):
            headerLabel = tk.Label(root, text=headers[j], font=("bold", 10))
            headerLabel.grid(row=0, column=j, padx=5, pady=5)

        # Populate table with given data
        
        for i in range(numRows):
            for j in range(numColumns):
                if j == 0:
                    cellValue = employees[i].id_employee
                elif j == 1:
                    cellValue = employees[i].first_name
                elif j == 2:
                    cellValue = employees[i].last_name
                else:
                    cellValue = employees[i].salary

                cellLabel = tk.Label(root, text=cellValue)
                cellLabel.grid(row=i+1, column=j, padx=5, pady=5)