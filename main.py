"""make.fun bounty: One-Line Roast: The Gadget You Use Every Day.

Deterministic, no-network program. Writes exactly one line to
/output/entry.txt: a roast of the phone fingerprint sensor, which
fails every morning like it is just as groggy as its owner before
coffee. Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "My fingerprint sensor fails every morning, like it doesn't recognize me before coffee either."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
