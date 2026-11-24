"""The One-Line Exit: a resignation letter exactly one line long.

The letter is a single line of 109 characters: a manager-facing
resignation that jokes the office coffee machine got replaced before
the writer got a raise. Built for make.fun's "The One-Line Exit"
bounty (u-kreutzx-the-one-line-exit-1dc652d1, $2 in USDC).

Writes the letter to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) with no trailing newline, so the entry file is
exactly one line.
"""

import os
from pathlib import Path

LINE = (
    "Dear Manager, I quit: the coffee machine got replaced before I got a "
    "raise, and honestly, it earned it first."
)

# Competition gate: the entry must be a single non-blank line of
# 1-140 characters. Checked at import so a bad line fails loudly
# instead of producing a silent invalid entry.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "gate: line must be 1-140 chars, not blank"


def write_entry() -> Path:
    """Write LINE to entry.txt in the output directory and return its path."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(LINE.encode("utf-8"))
    return out_path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
