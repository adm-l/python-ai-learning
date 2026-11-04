# 180-Day Python Mastery and AI Engineering Roadmap

This programme is deliberately focused on **Python**: the language, its runtime, standard library, ecosystem, engineering practices and Python libraries used in data science and AI. It does not include Linux, Docker, Kubernetes, cloud infrastructure or DevOps as curriculum topics.

The goal is to progress from Python fundamentals to advanced Python engineering and then Python-based AI application development. This is a learning plan, not a guarantee that 180 calendar days alone makes someone a senior engineer. Suggested pace: 1–2 focused hours daily, with extra time for projects and difficult concepts.

Every stage should include detailed explanations, runnable examples, exercises, tests, debugging practice and a practical project.

## Stage 1 — Python foundations (Days 01–15)
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

## Stage 2 — Professional Python (Days 16–30)
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

## Stage 3 — Python runtime and internals (Days 31–45)
31 Python execution model, names, objects and references
32 Mutability, copying, equality and hashing
33 Memory management, reference counting and garbage collection
34 Bytecode, disassembly, frames and stack traces
35 Class creation, MRO and method resolution
36 Descriptors and attribute lookup
37 Properties, slots and object model trade-offs
38 Metaclasses and class decorators
39 Import system, module caching and import hooks
40 CPython architecture and interpreter implementation overview
41 GIL, free-threading concepts and version-dependent behavior
42 Profiling CPU and memory usage
43 Algorithmic complexity and practical optimization
44 Caching, resource bounds and backpressure
45 Project: profile and optimize a Python application

## Stage 4 — Python concurrency, networking and reliability (Days 46–60)
46 Concurrency models and choosing the right execution model
47 Threading, locks and shared state
48 Multiprocessing and process pools
49 asyncio event loop, coroutines and tasks
50 asyncio synchronization, queues and bounded workers
51 Async HTTP clients and network I/O
52 Async generators and streaming
53 Python socket programming and networking fundamentals
54 HTTP resilience, timeouts, retries and rate limits
55 Queues, job processing and idempotency
56 Deadlines, bulkheads and graceful shutdown
57 Structured logging and Python observability libraries
58 Performance testing and latency percentiles
59 Concurrency testing and debugging
60 Project: resilient concurrent task runner

## Stage 5 — Data structures, algorithms and software design (Days 61–75)
61 Big-O analysis and problem decomposition
62 Arrays, strings, hash maps and sets
63 Dictionaries, sets and hash-table behavior
64 Stacks, queues, linked lists and deques
65 Trees, traversal and search
66 Binary search and sorted data
67 Sorting algorithms, stability and key functions
68 Recursion, iteration and backtracking
69 Graphs, BFS, DFS and topological ordering
70 Heaps, priority queues and top-k problems
71 Tries, prefix search and indexing
72 Dynamic programming and memoization
73 Pythonic algorithm design, iterators and generators
74 Software design principles, protocols and composition
75 Project: algorithm toolkit and benchmark suite

## Stage 6 — Python application and backend development (Days 76–90)
76 Backend architecture and Python request lifecycle
77 HTTP fundamentals and API contract design
78 FastAPI fundamentals and dependency injection
79 FastAPI asynchronous behavior and application lifecycle
80 API validation, errors and versioning
81 Relational database fundamentals and SQL
82 PostgreSQL transactions and isolation
83 Python database access and repository patterns
84 Redis Python client, caching and data structures
85 Rate limiting and coordination patterns in Python applications
86 Message queues and event-driven application patterns
87 Kafka Python client concepts, partitions and consumer groups
88 Outbox, inbox and idempotency patterns
89 Python API security and application hardening
90 Project: production-style Python order API

## Stage 7 — Advanced Python internals (Days 91–105)
91 Python data model and special methods
92 Object lifecycle, allocation and identity
93 Reference counting and cyclic garbage collection in depth
94 Attribute lookup, `__getattribute__` and `__getattr__`
95 Descriptors: data descriptors, non-data descriptors and binding
96 MRO, C3 linearization and multiple inheritance
97 Metaclasses and the class creation protocol
98 Advanced decorators: functions, classes and decorator factories
99 Iterator and generator protocol internals
100 Context manager protocol and resource lifecycle
101 Import machinery, finders, loaders and module caching
102 CPython bytecode, frames and execution model
103 GIL, free-threaded Python and practical concurrency implications
104 Memory profiling, allocation tracing and performance diagnosis
105 Project: build a Python object and runtime inspection toolkit

## Stage 8 — Advanced language features and Python library engineering (Days 106–120)
106 Modern type system: annotations and static type checking
107 Generics, TypeVar, bounds and variance
108 Protocols, structural subtyping and runtime-checkable protocols
109 TypedDict, Literal, Final, Required and NotRequired
110 Callable, ParamSpec, Concatenate and type-safe decorators
111 Dataclasses, slots, enums and Pydantic model design
112 Exception hierarchies, exception chaining and custom errors
113 Functional programming: purity, immutability and composition
114 Closures, lexical scope and higher-order functions
115 Dependency injection and inversion of control in Python
116 Design patterns: strategy, factory, adapter and observer
117 SOLID and composition applied to Python code
118 Packaging: pyproject.toml, build backends and dependency metadata
119 Reusable libraries, CLI design, versioning and documentation
120 Project: design, package and test a reusable Python library

## Stage 9 — Concurrency internals and performance engineering (Days 121–135)
121 Thread lifecycle, scheduling and thread-safety boundaries
122 Locks, RLock, Condition, Event and Semaphore
123 Multiprocessing start methods and process lifecycle
124 Process pools, IPC, queues and shared memory
125 asyncio event loop internals and scheduling
126 Coroutines, awaitables, Futures and Tasks
127 Cancellation propagation, timeouts and cleanup
128 TaskGroup and structured concurrency
129 Async generators, backpressure and streaming pipelines
130 Async context managers and resource cleanup
131 Comparing threads, processes and asyncio with experiments
132 CPU-bound versus I/O-bound workloads and optimization choices
133 Profiling and benchmarking with cProfile, timeit and pyinstrument
134 Memory-efficient programming, generators and allocation reduction
135 Project: concurrent, bounded Python data-processing engine

## Stage 10 — Python architecture, testing and engineering quality (Days 136–150)
136 Clean architecture and dependency direction in Python
137 Modular design, package boundaries and cohesive components
138 Domain modeling and domain-driven design fundamentals
139 Repository, Unit of Work and service-layer patterns
140 Dependency injection, composition roots and testability
141 pytest deeply: fixtures, parametrization, plugins and coverage
142 Integration testing and testing external boundaries
143 Mocking, fakes, stubs and test doubles
144 Property-based testing with Hypothesis
145 Test-driven development and refactoring safely
146 Static analysis, linting, formatting and type-checking workflows
147 Secure Python coding, validation and safe deserialization
148 Plugin systems, dynamic imports and extensible architectures
149 Releasing and maintaining high-quality Python packages
150 Project: build a modular, well-tested Python application

## Stage 11 — Python for data science and machine learning (Days 151–165)
151 NumPy arrays, shapes, dtypes and vectorization
152 Broadcasting, indexing, views, copies and numerical operations
153 Pandas Series, DataFrames and indexing
154 Data cleaning, joins, groupby and transformations
155 Polars and efficient columnar data processing
156 Statistics: distributions, central tendency, variance and sampling
157 Probability, conditional probability and Bayes' theorem
158 Linear algebra for ML: vectors, matrices, dot products and norms
159 Calculus intuition: derivatives, gradients and optimization
160 Machine-learning problem types, features, labels and datasets
161 Regression, classification and common algorithms
162 Clustering and unsupervised learning
163 Train/validation/test splits, cross-validation and evaluation metrics
164 Scikit-learn pipelines, preprocessing and model serialization
165 Project: end-to-end tabular machine-learning application

## Stage 12 — Python AI and LLM engineering (Days 166–180)
166 LLM architecture, neural networks and transformer foundations
167 Tokenization, token IDs, vocabularies and token budgets
168 Embeddings, vector representations and similarity
169 Hugging Face Transformers and model inference from Python
170 Running local LLMs with Ollama and Python clients
171 Hosted and local LLM API integration, structured outputs and validation
172 Prompt design, context windows and conversation management
173 Vector search, vector databases and retrieval from Python
174 RAG architecture: ingestion, chunking, retrieval and generation
175 Reranking, cross-encoders and retrieval evaluation
176 LLM evaluation, hallucinations, grounding and guardrails
177 MCP server and client development using Python
178 LangGraph: state, nodes, edges, routing and checkpoints
179 Multi-tool and multi-agent systems, coordination and evaluation
180 Capstone: build and defend a production-oriented Python AI agent

## Learning method for every day
Each daily lesson should include:
1. A clear explanation from fundamentals, including why the concept exists.
2. Internals: what Python or the relevant library is doing behind the scenes.
3. Complete runnable examples with expected behavior.
4. Exercises that require independent implementation.
5. Tests using pytest where appropriate.
6. Real-world use cases, limitations and trade-offs.
7. A short recap and questions to check understanding.

Major projects should include a clear package structure, documented setup, requirements and non-goals, tests, error handling, security considerations and design decisions. Use external services or databases only when they help teach Python application development; they are not separate infrastructure curriculum.

## Milestones
- Day 15: use Python fundamentals confidently and build a tested CLI.
- Day 30: deliver a typed, tested and installable Python package.
- Day 45: explain Python runtime and object-model behavior.
- Day 60: choose appropriately between async, threads and processes.
- Day 75: apply algorithms and software design principles.
- Day 90: deliver a Python backend application with persistence and clear boundaries.
- Day 105: explain advanced Python internals and inspect runtime behavior.
- Day 120: build and distribute a reusable Python library.
- Day 135: understand Python concurrency and optimize measured bottlenecks.
- Day 150: design and test a modular Python application.
- Day 165: build a reproducible machine-learning application.
- Day 180: build and evaluate a Python-based AI agent.

## Important learning rule
A day is complete only when the learner can explain the concept, run and modify the example, solve the exercises without copying, write tests, debug a failure and explain the trade-offs. Reading a lesson is not completion.

The roadmap is the master syllabus. Individual daily lesson folders, runnable code, exercises, tests and project implementations must be developed progressively; do not assume they all exist just because a topic appears here.
