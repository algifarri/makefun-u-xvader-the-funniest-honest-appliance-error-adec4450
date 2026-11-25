#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes a single line (at most 200 characters) to /output/entry.txt:
the funniest honest error message an appliance could show.

The line is fixed and deterministic: a toaster confessing, in its own
flat voice, that its heating element has never toasted both sides of
a slice evenly. The humour comes from the truth of the fault, not
from a pun bolted on.
"""

import os

ENTRY = (
    "ERROR: Setting 3 toasts one side. Setting 4 burns both. "
    "There is no setting that toasts both sides. There never was."
)
# 116 characters: one line, no trailing newline in the entry itself,
# so the gate counts exactly the message the toaster would show.


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
