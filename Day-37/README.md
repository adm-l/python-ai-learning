# Day 37 — Properties, slots and object-model trade-offs

## Outcomes
Use properties to preserve invariants, understand __slots__, and make evidence-based object-layout choices.

## Concepts
- Properties expose controlled attribute access while keeping a stable public interface.
- Validation belongs close to the state transition that must preserve an invariant.
- __slots__ can restrict instance attributes and may reduce per-instance memory in suitable classes.
- Slots affect inheritance, weak references, pickling and dynamic attributes; they are not a universal speed switch.
- Measure object counts and memory before adopting layout optimizations.

## Lab
Run python examples/properties_slots.py and compare ordinary and slotted instances with tracemalloc.

## Exercises
1. Implement a temperature value with validated property assignment.
2. Add slots to a high-volume record and test behavior.
3. Test inheritance and weak-reference behavior.
4. Write a benchmark and explain its limitations.

## Senior perspective
Optimize object representation only after identifying allocation volume as a real bottleneck.

## Acceptance criteria
Build an invariant-preserving property and justify whether slots help in a measured scenario.

## References
https://docs.python.org/3/reference/datamodel.html
