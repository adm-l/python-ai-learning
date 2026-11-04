# Day 38 — Metaclasses and class decorators

## Outcomes
Distinguish class decorators from metaclasses and recognize when class creation customization is justified.

## Concepts
- A class decorator receives a class object and returns a class or replacement.
- A metaclass controls class creation; type is the default metaclass.
- __init_subclass__ is often a simpler extension hook than a custom metaclass.
- Frameworks use class creation hooks to register models, validate declarations or build schemas.
- Excessive metaprogramming hides control flow and complicates debugging.

## Lab
Run python examples/class_customization.py.

## Exercises
1. Register subclasses using __init_subclass__.
2. Implement the same small feature with a class decorator.
3. Explain what a metaclass __new__ receives.
4. Identify a framework use case where a metaclass might be warranted.

## Senior perspective
Choose the least powerful mechanism: functions, decorators, __init_subclass__, then metaclasses.

## Acceptance criteria
Explain class creation and implement a registration hook without unnecessary metaclass complexity.

## References
https://docs.python.org/3/reference/datamodel.html
