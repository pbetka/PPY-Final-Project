from tkinter import *
from CRUD import *
from Tables.TableRent import *
from tkcalendar import Calendar
from datetime import datetime
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from ErrorMsgs import *


def removeLabel(label):
    label.destroy()

def createRentView(session):
    createWindow = Tk()

    createWindow.geometry("600x600")
    
    id_rentLabel = Label(createWindow, text="id_rent")

    id_rentLabel.pack()

    id_rentEntry = Entry(createWindow)

    id_rentEntry.pack()
    
    id_clientLabel = Label(createWindow, text="id_client")

    id_clientLabel.pack()

    id_clientEntry = Entry(createWindow)

    id_clientEntry.pack()

    labelsContainer = Frame(createWindow)

    rent_dateLabel = Label(createWindow, text="rent_date")

    rent_dateLabel.pack(padx=120, in_=labelsContainer, side="left")

    due_dateLabel = Label(createWindow, text="due_date")

    due_dateLabel.pack(padx=120, in_=labelsContainer, side="left")

    labelsContainer.pack()

    datesContainer = Frame(createWindow)

    rent_dateCal = Calendar(createWindow, selectmode = 'day',
               year = 2023, month = 6,
               day = 12)
 
    rent_dateCal.pack(padx = 10, pady = 10, in_=datesContainer, side="left")

    due_dateCal = Calendar(createWindow, selectmode = 'day',
               year = 2023, month = 6,
               day = 12)
 
    due_dateCal.pack(padx = 10, pady = 10, in_=datesContainer, side="right")

    datesContainer.pack()
    
    given_backLabel = Label(createWindow, text="given_back")

    given_backLabel.pack()

    trueFalseContainer = Frame(createWindow)

    given_back = bool(None)

    def trueCommand():
        trueButton.config(bg="green")
        falseButton.config(bg="white")
        given_back = True

    trueButton = Button(createWindow, text="True", command=trueCommand)

    trueButton.pack(in_=trueFalseContainer, side="left", padx=10)

    def falseCommand():
        falseButton.config(bg="green")
        trueButton.config(bg="white")
        given_back = False

    falseButton = Button(createWindow, text="False", command=falseCommand)

    falseButton.pack(in_=trueFalseContainer, side="left", padx=10)

    trueFalseContainer.pack(pady=10)
    
    id_employeeLabel = Label(createWindow, text="id_employee")

    id_employeeLabel.pack()

    id_employeeEntry = Entry(createWindow)

    id_employeeEntry.pack()
    
    id_copyLabel = Label(createWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(createWindow)

    id_copyEntry.pack()

    def createRentCommand():
        rent_date = datetime.strptime(rent_dateCal.get_date(), '%m/%d/%y').date()
        due_date = datetime.strptime(due_dateCal.get_date(), '%m/%d/%y').date()
        if rent_date > due_date:
            wrongInputLabel = Label(createWindow, text="Rent date after due date!", fg="red")
            wrongInputLabel.pack(side="bottom")
            createWindow.after(4000, removeLabel, wrongInputLabel)
        else:
            try:
                createRent(session, int(id_rentEntry.get()), 
                        int(id_clientEntry.get()), 
                        rent_date, due_date, 
                        given_back, 
                        int(id_employeeEntry.get()), 
                        int(id_copyEntry.get()))
                createWindow.destroy()
            except ValueError:
                wrongInputType(createWindow)
            except IntegrityError:
                integrityError(createWindow)
                session.rollback()

    createButton = Button(createWindow, text="Create", command=createRentCommand)

    createButton.pack()

def getRentView(session):
    readWindow = Tk()

    rents = getRents(session)

    TableRent(readWindow, rents)

def updateRentView(session):
    updateWindow = Tk()

    updateWindow.geometry("600x600")
    
    id_rentLabel = Label(updateWindow, text="id_rent")

    id_rentLabel.pack()

    id_rentEntry = Entry(updateWindow)

    id_rentEntry.pack()
    
    id_clientLabel = Label(updateWindow, text="id_client")

    id_clientLabel.pack()

    id_clientEntry = Entry(updateWindow)

    id_clientEntry.pack()

    labelsContainer = Frame(updateWindow)

    rent_dateLabel = Label(updateWindow, text="rent_date")

    rent_dateLabel.pack(padx=120, in_=labelsContainer, side="left")

    due_dateLabel = Label(updateWindow, text="due_date")

    due_dateLabel.pack(padx=120, in_=labelsContainer, side="left")

    labelsContainer.pack()

    datesContainer = Frame(updateWindow)

    rent_dateCal = Calendar(updateWindow, selectmode = 'day',
               year = 2023, month = 6,
               day = 12)
 
    rent_dateCal.pack(padx = 10, pady = 10, in_=datesContainer, side="left")

    due_dateCal = Calendar(updateWindow, selectmode = 'day',
               year = 2023, month = 6,
               day = 12)
 
    due_dateCal.pack(padx = 10, pady = 10, in_=datesContainer, side="right")

    datesContainer.pack()
    
    given_backLabel = Label(updateWindow, text="given_back")

    given_backLabel.pack()

    trueFalseContainer = Frame(updateWindow)

    given_back = bool()

    def trueCommand():
        trueButton.config(bg="green")
        falseButton.config(bg="white")
        given_back = True

    trueButton = Button(updateWindow, text="True", command=trueCommand)

    trueButton.pack(in_=trueFalseContainer, side="left", padx=10)

    def falseCommand():
        falseButton.config(bg="green")
        trueButton.config(bg="white")
        given_back = False

    falseButton = Button(updateWindow, text="False", command=falseCommand)

    falseButton.pack(in_=trueFalseContainer, side="left", padx=10)

    trueFalseContainer.pack(pady=10)
    
    id_employeeLabel = Label(updateWindow, text="id_employee")

    id_employeeLabel.pack()

    id_employeeEntry = Entry(updateWindow)

    id_employeeEntry.pack()
    
    id_copyLabel = Label(updateWindow, text="id_copy")

    id_copyLabel.pack()

    id_copyEntry = Entry(updateWindow)

    id_copyEntry.pack()

    def updateRentCommand():
        rent_date = datetime.strptime(rent_dateCal.get_date(), '%m/%d/%y').date()
        due_date = datetime.strptime(due_dateCal.get_date(), '%m/%d/%y').date()
        if rent_date > due_date:
            wrongInputLabel = Label(updateWindow, text="Rent date after due date!", fg="red")
            wrongInputLabel.pack(side="bottom")
            updateWindow.after(4000, removeLabel, wrongInputLabel)
        else:
            try:
                returnCode = updateRent(session, int(id_rentEntry.get()), 
                        int(id_clientEntry.get()), 
                        rent_date, due_date, 
                        given_back.get(), 
                        int(id_employeeEntry.get()), 
                        int(id_copyEntry.get()))
                
                if returnCode == -1:
                    noObject(updateWindow)
                else:
                    updateWindow.destroy()
            except ValueError:
                wrongInputType(updateWindow)
            except IntegrityError:
                FKError(updateWindow)
                session.rollback()

    updateButton = Button(updateWindow, text="Update", command=updateRentCommand)

    updateButton.pack()

def deleteRentView(session):
    deleteWindow = Tk()

    deleteWindow.geometry("300x100")

    id_rentLabel = Label(deleteWindow, text="id_rent")

    id_rentLabel.pack()

    id_rentEntry = Entry(deleteWindow)

    id_rentEntry.pack()

    def deleteRentCommand():
        try:
            deleteRent(session, int(id_rentEntry.get()))
            deleteWindow.destroy()

        except ValueError:
            wrongInputType(deleteWindow)
        except UnmappedInstanceError:
            noObject(deleteWindow)
            session.rollback()
        except IntegrityError:
            objectInUse(deleteWindow)
            session.rollback()

    deleteButton = Button(deleteWindow, text="Delete", command=deleteRentCommand)

    deleteButton.pack()