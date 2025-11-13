import string

from rich_typography.glyphs import Glyphs
from rich_typography.fonts._font import Font

LOWER = Glyphs(
    """
   ┐      ┐    ╭╮    ┐  .  . ┐  ┐                       ╷                   
┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼  ╭┬ ├╮ ┐  ┐ │╷ │ ┬┬╮ ┬╮ ╭╮ ┬╮ ┬╮ ┬╮ ╭┐ ┼ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
╭┤ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯
╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                  └╯      └╯                ╵   ╵                      └╯   
""",
    string.ascii_lowercase,
)

UPPER = Glyphs(
    """
┬╮ ┬╮ ╭╮ ┬╮ ┬╴ ┬╴ ╭╮ ┐╷ ┐  ┐ ┐╷ ┐  ┬┬╮ ┬╮ ╭╮ ┬╮ ╭╮  ┬╮ ╭┐ ┌┬┐ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯
││ ││ │  ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││ ││ │ 
╵╵ └╯ ╰╯ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └┘ ╵╵╵ ╵╵ ╰╯ ╵  ╰╯╮ ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                                                                           └╯   
""",
    string.ascii_uppercase,
)

DIGITS = Glyphs(
    """
╭╮ ┐ ╭╮ ╭╮ ╷╷ ┌╴ ╭╴ ┌┐ ╭╮ ╭╮
││ │ ╭╯  ┤ ╰┼ └╮ ├╮ ╭╯ ╭╯ ╰┤
││ │ │  ╷│  │ ╷│ ││ │  ││  │
╰╯ ╵ └┘ ╰╯  ╵ ╰╯ ╰╯ ╵  ╰╯ ╰╯
                            
""",
    string.digits,
)

EXTRA = Glyphs(
    """
    ╷ ╭╮    ╱ ╲    ╷             
    │ ╭╯   ╱   ╲   │ ┼┼       ╭─╮
    │ │   ╱     ╲  │ ┼┼ ╶╴    │╭┤
╵ · · ·  ╱       ╲ ╵       ╶╴ │╰╯
                              ╰─╯
""",
    ",.!?/\|#-_@",
)

SEMISERIF = Font("Semi Serif", UPPER | LOWER | DIGITS | EXTRA)


if __name__ == "__main__":
    from rich.console import Console

    console = Console()
    console.print(SEMISERIF)
