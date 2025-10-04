# Setup Instructions

## Local Development
1. Clone repo
2. Set env vars: OPENAI_API_KEY, ELEVENLABS_API_KEY, etc.
3. Run `docker-compose -f infra/docker-compose.yml up --build`

## Backend
- cd backend
- pip install -r requirements.txt
- uvicorn app:app --reload

## Frontend
- cd frontend
- npm install
- npm start

## Deploy
- Use CI/CD pipeline
- Deploy to cloud (e.g., AWS ECS)
