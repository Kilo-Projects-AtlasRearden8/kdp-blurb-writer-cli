"""Blurb generation providers."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from abc import ABC, abstractmethod


class ProviderError(RuntimeError):
    """Raised when a blurb provider fails."""


class BlurbProvider(ABC):
    """Interface for blurb generation backends."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a blurb from the given prompt."""


class OpenAICompatibleProvider(BlurbProvider):
    """Calls an OpenAI-compatible chat completions endpoint (e.g. Ollama)."""

    def __init__(self, endpoint: str, model: str = "") -> None:
        self.endpoint = endpoint.rstrip("/")
        self.model = model

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            self.endpoint,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise ProviderError(f"could not reach endpoint {self.endpoint}: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise ProviderError(f"invalid JSON from endpoint {self.endpoint}: {exc}") from exc

        try:
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise ProviderError(f"unexpected response from endpoint: {exc}") from exc
