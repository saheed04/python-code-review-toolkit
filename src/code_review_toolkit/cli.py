"""Command-line entry point: analyse one Python file and print a report."""

import argparse
import sys

from .analyzer import analyze_file, format_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analyse a Python file for code review.")
    parser.add_argument("path", help="Path to a Python file to analyse")
    args = parser.parse_args(argv)

    try:
        report = analyze_file(args.path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.path}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Error reading file: {exc}", file=sys.stderr)
        return 2

    print(format_report(report))
    return 1 if report.get("error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
