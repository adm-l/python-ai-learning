# Day 39 — Import system, module caching and import hooks

## Outcomes
Understand module search, initialization, sys.modules, package imports and circular-import failures.

## Concepts
- Import finds a module, creates/initializes it and binds a name.
- sys.path influences where import finders search; sys.meta_path contains finders.
- sys.modules caches module objects and prevents repeated initialization in normal imports.
- Importing executes module-level code. Keep side effects limited.
- Circular imports often expose partially initialized modules.
- Prefer explicit package boundaries and avoid manipulating sys.path in application code.

## Lab
Run python examples/import_inspection.py. Observe __name__, __file__, sys.path and sys.modules.

## Exercises
1. Build a package with absolute and relative imports.
2. Reproduce a circular import, then refactor to remove the cycle.
3. Use importlib.import_module for a plugin selected from trusted configuration.
4. Explain why importing a module should not start a server or connect to production databases.

## Senior perspective
Import-time side effects cause slow startup, brittle tests and surprising deployments. Make startup explicit.

## Acceptance criteria
Trace a package import and remove a circular dependency using a clean module boundary.

## References
https://docs.python.org/3/reference/import.html
