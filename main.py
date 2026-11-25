#!/usr/bin/env python3
"""Entry point for the 2026-11-24 make.fun news-image submission.

Reads the bundled news image that sits next to this script and streams
its bytes to standard output unchanged. The program is fully
deterministic: it performs no network access, uses no randomness or
clock, and touches no file other than the bundled image.
"""

import sys
from pathlib import Path


def main() -> int:
    image_path = Path(__file__).resolve().parent / "news-20261124.jpg"
    with open(image_path, "rb") as handle:
        sys.stdout.buffer.write(handle.read())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
