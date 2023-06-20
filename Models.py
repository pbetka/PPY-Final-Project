from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import registry, Mapped, mapped_column, relationship
from datetime import date

# Models for all table

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

# Author

@mapper_registry.mapped_as_dataclass
class Author:
    __tablename__ = "author"

    id_author: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(
        back_populates="author", default_factory=lambda: []
    )

# Book

@mapper_registry.mapped_as_dataclass
class Book:
    __tablename__ = "book"

    id_book: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int]
    id_author: Mapped[int] = mapped_column(ForeignKey("author.id_author"))
    author: Mapped[Author] = relationship(back_populates="books")
    copies: Mapped[list["Copy"]] = relationship(
        back_populates="book", default_factory=lambda: []
    )

# Copy

@mapper_registry.mapped_as_dataclass
class Copy:
    __tablename__ = "copy"

    id_copy: Mapped[int] = mapped_column(primary_key=True)
    id_book: Mapped[int] = mapped_column(ForeignKey("book.id_book"))
    book: Mapped[Book] = relationship(back_populates="copies")
    rents: Mapped[list["Rent"]] = relationship(
        back_populates="copy", default_factory=lambda: []
    )

# Employee

@mapper_registry.mapped_as_dataclass
class Employee:
    __tablename__ = "employee"

    id_employee: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    salary: Mapped[int]
    rents: Mapped[list["Rent"]] = relationship(
        back_populates="employee", default_factory=lambda: []
    )

# Client

@mapper_registry.mapped_as_dataclass
class Client:
    __tablename__ = "client"

    id_client: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    rents: Mapped[list["Rent"]] = relationship(
        back_populates="client", default_factory=lambda: []
    )

# Rent

@mapper_registry.mapped_as_dataclass
class Rent:
    __tablename__ = "rent"

    id_rent: Mapped[int] = mapped_column(primary_key=True)
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
    client: Mapped[Client] = relationship(back_populates="rents")
    rent_date: Mapped[date]
    due_date: Mapped[date]
    given_back: Mapped[bool]
    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"))
    employee: Mapped[Employee] = relationship(back_populates="rents")
    id_copy: Mapped[int] = mapped_column(ForeignKey("copy.id_copy"))
    copy: Mapped[Copy] = relationship(back_populates="rents")
