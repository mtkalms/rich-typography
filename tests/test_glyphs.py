import pytest
from tests.utilities.markup import MarkupResult
from rich_typography import Glyphs


def test_simple_glyphs() -> None:
    glyphs = Glyphs.from_lines(
        "abc",
        "   ╷    ",
        "┌╮ ├╮ ╭┐",
        "╭┤ ││ │ ",
        "╰┘ └╯ ╰╴",
        "        ",
    )
    assert [
        "  ",
        "┌╮",
        "╭┤",
        "╰┘",
        "  ",
    ] == glyphs.get("a")
    assert [
        "╷ ",
        "├╮",
        "││",
        "└╯",
        "  ",
    ] == glyphs.get("b")
    assert [
        "  ",
        "╭┐",
        "│ ",
        "╰╴",
        "  ",
    ] == glyphs.get("c")
    assert glyphs.get("d") is None


def test_line_length_missmatch() -> None:
    with pytest.raises(ValueError):
        Glyphs.from_lines(
            "abc",
            "   ╷",
            "┌╮ ├╮ ╭┐",
            "╭┤ ││ │ ",
            "╰┘ └╯ ╰╴",
            "        ",
        )


def test_char_glyph_missmatch() -> None:
    with pytest.raises(ValueError):
        Glyphs.from_lines(
            "abcd",
            "   ╷    ",
            "┌╮ ├╮ ╭┐",
            "╭┤ ││ │ ",
            "╰┘ └╯ ╰╴",
            "        ",
        )


def test_glyph_union() -> None:
    glyph_ab = Glyphs.from_lines(
        "ab",
        "   ╷ ",
        "┌╮ ├╮",
        "╭┤ ││",
        "╰┘ └╯",
        "     ",
    )
    glyph_c = Glyphs.from_lines(
        "c",
        "  ",
        "╭┐",
        "│ ",
        "╰╴",
        "  ",
    )
    glyphs = glyph_ab | glyph_c
    assert [
        "  ",
        "┌╮",
        "╭┤",
        "╰┘",
        "  ",
    ] == glyphs.get("a")
    assert [
        "╷ ",
        "├╮",
        "││",
        "└╯",
        "  ",
    ] == glyphs.get("b")
    assert [
        "  ",
        "╭┐",
        "│ ",
        "╰╴",
        "  ",
    ] == glyphs.get("c")


def test_str() -> None:
    glyphs = Glyphs.from_lines(
        "abc",
        "   ╷    ",
        "┌╮ ├╮ ╭┐",
        "╭┤ ││ │ ",
        "╰┘ └╯ ╰╴",
        "        ",
    )
    assert MarkupResult(
        "a  b  c ",
        "   ╷    ",
        "┌╮ ├╮ ╭┐",
        "╭┤ ││ │ ",
        "╰┘ └╯ ╰╴",
        "        ",
    ) == str(glyphs)


def test_repr() -> None:
    glyphs = Glyphs.from_lines(
        "abc",
        "   ╷    ",
        "┌╮ ├╮ ╭┐",
        "╭┤ ││ │ ",
        "╰┘ └╯ ╰╴",
        "        ",
    )
    assert "<Glyphs: a b c>" == glyphs.__repr__()
