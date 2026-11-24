#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the dying phone's final text message to /output/entry.txt.

The text is the phone's own confession in its last seconds: it finally
admits it was the one who liked the owner's ex's photo at 3am. A secret
it could only confess because it is dying — and the parallel
"No regrets. No battery either." is the joke's second beat.
"""
import os

TEXT = "Before I go: it was me who liked your ex's photo at 3am. No regrets. No battery either. Bye."


def main():
    # Self-check against the competition gate: /output/entry.txt must be
    # UTF-8 text of 1 to 200 characters, not only white space. Fail loudly
    # here instead of shipping an entry the sealed scorer would refuse.
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
