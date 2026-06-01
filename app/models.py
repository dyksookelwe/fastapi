from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
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
    author: Mapped[str] = mapped_column(
        String(100)
    )
    year: Mapped[int] = mapped_column(
        Integer
    )