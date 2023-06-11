from tkinter import *
from CRUD import *

def bookCreateButtonCommand():
    createWindow = Tk()
    
    id_bookLabel = Label(createWindow, text="id_book")

    id_bookLabel.pack()

    id_bookEntry = Entry(createWindow)

    id_bookEntry.pack()
    
    nameLabel = Label(createWindow, text="Name")

    nameLabel.pack()

    nameEntry = Entry(createWindow)

    nameEntry.pack()
    
    id_authorLabel = Label(createWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(createWindow)

    id_authorEntry.pack()

    def processCreateBook():
        createBook(int(id_bookEntry.get()), nameEntry.get(), int(id_authorEntry.get()))

    createButton = Button(createWindow, text="Create", command=processCreateBook)

    createButton.pack()

def bookGetButtonCommand(session):
    readWindow = Tk()

    books = getBooks(session)
    print(books)

    for book in books:
        id_bookLabel = Label(readWindow, text=book.id_book)

        id_bookLabel.pack()

        name = Label(readWindow, text=book.name)

        name.pack()

        id_author = Label(readWindow, text=book.id_author)
        id_author.pack()