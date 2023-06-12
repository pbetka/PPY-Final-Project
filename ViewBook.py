from tkinter import *
from CRUD import *
from threading import Thread

def createBookView(session):
    createWindow = Tk()

    createWindow.geometry("300x200")
    
    id_bookLabel = Label(createWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(createWindow)

    id_bookEntry.pack()
    
    nameLabel = Label(createWindow, text="name")

    nameLabel.pack()

    nameEntry = Entry(createWindow)

    nameEntry.pack()
    
    id_authorLabel = Label(createWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(createWindow)

    id_authorEntry.pack()

    def createBookCommand():
        createBook(session, int(id_bookEntry.get()), nameEntry.get(), int(id_authorEntry.get()))
        createWindow.destroy()

    createButton = Button(createWindow, text="Create", command=createBookCommand)

    createButton.pack()

def getBookView(session):
    readWindow = Tk()

    books = getBooks(session)

    for book in books:
        id_bookLabel = Label(readWindow, text=f"id_book: {str(book.id_book)}")

        id_bookLabel.pack()

        name = Label(readWindow, text=f"name: {book.name}")

        name.pack()

        id_author = Label(readWindow, text=f"id_author: {str(book.id_author)}")
        id_author.pack()

def updateBookView(session):
    updateWindow = Tk()

    updateWindow.geometry("300x200")

    id_bookLabel = Label(updateWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(updateWindow)

    id_bookEntry.pack()
    
    nameLabel = Label(updateWindow, text="name")

    nameLabel.pack()

    nameEntry = Entry(updateWindow)

    nameEntry.pack()
    
    id_authorLabel = Label(updateWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(updateWindow)

    id_authorEntry.pack()

    def updateBookCommand():
        try:
            updateBook(session, int(id_bookEntry.get()), nameEntry.get(), int(id_authorEntry.get()))
            
            thread = Thread(target=thread_function, args=(1,))
            updateWindow.destroy()
        except ValueError:
            wrongInputLabel = Label(updateWindow, text="Wrong input!", fg="red")
            wrongInputLabel.pack(side="bottom")

    updateButton = Button(updateWindow, text="Update", command=updateBookCommand)

    updateButton.pack()

def deleteBookView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_bookLabel = Label(deleteWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(deleteWindow)

    id_bookEntry.pack()

    def deleteBookCommand():
        deleteBook(session, int(id_bookEntry.get()))
        deleteWindow.destroy()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteBookCommand)

    deleteButton.pack()