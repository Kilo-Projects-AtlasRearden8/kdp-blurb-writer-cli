"""Command-line interface for the KDP blurb writer."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from .blurb import build_prompt
from .config import (
    DEFAULT_ENDPOINT,
    DEFAULT_LENGTH,
    DEFAULT_MODEL,
    DEFAULT_TONE,
    VALID_LENGTHS,
    VALID_TONES,
)
from .export import export_markdown
from .mock_provider import MockProvider
from .provider import BlurbProvider, OpenAICompatibleProvider, ProviderError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kdp-blurb-writer",
        description="Write a KDP book blurb from a short premise using a local, "
        "OpenAI-compatible endpoint (default Ollama).",
    )
    parser.add_argument("premise", help="Short premise or idea for the book.")
    parser.add_argument(
        "--tone",
        default=DEFAULT_TONE,
        choices=list(VALID_TONES),
        help="Tone of the blurb (default: %(default)s).",
    )
    parser.add_argument(
        "--length",
        default=DEFAULT_LENGTH,
        choices=list(VALID_LENGTHS),
        help="Length of the blurb (default: %(default)s).",
    )
    parser.add_argument(
        "--endpoint",
        default=DEFAULT_ENDPOINT,
        help="OpenAI-compatible chat completions URL (default: %(default)s).",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Model name. Ollama works fine without this (default: %(default)s).",
    )
    parser.add_argument(
        "--out",
        help="Write the blurb to a Markdown file at this path instead of printing it.",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use the built-in mock provider instead of calling the endpoint.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    provider: BlurbProvider = (
        MockProvider() if args.mock else OpenAICompatibleProvider(args.endpoint, args.model)
    )

    prompt = build_prompt(args.premise, args.tone, args.length)
    try:
        blurb = provider.generate(prompt)
    except ProviderError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.out:
        path = export_markdown(blurb, args.premise, args.out)
        print(f"Wrote blurb to {path}")
    else:
        print(blurb)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
