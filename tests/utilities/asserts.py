from itertools import zip_longest
from typing import Optional
from rich.console import RenderableType, JustifyMethod
from rich.text import Text

from tests.utilities.render import render_ansi


def assert_markup(
    renderable: RenderableType,
    markup: str,
    message: Optional[str] = None,
    preview: Optional[bool] = False,
    justify: JustifyMethod = "default",
) -> None:
    rendered_a = render_ansi(renderable, justify=justify)
    rendered_b = render_ansi(Text.from_markup(markup))
    if preview:
        _preview_ansi(rendered_a, rendered_b)
    assert rendered_a == rendered_b, message


def _preview_ansi(a: str, b: str):
    lines_a = a.splitlines()
    lines_b = b.splitlines()
    # Get max line length (without ANSI codes)
    max_len = max(len(Text.from_ansi(a)) for a in lines_a)
    print("\nPreview:")
    print(
        "\n".join(
            f'"{a}"'.ljust(max_len + 2) + f'\t"{b}"'
            for a, b in zip_longest(lines_a, lines_b)
        )
    )
