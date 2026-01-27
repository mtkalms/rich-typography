# Custom Fonts

One of the main objectives of rich-typography was to make it easy to create new fonts.
Fonts map characters to their rendered image, called **glyphs**, and define rules on how these are assembled to form text.
Additionally we can map groups of characters to a combined glyphs, called **ligatures**. 
This is usually done to avoid uneven gaps or resolve overlaps between glyphs.

```glyphs
                   Glyphs                            ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
            ╭──────────────────╮                     ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
            ┌──┐┌───┐┌──┐┌──┐┌─┐                     ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
            │  ││╭╭╮││  ││  ││╷│        ╭╭╮   ╷      ~~~~~~~~~~~~~~~~~~~~~~  ╭╭╮   ╷ ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~[overline]  ╭╭╮   ╷[/]  [medium_violet_red]overline[/]~
            │╭╮││┼┼ ││╭╮││┬╮││┼│      ╭╮┼┼╭╮┬╮┼      ~~~~~~~~~~~~~~~~~~~~~~╭╮┼┼╭╮┬╮┼ ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~╭╮┼┼╭╮┬╮┼~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
effort  ─→  │├┘││││ │││││││ ││││  ─→  ├┘│││││ │      ~~~~~~~~~~~~~~~~~~~~~~├┘│││││ │ ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~[strike]├┘│││││ │[/]  [medium_violet_red]strike[/]   
            │╰╴││╵╵ ││╰╯││╵ ││╰│      ╰╴╵╵╰╯╵ ╰      [on medium_violet_red]╰╴╵╵╰╯╵ ╰ [/] [medium_violet_red]baseline[/]     [underline]╰╴╵╵╰╯╵ ╰[/]  [medium_violet_red]underline[/]
            │  ││   ││  ││  ││ │                     ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
            └──┘└───┘└──┘└──┘└─┘                     ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
                  ↑                                  ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
              ligature                               ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
                                                     ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
```

There are two ways to define new fonts in rich-typography: as [Font](../api/font.md#rich_typography.Font) instances in memory or as `.glyphs` files.

## Creating fonts in memory

To create fonts programatically we first have to define glyphs. 
The [Glyphs](../api/glyph.md#rich_typography.Glyphs)

```python
import string

from rich_typography import Font, LineStyle, Glyphs


upper = Glyphs.from_lines(
    string.ascii_uppercase,
    "┬╮ ┬╮ ╭┐ ┬╮ ┬╴ ┬╴ ╭╮ ┐╷ ┐  ┐ ┐╷ ┐  ┬┬╮ ┬╮ ╭╮ ┬╮ ╭╮  ┬╮ ╭┐ ┌┬┐ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮",
    "├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯",
    "││ ││ │  ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││ ││ │ ",
    "╵╵ └╯ ╰╴ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └┘ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘",
    "                                                 ╰╯                        └╯   ",
)

lower = Glyphs.from_lines(
    string.ascii_lowercase,
    "   ┐      ┐    ╭╮    ┐  .  . ┐  ┐                       ╷                   ",
    "┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼  ╭┬ ├╮ ┐  ┐ │╷ │ ┬┬╮ ┬╮ ╭╮ ┬╮ ┬╮ ┬╮ ╭┐ ┼ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮",
    "╭┤ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯",
    "╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘",
    "                  └╯      └╯                ╵   ╵                      └╯   ",
)

ligatures = Glyphs.from_lines(
    list("ff fi ft fff ffi fft".split()),
    "╭╭╮ ╭╮ ╭┐ ╭╭╭╮ ╭╭╮ ╭╭┐",
    "┼┼  ┼┐ ┼┼ ┼┼┼  ┼┼┐ ┼┼┼",
    "││  ││ ││ │││  │││ │││",
    "╵╵  ╵╵ ╵╰ ╵╵╵  ╵╵╵ ╵╵╰",
    "                      ",
)

Font(
    name="My New Font",
    glyphs=(upper | lower | digits | punctuation),
    ligatures=ligatures,
    baseline=3,
    underline=4
    underline2=LineStyle(5, "custom", "▔")
)
```

## Adding and using font files

The `.glyphs` file format that defines fonts for rich-typography uses the standard [config format](https://docs.python.org/3/library/configparser.html).
All font files have a header section that defines the basic attributes like the font name and the position of the baseline.
More complex line defintions, like in this example `underline2`, get their own section.

As with Glyphs instances, you can use the constants from `string` to define the collection of characters a glyphs section represents. 

```config
[header]
name: My New Font
baseline: 3
underline: 4

[underline2]
index: 5
line: custom
char: ▔

[ascii_uppercase]
glyphs:
  │ ┬╮ ┬╮ ╭┐ ┬╮ ┬╴ ┬╴ ╭╮ ┐╷ ┐  ┐ ┐╷ ┐  ┬┬╮ ┬╮ ╭╮ ┬╮ ╭╮  ┬╮ ╭┐ ┌┬┐ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
  │ ├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯
  │ ││ ││ │  ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││ ││ │ 
  │ ╵╵ └╯ ╰╴ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └┘ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
  │                                                  ╰╯                        └╯   
[ascii_lowercase]
glyphs:
  │    ┐      ┐    ╭╮    ┐  .  . ┐  ┐                       ╷                   
  │ ┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼  ╭┬ ├╮ ┐  ┐ │╷ │ ┬┬╮ ┬╮ ╭╮ ┬╮ ┬╮ ┬╮ ╭┐ ┼ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
  │ ╭┤ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯
  │ ╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
  │                   └╯      └╯                ╵   ╵                      └╯
[digits]
glyphs:
  │ ╭╮ ┐ ╭╮ ╭╮ ╷╷ ┌╴ ╭╴ ┌┐ ╭╮ ╭╮
  │ ││ │ ╭╯  ┤ ╰┼ └╮ ├╮ ╭╯ ╭╯ ╰┤
  │ ││ │ │  ╷│  │ ╷│ ││ │  ││  │
  │ ╰╯ ╵ └┘ ╰╯  ╵ ╰╯ ╰╯ ╵  ╰╯ ╰╯
  │                             
[ligatures] 
sequences: ff fi ft fff ffi fft
glyphs:
  │ ╭╭╮ ╭╮ ╭┐ ╭╭╭╮ ╭╭╮ ╭╭┐
  │ ┼┼  ┼┐ ┼┼ ┼┼┼  ┼┼┐ ┼┼┼
  │ ││  ││ ││ │││  │││ │││
  │ ╵╵  ╵╵ ╵╰ ╵╵╵  ╵╵╵ ╵╵╰
  │                       
```