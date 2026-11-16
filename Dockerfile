# A small, official Python image (Debian "slim" = fewer extras, smaller download).
FROM python:3.14-slim

# Don't write .pyc files; print logs immediately; keep pip quiet and cache-free.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Run as a normal user, never as root, so a bug can't take over the container.
RUN useradd --create-home --uid 10001 appuser

# Copy requirements first: Docker caches this layer, so code changes don't
# trigger a full reinstall of every package.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY alembic.ini .
COPY migrations ./migrations
COPY app ./app

USER appuser
EXPOSE 8000

# Bring the database schema up to date, then start the web server.
CMD ["sh", "-c", "alembic upgrade head && exec uvicorn app.main:app --host 0.0.0.0 --port 8000"]
