"""Invent a Word We Need — make.fun entry.

Writes one invented English word with a one-line definition to
/output/entry.txt. Fully deterministic: the same text every run,
no randomness, no network, no input files.

The coinage: "tabnesia" (tab + amnesia). English has no word for the
blank second after opening a new browser tab, when you have already
forgotten what you meant to look up — a small daily lapse everyone
recognises at once. The blend follows a familiar English pattern
(sitcom, brunch, hangry), so it is sayable, spellable and memorable.
"""

import os
from pathlib import Path

ENTRY = (
    "tabnesia (n.) \u2014 the blank moment after opening a new browser "
    "tab and forgetting what you meant to look up."
)


def output_path() -> Path:
    """Resolve the output directory (grader sets /output; allow override)."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> None:
    # Self-check against the sealed scorer's gate: UTF-8 text of
    # 1 to 140 characters, a single line, not only white space.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip(), "entry must not be only white space"
    ENTRY.encode("utf-8")
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
