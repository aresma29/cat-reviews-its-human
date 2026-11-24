"""Print the one-star cat review from entry.txt.

Resolves entry.txt relative to this file, so the grader can run it
from any working directory on a read-only filesystem.
"""
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").rstrip("\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
