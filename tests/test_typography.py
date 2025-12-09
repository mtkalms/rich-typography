import io
from assets.fonts import OVERLAP
from rich.console import Console, RenderableType

from rich_typography.typography import Typography

def render(renderable: RenderableType) -> str:
    console = Console(file=io.StringIO(), legacy_windows=False, width=256)
    console.print(renderable, no_wrap=True)
    return console.file.getvalue()

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
