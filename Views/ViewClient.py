from tkinter import Label, Entry, Button, Tk
from CRUD import *
from Tables.TableClient import *
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *

def removeLabel(label):
    label.destroy()

def createClientView(session):
    createWindow = Tk()

    createWindow.geometry("300x300")
    
    id_clientLabel = Label(createWindow, text="id_client")

    id_clientLabel.pack()

    id_clientEntry = Entry(createWindow)

    id_clientEntry.pack()
    
    first_nameLabel = Label(createWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(createWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(createWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(createWindow)

    last_nameEntry.pack()
    
    phone_numberLabel = Label(createWindow, text="phone_number")

    phone_numberLabel.pack()

    phone_numberEntry = Entry(createWindow)

    phone_numberEntry.pack()

    def createClientCommand():
        try:
            createClient(session, int(id_clientEntry.get()), first_nameEntry.get(), last_nameEntry.get(), phone_numberEntry.get())
            createWindow.destroy()
        except ValueError:
            wrongInputType(createWindow)
        except IntegrityError:
            integrityError(createWindow)
            session.rollback()

    createButton = Button(createWindow, text="Create", command=createClientCommand)

    createButton.pack()

def getClientView(session):
    readWindow = Tk()

    clients = getClients(session)

    TableClient(readWindow, clients)

def updateClientView(session):
    updateWindow = Tk()

    updateWindow.geometry("300x300")

    id_clientLabel = Label(updateWindow, text="id_client")

    id_clientLabel.pack()

    id_clientEntry = Entry(updateWindow)

    id_clientEntry.pack()
    
    first_nameLabel = Label(updateWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(updateWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(updateWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(updateWindow)

    last_nameEntry.pack()
    
    phone_numberLabel = Label(updateWindow, text="phone_number")

    phone_numberLabel.pack()

    phone_numberEntry = Entry(updateWindow)

    phone_numberEntry.pack()

    def updateClientCommand():
        try:
            returnCode = updateClient(session, int(id_clientEntry.get()), first_nameEntry.get(), last_nameEntry.get(), phone_numberEntry.get())
            
            if returnCode == -1:
                noObject(updateWindow)
            else:
                updateWindow.destroy()
        except ValueError:
            wrongInputType(updateWindow)
        except IntegrityError:
            FKError(updateWindow)
            session.rollback()

    updateButton = Button(updateWindow, text="Update", command=updateClientCommand)

    updateButton.pack()

def deleteClientView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_clientLabel = Label(deleteWindow, text="id_client")

    id_clientLabel.pack()

    id_clientEntry = Entry(deleteWindow)

    id_clientEntry.pack()

    def deleteClientCommand():
        try:
            deleteClient(session, int(id_clientEntry.get()))
            deleteWindow.destroy()
        
        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteClientCommand)

    deleteButton.pack()