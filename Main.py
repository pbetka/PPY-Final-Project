from Models import *
from Seed import *
from CRUD import *
from ViewBook import *
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, registry, Mapped, mapped_column, relationship
from datetime import date
import random
from datetime import date, timedelta
from tkinter import *

DB_URL = "sqlite:///library.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
connection = engine.connect()

metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

print(getBooks(session))

if getBooks(session) == None and getAuthors(session) == None and getClients(session) == None and getCopies(session) == None and getEmployees(session) == None and getRents(session) == None:
    seedDB(session)

window = Tk()

labelBooks = Label(window, text="Books")

labelBooks.pack()

booksCreateButton = Button(window, text="Create", command=bookCreateButtonCommand)

booksCreateButton.pack()

def processBookGetButtonCommand():
    bookGetButtonCommand(session)

booksReadButton = Button(window, text="Read", command=processBookGetButtonCommand)

booksReadButton.pack()


window.mainloop()