# Development guidelines

This is an educational production-oriented RAG project.

Primary goal:
- learn production Python/backend/RAG engineering,
- understand every architectural decision,
- avoid blindly generating large amounts of code.

Working style:
- make small measurable changes,
- explain trade-offs before implementation,
- prefer simple architecture,
- write tests,
- use small logical Git commits,
- do not introduce LangChain/LlamaIndex yet,
- ask me to reason about important architecture decisions before implementing them.

Current stack:
- Python
- FastAPI
- PostgreSQL + pgvector
- Redis
- later Celery
- pytest
- OpenTelemetry
- Azure

Current milestone:
- FastAPI bootstrapped
- PostgreSQL and Redis run with Docker Compose
- /health exists
- next milestone: configuration, DB/Redis clients and /ready