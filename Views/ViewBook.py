from tkinter import *
from CRUD import *
from Tables.TableBook import *
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *


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
        try:
            createBook(session, int(id_bookEntry.get()), nameEntry.get(), int(id_authorEntry.get()))
            createWindow.destroy()
        except ValueError:
            wrongInputType(createWindow)
        except IntegrityError:
            integrityError(createWindow)
            session.rollback()

    createButton = Button(createWindow, text="Create", command=createBookCommand)

    createButton.pack()

def getBookView(session):
    readWindow = Tk()

    books = getBooks(session)

    TableBook(readWindow, books)

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
            returnCode = updateBook(session, int(id_bookEntry.get()), nameEntry.get(), int(id_authorEntry.get()))
            
            if returnCode == -1:
                noObject(updateWindow)
            else:
                updateWindow.destroy()
        except ValueError:
            wrongInputType(updateWindow)
        except IntegrityError:
            FKError(updateWindow)
            session.rollback()
        

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
        try:
            deleteBook(session, int(id_bookEntry.get()))
            deleteWindow.destroy()
        
        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteBookCommand)

    deleteButton.pack()