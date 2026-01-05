from rich_typography.fonts import Font
from rich_typography.glyphs import Glyphs


def test_simple_font() -> None:
    font = Font(
        "Simple Font",
        Glyphs(
            "af",
            "   ╭╮",
            "┌╮ ┼ ",
            "╭┤ │ ",
            "╰┘ ╵ ",
            "     ",
        ),
        ligatures=Glyphs(
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


def test_underlined() -> None:
    font = Font(
        "Simple Font",
        Glyphs(
            "opq",
            "        ",
            "╭╮ ╭╮ ╭╮",
            "││ ││ ││",
            "╰╯ ├╯ ╰┤",
            "   ╵   ╵",
        ),
    )
    assert [
        "  ",
        "╭╮",
        "││",
        "╰╯",
        "▔▔",
    ] == font.get("o", underline=True), "Failed underline o."

    assert [
        "  ",
        "╭╮",
        "││",
        "├╯",
        "╵▔",
    ] == font.get("p", underline=True), "Failed underline p."

    assert [
        "  ",
        "╭╮",
        "││",
        "╰┤",
        "▔╵",
    ] == font.get("q", underline=True), "Failed underline q."
