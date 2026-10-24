"""Write the digest markdown to a dated file for Obsidian/Notion."""

from __future__ import annotations

import os
from datetime import datetime, timezone

from .. import config


def write_archive(markdown: str) -> str:
    """Write markdown to archive/YYYY-MM-DD-devops-digest.md and return the path."""
    os.makedirs(config.ARCHIVE_DIR, exist_ok=True)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(config.ARCHIVE_DIR, f"{date}-devops-digest.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    return path
