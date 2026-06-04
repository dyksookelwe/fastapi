# Books API

A learning backend built with FastAPI. The goal here is to learn how to **design** APIs — not just accept and return JSON. The project is still in active development: the code and architecture will keep changing, and that's expected.

**End goal:** a full web app for managing a personal book collection, with search, filtering, and AI-powered analysis tools.

## What's implemented

- REST CRUD for books (`/books`) backed by **PostgreSQL**
- SQLAlchemy ORM model (`Book`) and session dependency (`get_db`)
- Pydantic schemas: `BookCreate`, `BookUpdate`, `BookResponse`
- Environment-based config via `.env` (passwords stay out of git)
- HTTP status codes: 201, 204, 404, 409

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic v2
- SQLAlchemy 2
- PostgreSQL
- python-dotenv

## Getting started

### 1. PostgreSQL

Create a database (e.g. `library_db`) and note your user/password.

### 2. Environment

```bash
cp .env.example .env
```

Edit `.env` and set a real `DATABASE_URL`, for example:

```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/library_db
```

### 3. Install and run

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: http://127.0.0.1:8000/docs

Tables are created automatically on startup (`init_db`).

## Project structure

```
app/
├── main.py       # FastAPI entry point
├── router.py     # /books endpoints
├── schemas.py    # request and response models
├── models.py     # SQLAlchemy Book model
└── database.py   # engine, SessionLocal, get_db
.env.example      # env template (commit this, not .env)
```

## API overview

| Method | Path | Description |
|--------|------|-------------|
| GET | `/books` | List all books |
| GET | `/books/{id}` | Get one book |
| POST | `/books` | Create a book |
| PATCH | `/books/{id}` | Partial update |
| DELETE | `/books/{id}` | Delete (204) |

## Roadmap

- [x] PostgreSQL + SQLAlchemy
- [ ] Alembic migrations
- [ ] List filters and pagination (`author`, `search`, `skip`, `limit`)
- [ ] User authentication
- [ ] Frontend
- [ ] AI-powered search and analytics

---

*Work in progress — feel free to look around or fork, but don't expect production-ready behavior just yet.*
