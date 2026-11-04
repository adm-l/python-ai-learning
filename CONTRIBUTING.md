# Practice workflow

Keep curriculum files stable. Put your solutions in your own branch or a separate practice repository.

```bash
git switch -c practice/day-01
# implement exercises
python -m compileall Day-01
git add .
git commit -m "practice: complete day 01"
```

Review checklist:
- Correct behavior and clear names
- Edge cases and actionable errors
- Side effects isolated behind boundaries
- Deterministic tests
- Useful types and documentation
- No unnecessary abstraction

Never commit API keys, passwords, tokens, databases, virtual environments or .env files.
