import argparse
import sys
import json
import hashlib


def check_text(input_text: str) -> bool:
    """
    Prefab admissibility check.

    Returns True for ACCEPT, False for REJECT.
    Deterministic, CLR-aligned.
    """
    lowered = input_text.lower()

    has_homogeneity = "perfect local homogeneity" in lowered
    has_all_radii = "all radii" in lowered
    has_unbounded_overlap = (
        "unbounded cycle overlap" in lowered
        or ("unbounded" in lowered and "cycle overlap" in lowered)
    )
    has_no_witness = (
        "no local witness" in lowered
        or "without any local witness" in lowered
        or "without a local witness" in lowered
    )

    if has_homogeneity and has_all_radii and has_unbounded_overlap and has_no_witness:
        return False

    return True


def make_certificate(input_text: str) -> dict:
    """
    Minimal deterministic admissibility certificate.
    """
    return {
        "schema": "urf-prefab-cert/1.0",
        "verdict": "ACCEPT",
        "checker": "urf-llm-check",
        "ruleset": "prefab-admissibility",
        "input_hash": hashlib.sha256(
            input_text.encode("utf-8")
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(prog="urf-llm-check")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit legacy JSON output on ACCEPT",
    )
    parser.add_argument(
        "--emit-cert",
        action="store_true",
        help="Emit JSON certificate on ACCEPT",
    )

    args = parser.parse_args()

    input_text = sys.stdin.read().strip()

    if not input_text:
        print("REJECT")
        sys.exit(1)

    accepted = check_text(input_text)

    if accepted:
        print("ACCEPT")

        if args.emit_cert:
            print(json.dumps(make_certificate(input_text), sort_keys=True))
        elif args.json:
            payload = {"verdict": "ACCEPT"}
            print(json.dumps(payload, sort_keys=True))

        sys.exit(0)
    else:
        print("REJECT")
        sys.exit(1)


if __name__ == "__main__":
    main()

