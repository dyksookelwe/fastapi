from pydantic import BaseModel, Field
from datetime import datetime

class AuthorResponse(BaseModel):
    id: int
    name: str
    
    model_config = {"from_attributes": True}

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author_id: int
    year: int = Field(..., ge=0, le=2100)

class BookUpdate(BaseModel):
    title: str | None = None
    author_id: int | None = None 
    year: int | None = Field(None, ge=0,le=2100)

class BookResponse(BaseModel):
    id: int
    title: str
    year: int
    created_at: datetime | None = None
    author: AuthorResponse
    model_config = {"from_attributes": True}

class BookShortResponse(BaseModel):
    id: int
    title: str = Field(..., min_length=1 , max_length=200)

class AuthorWithBooksResponse(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=200)
    books: list[BookShortResponse]

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)

class CategoryResponse(BaseModel):
    id:int
    name: str

class CategoryWithBooks(CategoryResponse):
    books = list[BookShortResponse]

class CategoryUpdate(BaseModel):
    name: str | None = None



