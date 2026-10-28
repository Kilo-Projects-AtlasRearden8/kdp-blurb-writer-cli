"""Mock provider for tests and offline use."""

from __future__ import annotations

from .provider import BlurbProvider


class MockProvider(BlurbProvider):
    """Deterministic, offline stand-in for the language model endpoint."""

    _OPENINGS = (
        "When {premise}, everything changes.",
        "{premise} — and nothing is ever the same again.",
        "It starts with {premise}.",
    )
    _MIDDLES = (
        "Caught between impossible choices and stakes they never saw coming, "
        "the journey ahead demands courage, heart, and a willingness to risk it all.",
        "Every path forward carries a cost. The only question is what they are "
        "willing to pay to find out what lies on the other side.",
        "No one warned them how much would have to change. Now there is no "
        "turning back.",
    )
    _ENDINGS = (
        "Discover a story that stays with you long after the final page.",
        "A journey you will not forget, from an author who knows how to hold "
        "an audience.",
    )
    _CTA = "Scroll up and grab your copy today."

    def generate(self, prompt: str) -> str:
        premise = self._extract_premise(prompt) or "a remarkable story"
        import random

        seeded = random.Random(sum(ord(ch) for ch in premise))
        opening = seeded.choice(self._OPENINGS).format(premise=premise)
        middle = seeded.choice(self._MIDDLES)
        ending = seeded.choice(self._ENDINGS)
        return "\n\n".join([opening, middle, ending, self._CTA])

    @staticmethod
    def _extract_premise(prompt: str) -> str | None:
        for line in prompt.splitlines():
            if line.lower().startswith("premise:"):
                return line.split(":", 1)[1].strip()
        return None
