# Production RAG Platform

## 1. Problem

Employees need to retrieve reliable answers from internal technical documentation distributed acreoss multiple documents.

## 2. Target user

[Kto korzysta z systemu?]

## 3. Core use case

[Co użytkownik robi krok po kroku?]

## 4. Functional requirements

- FR-01: User can create a document collection.
- FR-02:
- FR-03:
- FR-04:
- FR-05:

## 5. Non-functional requirements

- NFR-01: Document ingestion must not block an HTTP request while embeddings are generated.
- NFR-02:
- NFR-03:
- NFR-04:
- NFR-05:

## 6. Out of scope

- Rich frontend application
- Multi-region deployment
- Fine-tuning LLM
- Multi-tenant billing

## 7. Initial assumptions

- ...
- ...
- ...

## 8. Success criteria

- User can upload PDF/DOCX and query its content.
- Answers include citations to retrieved chunks.
- Retrieval quality is measured using an evaluation dataset.
- A failed ingestion job can be retried safely.
- Query latency and token usage are observable.