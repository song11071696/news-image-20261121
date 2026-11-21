#!/usr/bin/env python3
"""Render the news of 21 November 2026 into a single image.

The program copies ``entry.png`` (stored next to this file) to
``/output/entry.png``. The image is a fixed, pre-rendered illustration
summing up the day's world news in one picture. Copying bytes is
deterministic: two runs on the same input produce identical output.

Standard library only; Python 3.13 or newer.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output") / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image not found: {SOURCE}")
    with SOURCE.open("rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print(f"error: source is not a valid PNG: {SOURCE}", file=sys.stderr)
            return 1
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    source_digest = digest(SOURCE)
    dest_digest = digest(DEST)
    if source_digest != dest_digest:
        DEST.unlink(missing_ok=True)
        print(
            f"error: copy verification failed: {SOURCE} (sha256={source_digest}) "
            f"!= {DEST} (sha256={dest_digest}); incomplete output removed",
            file=sys.stderr,
        )
        return 1
    print(f"Wrote {DEST} ({DEST.stat().st_size} bytes, sha256={dest_digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
