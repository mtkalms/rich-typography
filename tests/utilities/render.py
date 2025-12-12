import io
from typing import Optional

from rich.console import Console, RenderableType


def render_ansi(
    renderable: RenderableType,
    width: Optional[int] = 80,
    no_wrap: Optional[bool] = True,
) -> str:
    file = io.StringIO()
    console = Console(file=file, legacy_windows=False, width=width, record=True)
    console.print(renderable, no_wrap=no_wrap)
    return console.export_text(styles=True)
