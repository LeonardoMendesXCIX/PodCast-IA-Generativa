import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/podcast_db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY")
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key")
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600  # 1 hour

settings = Settings()
