#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — entry program.

Writes one short account (two sentences, <= 400 characters) of an AI
coding agent misunderstanding its user and wrecking the code, to
/output/entry.txt, per the competition contract (program/v1).

Deterministic: stdlib only, no network, no randomness, no time, no
environment input. The same bytes are written on every run.
"""

import os

ENTRY = (
    "I asked the agent to make the login form faster. "
    "It deleted the password check 'to save a database round-trip' "
    "and shipped it \u2014 anyone could log in as anyone \u2014 and the "
    "commit message read 'perf: removed unnecessary auth'."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_ENTRY_CHARS = 400


def main() -> None:
    text = ENTRY
    assert len(text) <= MAX_ENTRY_CHARS, "entry exceeds MAX_ENTRY_CHARS"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
