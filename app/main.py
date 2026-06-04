from fastapi import FastAPI

from app.database import init_db
from app.router import router as books_router

app = FastAPI()

init_db()

app.include_router(books_router)
