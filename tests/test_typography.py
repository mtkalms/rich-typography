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
    expected = "\n".join([
        "╭╮   ╷  ",
        "┼╭╮┌╮┼╷╷",
        "││││ │││",
        "╵╰╯╵ ╰╰┤",
        "     ╰─╯",
    ]) + "\n"
    print(render(Typography("forty", font=OVERLAP)))
    assert render(Typography("forty", font=OVERLAP)) == expected
