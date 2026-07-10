"""WS Colors palette helper.

Provides a small command-line utility and importable function to find a
Wada Sanzo-inspired palette based on a provided color.
"""

from __future__ import annotations

import argparse
import json
from typing import Dict, List, Tuple

PALETTES: List[Dict[str, object]] = [
    {
        "name": "crimson harmony",
        "base_color": "#B33A3A",
        "colors": ["#B33A3A", "#F2D2A9", "#5D2E46", "#6A994E"],
    },
    {
        "name": "indigo calm",
        "base_color": "#3F51B5",
        "colors": ["#3F51B5", "#A3BFFA", "#1B1B3A", "#E8EAF6"],
    },
    {
        "name": "golden earth",
        "base_color": "#C4972F",
        "colors": ["#C4972F", "#7A5C2E", "#D9C7A4", "#3C2F2F"],
    },
    {
        "name": "teal garden",
        "base_color": "#2E8B8B",
        "colors": ["#2E8B8B", "#A7D7C5", "#22577A", "#F4F9F4"],
    },
]

NAMED_COLORS = {
    "red": "#B33A3A",
    "crimson": "#B33A3A",
    "blue": "#3F51B5",
    "indigo": "#3F51B5",
    "yellow": "#C4972F",
    "gold": "#C4972F",
    "teal": "#2E8B8B",
    "green": "#2E8B8B",
}


def _normalize_color(value: str) -> str:
    raw = value.strip().lower()
    if raw in NAMED_COLORS:
        return NAMED_COLORS[raw]

    hex_value = raw[1:] if raw.startswith("#") else raw
    if len(hex_value) == 3:
        hex_value = "".join(ch * 2 for ch in hex_value)
    if len(hex_value) == 6 and all(ch in "0123456789abcdef" for ch in hex_value):
        return f"#{hex_value.upper()}"

    raise ValueError(
        "Color must be a recognized name (e.g. 'teal') or a hex value like '#2E8B8B'."
    )


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))


def _distance(first: Tuple[int, int, int], second: Tuple[int, int, int]) -> int:
    return sum((a - b) ** 2 for a, b in zip(first, second))


def get_palette_for_color(color: str) -> Dict[str, object]:
    """Return the nearest WS Colors palette for the given color name or hex."""
    normalized = _normalize_color(color)
    target_rgb = _hex_to_rgb(normalized)

    return min(
        PALETTES,
        key=lambda palette: _distance(target_rgb, _hex_to_rgb(str(palette["base_color"]))),
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find a WS Colors palette based on a given input color."
    )
    parser.add_argument("color", help="Color name or hex value (example: teal or #2E8B8B)")
    args = parser.parse_args()

    palette = get_palette_for_color(args.color)
    print(json.dumps(palette, indent=2))


if __name__ == "__main__":
    main()
