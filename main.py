#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one funny line — the reply a hopeless tech support agent gives a
desperate customer after the restart ritual goes sideways — to
/output/entry.txt. Standard library only.

v2: the write is atomic (temp file in /output, then os.replace), and the
entry is also guarded by UTF-8 byte length (1-199 bytes) in addition to
the character-length guard.
"""

import os
import sys
import tempfile

ENTRY = "I turned it off and on again, sir \u2014 twice. The second time it beeped, which is either progress or the modem asking for a divorce."

MAX_CHARS = 199
MAX_BYTES = 199
OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("entry length %d chars out of range 1-%d" % (len(ENTRY), MAX_CHARS), file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    entry_bytes = ENTRY.encode("utf-8")
    if not 1 <= len(entry_bytes) <= MAX_BYTES:
        print("entry length %d UTF-8 bytes out of range 1-%d" % (len(entry_bytes), MAX_BYTES), file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir="/output", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
