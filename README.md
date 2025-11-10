Python URL Shortener Service

This is a complete, high-performance URL shortener service built from scratch using Python, FastAPI, and PostgreSQL. It's built to be fast, asynchronous, and scalable.

Features

Create Short URLs: Convert any long URL into a unique, 7-character short key.

Fast Redirects: Handles short URL redirects with a 307 Temporary Redirect.

Click Tracking: Automatically counts the number of clicks each short URL receives.

Stats Endpoint: A separate endpoint to check the click count and target URL for any short key.

Async First: Built with asyncio, FastAPI, SQLAlchemy (async), and asyncpg for high concurrency.

Data Validation: Uses Pydantic for robust request and response data validation.

Tech Stack

Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy 2.0 (with async support)

Database Driver: asyncpg

Data Validation: Pydantic

Configuration: Pydantic-Settings

Server: Uvicorn

Project Setup & Installation

1. Clone the Repository

git clone [https://github.com/JojoBaPb/url-shortener.git](https://github.com/JojoBaPb/url-shortener.git)
cd url-shortener



2. Create and Activate a Virtual Environment

# Create venv
python3 -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
# .\venv\Scripts\activate



3. Install Dependencies

Install all required libraries from the requirements.txt file.

pip install -r requirements.txt



4. Set Up PostgreSQL Database

You must have a PostgreSQL server running.

Start the PostgreSQL Service:

# On WSL (Ubuntu)
sudo service postgresql start

# On other Linux systems
# sudo systemctl start postgresql



Set a Password for the postgres User:

# Replace 'mysecretpassword' with your own
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'mysecretpassword';"



Create the Database:

# Replace 'url_shortener_db' if you use a different name
sudo -u postgres createdb url_shortener_db



5. Create Your .env File

This project uses a .env file to manage the database URL. This file is ignored by Git for security.

Create a file named .env in the root of the project.

Add your database URL. (This must match the credentials from Step 4).

# .env

DATABASE_URL="postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/url_shortener_db"



How to Run the Application

With your virtual environment active and your .env file in place, run the server using uvicorn:

uvicorn main:app --reload



main: The file main.py.

app: The object app = FastAPI() inside main.py.

--reload: Uvicorn will automatically restart the server when you change a file (great for development).

Once running, you can access the service at http://127.0.0.1:8000.

The interactive API documentation (powered by Swagger UI) is available at:
http://127.0.0.1:8000/docs

API Endpoints

The application has four defined endpoints:

1. GET /

Description: The root endpoint for a basic health check.

Response: {"message": "URL Shortener is running!"}

2. POST /create

Description: Creates a new short URL.

Request Body:

{
  "target_url": "[https://www.your-long-url.com/goes/here](https://www.your-long-url.com/goes/here)"
}



Success Response (200):

{
  "target_url": "[https://www.your-long-url.com/goes/here](https://www.your-long-url.com/goes/here)",
  "is_active": true,
  "clicks": 0,
  "key": "aBc123X"
}



3. GET /{short_key}

Description: Redirects the user to the target_url associated with the short key. Increments the click counter for that key.

Example Request: GET http://127.0.0.1:8000/aBc123X

Success Response (307): A 307 Temporary Redirect to the target_url.

Error Response (404): If the short_key is not found.

{
  "detail": "URL with key 'aBc123X' not found."
}



4. GET /stats/{short_key}

Description: Retrieves the click statistics and other info for a short key without redirecting.

Example Request: GET http://127.0.0.1:8000/stats/aBc123X

Success Response (200):

{
  "target_url": "[https://www.your-long-url.com/goes/here](https://www.your-long-url.com/goes/here)",
  "is_active": true,
  "clicks": 5,
  "key": "aBc123X"
}



Error Response (404): If the short_key is not found.

{
  "detail": "URL with key 'aBc123X' not found."
}

