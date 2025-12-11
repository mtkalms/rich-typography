from rich.console import RenderableType
from rich.text import Text

from tests.utilities.render import render


def assert_markup(renderable: RenderableType, markup: str) -> None:
    assert render(renderable) == render(Text.from_markup(markup))
