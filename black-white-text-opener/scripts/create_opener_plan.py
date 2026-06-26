#!/usr/bin/env python3
"""Generate a timing plan for a black-background white-text opener."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PRESETS = {
    "micro": {
        "duration": 3.0,
        "beats": [
            ("black_hold", 0.0, 0.2),
            ("hero_reveal", 0.2, 0.9),
            ("first_change", 0.9, 1.7),
            ("final_hold", 1.7, 2.5),
            ("transition_out", 2.5, 3.0),
        ],
    },
    "standard": {
        "duration": 5.4,
        "beats": [
            ("black_hold", 0.0, 0.3),
            ("hero_reveal", 0.3, 1.2),
            ("hero_hold", 1.2, 2.2),
            ("replacement", 2.2, 3.4),
            ("final_hold", 3.4, 4.7),
            ("transition_out", 4.7, 5.4),
        ],
    },
    "slow": {
        "duration": 7.0,
        "beats": [
            ("black_hold", 0.0, 0.5),
            ("hero_reveal", 0.5, 1.6),
            ("hero_hold", 1.6, 3.0),
            ("replacement", 3.0, 4.7),
            ("final_hold", 4.7, 6.3),
            ("transition_out", 6.3, 7.0),
        ],
    },
}


def build_plan(args: argparse.Namespace) -> dict:
    preset = PRESETS[args.preset]
    replacements = args.replace or []
    final = args.final or (replacements[-1] if replacements else args.title)
    beats = []
    for name, start, end in preset["beats"]:
        text = ""
        motion = ""
        if name == "black_hold":
            motion = "pure black, no text"
        elif name == "hero_reveal":
            text = args.title
            motion = "opacity fade plus slight blur-to-sharp reveal"
        elif name == "hero_hold":
            text = args.title
            motion = "hold readable phrase"
        elif name in {"first_change", "replacement"}:
            text = " -> ".join(replacements) if replacements else args.title
            motion = "replace key words with horizontal smear or crossfade"
        elif name == "final_hold":
            text = final
            motion = "large white final phrase hold"
        elif name == "transition_out":
            text = final
            motion = args.transition
        beats.append(
            {
                "name": name,
                "start": start,
                "end": end,
                "duration": round(end - start, 3),
                "text": text,
                "motion": motion,
            }
        )

    return {
        "title": args.title,
        "replace": replacements,
        "final": final,
        "preset": args.preset,
        "duration": preset["duration"],
        "ratio": args.ratio,
        "style": {
            "background": "#000000",
            "text": "#ffffff",
            "font": "clean sans-serif",
            "avoid": ["colored flash", "busy gradient", "persistent neon-line background"],
        },
        "beats": beats,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a black-white text opener timing plan.")
    parser.add_argument("--title", required=True, help="Primary opening phrase.")
    parser.add_argument("--replace", nargs="*", default=[], help="Optional replacement words or phrases.")
    parser.add_argument("--final", default="", help="Final hold phrase.")
    parser.add_argument("--preset", choices=sorted(PRESETS), default="standard")
    parser.add_argument("--ratio", default="16:9")
    parser.add_argument("--transition", default="white velocity wipe into next scene")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    plan = build_plan(args)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(args.out), "duration": plan["duration"], "beats": len(plan["beats"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
