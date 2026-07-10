import pytest

from src.ws_colors import get_palette_for_color


def test_palette_lookup_by_color_name():
    palette = get_palette_for_color("teal")
    assert palette["name"] == "teal garden"


def test_palette_lookup_by_hex():
    palette = get_palette_for_color("#3F55C0")
    assert palette["name"] == "indigo calm"


def test_palette_lookup_rejects_invalid_color():
    with pytest.raises(ValueError):
        get_palette_for_color("not-a-color")
