import io
from typing import Optional

from rich.console import Console, RenderableType


def render_ansi(renderable: RenderableType, width: Optional[int] = 256) -> str:
    file = io.StringIO()
    console = Console(file=file, legacy_windows=False, width=width, record=True)
    console.print(renderable, no_wrap=True)
    return console.export_text(styles=True)
