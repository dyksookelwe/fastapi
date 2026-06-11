from fastapi import APIRouter, HTTPException, Depends
from app.database import SessionLocal, get_db
from app.models import Author
from app.schemas import AuthorCreate, AuthorResponse, AuthorWithBooksResponse, BookShortResponse
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/", response_model=list[AuthorResponse], status_code=200)
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

@router.get("/{author_id}", response_model=AuthorWithBooksResponse, status_code=200)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
                status_code = 404,
                detail="Author not found"
        )
    return author

@router.get("/{author_id}/books", response_model=list[BookShortResponse], status_code=200)
def get_author_books(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
                status_code = 404,
                detail="Author not found"
        )
    if author.books is None:
        raise HTTPException(
            status_code=400,
            detail="Author has books"
        )
    return author.books

@router.post("/", response_model=AuthorResponse, status_code=201)
def post_author(author_info: AuthorCreate,db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.name == author_info.name).first()
    if author is not None:
        raise HTTPException(
                status_code = 409,
                detail="Author already exists"
            )
    
    new_author = Author(
        name = author_info.name
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.delete("/{author_id}", status_code=204)
def del_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
                status_code = 404,
                detail="Author does not exist"
            )
    if author.books:
        raise HTTPException(
            status_code=400,
            detail="Author has books"
        )
    return {"message": "success"}
    