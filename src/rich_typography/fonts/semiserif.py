import string

from rich_typography.fonts import Font
from rich_typography.glyphs import Glyphs

LOWER = Glyphs(
    string.ascii_lowercase,
    "   ┐      ┐    ╭╮    ┐  .  . ┐  ┐                       ╷                   ",
    "┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼  ╭┬ ├╮ ┐  ┐ │╷ │ ┬┬╮ ┬╮ ╭╮ ┬╮ ┬╮ ┬╮ ╭┐ ┼ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮",
    "╭┤ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯",
    "╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘",
    "                  └╯      └╯                ╵   ╵                      └╯   ",
)

UPPER = Glyphs(
    string.ascii_uppercase,
    "┬╮ ┬╮ ╭╮ ┬╮ ┬╴ ┬╴ ╭╮ ┐╷ ┐  ┐ ┐╷ ┐  ┬┬╮ ┬╮ ╭╮ ┬╮ ╭╮  ┬╮ ╭┐ ┌┬┐ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮",
    "├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯",
    "││ ││ │  ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││ ││ │ ",
    "╵╵ └╯ ╰╯ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └┘ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘",
    "                                                 ╰╯                        └╯   ",
)

DIGITS = Glyphs(
    string.digits,
    "╭╮ ┐ ╭╮ ╭╮ ╷╷ ┌╴ ╭╴ ┌┐ ╭╮ ╭╮",
    "││ │ ╭╯  ┤ ╰┼ └╮ ├╮ ╭╯ ╭╯ ╰┤",
    "││ │ │  ╷│  │ ╷│ ││ │  ││  │",
    "╰╯ ╵ └┘ ╰╯  ╵ ╰╯ ╰╯ ╵  ╰╯ ╰╯",
    "                            ",
)

PUNCTUATION = Glyphs(
    string.punctuation,
    "╷ ╷╷    ╭┼╮ ◯  ╱ ╭╮╷ ╷ ╭ ╮                   ╱      ╱    ╲  ╭╮     ┌╴ ╲    ╶┐ ╱╲    ╲ ╭╴ ╷ ╶╮    ",
    "│    ┼┼ ╰┼╮   ╱  ├─┼   │ │                  ╱  ·   ╱  ╶╴  ╲ ╭╯ ╭─╮ │   ╲    │         ┼  │  ┼ ╭╮ ",
    "│    ┼┼   │  ╱   │ │   │ │ ╶╳╴ ╶┼╴   ╶╴    ╱   · · ╲  ╶╴  ╱ │  │╭┤ │    ╲   │         │  │  │  ╰╯",
    "·       └┼╯ ╱  ◯ ╰╯╰   ╰ ╯         │    · ╱      │  ╲    ╱  ·  │╰╯ └╴    ╲ ╶┙    ╶╴   ╰╴ ╵ ╶╯    ",
    "                                                               ╰─╯                               ",
)

LIGATURES = Glyphs(
    [
        "re",
        "ra",
        "ri",
        "ro",
        "ru",
        "fb",
        "ff",
        "fh",
        "fi",
        "fj",
        "fk",
        "fl",
        "ft",
        "ffb",
        "fff",
        "ffh",
        "ffi",
        "ffj",
        "ffk",
        "ffl",
        "fft",
    ],
    "         .         ╭┐  ╭╭╮ ╭┐  ╭╮ ╭╮ ╭┐  ╭┐ ╭┐ ╭╭┐  ╭╭╭╮ ╭╭┐  ╭╭╮ ╭╭╮ ╭╭┐  ╭╭┐ ╭╭┐",
    "┬┬╮ ┬╮╮ ┬┐ ┬┬╮ ┬┐╷ ┼├╮ ┼┼  ┼├╮ ┼┐ ┼┐ ┼│╷ ┼│ ┼┼ ┼┼├╮ ┼┼┼  ┼┼├╮ ┼┼┐ ┼┼┐ ┼┼│╷ ┼┼│ ┼┼┼",
    "│├┘ │╭┤ ││ │││ │││ │││ ││  │││ ││ ││ │├╮ ││ ││ ││││ │││  ││││ │││ │││ ││├╮ │││ │││",
    "╵╰╴ ╵╰┘ ╵╵ ╵╰╯ ╵╰╯ ╵└╯ ╵╵  ╵╵╵ ╵╵ ╵│ ╵╵╵ ╵╰ ╵╰ ╵╵└╯ ╵╵╵  ╵╵╵╵ ╵╵╵ ╵╵│ ╵╵╵╵ ╵╵╰ ╵╵╰",
    "                                  └╯                               └╯             ",
)

SEMISERIF = Font(
    "Semi Serif", UPPER | LOWER | DIGITS | PUNCTUATION, LIGATURES, baseline=3
)


if __name__ == "__main__":
    from rich.console import Console

    from rich_typography.typography import Typography

    console = Console()
    console.print(Typography("Semiserif", font=SEMISERIF))
