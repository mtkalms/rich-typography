from string import ascii_lowercase, ascii_uppercase

from rich_typography.fonts import Font
from rich_typography.fonts._font import LineStyle
from rich_typography.glyphs import Glyphs

OVERLAP = Font(
    "Overlap",
    Glyphs.from_lines(
        ascii_lowercase,
        "   ╷      ╷    ╭╮      ╷  .  . ╷  ╷                       ╷                    ",
        "┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼    ╭┐ ├╮ ╷  ╷ │╷ │ ┌┬╮ ┌╮ ╭╮ ╭╮ ╭╮ ┌╮ ╭┐ ┼ ╷╷ ╷╷ ╷╷╷ ╷╷  ╷╷ ┌╮",
        "╭┤ ││ │  ││ ├┘ │    ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯  ││ ╭╯",
        "╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵    ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵  ╰┤ ╰┘",
        "                  ╰──╯      ╰╯                ╵   ╵                      ╰─╯   ",
    )
    | Glyphs.from_lines(
        ascii_uppercase,
        "┌╮ ┌╮ ╭╮ ┌╮ ┌╴ ┌─╴ ╭╮ ╷╷ ╷  ╷ ╷╷ ╷  ┌┬╮ ┌╮ ╭╮ ┌╮ ╭╮  ┌╮ ╭┐ ╶┬╴ ╷╷ ╷╷ ╷╷╷ ╷╷  ╷╷ ╶╮",
        "├┤ ├┤ │╵ ││ ├  ├   │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯  ││ ╭╯",
        "││ ││ │  ││ │  │   │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││  ││ │ ",
        "╵╵ └╯ ╰╯ └╯ └╴ ╵   ╰╯ ╵╵ ╵ ╰╯ ╵╵ └╴ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵  ╰┤ ╰╴",
        "                                                  ╰╯                        ╰─╯   ",
    )
    | Glyphs.from_lines(
        ".,",
        "   ",
        "   ",
        "   ",
        "· │",
        "   ",
    ),
    ligatures=Glyphs.from_lines(
        ["re", "ra", "ri", "ro", "ru", "fi", "ff", "ft", "ffi"],
        "         .         ╭╮ ╭╭╮ ╭╷ ╭╭╮",
        "┌┬╮ ┌╮╮ ┌┐ ┌┬╮ ┌┐╷ ┼┐ ┼┼  ┼┼ ┼┼┐",
        "│├┘ │╭┤ ││ │││ │││ ││ ││  ││ │││",
        "╵╰╴ ╵╰┘ ╵╵ ╵╰╯ ╵╰╯ ╵╵ ╵╵  ╵╰ ╵╵╵",
        "                                ",
    ),
    baseline=3,
    underline=LineStyle(4, "custom", "▔"),
)
