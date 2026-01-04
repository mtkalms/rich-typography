import string

from rich_typography.glyphs import Glyphs
from rich_typography.fonts import Font

LOWER = Glyphs(
    """
   ╷      ╷    ╭╮    ╷  .  . ╷  ╷                      ╷                   
╭╮ ├╮ ╭╮ ╭┤ ╭╮ ┼  ╭╮ ├╮ ╷  ╷ │╷ │ ╭╮╮ ╭╮ ╭╮ ╭╮ ╭╮ ╭ ╭╮ ┼ ╷╷ ╷╷ ╷╷╷ ╷╷ ╷╷ ┌╮
││ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │ ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯
╰╰ ╰╯ ╰╯ ╰╯ ╰╯ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵ ╰╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                  ╰╯      ╰╯                ╵   ╵                     ╰╯   
""",
    string.ascii_lowercase,
)

UPPER = Glyphs(
    """
╭╮ ┌╮ ╭╮ ┌╮ ┌╴ ┌╴ ╭╮ ╷╷ ╷  ╷ ╷╷ ╷  ╭╮╮ ╭╮ ╭╮ ╭╮ ╭╮  ┌╮ ╭╮ ╶┬╴ ╷╷ ╷╷ ╷╷╷ ╷╷ ╷╷ ┌╮
├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯
││ ││ │╷ ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││ ╷│  │  ││ ││ │││ ││ ││ │ 
╵╵ └╯ ╰╯ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └╴ ╵╵╵ ╵╵ ╰╯ ╵  ╰╯╮ ╵╵ ╰╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                                                                                
""",
    string.ascii_uppercase,
)

DIGITS = Glyphs(
    """
╭╮ ╷ ╭╮ ╭╮ ╷╷ ┌╴ ╭╮ ╶┐ ╭╮ ╭╮
││ │ ╭╯  ┤ ╰┤ └╮ ├╮ ╭╯ ╭╯ ╰┤
││ │ │  ╷│  │ ╷│ ││ │  ││ ╷│
╰╯ ╵ └╴ ╰╯  ╵ ╰╯ ╰╯ ╵  ╰╯ ╰╯
                            
""",
    string.digits,
)

LIGATURES = Glyphs(
    """
╭╮ .╷ ╷.  .
┼╷ ╷│ ┼╷ ╭┐
││ ││ ││ ││
╵╵ ╰╯ ╰╯ ╵╵
           
""",
    ["fi", "il", "ti", "ri"],
)

ILLUMINA = Font("Illumina", UPPER | LOWER | DIGITS, LIGATURES)


if __name__ == "__main__":
    from rich.console import Console

    from rich_typography.typography import Typography

    console = Console()
    console.print(Typography("Illumina", font=ILLUMINA))
