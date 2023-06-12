from tkinter import Label, Entry, Button, Tk
from CRUD import *
from Tables.TableEmployee import *
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *

def removeLabel(label):
    label.destroy()

def createEmployeeView(session):
    createWindow = Tk()

    createWindow.geometry("300x300")
    
    id_employeeLabel = Label(createWindow, text="id_employee")

    id_employeeLabel.pack()

    id_employeeEntry = Entry(createWindow)

    id_employeeEntry.pack()
    
    first_nameLabel = Label(createWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(createWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(createWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(createWindow)

    last_nameEntry.pack()
    
    salaryLabel = Label(createWindow, text="salary")

    salaryLabel.pack()

    salaryEntry = Entry(createWindow)

    salaryEntry.pack()

    def createEmployeeCommand():
        try:
            createEmployee(session, int(id_employeeEntry.get()), first_nameEntry.get(), last_nameEntry.get(), int(salaryEntry.get()))
            createWindow.destroy()
        except ValueError:
            wrongInputType(createWindow)
        except IntegrityError:
            integrityError(createWindow)
            session.rollback()

    createButton = Button(createWindow, text="Create", command=createEmployeeCommand)

    createButton.pack()

def getEmployeeView(session):
    readWindow = Tk()

    employees = getEmployees(session)

    TableEmployee(readWindow, employees)

def updateEmployeeView(session):
    updateWindow = Tk()

    updateWindow.geometry("300x300")

    id_employeeLabel = Label(updateWindow, text="id_employee")

    id_employeeLabel.pack()

    id_employeeEntry = Entry(updateWindow)

    id_employeeEntry.pack()
    
    first_nameLabel = Label(updateWindow, text="first_name")

    first_nameLabel.pack()

    first_nameEntry = Entry(updateWindow)

    first_nameEntry.pack()
    
    last_nameLabel = Label(updateWindow, text="last_name")

    last_nameLabel.pack()

    last_nameEntry = Entry(updateWindow)

    last_nameEntry.pack()
    
    salaryLabel = Label(updateWindow, text="salary")

    salaryLabel.pack()

    salaryEntry = Entry(updateWindow)

    salaryEntry.pack()

    def updateEmployeeCommand():
        try:
            returnCode = updateEmployee(session, int(id_employeeEntry.get()), first_nameEntry.get(), last_nameEntry.get(), int(salaryEntry.get()))

            if returnCode == -1:
                noObject(updateWindow)
            else:
                updateWindow.destroy()
        except ValueError:
            wrongInputType(updateWindow)
        except IntegrityError:
            FKError(updateWindow)
            session.rollback()

    updateButton = Button(updateWindow, text="Update", command=updateEmployeeCommand)

    updateButton.pack()

def deleteEmployeeView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_employeeLabel = Label(deleteWindow, text="id_employee")

    id_employeeLabel.pack()

    id_employeeEntry = Entry(deleteWindow)

    id_employeeEntry.pack()

    def deleteEmployeeCommand():
        try:
            deleteEmployee(session, int(id_employeeEntry.get()))
            deleteWindow.destroy()
        
        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteEmployeeCommand)

    deleteButton.pack()