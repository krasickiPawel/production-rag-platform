# ADR-001: Use PostgreSQL with pgvector as the initial vector store

## Status

Proposed

## Context

The application requires persistent storage for:

- collections,
- documents,
- document chunks,
- conversations,
- vector embeddings.

A vector storage solution is required for semantic retrieval.

The initial candidates are:

1. PostgreSQL + pgvector
2. Qdrant

## Decision

PostgreSQL + pgvector

## Options considered

### PostgreSQL + pgvector

Pros:
- ...
- ...

Cons:
- ...
- ...

### Qdrant

Pros:
- ...
- ...

Cons:
- ...
- ...

## Consequences

Positive:
- ...

Negative:
- ...

## When should we revisit this decision?

- ...