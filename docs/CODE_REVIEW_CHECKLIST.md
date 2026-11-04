# Code review checklist

Use this checklist when reviewing a pull request or a bug-fix change:

1. **Correctness** — Does it do what the issue or description says? Are edge cases handled?
2. **Tests** — Are there tests for the new behaviour and for the bug being fixed? Do all tests pass?
3. **Readability** — Are names, functions, and structure clear? Is anything unnecessarily complex?
4. **Security** — Is user input validated? Are secrets, tokens, or passwords never hard-coded?
5. **Performance** — Is there an obvious loop, query, or copy that will be slow on real data?
6. **Documentation** — Is the README or docstring updated if behaviour changed?

A review should say what is good, what must change before merging, and
what is only a suggestion. Keep comments specific and tied to code lines.
