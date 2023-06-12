from tkinter import *
from CRUD import *

def createAuthorView(session):
    createWindow = Tk()

    createWindow.geometry("300x200")
    
    id_authorLabel = Label(createWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(createWindow)

    id_authorEntry.pack()
    
    first_nameLabel = Label(createWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(createWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(createWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(createWindow)

    last_nameEntry.pack()

    def createAuthorCommand():
        createAuthor(session, int(id_authorEntry.get()), first_nameEntry.get(), last_nameEntry.get())
        createWindow.destroy()

    createButton = Button(createWindow, text="Create", command=createAuthorCommand)

    createButton.pack()

def getAuthorView(session):
    readWindow = Tk()

    authors = getAuthors(session)

    for author in authors:
        id_authorLabel = Label(readWindow, text=f"id_author: {str(author.id_author)}")

        id_authorLabel.pack()

        first_name = Label(readWindow, text=f"first_name: {author.first_name}")

        first_name.pack()

        last_name = Label(readWindow, text=f"last_name: {author.last_name}")
        
        last_name.pack()

def updateAuthorView(session):
    updateWindow = Tk()

    updateWindow.geometry("300x200")

    id_authorLabel = Label(updateWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(updateWindow)

    id_authorEntry.pack()
    
    first_nameLabel = Label(updateWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(updateWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(updateWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(updateWindow)

    last_nameEntry.pack()

    def updateAuthorCommand():
        updateAuthor(session, int(id_authorEntry.get()), first_nameEntry.get(), last_nameEntry.get())
        updateWindow.destroy()

    updateButton = Button(updateWindow, text="Update", command=updateAuthorCommand)

    updateButton.pack()

def deleteAuthorView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_authorLabel = Label(deleteWindow, text="id_author")

    id_authorLabel.pack()

    id_authorEntry = Entry(deleteWindow)

    id_authorEntry.pack()

    def deleteAuthorCommand():
        deleteAuthor(session, int(id_authorEntry.get()))
        deleteWindow.destroy()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteAuthorCommand)

    deleteButton.pack()