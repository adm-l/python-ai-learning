# Day 40 — CPython architecture and interpreter overview

## Outcomes
Describe the stages between source code and execution and distinguish language guarantees from CPython details.

## Concepts
- Python is a language with multiple implementations; CPython is the reference implementation most commonly deployed.
- CPython includes parsing/compilation, code objects, runtime objects, interpreter execution and a C API.
- Execution engine, bytecode and internal object layouts evolve between releases.
- Extension modules can call the CPython C API; ABI and version compatibility matter.
- PyPy and other implementations can have different performance characteristics and internals.

## Lab
Inspect sys.implementation, sys.version, platform.python_implementation() and a function's code object.

## Exercises
1. Draw source → parser/compiler → code object/bytecode → interpreter execution.
2. Mark statements as language-level or CPython-specific.
3. Research a C extension dependency and its supported Python versions.
4. Explain why code should not rely on object memory addresses.

## Senior perspective
Know your production interpreter and version. Pin and test supported versions; avoid undocumented implementation details.

## Acceptance criteria
Explain the execution pipeline and label CPython-specific assumptions.

## References
https://github.com/python/cpython/tree/main/InternalDocs
