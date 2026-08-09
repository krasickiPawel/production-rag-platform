# Production RAG Platform

## 1. Problem


Employees need to retrieve reliable answers from internal technical documentation distributed acreoss multiple documents.

### Description
Employees often need to find reliable information scattered across many internal technical documents such as runbooks, architecture decision records, API documentation, incident reports and operational procedures.

Traditional keyword search may fail when the user does not know the exact wording used in the source document. At the same time, a general-purpose LLM may generate plausible but unsupported answers.

The goal of this project is to build a production-oriented Retrieval-Augmented Generation (RAG) platform that allows users to upload internal documents and ask natural-language questions about their contents.

The system should retrieve relevant source fragments, generate an answer grounded in those fragments and provide citations so that the user can verify the answer.

---

## 2. Target user

The primary target user is a technical employee working in a software organization, for example:

- software engineer,
- DevOps / SRE engineer,
- support engineer,
- technical project member.

The user needs to quickly retrieve reliable information from internal technical documentation without manually browsing multiple files.

For the initial version, the system is designed for a single organization and does not implement full multi-tenant isolation.

---


## 3. Core use case


1. The user creates a document collection representing a knowledge domain, for example `Payment Platform Documentation`.
2. The user uploads one or more PDF or DOCX documents to the collection.
3. The API accepts the upload and schedules document processing asynchronously.
4. A background worker:
   - parses the document,
   - normalizes the extracted text,
   - splits it into chunks,
   - generates embeddings,
   - stores chunks and metadata in PostgreSQL.
5. When processing completes, the document becomes searchable.
6. The user sends a natural-language question to the collection.
7. The system retrieves relevant chunks using semantic and lexical retrieval.
8. Retrieved results may be fused and reranked.
9. The most relevant context is sent to an LLM.
10. The LLM generates a structured answer based only on the supplied context.
11. The response contains citations pointing to the source chunks.
12. The query, answer, citations, latency and token usage are recorded for observability and evaluation.

---

## 4. Functional requirements

- **FR-01:** User can create a document collection.
- **FR-02:** User can upload PDF and DOCX documents to a selected collection.
- **FR-03:** Uploaded documents are processed asynchronously and their processing status can be retrieved.
- **FR-04:** User can search indexed documents using a natural-language query.
- **FR-05:** The system can perform semantic vector retrieval over document chunks.
- **FR-06:** The system can perform lexical full-text retrieval.
- **FR-07:** The system can combine retrieval results using a hybrid retrieval strategy.
- **FR-08:** Retrieved candidates can be reranked before being sent to the LLM.
- **FR-09:** User can ask a question and receive an LLM-generated answer grounded in retrieved document context.
- **FR-10:** Generated answers include citations identifying the source document and chunk.
- **FR-11:** User can start a conversation and retrieve its message history.
- **FR-12:** The system stores metadata about document ingestion and query execution.
- **FR-13:** Failed ingestion jobs can be retried safely.
- **FR-14:** The system exposes health, readiness and metrics endpoints.

---


## 5. Non-functional requirements


- **NFR-01:** Document ingestion must not block an HTTP request while parsing, chunking or embeddings are generated.
- **NFR-02:** Document ingestion should be idempotent so retrying the same operation does not create duplicate indexed content.
- **NFR-03:** External LLM and embedding requests must use explicit timeouts and bounded retries.
- **NFR-04:** The system must expose observable query latency, retrieval latency, LLM latency and token usage.
- **NFR-05:** Important operations should be traceable using a correlation or trace identifier.
- **NFR-06:** The API must return structured and validated responses.
- **NFR-07:** The application should degrade safely when external AI providers are unavailable.
- **NFR-08:** Retrieval quality must be measurable using a repeatable evaluation dataset.
- **NFR-09:** Secrets must not be committed to the repository and should be provided through environment-based configuration.
- **NFR-10:** Core application logic should be covered by automated unit and integration tests.
- **NFR-11:** The system should be runnable locally using documented development commands and containerized infrastructure.
- **NFR-12:** The initial architecture should favor simplicity and maintainability over premature distributed-system complexity.

---


## 6. Out of scope

The first production-oriented version will intentionally not include:

- rich frontend application,
- native mobile application,
- multi-region deployment,
- fine-tuning LLMs,
- training custom embedding models,
- multi-tenant billing,
- enterprise SSO integration,
- advanced role-based access control,
- real-time collaborative editing,
- support for every possible document format,
- Kubernetes deployment,
- autonomous agent workflows,
- internet search as an additional knowledge source.

These features may be considered in future versions if justified by requirements.

---

## 7. Initial assumptions


- The initial system serves one logical organization.
- The initial dataset is small to medium-sized and does not require billions of vectors.
- PostgreSQL is required regardless of the vector-storage decision because the system stores relational application data.
- Documents used for development and evaluation contain synthetic or publicly available information only.
- PDF and DOCX are sufficient as the first supported file formats.
- The system may depend on an external LLM and embedding provider such as OpenAI or Azure OpenAI.
- Background processing is required because document parsing and embedding generation may take significantly longer than a typical HTTP request.
- Eventual consistency between document upload and search availability is acceptable.
- Users prefer a grounded answer with an explicit "insufficient information" response over an unsupported answer.
- The initial deployment can run in a single cloud region.
- The system should first be optimized for correctness, observability and maintainability rather than maximum throughput.

---

## 8. Success criteria

- User can create a collection.
- User can upload a PDF or DOCX document.
- The upload API returns without waiting for document embedding generation.
- A background worker processes the document and marks it as searchable.
- User can query the indexed content using natural language.
- Answers include citations pointing to retrieved source chunks.
- The system refuses or clearly indicates when available context is insufficient to answer a question.
- Retrieval quality is measured using a versioned evaluation dataset.
- Vector-only retrieval can be compared against hybrid retrieval using measurable metrics such as Recall@k and MRR.
- Failed ingestion jobs can be retried without duplicating document content.
- Query latency, retrieval latency, LLM latency and token usage are observable.
- Automated tests cover important application and infrastructure integration paths.
- The application can be started locally from documented commands.
- CI runs tests automatically for repository changes.
- A deployable version of the application is available in a cloud environment.
- The README explains the architecture, major design decisions, trade-offs and evaluation results.