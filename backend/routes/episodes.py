from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Episode
from services.ai_service import generate_script
from services.tts_service import generate_audio
from services.image_service import generate_image
from workers.audio_worker import process_audio_job
from config import settings
from pydantic import BaseModel

router = APIRouter()

class EpisodeCreate(BaseModel):
    title: str
    prompt: str

@router.post("/episodes")
def create_episode(episode: EpisodeCreate, db: Session = Depends(get_db)):
    # Generate script
    script = generate_script(episode.prompt)
    # Create episode in DB
    new_episode = Episode(title=episode.title, script=script, status="processing")
    db.add(new_episode)
    db.commit()
    # Queue audio and image generation
    process_audio_job.delay(new_episode.id, script)
    generate_image.delay(new_episode.id, episode.prompt)
    return {"episode_id": new_episode.id, "status": "processing"}

@router.get("/episodes/{episode_id}")
def get_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found")
    return episode

# Placeholder for get_db
def get_db():
    # Implement DB session
    pass
