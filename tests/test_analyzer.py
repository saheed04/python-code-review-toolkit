from code_review_toolkit.analyzer import analyze_source


def test_counts_functions_and_classes():
    source = '''
"""Example."""

class Greeter:
    """Greets people."""

    def hello(self, name):
        """Say hello."""
        return f"Hello, {name}"


def add(a, b):
    """Add two numbers."""
    return a + b
'''
    report = analyze_source(source)
    assert report["error"] is None
    assert report["functions"] == 2
    assert report["classes"] == 1


def test_detects_todo_and_missing_docstring():
    source = 'def work():\n    # TODO: handle errors\n    return 1\n'
    report = analyze_source(source)
    assert len(report["todos"]) == 1
    assert report["missing_docstrings"] == ["work"]


def test_empty_source():
    report = analyze_source("")
    assert report["error"] is None
    assert report["functions"] == 0
    assert report["lines"] == 0


def test_syntax_error_is_reported_not_raised():
    report = analyze_source("def broken(:\n")
    assert report["error"] is not None
