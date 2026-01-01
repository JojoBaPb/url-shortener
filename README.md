<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2165/2165012.png" width="100" alt="URL Shortener Logo" />
</p>

<h1 align="center">🚀 Enterprise URL Shortener (GDPR Compliant)</h1>

<p align="center">
A robust, high-performance, and GDPR-compliant URL shortening service.<br>
Built with a modern asynchronous stack, giving users full control over their data via private management keys.
</p>

---

## 📖 Table of Contents

- [✨ Key Features](#-key-features)
- [🛠 Tech Stack](#-tech-stack)
- [📦 Quick Start (Docker)](#-quick-start-docker)
- [⚙️ Manual Installation](#️-manual-installation)
- [📡 API Documentation](#-api-documentation)
- [⚖️ GDPR Compliance](#️-gdpr-compliance)

---

## ✨ Key Features

- ⚡ **High Performance** – Fully asynchronous I/O using **FastAPI** and **asyncpg**
- ⚖️ **Right to be Forgotten** – Users receive a `secret_key` to permanently delete their records
- 📊 **Real-time Analytics** – Track click counts and activity status
- 🐳 **Containerized** – Production-ready with Docker & Docker Compose
- 📝 **Auto-Docs** – Interactive Swagger UI and Redoc support

---

## 🛠 Tech Stack

| Component        | Technology            |
|------------------|-----------------------|
| Framework        | FastAPI               |
| Database         | PostgreSQL 15         |
| ORM              | SQLAlchemy 2.0        |
| Validation       | Pydantic v2           |
| Async Driver     | asyncpg               |
| Containerization | Docker / Docker Compose |

---

## 📦 Quick Start (Docker)

The fastest way to get started is using **Docker Compose**.

```bash
# Clone the repository
git clone https://github.com/JojoBaPb/url-shortener.git
cd url-shortener

# Spin up the containers
docker-compose up --build
