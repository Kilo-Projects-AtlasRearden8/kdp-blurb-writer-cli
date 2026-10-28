"""Configuration for the KDP blurb writer."""

DEFAULT_ENDPOINT = "http://localhost:11434/v1/chat/completions"
DEFAULT_MODEL = ""
DEFAULT_TONE = "warm"
DEFAULT_LENGTH = "medium"

VALID_TONES = ("professional", "warm", "hype", "mysterious", "minimal", "friendly")
VALID_LENGTHS = ("short", "medium", "long")
