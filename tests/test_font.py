import string
from pathlib import Path
from rich_typography import Font, Glyphs, LineStyle

FONT_FOLDER = Path(__file__).parent / "fonts"


def test_simple_font() -> None:
    font = Font(
        "Simple Font",
        Glyphs.from_lines(
            "af",
            "   ╭╮",
            "┌╮ ┼ ",
            "╭┤ │ ",
            "╰┘ ╵ ",
            "     ",
        ),
        ligatures=Glyphs.from_lines(
            ["fi", "ff", "ft"],
            "╭╮ ╭╭╮ ╭╷",
            "┼┐ ┼┼  ┼┼",
            "││ ││  ││",
            "╵╵ ╵╵  ╵╰",
            "         ",
        ),
    )
    assert [
        "  ",
        "┌╮",
        "╭┤",
        "╰┘",
        "  ",
    ] == font.get("a"), "Failed to return glyph a."
    assert [
        "╭╮",
        "┼ ",
        "│ ",
        "╵ ",
        "  ",
    ] == font.get("f"), "Failed to return glyph f."
    assert [
        "╭╭╮",
        "┼┼ ",
        "││ ",
        "╵╵ ",
        "   ",
    ] == font.get("ff"), "Failed to return ligature ff."
    assert [
        "┌─┐",
        "│ │",
        "│ │",
        "│ │",
        "└─┘",
    ] == font.get("d"), "Failed to return placeholder for missing glyph."


def test_from_file() -> None:
    font = Font.from_file(FONT_FOLDER / "simple.toff")
    assert font.name == "Simple Test Font"
    assert font.baseline == 3
    assert font.underline == LineStyle(4, "custom", "▔")
    assert font.overline == LineStyle(1, "overline")
    assert font.underline2 == LineStyle(5, "overline")
    for char in string.ascii_lowercase:
        assert char in font
    for char in string.ascii_uppercase:
        assert char in font
    for char in string.punctuation:
        assert char in font
    for char in ["ä", "ö", "ü", "ß"]:
        assert char in font
    assert font.ligatures == ["re", "ra", "ri", "ro", "ru", "fi", "ff", "ft", "ffi"]
