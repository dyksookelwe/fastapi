# Books API

A learning backend built with FastAPI. The goal here is to learn how to **design** APIs — not just accept and return JSON. The project is still in active development: the code and architecture will keep changing, and that's expected.

**End goal:** a full web app for managing a personal book collection, with search, filtering, and AI-powered analysis tools.

## What's implemented

- REST CRUD for books (`/books`)
- Pydantic schemas: `BookCreate`, `BookUpdate`, `BookResponse`
- List filters and pagination: `author`, `year`, `search`, `sort`, `skip`, `limit`
- In-memory storage (`fake_db.py`) — no real database yet, API design comes first

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic v2

## Getting started

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

## Project structure

```
app/
├── main.py      # FastAPI entry point
├── router.py    # /books endpoints
├── schemas.py   # request and response models
└── fake_db.py   # temporary in-memory storage
```

## Roadmap

- [ ] PostgreSQL + SQLAlchemy
- [ ] User authentication
- [ ] Frontend
- [ ] AI-powered search and analytics

---
