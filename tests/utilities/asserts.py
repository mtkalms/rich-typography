from itertools import zip_longest
from typing import Optional
from rich.console import RenderableType
from rich.text import Text

from tests.utilities.render import render_ansi


def assert_markup(
    renderable: RenderableType, markup: str, preview: Optional[bool] = False
) -> None:
    rendered_a = render_ansi(renderable)
    rendered_b = render_ansi(Text.from_markup(markup))
    if preview:
        lines_a = rendered_a.splitlines()
        lines_b = rendered_b.splitlines()
        print()
        print("\n".join(a + "\t" + b for a, b in zip_longest(lines_a, lines_b)))
    assert rendered_a == rendered_b
