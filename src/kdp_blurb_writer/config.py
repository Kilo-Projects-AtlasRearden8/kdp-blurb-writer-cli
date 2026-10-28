"""Configuration for the KDP blurb writer."""

from dataclasses import dataclass

DEFAULT_ENDPOINT = "http://localhost:11434/v1/chat/completions"
DEFAULT_MODEL = ""
DEFAULT_TONE = "warm"
DEFAULT_LENGTH = "medium"

VALID_TONES = ("professional", "warm", "hype", "mysterious", "minimal", "friendly")
VALID_LENGTHS = ("short", "medium", "long")


@dataclass
class Config:
    endpoint: str = DEFAULT_ENDPOINT
    model: str = DEFAULT_MODEL
    tone: str = DEFAULT_TONE
    length: str = DEFAULT_LENGTH
    out: str | None = None
    mock: bool = False
