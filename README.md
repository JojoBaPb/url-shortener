<p align="center">
<img src="https://www.google.com/search?q=https://cdn-icons-png.flaticon.com/512/2165/2165012.png" width="100" alt="URL Shortener Logo" />
</p>

🚀 Enterprise URL Shortener (GDPR Compliant)

A robust, high-performance, and GDPR-compliant URL shortening service. Built with a modern asynchronous stack, it provides users with full control over their data via private management keys.

📖 Table of Contents

✨ Key Features

🛠 Tech Stack

📦 Quick Start (Docker)

⚙️ Manual Installation

📡 API Documentation

⚖️ GDPR Compliance

✨ Key Features

⚡ High Performance: Fully asynchronous I/O using FastAPI and asyncpg.

⚖️ Right to be Forgotten: Users receive a secret_key to permanently delete their records.

📊 Real-time Analytics: Track click counts and activity status.

🐳 Containerized: Ready for production with Docker and Docker Compose.

📝 Auto-Docs: Interactive Swagger UI and Redocly integration.

🛠 Tech Stack

Component

Technology

Framework

FastAPI

Database

PostgreSQL 15

ORM

SQLAlchemy 2.0

Validation

Pydantic v2

Containerization

Docker

📦 Quick Start (Docker)

The fastest way to get started is using Docker Compose.

# Clone the repository
git clone [https://github.com/YOUR_GITHUB_USERNAME/url-shortener.git](https://github.com/YOUR_GITHUB_USERNAME/url-shortener.git)
cd url-shortener

# Spin up the containers
docker-compose up --build


Your app will be live at http://localhost:8000 and the database will be handled automatically.

⚙️ Manual Installation

If you prefer to run locally without Docker:

Environment Setup

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Configuration
Create a .env file in the root:

DATABASE_URL="postgresql+asyncpg://postgres:yourpassword@localhost:5432/url_shortener_db"


Run Service

uvicorn main:app --reload


📡 API Documentation

Once the server is running, explore the interactive documentation:

Swagger UI: http://localhost:8000/docs

ReDocs: http://localhost:8000/redoc

Core Endpoints

Method

Endpoint

Description

POST

/create

Shorten a URL (returns key & secret_key)

GET

/{key}

Redirect to target URL

GET

/stats/{secret_key}

View click statistics

DELETE

/admin/{secret_key}

Right to be Forgotten (Permanently delete data)

⚖️ GDPR Compliance

This service is designed with Privacy by Design principles:

No PII Collection: We do not collect emails or IP addresses by default.

Data Portability: Users can view their data using the secret_key.

Right to Erasure: Users can instantly and permanently delete their shortened URLs and associated metrics via the /admin endpoint.

<p align="center">
Developed with ❤️ by <a href="https://www.google.com/search?q=https://github.com/YOUR_GITHUB_USERNAME">YOUR_NAME</a>
</p>
