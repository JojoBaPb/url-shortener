🚀 Python URL Shortener Service

A complete, high-performance URL shortener built from scratch using Python, FastAPI, and PostgreSQL.
Optimized for speed, asynchronous execution, and scalability.

✨ Features

🔗 Create Short URLs: Convert any long URL into a unique 7-character short key.

⚡ Fast Redirects: Handles short URL redirects using HTTP 307 Temporary Redirect.

📈 Click Tracking: Automatically counts how many times each short URL is accessed.

📊 Stats Endpoint: Check click counts and target URLs for any short key.

🧵 Async First: Powered by asyncio, FastAPI, SQLAlchemy (async), and asyncpg.

✅ Data Validation: Uses Pydantic for reliable request & response validation.

🧰 Tech Stack
Component	Technology
Framework	FastAPI
Database	PostgreSQL
ORM	SQLAlchemy 2.0 (Async)
Database Driver	asyncpg
Data Validation	Pydantic
Configuration	Pydantic-Settings
Server	Uvicorn
