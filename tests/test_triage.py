from code_review_toolkit.triage import priority_label, triage_issues


def test_security_and_bugs_come_first():
    issues = [
        {"title": "Add dark mode", "type": "feature", "severity": "low"},
        {"title": "Login crashes", "type": "bug", "severity": "high"},
        {"title": "Token leak", "type": "security", "severity": "critical"},
    ]
    ordered = triage_issues(issues)
    assert [i["title"] for i in ordered] == [
        "Token leak",
        "Login crashes",
        "Add dark mode",
    ]


def test_original_list_is_not_modified():
    issues = [{"title": "B", "type": "bug", "severity": "low"}]
    triage_issues(issues)
    assert issues[0]["title"] == "B"


def test_priority_labels():
    assert priority_label({"severity": "critical"}) == "P0"
    assert priority_label({"severity": "medium"}) == "P1"
    assert priority_label({"severity": "low"}) == "P2"
