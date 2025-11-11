# 🚀 Python URL Shortener Service

A **complete,  high-performance URL shortener** built from scratch using **Python**, **FastAPI**, and **PostgreSQL**.  
Optimized for **speed**, **asynchronous execution**, and **scalability**.

---

## ✨ Features

- 🔗 **Create Short URLs:** Convert any long URL into a unique 7-character short key.  
- ⚡ **Fast Redirects:** Handles short URL redirects using HTTP `307 Temporary Redirect`.  
- 📈 **Click Tracking:** Automatically counts how many times each short URL is accessed.  
- 📊 **Stats Endpoint:** Check click counts and target URLs for any short key.  
- 🧵 **Async First:** Powered by `asyncio`, `FastAPI`, `SQLAlchemy (async)`, and `asyncpg`.  
- ✅ **Data Validation:** Uses **Pydantic** for reliable request & response validation.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy 2.0 (Async) |
| **Database Driver** | asyncpg |
| **Data Validation** | Pydantic |
| **Configuration** | Pydantic-Settings |
| **Server** | Uvicorn |

---

## ⚙️ Project Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/JojoBaPb/url-shortener.git
cd url-shortener
```

---

### 2️⃣ Create and Activate a Virtual Environment
```bash
# Create venv
python3 -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
.\env\Scripts\activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up PostgreSQL Database

Ensure PostgreSQL is running:

```bash
# On WSL (Ubuntu)
sudo service postgresql start

# On other Linux systems
sudo systemctl start postgresql
```

Set a password for the default user:
```bash
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'mysecretpassword';"
```

Create a database:
```bash
sudo -u postgres createdb url_shortener_db
```

---

### 5️⃣ Create Your `.env` File

Create a `.env` file in the project root with the following:
```bash
DATABASE_URL="postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/url_shortener_db"
```

---

## ▶️ How to Run the Application

Run the FastAPI server:
```bash
uvicorn main:app --reload
```

**Explanation:**
- `main` → The file `main.py`  
- `app` → The `FastAPI()` instance  
- `--reload` → Auto-restarts on file changes (for development)

Once running:
- 🌐 **App:** http://127.0.0.1:8000  
- 📘 **Docs (Swagger UI):** http://127.0.0.1:8000/docs  

---

## 🔌 API Endpoints

### 1. `GET /`
**Description:** Health check endpoint.  
**Response:**
```json
{"message": "URL Shortener is running!"}
```

---

### 2. `POST /create`
**Description:** Creates a new short URL.  
**Request Body:**
```json
{
  "target_url": "https://www.your-long-url.com/goes/here"
}
```

**Success Response (200):**
```json
{
  "target_url": "https://www.your-long-url.com/goes/here",
  "is_active": true,
  "clicks": 0,
  "key": "aBc123X"
}
```

---

### 3. `GET /{short_key}`
**Description:** Redirects to the target URL and increments click count.  
**Example Request:**  
`GET http://127.0.0.1:8000/aBc123X`

**Success Response (307):** Temporary Redirect to the target URL.  
**Error (404):**
```json
{"detail": "URL with key 'aBc123X' not found."}
```

---

### 4. `GET /stats/{short_key}`
**Description:** Retrieve click stats and target info.  
**Example Request:**  
`GET http://127.0.0.1:8000/stats/aBc123X`

**Success Response (200):**
```json
{
  "target_url": "https://www.your-long-url.com/goes/here",
  "is_active": true,
  "clicks": 5,
  "key": "aBc123X"
}
```

**Error (404):**
```json
{"detail": "URL with key 'aBc123X' not found."}
```

---

## 🧠 Summary

This project demonstrates how to build a **production-ready**, **asynchronous FastAPI service** with clean architecture, database integration, and real-time analytics — ideal for learning and deployment in modern Python backends.
