from pathlib import Path
import string
from rich_typography.fonts import Font
from rich_typography.glyphs import Glyphs


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
    font = Font.from_file(Path(__file__).parent / "utilities/files/simple.glyphs")
    assert font.name == "Simple Test Font"
    assert font.baseline == 3
    print(font.get("a"))
    for char in string.ascii_lowercase:
        assert char in font
    for char in string.ascii_uppercase:
        assert char in font
    assert font.ligatures == ["re", "ra", "ri", "ro", "ru", "fi", "ff", "ft", "ffi"]
