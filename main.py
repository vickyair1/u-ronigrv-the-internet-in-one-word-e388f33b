#!/usr/bin/env python3
"""The Internet in One Word: a single word for the whole internet.

Writes exactly the word to /output/entry.txt, no trailing newline.
"""

import os

# The word: the whole internet, every app and every argument, is just
# strangers yapping at each other non-stop. Funny on its own, true of the
# internet as a whole, and not the obvious word anyone reaches for.
LINE = "yapping"


MAX_CHARS = 30


def normalize_line(line: str) -> str:
    """Collapse accidental double spaces and strip edge whitespace.

    Defensive formatting only: the sealed word is already clean, so this
    returns it byte-identical.
    """
    return " ".join(line.split())


def get_line() -> str:
    """Return the entry word, normalized."""
    return normalize_line(LINE)


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the word to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the sealed scorer needs 1-30 chars, UTF-8, not only
    whitespace, and exactly ONE word (no spaces at all). Fail loudly here
    rather than ship an invalid entry."""
    assert 1 <= len(line) <= MAX_CHARS, "word must be 1-30 characters"
    line.encode("utf-8")
    assert line.strip() == line and " " not in line and "\n" not in line, \
        "must be a single clean word"


def main() -> None:
    line = get_line()
    validate_line(line)
    write_entry(line)


if __name__ == "__main__":
    main()
