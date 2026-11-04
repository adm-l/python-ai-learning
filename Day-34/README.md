# Day 34 — Bytecode, disassembly, frames and stack traces

## Outcomes
Understand source compilation, code objects and bytecode; use tracebacks to debug failures.

## Concepts
- Python source is parsed and compiled into code objects; CPython executes bytecode in its interpreter.
- Bytecode is an implementation detail and can change between Python versions.
- The dis module is diagnostic, not a stable optimization contract.
- A frame contains execution context such as code, local/global namespaces and instruction position.
- A traceback links frames describing where an exception propagated.

## Lab
Run python examples/bytecode_frames.py and compare disassembly on Python versions available to you.

## Exercises
1. Disassemble a loop and comprehension. Describe behavior, not exact opcode names.
2. Trigger a nested exception and print its traceback.
3. Use inspect to examine a function signature and source location.
4. Explain why production code should not depend on a particular bytecode sequence.

## Senior perspective
Use bytecode and frame inspection to deepen understanding, but optimize based on profiling and language-level behavior.

## Acceptance criteria
Explain compilation vs execution, inspect a code object, and diagnose a multi-frame traceback.

## References
https://docs.python.org/3/library/dis.html
