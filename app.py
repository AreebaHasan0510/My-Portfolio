"""
FastAPI Server for Areeba Hasan Portfolio
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import os
import uvicorn

from api.routes import router as api_router

app = FastAPI(
    title="Areeba Hasan - Data Science & Analyst Portfolio",
    description="Advanced Portfolio & API Service for Areeba Hasan",
    version="2.0.0"
)

# Include API Router
app.include_router(api_router)

# Mount Static directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h1>Areeba Hasan Portfolio API Running. Frontend loading...</h1>")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
