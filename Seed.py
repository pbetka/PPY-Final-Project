from Models import Author, Book, Employee, Client, Rent, Copy
from datetime import date, timedelta
from random import random

def seedDB(session):
    # Seed Authors
    a = Author(id_author=1, first_name="J.R.R.", last_name="Tolkien")

    session.add(a)

    # Seed Books
    b1 = Book(id_book=1, name="Lord of the Rings: The Fellowship of the Ring", id_author=a.id_author, author=a)
    b2 = Book(id_book=2, name="Lord of the Rings: The Two Towers", id_author=a.id_author, author=a)
    b3 = Book(id_book=3, name="Lord of the Rings: The Return of the King", id_author=a.id_author, author=a)

    session.add_all([b1, b2, b3])

    # Seed Copies
    for book in [b1, b2]:
        for i in range(5):
            copy = Copy(id_copy=(book.id_book * 10) + i, id_book=book.id_book, book=book)
            session.add(copy)

    # Seed Employees
    for i in range(5):
        employee = Employee(
            id_employee=i+1,
            first_name=f"Employee{i+1}",
            last_name="Smith",
            salary=random.randint(2000, 5000)
        )
        session.add(employee)

    # Seed Clients
    for i in range(10):
        client = Client(
            id_client=i+1,
            first_name=f"Client{i+1}",
            last_name="Doe",
            phone_number="867652743"
        )
        session.add(client)

    session.commit()

    # Seed Rents
    copies = session.query(Copy).all()
    employees = session.query(Employee).all()
    clients = session.query(Client).all()
    for i in range(10):
        copy = random.choice(copies)
        employee = random.choice(employees)
        client = random.choice(clients)
        rent_date = date.today() - timedelta(days=random.randint(1, 30))
        due_date = rent_date + timedelta(days=random.randint(7, 30))
        given_back = random.choice([True, False])

        rent = Rent(
            id_rent=i+1,
            id_client=client.id_client,
            client=client,
            rent_date=rent_date,
            due_date=due_date,
            given_back=given_back,
            id_employee=employee.id_employee,
            employee=employee,
            id_copy=copy.id_copy,
            copy=copy
        )
        session.add(rent)

    session.commit()

    for x in [a, b1, b2, b3]:
        session.refresh(x)