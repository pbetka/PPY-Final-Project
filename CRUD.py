from Models import Book, Author, Employee, Client, Copy, Rent

# Book

# Create
def createBook(session, id_book, name, id_author):
    author = session.query(Author).filter_by(id_author=id_author).first()
    book = Book(id_book=id_book, name=name, id_author=id_author, author=author)
    session.add(book)
    session.commit()

# Read
def getBooks(session):
    books = session.query(Book).all()
    for book in books:
        print(book.id_book, book.name, book.id_author)
    return books

# Update
def updateBook(session, id_book, name, id_author):
    book = session.query(Book).filter_by(id_book=id_book).first()
    book.name = name
    book.id_author = id_author
    session.commit()

# Delete
def deleteBook(session, id_book):
    book = session.query(Book).filter_by(id_book=id_book).first()
    session.delete(book)
    session.commit()

# Author

# Create
def createAuthor(session, id_author, first_name, last_name):
    author = Author(id_author=id_author, first_name=first_name, last_name=last_name)
    session.add(author)
    session.commit()

# Read
def getAuthors(session, ):
    authors = session.query(Author).all()
    for author in authors:
        print(author.id_author, author.first_name, author.last_name)
    return authors

# Update
def updateAuthor(session, id_author, first_name, last_name):
    author = session.query(Author).filter_by(id_author=id_author).first()
    author.first_name = first_name
    author.last_name = last_name
    session.commit()

# Delete
def deleteAuthor(session, id_author):
    author = session.query(Author).filter_by(id_author=id_author).first()
    session.delete(author)
    session.commit()

# Copy

# Create
def createCopy(session, id_copy, id_book):
    copy = Copy(id_copy=id_copy, id_book=id_book)
    session.add(copy)
    session.commit()

# Read
def getCopies(session):
    copies = session.query(Copy).all()
    for copy in copies:
        print(copy.id_copy, copy.id_book)
    return copies

# Update
def updateCopy(session, id_copy, id_book):
    copy = session.query(Copy).filter_by(id_copy=id_copy).first()
    copy.id_book = id_book
    session.commit()

# Delete
def deleteCopy(session, id_copy):
    copy = session.query(Copy).filter_by(id_copy=id_copy).first()
    session.delete(copy)
    session.commit()

# Employee

# Create
def createEmployee(session, id_employee, first_name, last_name, salary):
    employee = Employee(id_employee=id_employee, first_name=first_name, last_name=last_name, salary=salary)
    session.add(employee)
    session.commit()

# Read
def getEmployees(session):
    employees = session.query(Employee).all()
    for employee in employees:
        print(employee.id_employee, employee.first_name, employee.last_name, employee.salary)
    return employees

# Update
def updateEmployee(session, id_employee, first_name, last_name, salary):
    employee = session.query(Employee).filter_by(id_employee=id_employee).first()
    employee.first_name = first_name
    employee.last_name = last_name
    employee.salary = salary
    session.commit()

# Delete
def deleteEmployee(session, id_employee):
    employee = session.query(Employee).filter_by(id_employee=id_employee).first()
    session.delete(employee)
    session.commit()

# Client

# Create
def createClient(session, id_client, first_name, last_name, phone_number):
    client = Client(id_client=id_client, first_name=first_name, last_name=last_name, phone_number=phone_number)
    session.add(client)
    session.commit()
# Read
def getClients(session, ):
    clients = session.query(Client).all()
    for client in clients:
        print(client.id_client, client.first_name, client.last_name, client.phone_number)
    return clients

# Update
def updateClient(session, id_client, first_name, last_name, phone_number):
    client = session.query(Client).filter_by(id_client=id_client).first()
    client.first_name = first_name
    client.last_name = last_name
    client.phone_number = phone_number
    session.commit()

# Delete
def deleteClient(session, id_client):
    client = session.query(Client).filter_by(id_client=id_client).first()
    session.delete(client)
    session.commit()

# Rent

# Create
def createRent(session, id_rent, id_client, id_copy, rent_date, due_date, given_back, id_employee):
    rent = Rent(
        id_rent=id_rent,
        id_client=id_client,
        id_copy=id_copy,
        rent_date=rent_date,
        due_date=due_date,
        given_back=given_back,
        id_employee=id_employee
    )
    session.add(rent)
    session.commit()

# Read
def getRents(session, ):
    rents = session.query(Rent).all()
    for rent in rents:
        print(
            rent.id_rent,
            rent.id_client,
            rent.rent_date,
            rent.due_date,
            rent.given_back,
            rent.id_employee,
            rent.id_copy
        )
    return rents

# Update
def updateRent(session, id_rent, id_client, id_copy, rent_date, due_date, given_back, id_employee):
    rent = session.query(Rent).filter_by(id_rent=id_rent).first()
    rent.id_client = id_client
    rent.id_copy = id_copy
    rent.rent_date = rent_date
    rent.due_date = due_date
    given_back = given_back
    id_employee = id_employee

# Delete
def deleteRent(session, id_rent):
    rent = session.query(Rent).filter_by(id_rent=id_rent).first()
    session.delete(rent)
    session.commit()