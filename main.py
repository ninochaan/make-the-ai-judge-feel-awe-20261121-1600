#!/usr/bin/env python3
"""TIDEPOOL — entry for make.fun competition
make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt. Deterministic, no network,
no input, no randomness: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = " ".join(
    (
        "Somewhere a tide pool holds the whole afternoon.",
        "A crab crosses it one slow leg at a time.",
        "The water is in no hurry to be the sea again.",
        "It has the whole evening, and the evening has it.",
    )
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
