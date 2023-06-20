from tkinter import Label

# Custom error messeges displayed on GUI disappearing few seconds after

# Function used to remove labels

def removeLabel(label):
    label.destroy()

# Function for displaying error when: Object with this PK exists or no object with PK equal new FK

def integrityError(window):
    label = Label(window, text="Object with this PK exists\nor no object with PK equal new FK!", fg="red")
    label.pack(side="bottom")
    window.after(7000, removeLabel, label)

# Function for displaying error when: input type is wrong for any text field

def wrongInputType(window):
    label = Label(window, text="Wrong input type!", fg="red")
    label.pack(side="bottom")
    window.after(4000, removeLabel, label)

# Function for displaying error when: No object with PK equal new FK

def FKError(window):
    label = Label(window, text="No object with PK equal new FK!", fg="red")
    label.pack(side="bottom")
    window.after(5000, removeLabel, label)

# Function for displaying error when: No object with this PK

def noObject(window):
    label = Label(window, text="No object with this PK", fg="red")
    label.pack(side="bottom")
    window.after(4000, removeLabel, label)

# Function for displaying error when: Deleting and object used as FK in other table

def objectInUse(window):
    label = Label(window, text="Object used as FK in other table", fg="red")
    label.pack(side="bottom")
    window.after(5000, removeLabel, label)