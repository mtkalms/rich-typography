import io
from typing import Optional

from rich.console import Console, RenderableType, JustifyMethod


def render_ansi(
    renderable: RenderableType,
    width: Optional[int] = 80,
    no_wrap: Optional[bool] = True,
    justify: JustifyMethod = "default",
) -> str:
    file = io.StringIO()
    console = Console(file=file, legacy_windows=False, width=width, record=True)
    console.print(renderable, no_wrap=no_wrap, justify=justify)
    return console.export_text(styles=True)
