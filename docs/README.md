# AI Podcast Generator

A platform to create podcasts using AI: generate scripts, convert to audio, create covers, and post-process.

## Features
- AI script generation (OpenAI)
- Text-to-speech (ElevenLabs)
- Image generation (DALL-E)
- Audio post-processing
- Web interface
- Async job processing

## Stack
- Backend: Python/FastAPI
- Frontend: React/TypeScript
- DB: PostgreSQL
- Queue: Redis/Celery
- Infra: Docker, Kubernetes

## Setup
See docs/setup.md

## API
- POST /api/v1/episodes: Create episode
- GET /api/v1/episodes/{id}: Get episode

## Future Improvements
- Multi-user support
- Monetization
- Collaborative editing
