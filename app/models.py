from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, relationships
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    title: Mapped[str] = mapped_column(
        String(200)
    )
    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("authors.id")
    )
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("category.id")
    )
    year: Mapped[int] = mapped_column(
        Integer
    )
    author = relationship(
        "Author",
        back_populates="books"
    )
    category = relationship(
        "Category",
        back_populates="books"
    )

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(200)
    )
    books = relationship(
        "Book",
        back_populates = "author"
    )

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(200)
    )
    books = relationship(
        "Book",
        back_populates="category"
    )