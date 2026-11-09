#!/usr/bin/env python3
"""Generate the Manus entry point from skills/elevate/SKILL.md.

Run after editing the canonical skill. Use --check to verify without writing.
The nested skill remains the source for Claude Code and release archives.
"""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "elevate" / "SKILL.md"
TARGET = ROOT / "SKILL.md"
NOTICE = (
    "<!-- Generated from skills/elevate/SKILL.md by scripts/sync_root_skill.py. "
    "Edit the source, then run the script. -->\n\n"
)


def render():
    source = SOURCE.read_text(encoding="utf-8")
    header, body = source.split("\n---\n", 1)
    body = body.replace("references/", "skills/elevate/references/")
    return header + "\n---\n\n" + NOTICE + body.lstrip("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    paths = re.findall(r"skills/elevate/references/[\w-]+\.md", expected)
    for path in paths:
        if not (ROOT / path).is_file():
            raise SystemExit(f"Missing bundled reference: {path}")
    if args.check:
        if not TARGET.is_file() or TARGET.read_text(encoding="utf-8") != expected:
            raise SystemExit("Root SKILL.md is out of date. Run scripts/sync_root_skill.py.")
        print(f"Root skill matches the source; {len(set(paths))} references resolve.")
    else:
        with TARGET.open("w", encoding="utf-8", newline="\n") as output:
            output.write(expected)
        print("Updated root SKILL.md for Manus GitHub import.")


if __name__ == "__main__":
    main()
