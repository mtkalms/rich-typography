import io
from typing import Optional

from assets.fonts import OVERLAP
from rich.console import Console, RenderableType
from rich.text import Text

from rich_typography.typography import Typography


def render(renderable: RenderableType, width: Optional[int] = 256) -> str:
    file = io.StringIO()
    console = Console(file=file, legacy_windows=False, width=width, record=True)
    console.print(renderable, no_wrap=True)
    return console.export_text(styles=True)


def assert_markup(renderable: RenderableType, markup: str) -> None:
    assert render(renderable) == render(Text.from_markup(markup))


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
