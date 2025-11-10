from fastapi import FastAPI
from .database import engine, Base  #IMPORT THESE

# --- New function to create tables ---
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
# -------------------------------------

# Create the FastAPI app instance
app = FastAPI()

# --- New startup event handler ---
@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
# ---------------------------------

@app.get("/")
async def root():
    """
    Root endpoint for a basic health check.
    """
    return {"message": "URL Shortener is running!"}
