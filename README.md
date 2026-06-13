# Books API

A learning backend built with FastAPI. The project is focused on practicing backend fundamentals: routing, validation, SQLAlchemy models, PostgreSQL, and basic Alembic usage.

## Last README baseline

`README.md` was last changed in git on `2026-06-04 02:15:30 +0200` in commit `65af988`.

Since that point, the project gained:

- separate routers for books, authors, and categories
- SQLAlchemy relationships between books, authors, and categories
- richer nested response schemas
- Alembic configuration and migration files
- migration practice files for `books.rating` and `category.description`
- editor config files for spelling and type-checking

## Current features

- PostgreSQL-backed API using `DATABASE_URL` from `.env`
- CRUD for books at `/books`
- CRUD for authors at `/authors`
- CRUD for categories at `/category`
- nested related data in book, author, and category responses
- SQLAlchemy 2 models with relationships
- Alembic configured to read metadata from `Base.metadata`

## Tech stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic v2
- SQLAlchemy 2
- PostgreSQL
- Alembic
- python-dotenv

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

Copy `.env.example` to `.env` and set a real PostgreSQL connection string:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/library_db
```

### 4. Run the app

```bash
uvicorn app.main:app --reload
```

Swagger UI: `http://127.0.0.1:8000/docs`

## Database notes

The app still calls `init_db()` on startup, so tables can be created automatically from SQLAlchemy models.

Alembic is also configured and reads metadata from `Base.metadata` in `alembic/env.py`. That allows migration autogeneration from your ORM models.

Useful commands:

```bash
alembic revision --autogenerate -m "describe_change"
alembic upgrade head
```

## API overview

### Books

| Method | Path | Description |
|--------|------|-------------|
| GET | `/books/` | List all books |
| GET | `/books/{book_id}` | Get one book |
| POST | `/books/` | Create a book |
| PATCH | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

### Authors

| Method | Path | Description |
|--------|------|-------------|
| GET | `/authors/` | List all authors |
| GET | `/authors/{author_id}` | Get one author with books |
| GET | `/authors/{author_id}/books` | Get only that author's books |
| POST | `/authors/` | Create an author |
| PATCH | `/authors/{author_id}` | Update an author |
| DELETE | `/authors/{author_id}` | Delete an author |

### Categories

| Method | Path | Description |
|--------|------|-------------|
| GET | `/category/` | List all categories |
| GET | `/category/{category_id}` | Get one category with books |
| POST | `/category/` | Create a category |
| PATCH | `/category/{category_id}` | Update a category |
| DELETE | `/category/{category_id}` | Delete a category |

## Project structure

```text
app/
|-- main.py
|-- database.py
|-- models.py
|-- schemas.py
`-- routers/
    |-- authors.py
    |-- books.py
    `-- category.py
alembic/
|-- env.py
`-- versions/
alembic.ini
.env.example
requirements.txt
```

## Notes for learning

- `alembic.ini` stores configuration values.
- `alembic/env.py` contains Python logic for Alembic.
- `target_metadata` is configured in `alembic/env.py`, not in `alembic.ini`.

## Roadmap

- [x] PostgreSQL + SQLAlchemy
- [x] Routers for books, authors, and categories
- [x] Basic Alembic setup
- [ ] Clean up migration history and rely on migrations instead of `init_db()`
- [ ] List filters and pagination
- [ ] User authentication
- [ ] Frontend
