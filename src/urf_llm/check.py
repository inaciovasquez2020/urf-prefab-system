from __future__ import annotations

import json
import sys
from typing import List, Tuple


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

