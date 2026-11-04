# Day 35 — Class creation, MRO and method resolution

## Outcomes
Explain class objects, inheritance lookup, method resolution order and cooperative multiple inheritance.

## Concepts
- A class is itself an object; instances refer to their class.
- Attribute lookup follows defined rules, including instance attributes, descriptors and class hierarchy.
- Python computes a method resolution order (MRO), using C3 linearization.
- Class.__mro__ and Class.mro() reveal lookup order.
- In multiple inheritance, use cooperative super() consistently and ensure compatible method signatures.

## Lab
Run python examples/mro_super.py. Trace the MRO and order of calls.

## Exercises
1. Create a diamond inheritance hierarchy and print its MRO.
2. Implement cooperative initialization with super().
3. Demonstrate instance attributes vs class attributes.
4. Explain why directly calling a named parent method can break cooperative behavior.

## Senior perspective
Prefer composition for independent capabilities. Use multiple inheritance only when the lookup contract is clear and tested.

## Acceptance criteria
Predict MRO, explain super() as next-in-MRO lookup, and test cooperative inheritance.

## References
https://docs.python.org/3/reference/datamodel.html
