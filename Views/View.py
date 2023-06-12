from tkinter import *
from Views.ViewBook import *
from Views.ViewAuthor import *
from Views.ViewCopy import *
from Views.ViewClient import *
from Views.ViewEmployee import *
from Views.ViewRent import *

class Window:
    def __init__(self, session):
        self.window = Tk()

        self.window.geometry("300x155")
        
        #Book

        booksContainer = Frame(self.window)

        booksLabel = Label(self.window, text="Books")

        booksLabel.pack(in_=booksContainer, side="left")

        def deleteBookCommand():
            deleteBookView(session)

        booksDeleteButton = Button(self.window, text="Delete", command=deleteBookCommand)

        booksDeleteButton.pack(in_=booksContainer, side="right")

        booksContainer.pack(side="top", fill="x")

        def updateBookCommand():
            updateBookView(session)

        booksUpdateButton = Button(self.window, text="Update", command=updateBookCommand)

        booksUpdateButton.pack(in_=booksContainer, side="right")

        def getBookCommand():
            getBookView(session)

        booksReadButton = Button(self.window, text="Read", command=getBookCommand)

        booksReadButton.pack(in_=booksContainer, side="right")

        def createBookCommand():
            createBookView(session)

        booksCreateButton = Button(self.window, text="Create", command=createBookCommand)

        booksCreateButton.pack(in_=booksContainer, side="right")

        #Author
        
        authorsContainer = Frame(self.window, background="#5A5A5A")

        authorsLabel = Label(self.window, text="Authors")

        authorsLabel.pack(in_=authorsContainer, side="left")

        def deleteAuthorCommand():
            deleteAuthorView(session)

        authorsDeleteButton = Button(self.window, text="Delete", command=deleteAuthorCommand)

        authorsDeleteButton.pack(in_=authorsContainer, side="right")

        authorsContainer.pack(side="top", fill="x")

        def updateAuthorCommand():
            updateAuthorView(session)

        authorsUpdateButton = Button(self.window, text="Update", command=updateAuthorCommand)

        authorsUpdateButton.pack(in_=authorsContainer, side="right")

        def getAuthorCommand():
            getAuthorView(session)

        authorsReadButton = Button(self.window, text="Read", command=getAuthorCommand)

        authorsReadButton.pack(in_=authorsContainer, side="right")

        def createAuthorCommand():
            createAuthorView(session)

        authorsCreateButton = Button(self.window, text="Create", command=createAuthorCommand)

        authorsCreateButton.pack(in_=authorsContainer, side="right")

        #Copy
        
        copiesContainer = Frame(self.window)

        copiesLabel = Label(self.window, text="Copies")

        copiesLabel.pack(in_=copiesContainer, side="left")

        def deleteCopyCommand():
            deleteCopyView(session)

        copiesDeleteButton = Button(self.window, text="Delete", command=deleteCopyCommand)

        copiesDeleteButton.pack(in_=copiesContainer, side="right")

        copiesContainer.pack(side="top", fill="x")

        def updateCopyCommand():
            updateCopyView(session)

        copiesUpdateButton = Button(self.window, text="Update", command=updateCopyCommand)

        copiesUpdateButton.pack(in_=copiesContainer, side="right")

        def getCopyCommand():
            getCopyView(session)

        copiesReadButton = Button(self.window, text="Read", command=getCopyCommand)

        copiesReadButton.pack(in_=copiesContainer, side="right")

        def createCopyCommand():
            createCopyView(session)

        copiesCreateButton = Button(self.window, text="Create", command=createCopyCommand)

        copiesCreateButton.pack(in_=copiesContainer, side="right")

        #Client
        
        clientsContainer = Frame(self.window, background="#5A5A5A")

        clientsLabel = Label(self.window, text="Clients")

        clientsLabel.pack(in_=clientsContainer, side="left")

        def deleteClientCommand():
            deleteClientView(session)

        clientsDeleteButton = Button(self.window, text="Delete", command=deleteClientCommand)

        clientsDeleteButton.pack(in_=clientsContainer, side="right")

        clientsContainer.pack(side="top", fill="x")

        def updateClientCommand():
            updateClientView(session)

        clientsUpdateButton = Button(self.window, text="Update", command=updateClientCommand)

        clientsUpdateButton.pack(in_=clientsContainer, side="right")

        def getClientCommand():
            getClientView(session)

        clientsReadButton = Button(self.window, text="Read", command=getClientCommand)

        clientsReadButton.pack(in_=clientsContainer, side="right")

        def createClientCommand():
            createClientView(session)

        clientsCreateButton = Button(self.window, text="Create", command=createClientCommand)

        clientsCreateButton.pack(in_=clientsContainer, side="right")

        #Employee
        
        employeesContainer = Frame(self.window)

        employeesLabel = Label(self.window, text="Employees")

        employeesLabel.pack(in_=employeesContainer, side="left")

        def deleteEmployeeCommand():
            deleteEmployeeView(session)

        employeesDeleteButton = Button(self.window, text="Delete", command=deleteEmployeeCommand)

        employeesDeleteButton.pack(in_=employeesContainer, side="right")

        employeesContainer.pack(side="top", fill="x")

        def updateEmployeeCommand():
            updateEmployeeView(session)

        employeesUpdateButton = Button(self.window, text="Update", command=updateEmployeeCommand)

        employeesUpdateButton.pack(in_=employeesContainer, side="right")

        def getEmployeeCommand():
            getEmployeeView(session)

        employeesReadButton = Button(self.window, text="Read", command=getEmployeeCommand)

        employeesReadButton.pack(in_=employeesContainer, side="right")

        def createEmployeeCommand():
            createEmployeeView(session)

        employeesCreateButton = Button(self.window, text="Create", command=createEmployeeCommand)

        employeesCreateButton.pack(in_=employeesContainer, side="right")

        #Rent
        
        rentsContainer = Frame(self.window, background="#5A5A5A")

        rentsLabel = Label(self.window, text="Rents")

        rentsLabel.pack(in_=rentsContainer, side="left")

        def deleteRentCommand():
            deleteRentView(session)

        rentsDeleteButton = Button(self.window, text="Delete", command=deleteRentCommand)

        rentsDeleteButton.pack(in_=rentsContainer, side="right")

        rentsContainer.pack(side="top", fill="x")

        def updateRentCommand():
            updateRentView(session)

        rentsUpdateButton = Button(self.window, text="Update", command=updateRentCommand)

        rentsUpdateButton.pack(in_=rentsContainer, side="right")

        def getRentCommand():
            getRentView(session)

        rentsReadButton = Button(self.window, text="Read", command=getRentCommand)

        rentsReadButton.pack(in_=rentsContainer, side="right")

        def createRentCommand():
            createRentView(session)

        rentsCreateButton = Button(self.window, text="Create", command=createRentCommand)

        rentsCreateButton.pack(in_=rentsContainer, side="right")

        self.window.mainloop()