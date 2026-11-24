"""Output the 24 November 2026 world-news summary image (v2).

Deterministic: reads the bundled JPEG and writes its exact bytes to stdout.
No network access, no randomness, no time dependence.
"""

import sys
from pathlib import Path

IMAGE = Path(__file__).with_name("news-20261124.jpg")


def main() -> None:
    sys.stdout.buffer.write(IMAGE.read_bytes())


if __name__ == "__main__":
    main()
