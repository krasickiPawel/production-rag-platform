# Architecture

## System context / containers


```mermaid
flowchart LR
    Client[API Client]
    API[FastAPI]
    DB[(PostgreSQL)]
    Redis[(Redis)]
    Worker[Celery Worker]
    LLM[LLM / Embedding Provider]

    Client --> API
    API --> DB
    API --> Redis
    Redis --> Worker
    Worker --> DB
    Worker --> LLM
    API --> LLM
```
