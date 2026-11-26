#!/usr/bin/env python3
"""Name the Robot Band entry generator (make.fun).

Writes one entry line -- a funny robot band name plus a few words on its
hit song -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only.
"""

import os

# Band name + hit song. Target: under 200 chars, lands on first read.
ENTRY = (
    "The Firmware Updates \u2014 "
    "Please Do Not Power Off (I\u2019m Almost Done)"
)


def output_dir() -> str:
    """Resolve the output directory, honoring MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_text() -> str:
    """Return the entry line, stripped and guaranteed non-empty."""
    text = ENTRY.strip()
    if not text:
        raise RuntimeError("entry text is empty")
    return text


def write_entry() -> str:
    """Write the entry to <output_dir>/entry.txt and return the path."""
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())
    return path


def main() -> None:
    path = write_entry()
    count = len(entry_text())
    print(f"wrote {path} ({count} chars)")


if __name__ == "__main__":
    main()
