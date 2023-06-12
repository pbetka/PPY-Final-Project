from tkinter import *
from ViewBook import *
from ViewAuthor import *

class Window:
    def __init__(self, session):
        self.window = Tk()

        self.window.geometry("300x200")
        
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

        self.window.mainloop()