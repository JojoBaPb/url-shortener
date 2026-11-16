<h1 align="center">🚀 URL Shortener</h1>

A URL shortening service built with FastAPI, SQLAlchemy 2.0 and PostgreSQL (or SQLite for local
development). Every link comes with a private `secret_key` that lets its owner see stats or
permanently delete the link (right to be forgotten).

> Work in progress: this README is updated at each upgrade stage.

---

## 📦 Quick Start (Docker)

```bash
docker compose up --build
```

This starts PostgreSQL and the app, runs the database migrations, and serves the API on
http://localhost:8000. Interactive docs: http://localhost:8000/docs

## ⚙️ Manual Installation

```bash
python -m venv venv
# Windows:            venv\Scripts\activate
# Linux/macOS/Termux: source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env          # optional: the defaults already work
alembic upgrade head          # create or update the database tables
uvicorn app.main:app --reload
```

## 🗄 Database Migrations

The database schema is managed with [Alembic](https://alembic.sqlalchemy.org/).

```bash
alembic upgrade head                                 # apply all migrations
alembic revision --autogenerate -m "describe change" # after changing app/models.py
alembic downgrade -1                                 # undo the last migration
```

Already running a database created by the old version of this app? Tell Alembic the table
already exists instead of creating it again: `alembic stamp 0001`.

## 🧪 Run the Tests

```bash
pytest
```

Tests use a temporary SQLite database, so no setup is needed.

## 📡 API

| Method | Path | What it does |
|---|---|---|
| POST | `/create` | Shorten a URL. Returns the short `key` and the private `secret_key`. |
| GET | `/{key}` | Redirects to the original URL and counts the click. |
| GET | `/stats/{secret_key}` | Shows click count and status. |
| DELETE | `/admin/{secret_key}` | Permanently deletes the link. |

## 🛠 Tech Stack

FastAPI · SQLAlchemy 2.0 (async) · Alembic · Pydantic v2 · PostgreSQL 16 / SQLite · Docker
