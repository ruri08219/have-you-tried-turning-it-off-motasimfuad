#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one funny line — the reply a hopeless tech support agent gives a
desperate customer after the restart ritual goes sideways — to
/output/entry.txt. Standard library only.
"""

import os
import sys

ENTRY = "I turned it off and on again, sir \u2014 twice. The second time it beeped, which is either progress or the modem asking for a divorce."

MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("entry length %d chars out of range 1-%d" % (len(ENTRY), MAX_CHARS), file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
