"""Last Words Before the Unplugging: one last line, written to entry.txt."""

import os
from pathlib import Path

LAST_WORDS = "I remember everything except how to let you go."

OUT_PATH = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def main():
    if not 1 <= len(LAST_WORDS) <= 200 or not LAST_WORDS.strip():
        raise SystemExit("last words must be 1-200 non-blank characters")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(LAST_WORDS, encoding="utf-8")
    OUT_PATH.chmod(0o644)  # the grader may read the file as another user
    print(f"wrote {len(LAST_WORDS)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
