"""Markdown export for generated blurbs."""

from __future__ import annotations

from pathlib import Path


def export_markdown(blurb: str, title: str, out_path: str) -> Path:
    """Write the blurb to a Markdown file and return the path."""
    content = f"# {title}\n\n{blurb}\n"
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path
