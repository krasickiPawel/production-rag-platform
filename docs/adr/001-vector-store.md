# ADR-001: Use PostgreSQL with pgvector as the initial vector store

## Status

Accepted

## Context

The Production RAG Platform requires persistent storage for several types of data:

- document collections,
- document metadata,
- document chunks,
- ingestion job state,
- conversations,
- messages,
- citations,
- vector embeddings.
A vector storage solution is required for semantic retrieval.

The application requires semantic similarity search over document chunk embeddings.

Two initial approaches were considered:

1. PostgreSQL with the pgvector extension
2. PostgreSQL for relational data plus Qdrant as a dedicated vector database

PostgreSQL is required regardless of the vector search solution because the application contains relational domain data.

The initial expected dataset is small to medium-sized. The primary goal of the first version is to build a correct, observable and maintainable production-oriented RAG system rather than optimize prematurely for very large-scale vector search.

---


## Decision

The initial implementation will use PostgreSQL with the pgvector extension for storing embeddings and performing vector similarity search.

Relational application data and vector embeddings will therefore initially be stored in a single PostgreSQL database.

A dedicated vector database such as Qdrant may be introduced later if measurements demonstrate that PostgreSQL with pgvector no longer satisfies retrieval performance, scalability or operational requirements.

---

## Options considered

### Option 1: PostgreSQL + pgvector

#### Advantages
- PostgreSQL is already required for relational application data.
- Embeddings and document metadata can be stored together.
- Fewer infrastructure components need to be deployed, monitored and backed up.
- SQL can be used to combine relational filters and retrieval logic.
- Metadata updates and chunk data can participate in normal database transactions.
- PostgreSQL full-text search can be combined with vector search to implement hybrid retrieval.
- pgvector supports exact nearest-neighbor search.
- pgvector also supports approximate nearest-neighbor indexes such as HNSW and IVFFlat.
- Local development is simpler because only one primary persistent database is required.
- The architecture is easier to understand and operate during the initial project phase.


#### Disadvantages

- PostgreSQL is a general-purpose relational database rather than a dedicated vector-search engine.
- Very large vector workloads may require more tuning or additional infrastructure.
- Scaling relational workloads and vector-search workloads independently is more difficult when they share the same database.
- Dedicated vector databases may provide more specialized vector-search functionality and operational tooling.

---

### Option 2: PostgreSQL + Qdrant

#### Advantages

- Qdrant is designed specifically for vector similarity search.
- Vector workloads can be scaled independently from relational application data.
- Qdrant provides specialized vector indexing and metadata filtering capabilities.
- Separation may be beneficial for very large vector datasets or retrieval-heavy systems.

#### Disadvantages

- PostgreSQL would still be required for relational application data.
- The system would therefore require two persistent data stores.
- More infrastructure means additional deployment, monitoring, backup and failure scenarios.
- Application logic must maintain consistency between PostgreSQL metadata and vectors stored in Qdrant.
- Document deletion and reindexing operations become distributed operations.
- Local development becomes more complex.
- The additional complexity is not currently justified by measured requirements.

---


## Consequences

### Positive consequences

- The initial architecture remains operationally simple.
- Relational metadata, chunks and embeddings can be queried within the same database.
- Hybrid search can use PostgreSQL full-text search together with pgvector.
- Fewer infrastructure dependencies make local development and cloud deployment easier.
- There is no cross-database consistency problem during initial ingestion.
- The project provides an opportunity to learn PostgreSQL indexing and query behavior alongside vector retrieval.

### Negative consequences

- PostgreSQL becomes responsible for both transactional application data and vector retrieval.
- Vector search could eventually compete with other database workloads.
- Scaling vector search independently may require architectural changes later.
- Migration to a dedicated vector database would require changes in storage and retrieval infrastructure.

---

## Alternatives rejected

### Qdrant as the only database

Rejected because the application requires relational data such as collections, conversations, messages and ingestion state. A relational database is a more natural fit for these entities.

### In-memory vector storage

Rejected because the project is intended to model a persistent production system. Data must survive application restarts and deployments.

---

## Validation

The decision will be validated through measurements rather than assumptions.

The project will measure:

- retrieval latency,
- p95 retrieval latency,
- Recall@k,
- MRR,
- database size,
- ingestion throughput,
- query performance as the number of chunks grows.

---

## When should we revisit this decision?

This decision should be revisited if one or more of the following occur:

- vector search latency no longer meets the project's latency target,
- the number of stored vectors increases substantially,
- vector workload negatively affects transactional PostgreSQL workloads,
- independent scaling of vector search becomes necessary,
- required vector-search functionality is difficult or inefficient to implement with pgvector,
- a benchmark shows that a dedicated vector database provides a meaningful benefit that justifies the additional operational complexity.

If those conditions occur, Qdrant will be reevaluated as a dedicated vector-search service.