from fastapi import FastAPI
from app.database import init_db
from app.routers import books as books_router, authors as authors_router

app = FastAPI()

init_db()

app.include_router(books_router)
app.include_router(authors_router)
