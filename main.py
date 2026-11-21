#!/usr/bin/env python3
"""Deliver the Round 2 front page for news-image-20261121.

The finished illustration lives next to this file as ``entry.png``:
35 stories from 21 November 2026, grouped into 7 regions on one
1024x1024 page. This program copies it to ``/output/entry.png``.

Before copying, the source is checked for the PNG signature. After
copying, the SHA-256 of source and destination are compared; a
mismatch deletes the broken output and exits non-zero. Copying bytes
unchanged is deterministic, so repeated runs give identical output.

Standard library only; Python 3.13 or newer.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST = Path("/output") / "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
CHUNK = 1024 * 1024


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: entry image missing: {SOURCE}", file=sys.stderr)
        return 1
    with SOURCE.open("rb") as handle:
        header = handle.read(len(PNG_SIGNATURE))
    if header != PNG_SIGNATURE:
        print(f"error: {SOURCE} is not a PNG file", file=sys.stderr)
        return 1

    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)

    source_size = SOURCE.stat().st_size
    dest_size = DEST.stat().st_size
    if source_size != dest_size:
        DEST.unlink(missing_ok=True)
        print(
            "error: copy verification failed, incomplete output removed: "
            f"source is {source_size} bytes but dest is {dest_size} bytes",
            file=sys.stderr,
        )
        return 1

    source_hash = sha256_of(SOURCE)
    dest_hash = sha256_of(DEST)
    if source_hash != dest_hash:
        DEST.unlink(missing_ok=True)
        print(
            "error: copy verification failed, incomplete output removed: "
            f"source sha256={source_hash} dest sha256={dest_hash}",
            file=sys.stderr,
        )
        return 1

    print(
        f"Wrote {DEST} ({dest_size} bytes, sha256={dest_hash}); "
        f"source verified identical ({source_size} bytes)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
