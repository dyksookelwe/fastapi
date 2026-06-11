from fastapi import APIRouter, HTTPException, Depends
from app.database import SessionLocal, get_db
from app.models import Book, Author
from app.schemas import BookCreate, BookUpdate, BookResponse
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/", response_model=list[BookResponse], status_code=200)
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
    

@router.get("/{book_id}", response_model=BookResponse, status_code=200)
def get_book(book_id: int, db: Session = Depends(get_db)):
        book = db.query(Book).where(Book.id == book_id).first()
        if (book is None):
            raise HTTPException(
                status_code = 404,
                detail="Book not found"
            )
        return book

@router.post("/", response_model=BookResponse, status_code=201)
def post_book(book_info: BookCreate, db: Session = Depends(get_db)):
        existing_book = (
            db.query(Book).where(Book.title == book_info.title, Book.author_id == book_info.author_id).first()
        )
        if existing_book is not None:
            raise HTTPException(
                status_code = 409,
                detail = "Book already exists"
            )
        author = db.query(Author).where(Author.id == book_info.author_id).first()
        if author is None:
            raise HTTPException(
                status_code = 404,
                detail = "Author is not found"
            )

        new_book = Book(
            title = book_info.title,
            author_id = book_info.author_id,
            year = book_info.year
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

@router.patch("/{book_id}", response_model=BookResponse, status_code=200)
def update_book(book_id: int,book_data: BookUpdate,db: Session = Depends(get_db)):
    temp_book = db.query(Book).where(Book.id == book_id).first()
    if temp_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book is not found"
        )
    if (book_data.author_id):
        raise HTTPException(
            status_code=404,
            detail="Author is not found"
        )
    update_data = book_data.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(temp_book,key,value)
    db.commit()
    db.refresh(temp_book)
    return temp_book
    
    
    

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).where(Book.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book is not found"
        )
    db.delete(book)
    db.commit()
    return