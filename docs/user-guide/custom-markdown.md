# Custom Markdown

We can modify [this example](https://rich.readthedocs.io/en/latest/markdown.html) from Rich to render H1 headings as Typography.

```python
MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

## This is an h2

1. This is a list item
2. This is another list item
"""
from rich.markdown import Markdown as RichMarkdown, Heading as RichHeading
from rich.console import Console, RenderResult
from rich_typography.typography import Typography

class Heading(RichHeading):
    def __rich_console__(
        self, *args, **kwargs
    ) -> RenderResult:
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
```