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
    return books

# Update
def updateBook(session, id_book, name, id_author):
    book = session.query(Book).filter_by(id_book=id_book).first()
    if book == None:
        return -1
    author = session.query(Author).filter_by(id_author=id_author).first()
    book.name = name
    book.id_author = id_author
    book.author = author
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
    return authors

# Update
def updateAuthor(session, id_author, first_name, last_name):
    author = session.query(Author).filter_by(id_author=id_author).first()
    if author == None:
        return -1
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
    book = session.query(Book).filter_by(id_book=id_book).first()
    copy = Copy(id_copy=id_copy, id_book=id_book, book=book)
    session.add(copy)
    session.commit()

# Read
def getCopies(session):
    copies = session.query(Copy).all()
    return copies

# Update
def updateCopy(session, id_copy, id_book):
    copy = session.query(Copy).filter_by(id_copy=id_copy).first()
    if copy == None:
        return -1
    book = session.query(Book).filter_by(id_book=id_book).first()
    copy.id_book = id_book
    copy.book = book
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
    return employees

# Update
def updateEmployee(session, id_employee, first_name, last_name, salary):
    employee = session.query(Employee).filter_by(id_employee=id_employee).first()
    if employee == None:
        return -1
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
def getClients(session):
    clients = session.query(Client).all()
    return clients

# Update
def updateClient(session, id_client, first_name, last_name, phone_number):
    client = session.query(Client).filter_by(id_client=id_client).first()
    if client == None:
        return -1
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
def createRent(session, id_rent, id_client, rent_date, due_date, given_back, id_employee, id_copy):
    client = session.query(Client).filter_by(id_client=id_client).first()
    employee = session.query(Employee).filter_by(id_employee=id_employee).first()
    copy = session.query(Copy).filter_by(id_copy=id_copy).first()
    rent = Rent(
        id_rent=id_rent,
        id_client=id_client,
        client=client,
        rent_date=rent_date,
        due_date=due_date,
        given_back=given_back,
        id_employee=id_employee,
        employee=employee,
        id_copy=id_copy,
        copy=copy
    )
    session.add(rent)
    session.commit()

# Read
def getRents(session, ):
    rents = session.query(Rent).all()
    return rents

# Update
def updateRent(session, id_rent, id_client, rent_date, due_date, given_back, id_employee, id_copy):
    rent = session.query(Rent).filter_by(id_rent=id_rent).first()
    if rent == None:
        return -1
    client = session.query(Client).filter_by(id_client=id_client).first()
    employee = session.query(Employee).filter_by(id_employee=id_employee).first()
    copy = session.query(Copy).filter_by(id_copy=id_copy).first()
    rent.id_client = id_client
    rent.client = client
    rent.id_copy = id_copy
    rent.copy = copy
    rent.rent_date = rent_date
    rent.due_date = due_date
    rent.given_back = given_back
    rent.id_employee = id_employee
    rent.employee = employee
    session.commit()

# Delete
def deleteRent(session, id_rent):
    rent = session.query(Rent).filter_by(id_rent=id_rent).first()
    session.delete(rent)
    session.commit()