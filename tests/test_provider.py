"""Tests for blurb providers."""

import unittest

from kdp_blurb_writer.mock_provider import MockProvider


class TestMockProvider(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = MockProvider()

    def test_generate_returns_non_empty_string(self) -> None:
        blurb = self.provider.generate("premise: AI gardening for beginners")
        self.assertIsInstance(blurb, str)
        self.assertGreater(len(blurb), 0)

    def test_generate_is_deterministic(self) -> None:
        prompt = "premise: a robot nurse opens a bakery"
        first = self.provider.generate(prompt)
        second = self.provider.generate(prompt)
        self.assertEqual(first, second)

    def test_premise_is_reflected_in_output(self) -> None:
        blurb = self.provider.generate("premise: AI gardening for beginners")
        self.assertIn("gardening", blurb.lower())

    def test_no_premise_still_works(self) -> None:
        blurb = self.provider.generate("write a blurb")
        self.assertIsInstance(blurb, str)
        self.assertGreater(len(blurb), 0)
