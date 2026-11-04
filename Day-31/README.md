# Day 31 — Python execution model: names, objects and references

## Outcomes
Explain that variables are names bound to objects, distinguish identity from equality, and trace assignments and function calls.

## Core model
- Every value is an object with identity, type and value.
- Assignment binds a name; it does not copy an object.
- == compares values; is compares identity. Use is None for the None singleton.
- Function arguments use call-by-sharing: rebinding a parameter does not rebind the caller's name, but mutating a shared mutable object is visible to the caller.
- id() is an identity token during an object's lifetime. CPython commonly exposes an address-like value, but portable code must not depend on that.

## Lab
Run python examples/object_references.py. Predict output first. Draw name-to-object diagrams for aliasing, function calls and copies.

## Exercises
1. Write one function that mutates a list and another that rebinds its parameter. Explain the difference.
2. Build a nested structure and compare shallow and deep copies.
3. Explain why two equal lists can be different objects.
4. Write a function that returns a copy without accidentally sharing nested mutable state.

## Senior perspective
Unexpected aliasing causes bugs in caches, request state, defaults and concurrent code. Make ownership and mutation boundaries explicit.

## Acceptance criteria
Draw the object graph, explain call-by-sharing, and test equality, identity, mutation and rebinding.

## References
https://docs.python.org/3/reference/datamodel.html
