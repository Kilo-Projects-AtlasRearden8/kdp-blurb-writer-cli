"""Tests for Markdown export."""

import os
import tempfile
import unittest

from kdp_blurb_writer.export import export_markdown


class TestExport(unittest.TestCase):
    def test_writes_markdown_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "my-blurb.md")
            returned = export_markdown("# Blurb\n\nHello world.", "Test Book", path)
            self.assertEqual(str(returned), path)
            with open(path, encoding="utf-8") as handle:
                content = handle.read()
            self.assertIn("Test Book", content)
            self.assertIn("Hello world.", content)

    def test_creates_parent_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "sub", "dir", "blurb.md")
            export_markdown("# Blurb\n\nText.", "Book", path)
            self.assertTrue(os.path.exists(path))
