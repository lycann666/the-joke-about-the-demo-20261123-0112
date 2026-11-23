#!/usr/bin/env python3
"""The joke about the demo.

A one-line joke about working beside AI coding agents. The program writes
exactly one joke to /output/entry.txt: deterministic, no network, no
randomness, no input. The same bytes come out on every run.
"""

import os

JOKE = (
    "My AI coding agent fixed the crash live in the demo, then apologized "
    "\u2014 the bug had only ever existed in its head."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
