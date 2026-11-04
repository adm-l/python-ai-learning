# Day 01 — Environment, interpreter and variables

## Outcomes
- Create and activate an isolated Python environment.
- Run a Python module from the terminal.
- Understand names, objects, assignment and built-in types.
- Inspect values with type() and isinstance().

## Concepts
Python variables are names bound to objects; assignment does not declare a fixed storage type. Python is dynamically typed, but types still matter. Distinguish a name, an object and its type.

Core types: str, int, float, bool and NoneType. Python uses None for absence of a value; boolean literals are True and False.

## Run
```bash
python examples/variables.py
```

## Exercises
1. Create variables for service name, retry count, timeout and enabled flag. Print values and types.
2. Assign an integer to a name, then a string. Explain what changed.
3. Use isinstance() to validate a retry count. Note that bool is a subclass of int; decide whether True should be accepted.
4. Print a formatted summary of an AI application configuration.

## Senior perspective
Dynamic typing moves some errors to runtime. Use clear boundaries, validation and type hints instead of assuming every value is correct.

## Acceptance
- [ ] Explain name binding vs declaration.
- [ ] Distinguish the core built-in types.
- [ ] Run a script inside a virtual environment.
- [ ] Complete exercises and document the bool/int edge case.
