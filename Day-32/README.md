# Day 32 — Mutability, copying, equality and hashing

## Outcomes
Understand mutable and immutable objects, shallow/deep copying, equality contracts and hashability.

## Concepts
- Mutability belongs to the object, not the variable name.
- A tuple is immutable as a container, but can contain a mutable object.
- Shallow copies duplicate the outer container while retaining references to nested objects.
- Deep copies recursively copy supported object graphs; custom classes may need special handling.
- Hashable objects have stable hash values during their lifetime. Equal objects must have equal hashes.
- Mutable objects that participate in equality should generally not be hashable.

## Lab
Run python examples/mutability_copying.py. Inspect nested aliasing and set/dictionary key behavior.

## Exercises
1. Demonstrate a tuple containing a list changing its observable contents.
2. Implement a value object with correct equality and hashing.
3. Explain why a list cannot be a dictionary key.
4. Test that a shallow copy still shares nested state.

## Senior perspective
Copying can be expensive and obscure ownership. Define whether APIs accept, retain, mutate or copy caller-owned objects.

## Acceptance criteria
Choose a copy strategy deliberately and explain the equality/hash contract with tests.

## References
https://docs.python.org/3/reference/datamodel.html
