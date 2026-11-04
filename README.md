# Python AI Engineering Mastery

A practical **180-day Python-only curriculum** progressing from Python fundamentals to advanced Python engineering, data science, machine learning and AI/LLM application development.

The focus is Python language mastery, runtime internals, standard library, Python ecosystem and building applications with Python. This curriculum does **not** include Linux, Docker, Kubernetes, cloud infrastructure or DevOps as study phases.

This is a long-form learning programme, not a promise that completing a calendar schedule alone makes someone a senior engineer. Every milestone requires implementation, testing, debugging and the ability to explain trade-offs.

## Setup

Requires Python 3.12+ for the main learning environment. Some lessons compare version-specific behavior; always record the interpreter version used.

```bash
git clone https://github.com/adm-l/python-ai-learning.git
cd python-ai-learning
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Start with [Day 01](Day-01/README.md). Run:

```bash
python Day-01/examples/variables.py
```

## Curriculum

- Days 01–15: Python foundations
- Days 16–30: Professional Python, typing, testing, packaging and design
- Days 31–45: Python runtime, object model, memory, interpreter and profiling
- Days 46–60: Python concurrency, networking, reliability and performance
- Days 61–75: Algorithms, data structures and software design in Python
- Days 76–90: Python backend development, APIs, databases and Python client libraries
- Days 91–105: Advanced Python internals and object model
- Days 106–120: Advanced typing, metaprogramming, packaging and reusable libraries
- Days 121–135: Concurrency internals, asyncio and Python performance
- Days 136–150: Python architecture, testing and professional engineering
- Days 151–165: NumPy, Pandas, statistics and machine learning
- Days 166–180: Python AI engineering, LLMs, RAG, MCP and LangGraph

See [ROADMAP.md](ROADMAP.md) for the full day-by-day syllabus.

## How to study

1. Study one day at a time; type examples yourself rather than only copying.
2. Predict what an example will do before running it.
3. Complete exercises independently and add edge cases.
4. Run tests from a clean environment.
5. Debug at least one failure intentionally.
6. Record one design trade-off, one failure mode and one unresolved question.
7. Keep practice commits on a personal branch.

## Definition of done

- [ ] Explain the day's concepts without reading notes.
- [ ] Run and modify every provided example.
- [ ] Complete exercises independently.
- [ ] Add tests for important behavior and edge cases.
- [ ] Explain complexity, failure modes and security implications where relevant.
- [ ] Document one trade-off and one question for review.

## Project quality bar

Substantial projects should include requirements and non-goals, a clear package structure, API/data contracts where relevant, unit and integration tests, failure-mode analysis, security considerations, structured logs and metrics where appropriate, reproducible setup, documentation and explicit trade-off records.

No GitHub Actions workflow is required for this learning repository. Local tests and manual review are part of the learning workflow.

Finishing a syllabus does not automatically make someone a senior architect. Senior ability comes from repeated implementation, debugging, code review, ownership and explaining trade-offs.
