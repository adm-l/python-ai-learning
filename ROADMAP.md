# 90-Day Python AI Engineering Roadmap

Suggested pace: 60–120 focused minutes daily. Spend longer when a concept is unclear.

## Stage 1 — Python foundations
01 Environment, interpreter, names, variables and primitive types
02 Operators, expressions, truthiness and comparisons
03 Strings, formatting, Unicode and text processing
04 Lists, indexing, slicing, mutation and copying
05 Tuples, sets, hashability and collection selection
06 Dictionaries, nested data and JSON-like records
07 Conditions, loops, iteration and control flow
08 Functions, parameters, scope and side effects
09 Comprehensions and collection transformations
10 Modules, imports and package structure
11 Files, pathlib, JSON and CSV
12 Exceptions and defensive input handling
13 Classes, instances, methods and object lifecycle
14 Composition, inheritance, dataclasses and enums
15 Project: tested command-line task tracker

## Stage 2 — Professional Python
16 Type hints, generics, Protocol and static analysis
17 Runtime validation and schema design
18 Iterables, iterators and generators
19 Decorators, closures and higher-order functions
20 Context managers and resource lifecycle
21 pytest, fixtures, parametrization and coverage
22 Fakes, mocks and dependency boundaries
23 Logging, debugging and exception design
24 Packaging, virtual environments and dependency pinning
25 Clean architecture, SOLID and dependency inversion
26 SQL, transactions and repository boundaries
27 HTTP clients, timeouts, retries and idempotency
28 Configuration, environment variables and secrets
29 Formatting, linting, typing and security basics
30 Project: typed, tested Python API client and CLI

## Stage 3 — Runtime and systems
31 Python execution model, names, objects and references
32 Mutability, copying, equality and hashing
33 Memory management, garbage collection and profiling
34 Stack traces, debugging and exception internals
35 Async I/O, event loop, coroutines and await
36 asyncio tasks, cancellation and timeouts
37 Concurrency vs parallelism
38 Threads, locks, queues and thread safety
39 Multiprocessing and process boundaries
40 GIL and workload selection
41 Profiling, algorithmic complexity and optimization
42 Caching, resource bounds and backpressure
43 Retries, circuit breakers and idempotency
44 Graceful shutdown and application lifecycle
45 Project: concurrent service health checker

## Stage 4 — Data and API engineering
46 NumPy arrays, shapes, dtypes and vectorization
47 Pandas, cleaning and missing values
48 Data validation and reproducible pipelines
49 SQL fundamentals, indexes and query plans
50 FastAPI request/response models
51 Dependency injection, middleware and lifecycle
52 Authentication, authorization and API security
53 PostgreSQL, transactions and connection pools
54 Background work, queues and worker design
55 Docker and Compose
56 Structured logs, metrics, traces and correlation IDs
57 Unit, integration and contract testing
58 Deployment, health checks and operational readiness
59 Modular monolith vs microservices
60 Project: document ingestion API

## Stage 5 — AI engineering
61 AI application architecture and system boundaries
62 Local/hosted LLM APIs, timeouts and errors
63 Prompt roles, instruction hierarchy and versioning
64 Tokenization, token budgets and context windows
65 Structured outputs and schema validation
66 Tool calling and safe execution boundaries
67 Embeddings, dimensions and similarity
68 Vector search, metadata filtering and persistence
69 Document ingestion, chunking and metadata
70 RAG retrieval and grounded generation
71 Reranking and retrieval evaluation
72 RAG tests, quality metrics and failure analysis
73 Streaming LLM responses
74 Model routing, caching, cost and latency
75 Project: grounded document Q&A service

## Stage 6 — Agentic systems and architecture
76 Agent vs workflow and when autonomy is justified
77 Agent loop: observe, decide, act and verify
78 State design, persistence and checkpointing
79 MCP: tools, resources, prompts and transports
80 MCP server implementation and contracts
81 MCP client lifecycle and multiple servers
82 LangGraph nodes, edges and state
83 Conditional routing, loops and human approval
84 Planning, orchestration and result synthesis
85 Memory engineering: short-term vs long-term
86 Guardrails, permissions and prompt injection
87 Evaluation datasets and model-based evaluation
88 Agent observability, tool traces and token/cost metrics
89 Production architecture, queues, scaling and recovery
90 Capstone: production-oriented DevOps investigation agent

## Milestones
- Day 15: confidently use core Python collections, functions and OOP.
- Day 30: deliver a typed, tested, installable package.
- Day 45: choose appropriately between async, threads and processes.
- Day 60: deliver an API with persistence, tests and observability.
- Day 75: measure and explain RAG quality and failure modes.
- Day 90: deliver an agent workflow with state, tools, safety and evaluation.

## Senior/architect deliverables for every project
Requirements and non-goals; component/data-flow diagram; API and data contracts; failure-mode analysis; unit/integration tests; logs, metrics, traces and health checks; deployment instructions; trade-off record.
