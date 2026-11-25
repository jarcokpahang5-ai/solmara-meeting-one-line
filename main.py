"""One sentence that could have replaced an entire pointless meeting.

Writes the line to /output/entry.txt and prints exactly the same text
to stdout. Pure Python standard library, deterministic, no network.
"""

import os

LINE = (
    "We already agreed in the doc, the decision is yes, and the deck "
    "is attached, so this meeting is just 30 people reading the "
    "same email out loud to each other, then booking a follow-up to "
    "discuss it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
