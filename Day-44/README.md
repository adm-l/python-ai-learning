# Day 44 — Caching, resource bounds and backpressure

## Outcomes
Design bounded caches and queues, understand invalidation and prevent overload from becoming unbounded memory growth.

## Concepts
- A cache needs a key, value, eviction policy, capacity, TTL/invalidation and concurrency semantics.
- Cache only data whose staleness and consistency requirements are understood.
- Unbounded queues turn overload into latency and memory growth.
- Backpressure slows or rejects producers when consumers cannot keep up.
- Bound concurrency, request sizes, queue lengths, retries and retained history.
- Cache stampedes can occur when many callers miss the same key simultaneously.

## Lab
Run python examples/bounded_cache_queue.py. Observe bounded queue behavior and an LRU cache.

## Exercises
1. Implement a TTL cache with tests for expiry and capacity.
2. Simulate a slow consumer and bounded producer queue.
3. Design a cache key that safely includes tenant and authorization context.
4. Describe how to prevent a cache stampede.

## Senior perspective
Every in-memory structure in a service needs an ownership and capacity story. Observe cache hit rate, evictions, queue depth and rejected work.

## Acceptance criteria
Implement bounded storage and explain invalidation, tenant isolation and overload behavior.

## References
https://docs.python.org/3/library/functools.html
