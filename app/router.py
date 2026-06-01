from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Book
from app.fake_db import books_db
from app.schemas import BookCreate, BookUpdate, BookResponse
from datetime import datetime

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/db-test")
def db_test():
    db = SessionLocal()

    try:
        books = db.query(Book).all()
        return books
    finally:
        db.close()

@router.get("/", response_model=list[BookResponse], status_code=200)
def get_books(author: str | None = None, year: int | None = None, search: str | None = None, sort: str | None = None, skip: int = 0, limit: int = 10):
    result = books_db
    if author:
        result = [
            book 
            for book in result
            if book["author"] == author
        ]
    if year:
        result = [
            book
            for book in result
            if book["year"] == year
        ]
    if search:
        result = [
            book 
            for book in result
            if search.lower() in book["title"].lower()
        ]
    if sort == "title":
        result = sorted(
            result,
            key=lambda book: book["title"]
        )
    if sort == "year":
        result = sorted(
            result,
            key = lambda book: book["year"]
        )
    result = result[skip:skip+limit]
    return result

@router.get("/{book_id}", response_model=BookResponse, status_code=200)
def get_book(book_id: int):
    for temp in books_db:
        if temp["id"] == book_id:
            return temp
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

@router.post("/", response_model=BookResponse, status_code=201)
def post_book(book_info: BookCreate):
    for book in books_db:
        if(
            book["title"] == book_info.title
            and book["author"] == book_info.author
            and book["year"] == book_info.year
        ):
            raise HTTPException(
                status_code=409,
                detail="Book already exists"
                )
    new_book = {
        "id": len(books_db) + 1,
        "title": book_info.title,
        "author": book_info.author,
        "year": book_info.year,
        "created_at": datetime.now()
    }
    books_db.append(new_book)
    return new_book

@router.patch("/{book_id}", response_model=BookResponse, status_code=200)
def update_book(book_id: int,book: BookUpdate):
    for temp in books_db:
        if temp["id"] == book_id:
            update_data = book.model_dump(exclude_unset = True)
            temp.update(update_data)
            return temp
    raise HTTPException(
        status_code = 404,
        detail = "Book Not Found"
    )

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    for temp in books_db:
        if temp["id"] == book_id:
            books_db.remove(temp)
            return None
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )