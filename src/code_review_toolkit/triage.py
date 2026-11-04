"""Triage GitHub-style issues in a consistent, explainable order.

Priority is based on severity first, then type. This mirrors a simple
review workflow: fix security and correctness problems before features
and chores, and keep the ordering deterministic so two reviewers get
the same result from the same input.
"""

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
TYPE_ORDER = {"security": 0, "bug": 1, "feature": 2, "chore": 3}


def triage_issues(issues: list[dict]) -> list[dict]:
    """Return issues sorted by severity, then type, then title.

    Each issue is a dict with at least ``title``. ``severity`` and
    ``type`` are optional and default to ``low`` and ``chore``.
    The original list is not modified.
    """
    def sort_key(issue: dict):
        severity = str(issue.get("severity", "low")).lower()
        issue_type = str(issue.get("type", "chore")).lower()
        return (
            SEVERITY_ORDER.get(severity, 99),
            TYPE_ORDER.get(issue_type, 99),
            str(issue.get("title", "")),
        )

    return sorted(issues, key=sort_key)


def priority_label(issue: dict) -> str:
    """Return a short priority label for one issue, e.g. 'P0' or 'P2'."""
    severity = str(issue.get("severity", "low")).lower()
    if severity in ("critical", "high"):
        return "P0"
    if severity == "medium":
        return "P1"
    return "P2"
