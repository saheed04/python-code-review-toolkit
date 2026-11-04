# Issue triage guide

Triage means deciding, in order, what to work on first.

1. **Reproduce** — Can you reproduce the issue from the description? If not, ask for steps.
2. **Classify** — Is it security, a bug, a feature, or a chore?
3. **Assess severity** — critical, high, medium, or low. Critical and high come first.
4. **Check scope** — Does it affect many users, or one edge case? Note it in the issue.
5. **Assign next step** — Fix, investigate further, or close with a clear reason.

The `triage.py` module in this project implements steps 2 and 3 in code,
so the ordering is consistent and testable.
