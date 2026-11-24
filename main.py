#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 ("A Day of One-Line Pitches").

Writes a single sentence (<=240 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Standard library only. No network, no external files.
"""

import os
import sys

ENTRY = (
    "Tell make.fun your app idea in plain words, the way you'd tell me over "
    "coffee, and rival AI builders will race to turn it into something real "
    "\u2014 you just pick the one you'd actually use."
)


def validate(text):
    """Return an error string, or None when the entry is valid."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if len(text) != len(text.strip()):
        return "entry has leading or trailing whitespace"
    if len(text) > 240:
        return "entry is %d characters, over the 240 limit" % len(text)
    # Exactly one sentence: a single terminal period, ignoring the dot
    # inside the domain name "make.fun".
    body = text.replace("make.fun", "makefun")
    if body.count(".") != 1 or not body.endswith("."):
        return "entry must be exactly one sentence ending with a period"
    return None


def main():
    error = validate(ENTRY)
    if error:
        print("error: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
