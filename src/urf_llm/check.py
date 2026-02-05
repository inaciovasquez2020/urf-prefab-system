from __future__ import annotations

import sys
import json
from typing import List, Tuple


def tokenize(text: str) -> List[str]:
    text = text.lower()
    tokens = []
    current = ""

    for ch in text:
        if ch.isalnum():
            current += ch
        else:
            if current:
                tokens.append(current)
                current = ""
    if current:
        tokens.append(current)

    return tokens


CLR_FORBIDDEN = [
    ["locally", "indistinguishable", "everywhere", "forever"],
    ["perfectly", "uniform", "local", "view", "for", "all", "radii"],
    ["cycles", "do", "not", "force", "any", "local", "difference"],
]

AKR_FORBIDDEN = [
    ["weak", "but", "persistent", "global", "influence"],
    ["hidden", "long", "range", "mode", "survives", "decay"],
    ["effect", "persists", "without", "local", "support"],
]


def contains_phrase(tokens: List[str], phrase: List[str]) -> bool:
    n = len(phrase)
    for i in range(len(tokens) - n + 1):
        if tokens[i:i + n] == phrase:
            return True
    return False


def check(tokens: List[str]) -> Tuple[bool, bool]:
    clr_ok = True
    akr_ok = True

    for phrase in CLR_FORBIDDEN:
        if contains_phrase(tokens, phrase):
            clr_ok = False

    for phrase in AKR_FORBIDDEN:
        if contains_phrase(tokens, phrase):
            akr_ok = False

    return clr_ok, akr_ok


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    text = sys.stdin.read()
    tokens = tokenize(text)
    clr_ok, akr_ok = check(tokens)

    verdict = "ACCEPT" if (clr_ok and akr_ok) else "REJECT"

    if args.json:
        print(json.dumps({
            "verdict": verdict,
            "clr_ok": clr_ok,
            "akr_ok": akr_ok,
            "token_count": len(tokens)
        }))
    else:
        print(verdict)

    if verdict == "ACCEPT":
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()

