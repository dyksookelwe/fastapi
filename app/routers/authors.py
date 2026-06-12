from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Author
from app.schemas import AuthorCreate, AuthorResponse, AuthorWithBooksResponse, BookShortResponse, AuthorUpdate

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
            status_code=404,
            detail="Author not found"
        )
    return author


@router.get("/{author_id}/books", response_model=list[BookShortResponse], status_code=200)
def get_author_books(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )
    if not author.books:
        raise HTTPException(
            status_code=404,
            detail="Author has no books"
        )
    return author.books


@router.post("/", response_model=AuthorResponse, status_code=201)
def post_author(author_info: AuthorCreate, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.name == author_info.name).first()
    if author is not None:
        raise HTTPException(
            status_code=409,
            detail="Author already exists"
        )

    new_author = Author(
        name=author_info.name
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.patch("/{author_id}", response_model=AuthorResponse, status_code=200)
def update_author(author_id: int, author_data: AuthorUpdate, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )
    update_author = author_data.model_dump(exclude_unset=True)
    for key, value in update_author.items():
        setattr(author, key, value)
    db.commit()
    db.refresh(author)
    return author


@router.delete("/{author_id}", status_code=204)
def del_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).where(Author.id == author_id).first()
    if author is None:
        raise HTTPException(
            status_code=404,
            detail="Author does not exist"
        )
    if author.books:
        raise HTTPException(
            status_code=400,
            detail="Author has books, delete them first"
        )
    db.delete(author)
    db.commit()
    return
