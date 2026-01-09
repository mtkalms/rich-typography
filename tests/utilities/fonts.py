from string import ascii_lowercase, ascii_uppercase

from rich_typography.fonts import Font
from rich_typography.fonts._font import LineStyle
from rich_typography.glyphs import Glyphs

OVERLAP = Font(
    "Overlap",
    Glyphs(
        ascii_lowercase,
        "   ╷      ╷    ╭╮      ╷  .  . ╷  ╷                       ╷                    ",
        "┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼    ╭┐ ├╮ ╷  ╷ │╷ │ ┌┬╮ ┌╮ ╭╮ ╭╮ ╭╮ ┌╮ ╭┐ ┼ ╷╷ ╷╷ ╷╷╷ ╷╷  ╷╷ ┌╮",
        "╭┤ ││ │  ││ ├┘ │    ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯  ││ ╭╯",
        "╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵    ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵  ╰┤ ╰┘",
        "                  ╰──╯      ╰╯                ╵   ╵                      ╰─╯   ",
    )
    | Glyphs(
        ascii_uppercase,
        "┌╮ ┌╮ ╭╮ ┌╮ ┌╴ ┌─╴ ╭╮ ╷╷ ╷  ╷ ╷╷ ╷  ┌┬╮ ┌╮ ╭╮ ┌╮ ╭╮  ┌╮ ╭┐ ╶┬╴ ╷╷ ╷╷ ╷╷╷ ╷╷  ╷╷ ╶╮",
        "├┤ ├┤ │╵ ││ ├  ├   │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯  ││ ╭╯",
        "││ ││ │  ││ │  │   │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││  ││ │ ",
        "╵╵ └╯ ╰╯ └╯ └╴ ╵   ╰╯ ╵╵ ╵ ╰╯ ╵╵ └╴ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵  ╰┤ ╰╴",
        "                                                  ╰╯                        ╰─╯   ",
    )
    | Glyphs(
        ".,",
        "   ",
        "   ",
        "   ",
        "· │",
        "   ",
    ),
    ligatures=Glyphs(
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
