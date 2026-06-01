from fastapi import FastAPI
from app.models import Book
from app.router import router as books_router

app = FastAPI()

app.include_router(books_router)
