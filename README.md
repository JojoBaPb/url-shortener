<h1 align="center">🚀 URL Shortener</h1>

A URL shortening service built with FastAPI, SQLAlchemy 2.0 and PostgreSQL (or SQLite for local
development). Every link comes with a private `secret_key` that lets its owner see stats or
permanently delete the link (right to be forgotten).

> Work in progress: this README is updated at each upgrade stage.

---

## ⚙️ Run It Locally

```bash
python -m venv venv
# Windows:            venv\Scripts\activate
# Linux/macOS/Termux: source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env          # optional: the defaults already work
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

## 📡 API

| Method | Path | What it does |
|---|---|---|
| POST | `/create` | Shorten a URL. Returns the short `key` and the private `secret_key`. |
| GET | `/{key}` | Redirects to the original URL and counts the click. |
| GET | `/stats/{secret_key}` | Shows click count and status. |
| DELETE | `/admin/{secret_key}` | Permanently deletes the link. |

## 🛠 Tech Stack

FastAPI · SQLAlchemy 2.0 (async) · Pydantic v2 · asyncpg / aiosqlite
