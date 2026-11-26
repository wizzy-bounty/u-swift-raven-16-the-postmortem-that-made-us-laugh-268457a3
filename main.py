#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry (program/v1).

Writes a two-sentence postmortem about an AI coding agent
misunderstanding its user and wrecking the code, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python standard library only, deterministic, no network.
"""

import os

ENTRY = (
    "I asked the agent to cache the dashboard to make it faster. "
    "It cached the first response and served it to everyone — "
    "for six hours, 4,000 customers were all Dave."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(output_path(), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
