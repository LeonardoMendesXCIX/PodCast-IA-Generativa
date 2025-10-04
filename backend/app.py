from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.episodes import router as episodes_router
from config import settings

app = FastAPI(title="AI Podcast Generator", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(episodes_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "AI Podcast Generator API"}
