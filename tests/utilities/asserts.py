from rich.console import RenderableType
from rich.text import Text

from tests.utilities.render import render_ansi


def assert_markup(renderable: RenderableType, markup: str) -> None:
    assert render_ansi(renderable) == render_ansi(Text.from_markup(markup))
