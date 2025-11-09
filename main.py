from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint for a basic health check.
    """
    return {"message": "URL Shortener is running!"}
