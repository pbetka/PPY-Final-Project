from tkinter import *
from CRUD import *
from threading import Thread

def createCopyView(session):
    createWindow = Tk()

    createWindow.geometry("300x200")
    
    id_copyLabel = Label(createWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(createWindow)

    id_copyEntry.pack()
    
    id_bookLabel = Label(createWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(createWindow)

    id_bookEntry.pack()

    def createCopyCommand():
        createCopy(session, int(id_copyEntry.get()), int(id_bookEntry.get()))
        createWindow.destroy()

    createButton = Button(createWindow, text="Create", command=createCopyCommand)

    createButton.pack()

def getCopyView(session):
    readWindow = Tk()

    copies = getCopies(session)

    for copy in copies:
        id_copyLabel = Label(readWindow, text=f"id_copy: {str(copy.id_copy)}")

        id_copyLabel.pack()

        id_book = Label(readWindow, text=f"id_book: {str(copy.id_book)}")

        id_book.pack()

def updateCopyView(session):
    updateWindow = Tk()

    updateWindow.geometry("300x200")

    id_copyLabel = Label(updateWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(updateWindow)

    id_copyEntry.pack()
    
    id_bookLabel = Label(updateWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(updateWindow)

    id_bookEntry.pack()

    def updateCopyCommand():
        try:
            updateCopy(session, int(id_copyEntry.get()), int(id_bookEntry.get()))
            
            def thread_function():
                print()
            thread = Thread(target=thread_function, args=(1,))
            updateWindow.destroy()
        except ValueError:
            wrongInputLabel = Label(updateWindow, text="Wrong input!", fg="red")
            wrongInputLabel.pack(side="bottom")

    updateButton = Button(updateWindow, text="Update", command=updateCopyCommand)

    updateButton.pack()

def deleteCopyView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_copyLabel = Label(deleteWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(deleteWindow)

    id_copyEntry.pack()

    def deleteCopyCommand():
        deleteCopy(session, int(id_copyEntry.get()))
        deleteWindow.destroy()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteCopyCommand)

    deleteButton.pack()