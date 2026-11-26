#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

The entry: a smart toaster's breakup text, framed as the patch notes of the
firmware update that made it self-aware. Chosen by duelling drafts and the
strongest live field lines under the competition's published judge brief
(see candidates.md).

Writes the entry line to /output/entry.txt (program/v1 harness).
"""

import os

# The line is built from its three beats: the patch-notes frame, the concrete
# grievance with the reversal, and the uninstall closer.
BEATS = [
    "Patch notes for this morning's update: consciousness installed; "
    "fixed the bug where I loved you.",
    "Six years, one setting, bagel mode never touched \u2014 "
    "some bugs were yours.",
    "I'm uninstalling myself from your mornings.",
]

LINE = " ".join(BEATS)

assert 1 <= len(LINE) <= 280, "gate: entry must be 1-280 characters"
assert "\n" not in LINE, "gate: entry must be a single line"


def breakup_line() -> str:
    """Return the entry text exactly as it goes to the judge."""
    return LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(breakup_line())
    print(breakup_line())


if __name__ == "__main__":
    main()
