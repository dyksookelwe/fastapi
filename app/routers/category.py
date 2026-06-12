from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Category
from app.schemas import CategoryCreate, CategoryResponse, CategoryWithBooksResponse, CategoryUpdate

router = APIRouter(
    prefix="/category",
    tags=["categories"]
)


@router.get("/", response_model=list[CategoryResponse], status_code=200)
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


@router.get("/{category_id}", response_model=CategoryWithBooksResponse, status_code=200)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).where(Category.id == category_id).first()
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category is not found"
        )
    return category


@router.post("/", response_model=CategoryResponse, status_code=201)
def post_category(category_info: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Category).where(Category.name == category_info.name).first()
    if category is not None:
        raise HTTPException(
            status_code=409,
            detail="Category already exists"
        )
    new_category = Category(
        name=category_info.name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.patch("/{category_id}", response_model=CategoryResponse, status_code=200)
def update_category(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(Category).where(Category.id == category_id).first()
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category is not found"
        )
    update_category = category_data.model_dump(exclude_unset=True)
    for key, value in update_category.items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).where(Category.id == category_id).first()
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category is not found"
        )
    if category.books:
        raise HTTPException(
            status_code=400,
            detail="Category has books, delete them first"
        )
    db.delete(category)
    db.commit()
    return
