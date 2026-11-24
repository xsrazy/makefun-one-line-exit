"""The One-Line Exit: a resignation letter exactly one line long.

Writes the letter to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
with no trailing newline.
"""

LINE = (
    "Dear Manager, I quit: the coffee machine got replaced before I got a "
    "raise, and honestly, it earned it first."
)

assert 1 <= len(LINE) <= 140 and LINE.strip(), "gate: line must be 1-140 chars, not blank"


def main() -> None:
    import os
    from pathlib import Path

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
