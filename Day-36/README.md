# Day 36 — Descriptors and attribute lookup

## Outcomes
Understand descriptors and how properties, methods and ORM fields participate in attribute access.

## Concepts
- A descriptor defines one or more of __get__, __set__ or __delete__.
- Data descriptors take precedence over instance dictionary entries; non-data descriptors can be shadowed.
- Functions stored on classes are non-data descriptors that bind methods.
- property is a descriptor.
- Descriptors support validation, lazy values and reusable managed attributes, but can make code harder to inspect.

## Lab
Run python examples/descriptors.py.

## Exercises
1. Build a descriptor that validates a positive integer.
2. Demonstrate descriptor access through class and instance.
3. Explain data vs non-data descriptor precedence.
4. Compare a descriptor with property and a Pydantic field.

## Senior perspective
Use descriptors when behavior is genuinely reusable across attributes. Prefer explicit properties or boundary validation when clearer.

## Acceptance criteria
Implement a tested descriptor and explain attribute lookup precedence.

## References
https://docs.python.org/3/howto/descriptor.html
