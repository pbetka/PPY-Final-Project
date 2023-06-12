from tkinter import *
from CRUD import *
from Tables.TableAuthor import *
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *

def removeLabel(label):
    label.destroy()

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
        try:
            createAuthor(session, int(id_authorEntry.get()), first_nameEntry.get(), last_nameEntry.get())
            createWindow.destroy()
        except ValueError:
            wrongInputType(createWindow)
        except IntegrityError:
            integrityError(createWindow)
            session.rollback()

    createButton = Button(createWindow, text="Create", command=createAuthorCommand)

    createButton.pack()

def getAuthorView(session):
    readWindow = Tk()

    authors = getAuthors(session)

    TableAuthor(readWindow, authors)

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
        try:
            returnCode = updateAuthor(session, int(id_authorEntry.get()), first_nameEntry.get(), last_nameEntry.get())
            
            if returnCode == -1:
                noObject(updateWindow)
            else:
                updateWindow.destroy()
        except ValueError:
            wrongInputType(updateWindow)
        except IntegrityError:
            FKError(updateWindow)
            session.rollback()

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
        try:
            deleteAuthor(session, int(id_authorEntry.get()))
            deleteWindow.destroy()
        
        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteAuthorCommand)

    deleteButton.pack()