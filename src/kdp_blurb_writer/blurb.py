"""Prompt templates for KDP blurb generation."""

TONE_GUIDANCE = {
    "professional": "Polished, confident tone suited to nonfiction and business readers.",
    "warm": "Warm, approachable tone, like a recommendation from a trusted friend.",
    "hype": "Energetic, high-stakes tone that builds excitement and urgency.",
    "mysterious": "Intriguing tone that holds back just enough to keep readers guessing.",
    "minimal": "Tight, spare writing with short sentences and no fluff.",
    "friendly": "Casual, friendly tone as if chatting over coffee.",
}

LENGTH_GUIDANCE = {
    "short": "Two short paragraphs: hook, stakes, one-line call to action.",
    "medium": "Three to four paragraphs: hook, conflict, stakes, call to action.",
    "long": "Five or more paragraphs with character depth, setting, conflict, stakes, and a strong call to action.",
}

SYSTEM_REMINDER = (
    "You write Kindle Direct Publishing (KDP) book blurbs that sell. "
    "Return only the blurb text, with no labels, headings, or quotation marks around it. "
    "Do not mention that you are an AI."
)

GUIDELINES = (
    "- Open with a strong hook in the first line or two.\n"
    "- Establish the main character, setting, and central conflict without spoilers.\n"
    "- Make the stakes clear so readers care.\n"
    "- End with a clear call to action encouraging readers to buy or read.\n"
)


def build_prompt(premise: str, tone: str, length: str) -> str:
    """Build the prompt sent to the language model."""
    return "\n".join(
        [
            SYSTEM_REMINDER,
            "",
            "Task: Write a compelling book blurb based on the premise below.",
            "",
            f"Premise: {premise}",
            "",
            f"Tone: {tone} - {TONE_GUIDANCE[tone]}",
            f"Length: {length} - {LENGTH_GUIDANCE[length]}",
            "",
            "Guidelines:",
            GUIDELINES,
            "Blurb:",
        ]
    )
