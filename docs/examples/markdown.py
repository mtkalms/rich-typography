from rich.markdown import Markdown as RichMarkdown, Heading as RichHeading
from rich.console import Console, RenderResult
from rich_typography import Typography


MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

## This is an h2

1. This is a list item
2. This is another list item
"""


class Heading(RichHeading):
    def __rich_console__(self, *args, **kwargs) -> RenderResult:
        self.text.style = "red"
        if self.tag == "h1":
            text = Typography.from_text(self.text)
            text.justify = "center"
            yield text
        else:
            yield from super().__rich_console__(*args, **kwargs)


class Markdown(RichMarkdown):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.elements["heading_open"] = Heading


console = Console()
console.print(Markdown(MARKDOWN))
