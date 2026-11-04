# Day 41 — GIL, free-threading and workload selection

## Outcomes
Explain the traditional CPython GIL model, free-threaded builds at a high level, and choose concurrency based on measurements.

## Concepts
- In traditional GIL-enabled CPython builds, the GIL constrains simultaneous execution of Python bytecode by threads within one interpreter.
- Threads remain useful for overlapping blocking I/O.
- Processes provide separate interpreters and address spaces, with serialization/IPC costs.
- Native extensions may release the GIL during work.
- Free-threaded CPython builds are available as an optional build from Python 3.13 and have compatibility/performance trade-offs.
- Inspect the runtime and test dependencies; do not assume a particular build mode.

## Lab
Run python examples/gil_workloads.py. Compare sequential, threaded and process-based CPU and I/O workloads. Keep inputs small on memory-constrained laptops.

## Exercises
1. Benchmark CPU-bound work sequentially, with threads and with processes.
2. Benchmark simulated I/O sequentially and with threads.
3. Explain process startup and serialization overhead.
4. Record Python version/build and avoid universal conclusions from one run.

## Senior perspective
Choose concurrency from workload, latency, throughput, memory, deployment and dependency constraints.

## Acceptance criteria
Explain GIL limitations and defend a concurrency choice using repeatable measurements.

## References
https://docs.python.org/3/library/threading.html
