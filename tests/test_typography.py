from tests.utilities.fonts import OVERLAP
from rich.text import Text

from rich_typography.typography import Typography
from tests.utilities.asserts import assert_markup


def test_overlap() -> None:
    expected = "\n".join(
        [
            "╭╮   ╷  ",
            "┼╭╮┌╮┼╷╷",
            "││││ │││",
            "╵╰╯╵ ╰╰┤",
            "     ╰─╯",
        ]
    )
    assert_markup(Typography("forty", font=OVERLAP), expected)


def test_overlap_styles() -> None:
    markup = "[red on blue]f[/red on blue][purple on green]ort[/purple on green][red on blue]y[/red on blue]"
    expected = "\n".join(
        [
            "[red on blue]╭[/red on blue][red on green]╮[/red on green][purple on green]   ╷[/purple on green][red on blue]  [/red on blue]",
            "[red on blue]┼[/red on blue][purple on green]╭╮┌╮┼[/purple on green][red on blue]╷╷[/red on blue]",
            "[red on blue]│[/red on blue][purple on green]│││ │[/purple on green][red on blue]││[/red on blue]",
            "[red on blue]╵[/red on blue][purple on green]╰╯╵ ╰[/purple on green][red on blue]╰┤[/red on blue]",
            "[red on blue] [/red on blue][purple on green]    [/purple on green][red on green]╰[/red on green][red on blue]─╯[/red on blue]",
        ]
    )
    result = Typography.from_text(Text.from_markup(markup), font=OVERLAP)
    assert_markup(result, expected)
