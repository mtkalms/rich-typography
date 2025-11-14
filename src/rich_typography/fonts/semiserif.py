import string

from rich_typography.glyphs import Glyphs
from rich_typography.fonts import Font

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

PUNCTUATION = Glyphs(
    """
╷ ╷╷    ╭┼╮ ◯  ╱ ╭╮╷ ╷ ╭ ╮                   ╱      ╱    ╲  ╭╮     ┌╴ ╲    ╶┐ ╱╲    ╲ ╭╴ ╷ ╶╮    
│    ┼┼ ╰┼╮   ╱  ├─┼   │ │                  ╱  · · ╱  ╶╴  ╲ ╭╯ ╭─╮ │   ╲    │         ┼  │  ┼ ╭╮ 
│    ┼┼   │  ╱   │ │   │ │ ╶╳╴ ╶┼╴ ╷ ╶╴    ╱   · ╷ ╲  ╶╴  ╱ │  │╭┤ │    ╲   │         │  │  │  ╰╯
·       └┼╯ ╱  ◯ ╰╯╰   ╰ ╯         ╵    · ╱      ╵  ╲    ╱  ·  │╰╯ └╴    ╲ ╶┙    ╶╴   ╰╴ ╵ ╶╯    
                                                               ╰─╯                               
""",
    string.punctuation,
)

SEMISERIF = Font("Semi Serif", UPPER | LOWER | DIGITS | PUNCTUATION)


if __name__ == "__main__":
    from rich.console import Console
    from rich_typography.typography import Typography

    console = Console()
    console.print(
        Typography(
            '"The quick brown fox jumps over the lazy dog," which contains every letter of the alphabet. ',
            SEMISERIF,
        )
    )

    console.print(Typography("Tom & Jerry ", SEMISERIF))
