from tkinter import Label

def removeLabel(label):
    label.destroy()


def integrityError(window):
    label = Label(window, text="Object with this PK exists\nor no object with PK equal new FK!", fg="red")
    label.pack(side="bottom")
    window.after(7000, removeLabel, label)

def wrongInputType(window):
    label = Label(window, text="Wrong input type!", fg="red")
    label.pack(side="bottom")
    window.after(4000, removeLabel, label)

def FKError(window):
    label = Label(window, text="No object with PK equal new FK!", fg="red")
    label.pack(side="bottom")
    window.after(5000, removeLabel, label)

def noObject(window):
    label = Label(window, text="No object with this PK", fg="red")
    label.pack(side="bottom")
    window.after(4000, removeLabel, label)

def objectInUse(window):
    label = Label(window, text="Object used as FK in other table", fg="red")
    label.pack(side="bottom")
    window.after(5000, removeLabel, label)