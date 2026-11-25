#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes our own make.fun username and nothing else — one word, at most
30 characters — to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "hazel-fox-13-7204"


def main():
    # Fail fast if the entry ever stops being one word of at most 30 chars.
    if len(LINE) > 30 or len(LINE.split()) != 1:
        raise SystemExit("LINE must be one word of at most 30 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
