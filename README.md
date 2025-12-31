Enterprise-Grade URL Shortener Service (GDPR Compliant)

This is a professional, high-performance URL shortener service built with Python, FastAPI, and PostgreSQL. It features a "Right to be Forgotten" implementation to comply with GDPR data privacy standards.

Features

Create Short URLs: Convert long URLs into unique 7-character short keys.

Privacy First (GDPR): Every created URL generates a private secret_key. This key allows users to manage or delete their data without needing a full account system.

Secure Deletion: A dedicated DELETE endpoint for the "Right to be Forgotten," physically removing data from the database.

Strict Validation: Uses Pydantic Field for robust data integrity and auto-generated documentation.

Async Architecture: Fully asynchronous stack using FastAPI, SQLAlchemy 2.0, and asyncpg.

Click Tracking: Real-time analytics for every shortened link.

Tech Stack

Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy 2.0 (Async)

Validation: Pydantic v2

Server: Uvicorn

Project Setup & Installation

1. Clone & Environment

git clone https://github.com/JojoBaPb/url-shortener.git
cd url-shortener
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


2. Database & Environment Variables

Ensure PostgreSQL is running and create your database. Then, create a .env file:

DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/url_shortener_db"


3. Run the App

uvicorn main:app --reload


Access the interactive docs at: http://127.0.0.1:8000/docs

API Endpoints

1. Create URL (POST /create)

Generates a short link. Save the secret_key returned in the response; it is the only time it will be shown.

Request: {"target_url": "https://example.com"}

Returns: key and secret_key.

2. Redirect (GET /{short_key})

Redirects to the target URL and increments the click counter.

3. Statistics (GET /stats/{secret_key})

Retrieves click counts and metadata. Requires the private secret_key for access.

4. Delete / Right to be Forgotten (DELETE /admin/{secret_key})

Permanently removes the URL and all associated data from the system.

Returns: 204 No Content on success.

Project Structure

main.py: API Routing and FastAPI configuration.

models.py: SQLAlchemy database models.

schemas.py: Pydantic data schemas and validation.

crud.py: Create, Read, Update, and Delete logic.

keygen.py: Unique string generation utilities.

database.py: Database engine and session management.
