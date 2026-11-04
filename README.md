# Python Code Review Toolkit

A small, well-tested Python toolkit for the kind of work a code reviewer does every day:
analysing a Python file, checking test quality, and triaging issues in a consistent way.

This project was built to demonstrate practical Python, Git, Docker, and testing skills:
setting up a repository, running code locally, evaluating tests, and reviewing code
against a clear checklist — not just writing code that runs once.

## What it does

- **Analyses a Python file** with `analyzer.py`:
  counts functions, classes, lines, TODO comments, long functions, and
  functions missing docstrings.
- **Triages issues** with `triage.py`:
  sorts issues by severity and type, so bugs and security issues come first.
- **Runs from the command line** with `cli.py`:
  `python -m code_review_toolkit.cli examples/sample.py`

## Quick start (local, no Docker)

```bash
git clone <your-repo-url>
cd python-code-review-toolkit
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
python -m code_review_toolkit.cli examples/sample.py
```

Expected output includes a short report: functions, classes, lines,
TODOs, long functions, and missing docstrings for the sample file.

## Quick start (Docker)

```bash
docker build -t code-review-toolkit .
docker run --rm code-review-toolkit examples/sample.py
docker run --rm code-review-toolkit python -m pytest -q
```

The Dockerfile uses a slim Python image, copies only the project files,
installs test dependencies, and runs the toolkit as the default command.

## Project layout

```
src/code_review_toolkit/
  analyzer.py   # AST-based analysis of a Python file
  triage.py     # Issue triage and prioritisation
  cli.py        # Command-line entry point
tests/
  test_analyzer.py
  test_triage.py
examples/
  sample.py     # A small file to analyse and review
docs/
  CODE_REVIEW_CHECKLIST.md
  ISSUE_TRIAGE_GUIDE.md
.github/workflows/ci.yml   # Runs pytest on every push
```

## Tests

```bash
python -m pytest -q
python -m pytest --cov=src/code_review_toolkit -q   # if coverage is installed
```

Tests cover:
- counting functions, classes, and lines correctly
- detecting TODO comments, long functions, and missing docstrings
- triage ordering: security and bug issues before features and chores
- handling an empty file and a file that does not parse

## Code review checklist

See `docs/CODE_REVIEW_CHECKLIST.md` for the checklist used when reviewing
a change: correctness, readability, tests, security, and performance.
See `docs/ISSUE_TRIAGE_GUIDE.md` for how issues are prioritised.

## Notes on honesty

This is a demonstration project, built from scratch for learning and
for showing working habits: clear structure, tests, Docker setup, and
documentation. It does not claim contributions to other open-source
projects. If you use it in an application, describe it accurately as
your own demonstration work.
