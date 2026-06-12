from fastapi import FastAPI
from app.database import init_db
from app.routers.books import router as books_router
from app.routers.authors import router as authors_router
from app.routers.category import router as category_router

app = FastAPI()

init_db()

app.include_router(books_router)
app.include_router(authors_router)
app.include_router(category_router)