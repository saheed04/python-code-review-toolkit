"""Analyse a Python source file using the standard library ``ast`` module.

The goal is deliberately small and reviewable: count the main structures,
flag the most common review issues, and return a plain dictionary that
tests and the CLI can use without any third-party dependency.
"""

import ast
from pathlib import Path

LONG_FUNCTION_LINES = 30


def analyze_source(source: str) -> dict:
    """Analyse Python source text and return a review report.

    Returns a dict with counts and lists of findings. A file that does
    not parse is reported as an error instead of raising, because a
    reviewer needs to see that clearly.
    """
    lines = source.splitlines()
    todos = [line.strip() for line in lines if "TODO" in line]

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return {
            "lines": len(lines),
            "functions": 0,
            "classes": 0,
            "todos": todos,
            "long_functions": [],
            "missing_docstrings": [],
            "error": f"{exc.msg} (line {exc.lineno})",
        }

    functions = []
    classes = []
    missing_docstrings = []
    long_functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
            if ast.get_docstring(node) is None:
                missing_docstrings.append(node.name)
            end = getattr(node, "end_lineno", None) or node.lineno
            if end - node.lineno + 1 > LONG_FUNCTION_LINES:
                long_functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
            if ast.get_docstring(node) is None:
                missing_docstrings.append(node.name)

    return {
        "lines": len(lines),
        "functions": len(functions),
        "classes": len(classes),
        "todos": todos,
        "long_functions": long_functions,
        "missing_docstrings": missing_docstrings,
        "error": None,
    }


def analyze_file(path: str | Path) -> dict:
    """Read a file and analyse it. The report also includes the path."""
    text = Path(path).read_text(encoding="utf-8")
    report = analyze_source(text)
    report["path"] = str(path)
    return report


def format_report(report: dict) -> str:
    """Format a report as short, human-readable text for the CLI."""
    if report.get("error"):
        return f"{report.get('path', 'file')}: parse error: {report['error']}"

    def _list(values):
        return ", ".join(values) if values else "none"

    return "\n".join(
        [
            f"File: {report.get('path', 'input')}",
            f"Lines: {report['lines']}",
            f"Functions: {report['functions']}",
            f"Classes: {report['classes']}",
            f"TODOs: {_list(report['todos'])}",
            f"Long functions (>{LONG_FUNCTION_LINES} lines): {_list(report['long_functions'])}",
            f"Missing docstrings: {_list(report['missing_docstrings'])}",
        ]
    )
