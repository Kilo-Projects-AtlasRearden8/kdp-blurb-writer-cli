"""Tests for the command-line interface."""

import os
import tempfile
import unittest

from kdp_blurb_writer.cli import main


class TestCLI(unittest.TestCase):
    def test_mock_run_prints_blurb(self) -> None:
        rc = main(
            ["A robot nurse opens a bakery", "--mock", "--tone", "warm", "--length", "short"]
        )
        self.assertEqual(rc, 0)

    def test_out_writes_markdown_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "blurb.md")
            rc = main(
                ["A robot nurse opens a bakery", "--mock", "--out", path]
            )
            self.assertEqual(rc, 0)
            self.assertTrue(os.path.exists(path))
            with open(path, encoding="utf-8") as handle:
                content = handle.read()
            self.assertIn("A robot nurse opens a bakery", content)
            self.assertTrue(content.startswith("# "))
