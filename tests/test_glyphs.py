import pytest
from rich_typography.glyphs import Glyphs
from tests.utilities.markup import MarkupResult


def test_simple_glyphs() -> None:
    glyphs = Glyphs(
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
        Glyphs(
            "abc",
            "   ╷",
            "┌╮ ├╮ ╭┐",
            "╭┤ ││ │ ",
            "╰┘ └╯ ╰╴",
            "        ",
        )


def test_char_glyph_missmatch() -> None:
    with pytest.raises(ValueError):
        Glyphs(
            "abcd",
            "   ╷    ",
            "┌╮ ├╮ ╭┐",
            "╭┤ ││ │ ",
            "╰┘ └╯ ╰╴",
            "        ",
        )


def test_glyph_union() -> None:
    glyph_ab = Glyphs(
        "ab",
        "   ╷ ",
        "┌╮ ├╮",
        "╭┤ ││",
        "╰┘ └╯",
        "     ",
    )
    glyph_c = Glyphs(
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


def test_glyph_union_height_missmatch() -> None:
    glyph_ab = Glyphs(
        "ab",
        "   ╷ ",
        "┌╮ ├╮",
        "╭┤ ││",
        "╰┘ └╯",
        "     ",
    )
    glyph_c = Glyphs(
        "c",
        "╭┐",
        "│ ",
        "╰╴",
        "  ",
    )
    with pytest.raises(ValueError):
        _ = glyph_ab | glyph_c


def test_glyph_union_unsupported_type() -> None:
    glyph_ab = Glyphs(
        "ab",
        "   ╷ ",
        "┌╮ ├╮",
        "╭┤ ││",
        "╰┘ └╯",
        "     ",
    )
    glyph_c = [
        "  ",
        "╭┐",
        "│ ",
        "╰╴",
        "  ",
    ]
    with pytest.raises(TypeError):
        _ = glyph_ab | glyph_c


def test_str() -> None:
    glyphs = Glyphs(
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
    glyphs = Glyphs(
        "abc",
        "   ╷    ",
        "┌╮ ├╮ ╭┐",
        "╭┤ ││ │ ",
        "╰┘ └╯ ╰╴",
        "        ",
    )
    assert "<Glyphs: a b c>" == glyphs.__repr__()
