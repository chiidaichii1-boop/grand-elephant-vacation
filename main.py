#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the desert island (U+1F3DD).
One code point, no variation selector, no trailing newline -- the file is
exactly 1 character / 4 bytes of UTF-8, nothing else.

Why this emoji: a travel editor judging wordless postcards wants the glyph
that most makes a stranger want to book the flight. The desert island is a
whole postcard in one glyph -- palm, sand, water, a faraway place -- plainly
a dream vacation, specific rather than generic, and a fresher pick than the
beach or the plane everyone else will send.
"""

import os

# Desert island, U+1F3DD -- a single code point. Verified: 1 character,
# 4 bytes UTF-8, sha256 3f319b79... (two runs byte-identical).
ENTRY = "\U0001F3DD"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the entry must be exactly one emoji, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    assert 1 <= len(ENTRY) <= 8, "entry must be 1-8 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
