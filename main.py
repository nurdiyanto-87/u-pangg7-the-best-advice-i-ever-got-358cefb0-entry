#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one single sentence, about the best advice the writer ever
received, to /output/entry.txt. Pure Python standard library only;
no third-party packages.
"""

import os

ADVICE = (
    "My English teacher, handing back my worst essay, said, "
    "'Write it badly first \u2014 a bad draft is a door, a blank page "
    "is a wall,' and I've opened that door ever since."
)


def main() -> None:
    # The sealed scorer gates on 1-200 chars of UTF-8 text, not only
    # whitespace, in a single sentence. Fail loudly here rather than
    # ship an entry the gate would refuse.
    assert 1 <= len(ADVICE) <= 200, "advice must be 1-200 characters"
    # Exactly one sentence: a single terminal period and no other
    # sentence-ending punctuation anywhere in the line.
    assert ADVICE.count(".") == 1 and ADVICE.endswith("."), (
        "advice must be exactly one sentence"
    )
    assert "?" not in ADVICE and "!" not in ADVICE, (
        "advice must be exactly one sentence"
    )
    # The line must quote what was actually said, not paraphrase a slogan.
    assert "'" in ADVICE, "advice must quote what was actually said"
    assert "\n" not in ADVICE, "advice must be a single line"
    assert ADVICE.strip(), "advice must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
