#!/usr/bin/env python3
"""The Dog Reviews the Mailman — one funny one-line review, under 200 chars.

Writes the review to /output/entry.txt.
"""

import os

ENTRY = (
    "One star. He comes every single day, stuffs paper through my slot, "
    "and has never once brought me a treat — so I bark. That is the review."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
