# AI Podcast Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.9.5-blue.svg)](https://www.typescriptlang.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10.21-blue.svg)](https://www.docker.com/)

Uma plataforma completa para criação de podcasts utilizando inteligência artificial. Gera roteiros automaticamente, converte texto em áudio realista, cria capas visuais e realiza pós-processamento de áudio.

## Funcionalidades Principais

- **Geração de Roteiro**: Utilize IA (OpenAI GPT) para criar scripts de episódios baseados em prompts.
- **Conversão Texto-Áudio**: Transforme o roteiro em voz realista com ElevenLabs TTS.
- **Geração de Capa**: Crie imagens de capa automaticamente via DALL-E (OpenAI).
- **Pós-Processamento de Áudio**: Mixagem, adição de trilha sonora e normalização usando pydub.
- **Interface Web**: Painel intuitivo para entrada de parâmetros, visualização e download de episódios.
- **Processamento Assíncrono**: Jobs em fila com Celery/Redis para tarefas pesadas.
- **API REST**: Endpoints para criação, consulta e gerenciamento de episódios.
- **Persistência de Dados**: Armazenamento em PostgreSQL com SQLAlchemy.
- **Segurança Básica**: Autenticação JWT e controle de uso.

## Stack Tecnológica

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Pydantic
- **Frontend**: React 18, TypeScript, Axios
- **Banco de Dados**: PostgreSQL
- **Fila de Tarefas**: Redis, Celery
- **Integrações IA**:
  - OpenAI (GPT-3.5 para roteiro, DALL-E para imagens)
  - ElevenLabs (TTS)
- **Infraestrutura**: Docker, Docker Compose, GitHub Actions (CI/CD)
- **Testes**: Pytest

## Estrutura de Pastas

```
podcast-ai-platform/
├── backend/
│   ├── app.py                 # Aplicação principal FastAPI
│   ├── config.py              # Configurações e variáveis de ambiente
│   ├── models.py              # Modelos de dados SQLAlchemy
│   ├── requirements.txt       # Dependências Python
│   ├── routes/
│   │   └── episodes.py        # Endpoints da API
│   ├── services/
│   │   ├── ai_service.py      # Integração OpenAI
│   │   ├── tts_service.py     # Integração ElevenLabs
│   │   └── image_service.py   # Integração DALL-E
│   ├── workers/
│   │   └── audio_worker.py    # Jobs Celery para processamento
│   └── tests/
│       ├── test_api.py        # Testes unitários da API
│       └── test_integration.py # Testes de integração
├── frontend/
│   ├── package.json           # Dependências Node.js
│   └── src/
│       ├── App.tsx            # Componente principal
│       └── components/
│           ├── EpisodeForm.tsx    # Formulário de criação
│           ├── EpisodeList.tsx    # Lista de episódios
│           └── Preview.tsx        # Visualização de episódio
├── infra/
│   ├── Dockerfile.backend     # Container backend
│   ├── Dockerfile.frontend    # Container frontend
│   └── docker-compose.yml     # Orquestração local
├── docs/
│   ├── README.md              # Documentação adicional
│   └── setup.md               # Instruções detalhadas
├── .github/workflows/
│   └── ci-cd.yml              # Pipeline CI/CD
├── .gitignore
├── LICENSE
├── README.md
```

## Instalação e Execução

### Pré-requisitos

- Docker e Docker Compose
- Chaves de API: OpenAI, ElevenLabs

### Execução Local com Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/LeonardoMendesXCIX/PodCast-IA-Generativa.git
   cd podcast-ai-platform
   ```

2. Configure variáveis de ambiente:
   Crie um arquivo `.env` na raiz:
   ```
   OPENAI_API_KEY=your_openai_key
   ELEVENLABS_API_KEY=your_elevenlabs_key
   DATABASE_URL=postgresql://user:password@db/podcast_db
   REDIS_URL=redis://redis:6379/0
   SECRET_KEY=your_secret_key
   ```

3. Execute com Docker Compose:
   ```bash
   docker-compose -f infra/docker-compose.yml up --build
   ```

4. Acesse:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Documentação API: http://localhost:8000/docs

### Execução Local sem Docker

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## Próximos Passos / Melhorias Futuras

- **Multi-usuário**: Suporte a contas de usuário com isolamento de dados.
- **Colaboração**: Edição colaborativa de scripts e feedback em tempo real.
- **Monetização**: Sistema de assinaturas, créditos de IA e analytics.
- **Escalabilidade**: Migração para Kubernetes, serverless para jobs.
- **Integrações**: Suporte a outras APIs (Google TTS, Midjourney).
- **Analytics**: Métricas de uso, performance e engajamento.
- **Mobile App**: Versão mobile com React Native.
- **Templates**: Roteiros pré-definidos para diferentes tipos de podcast.

## Contribuição

Contribuições são bem-vindas! Abra issues para bugs ou sugestões, e pull requests para melhorias.

## Créditos

Criado por [Leonardo Mendes](https://github.com/LeonardoMendesXCIX)

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
