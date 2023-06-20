from tkinter import Label, Entry, Button, Tk
from CRUD import *
from Tables.TableCopy import *
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *

# Additional windows popping up when doing operations on Copies

# Window for creating

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

        # Performing operations on DB and displaying potential errors on GUI
        
        try:
            createCopy(session, int(id_copyEntry.get()), int(id_bookEntry.get()))
            createWindow.destroy()
        except ValueError:
            wrongInputType(createWindow)
        except IntegrityError:
            integrityError(createWindow)
            session.rollback()

    createButton = Button(createWindow, text="Create", command=createCopyCommand)

    createButton.pack()

# Window for reading

def getCopyView(session):
    readWindow = Tk()

    copies = getCopies(session)

    TableCopy(readWindow, copies)

# Window for updating

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

        # Performing operations on DB and displaying potential errors on GUI
        
        try:
            returnCode = updateCopy(session, int(id_copyEntry.get()), int(id_bookEntry.get()))
            
            if returnCode == -1:
                noObject(updateWindow)
            else:
                updateWindow.destroy()
        except ValueError:
            wrongInputType(updateWindow)
        except IntegrityError:
            FKError(updateWindow)
            session.rollback()

    updateButton = Button(updateWindow, text="Update", command=updateCopyCommand)

    updateButton.pack()

# Window for deleting

def deleteCopyView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_copyLabel = Label(deleteWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(deleteWindow)

    id_copyEntry.pack()

    def deleteCopyCommand():

        # Performing operations on DB and displaying potential errors on GUI
        
        try:
            deleteCopy(session, int(id_copyEntry.get()))
            deleteWindow.destroy()
        
        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteCopyCommand)

    deleteButton.pack()