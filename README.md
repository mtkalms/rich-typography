[![Test](https://github.com/mtkalms/rich-typography/actions/workflows/python-package.yml/badge.svg)](https://github.com/mtkalms/rich-typography/actions/workflows/python-package.yml)
[![Ruff](https://github.com/mtkalms/rich-typography/actions/workflows/ruff-format.yml/badge.svg)](https://github.com/mtkalms/rich-typography/actions/workflows/ruff-format.yml)
[![Documentation](https://github.com/mtkalms/rich-typography/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/mtkalms/rich-typography/actions/workflows/gh-pages.yml)

# rich-typography
Large letter typography for [Rich](https://github.com/Textualize/rich) and [Textual](https://github.com/Textualize/textual).

![rich-typography example](https://github.com/mtkalms/rich-typography/raw/main/images/preview.svg)

## Installation

Install with `uv` or your favorite PYPI package manager:

```bash
uv add rich-typography
```

## Usage

```python
from rich.console import Console
from rich_typography import Typography

console = Console()
text = Typography.from_markup("Hello from [purple]rich-typography[/purple]")
console.print(text)
```

![rich-typography usage](https://github.com/mtkalms/rich-typography/raw/main/images/usage.svg)

### Custom Markdown

Rich allows you to create your own Markdown renderable and overwrite how specific markdown blocks are rendered.
With that we can modify [this example](https://rich.readthedocs.io/en/latest/markdown.html) to render H1 headings as `Typography` instead of `Text`.

```python
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



output = Markdown(MARKDOWN)
```

![markdown example](https://github.com/mtkalms/rich-typography/raw/main/images/markdown.svg)

## Alternative Approaches

### Render with Pillow and use with textual-image

- Allows you to use any font
- Depends on terminal supporting terminal graphics protocol (TPG) or sixel graphics protocol
- Layout is more difficult to control

```python
from PIL import Image, ImageDraw, ImageFont
from textual_image.renderable import Image as RichImage
from rich.console import Console

img = Image.new("RGBA", (500, 64))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("CascadiaCode.ttf", 64)
draw.text((0, 0), "This is an h1", font=font, fill=(255, 0, 0))

console = Console()
console.print(RichImage(img))
```

TGP:

![Pillow font rendering with terminal graphics protocol](https://github.com/mtkalms/rich-typography/raw/main/images/pillow-tgp.png)

Sixel:

![Pillow font rendering with sixel graphics](https://github.com/mtkalms/rich-typography/raw/main/images/pillow-sixel.png)

Half block fallback:

![Pillow font rendering with characters](https://github.com/mtkalms/rich-typography/raw/main/images/pillow-chars.png)

### Text Sizing Protocol

Kitty has proposed a [text sizing protocol](https://sw.kovidgoyal.net/kitty/text-sizing-protocol/) but support by popular terminals is currently still limited.

## Similar Projects

- [rich-pyfiglet](https://github.com/edward-jazzhands/rich-pyfiglet)
- [textual-pyfiglet](https://github.com/edward-jazzhands/textual-pyfiglet)