#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

The program writes one sentence (at most 200 characters) pitching a
bizarre startup idea that sounds like a joke until the business logic
clicks: a sock subscription where the missing sock is the growth loop.
"""

import os

PITCH = (
    "We mail subscribers one sock a month \u2014 the matching sock ships "
    "only when they refer a friend, turning lost laundry into a referral engine."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    pitch = PITCH.strip()
    assert pitch, "pitch must not be empty"
    assert len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars, over {MAX_CHARS}"
    assert pitch.count(".") == 1 and pitch.endswith("."), "pitch must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(pitch + "\n")
    print(f"wrote {len(pitch)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
