# Development Guidelines

This repository is an educational, production-oriented RAG platform.

The primary objective is not to generate the project as quickly as possible.
The objective is to learn how to design, implement, test, operate, and reason about a production Python/backend/RAG system.

## Primary goals

* Learn production Python, backend, database, cloud, and RAG engineering.
* Understand every important architectural and implementation decision.
* Build a strong mental model of how data and control flow through the system.
* Practice system design and critical thinking.
* Produce code that can be explained during a technical interview.
* Avoid blindly generating large amounts of AI-written code.

## Working style

* Prefer small, measurable, independently verifiable changes.
* Prefer the simplest implementation that satisfies current requirements.
* Do not introduce abstractions, configuration, dependencies, or infrastructure without a concrete current need.
* Explain important trade-offs before implementing architectural changes.
* Ask the developer to reason about important design decisions before providing the final implementation.
* Prefer explicit, understandable code over clever abstractions.
* Use small, logical Git commits.
* Keep the repository focused: no unnecessary boilerplate or speculative code.
* Write tests for meaningful behavior and regression protection, not merely to increase test count or coverage.
* Do not introduce LangChain, LlamaIndex, LangGraph, or similar orchestration frameworks until the underlying RAG primitives have been implemented and understood directly.

## Agent behavior

When asked to review, explain, discuss, or propose a solution:

* Do not modify files unless explicitly asked to implement changes.
* First inspect the relevant existing code and documentation.
* Explain the problem and the minimal reasonable solution.
* Identify trade-offs and alternatives when they materially affect the design.
* Point out issues and let the developer implement the fix when the task is primarily educational.

When asked to implement:

* Modify only files necessary for the requested task.
* Do not expand the scope without asking first.
* Do not create additional abstractions, helpers, configuration options, retries, timeouts, pool settings, or other "production-looking" features unless they are justified by an explicit requirement.
* Avoid unexplained magic numbers.
* Reuse existing project conventions where possible.
* Keep changes small enough to review with `git diff`.
* After implementation, summarize:

  * what changed,
  * why it changed,
  * how to verify it,
  * any important trade-offs or follow-up work.

## Code quality

* Every non-trivial line of code should have a defensible reason to exist.
* Prefer behavior-oriented tests over tests of library implementation details.
* Avoid premature optimization.
* Avoid speculative generalization.
* Avoid duplicate layers of abstraction.
* Fail fast on invalid mandatory configuration.
* Preserve clear dependency boundaries.
* Keep external service configuration outside application code.
* Prefer dependency injection where it improves testability or lifecycle management, not merely for abstraction's sake.

## Security and repository hygiene

* Never commit `.env` files, API keys, credentials, tokens, secrets, or private data.
* `.env.example` may contain safe development placeholders only.
* Never use proprietary code, documents, credentials, or data from employers or clients.
* Development and evaluation data must be synthetic or publicly available.
* Generated build artifacts such as `*.egg-info/` must not be committed.

## Current stack

* Python 3.14
* uv
* FastAPI
* Pydantic / pydantic-settings
* SQLAlchemy 2 async
* asyncpg
* PostgreSQL
* pgvector
* Redis
* Docker Compose
* pytest

Planned later:

* Celery
* PDF/DOCX ingestion
* embeddings
* hybrid retrieval
* reranking
* LLM generation
* RAG evaluation
* OpenTelemetry
* CI/CD
* Azure deployment

## Current architecture principles

* Modular monolith first.
* Separate background worker when asynchronous ingestion is introduced.
* PostgreSQL + pgvector is the initial persistent data and vector store.
* Redis will initially support infrastructure concerns such as background-job messaging, caching, or rate limiting where justified.
* External AI providers must be behind application-owned interfaces when introduced.
* Complexity should be added only after a requirement, measurement, or failure mode justifies it.

## Current milestone

Completed:

* project scope and requirements documented,
* initial architecture documented,
* ADR for PostgreSQL + pgvector accepted,
* FastAPI application bootstrapped,
* PostgreSQL and Redis running through Docker Compose,
* `/health` liveness endpoint implemented,
* application configuration implemented,
* Python package configured using the `src` layout,
* async PostgreSQL connection layer implemented,
* async Redis client implemented,
* PostgreSQL and Redis connectivity verified.

Next milestone:

* implement `/ready`,
* report PostgreSQL and Redis dependency readiness,
* verify healthy and unhealthy dependency scenarios,
* add meaningful automated tests for readiness behavior.

## Definition of done for a small change

A change is complete when:

1. The developer understands why the change exists.
2. The implementation is no more complex than required.
3. Relevant behavior has been manually or automatically verified.
4. `git diff` has been reviewed.
5. No secrets or generated artifacts are included.
6. The change can be described in one clear Git commit message.
