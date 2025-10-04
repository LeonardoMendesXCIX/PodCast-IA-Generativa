from celery import Celery
from services.tts_service import generate_audio
from services.image_service import generate_image
from pydub import AudioSegment
import os

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_audio_job(episode_id: int, script: str):
    # Generate audio
    audio_url = generate_audio(script)
    # Post-process: add background music, normalize
    audio = AudioSegment.from_mp3(audio_url)
    # Add music (placeholder)
    # Normalize
    audio = audio.normalize()
    # Save and update DB
    # Placeholder: update episode status to completed

@app.task
def generate_image_job(episode_id: int, prompt: str):
    image_url = generate_image(prompt)
    # Update DB
