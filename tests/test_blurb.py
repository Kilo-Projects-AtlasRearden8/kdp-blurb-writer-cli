"""Tests for prompt/blurb building."""

import unittest

from kdp_blurb_writer.blurb import build_prompt
from kdp_blurb_writer.config import VALID_LENGTHS, VALID_TONES


class TestBlurbBuilding(unittest.TestCase):
    def test_prompt_contains_premise(self) -> None:
        prompt = build_prompt(
            "A nurse discovers a time-traveling stethoscope", "warm", "medium"
        )
        self.assertIn("A nurse discovers a time-traveling stethoscope", prompt)

    def test_all_tone_and_length_combinations(self) -> None:
        for tone in VALID_TONES:
            for length in VALID_LENGTHS:
                prompt = build_prompt("A robot opens a bakery", tone, length)
                self.assertIsInstance(prompt, str)
                self.assertGreater(len(prompt), 0)

    def test_length_changes_prompt(self) -> None:
        short = build_prompt("A robot opens a bakery", "warm", "short")
        long = build_prompt("A robot opens a bakery", "warm", "long")
        self.assertNotEqual(short, long)

    def test_unknown_tone_raises(self) -> None:
        with self.assertRaises(KeyError):
            build_prompt("A robot opens a bakery", "not-a-tone", "medium")
