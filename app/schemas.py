from pydantic import BaseModel, Field
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str
    year: int = Field(..., ge=0, le=2100)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = Field(None, ge=0,le=2100)

class BookResponse(BookBase):
    id: int
    created_at: datetime | None = None
    model_config = {"from_attributes": True}