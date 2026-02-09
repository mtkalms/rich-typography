# Custom Fonts

The font system in rich-typography aims to make the process of defining and using custom fonts easy and intuitive.
There are two ways to define custom fonts in rich-typography: in memory as [Font](../api/font.md#rich_typography.Font) instances or as `.toff` files.

!!! info "Fonts"
    Fonts map **characters** to shapes, called **glyphs**, and define rules on how these shapes assemble to form the final image.
    Additionally we can map groups of characters to combined glyphs, called **ligatures**. 
    This is usually done to avoid uneven gaps or resolve overlaps between glyphs.

    ```glyphs
                      Glyphs                             ~~~~~~~~~~~~~~~~~~~~~~          ~~~ ~~~~~~~~~~~~~~~~~~~        ~~~     ~~~~~~~~~~~         ~~~  ~~~~~~~~~~~~~~~~~~~         ~~~
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



## Creating fonts in memory

To create a custom font, first define the character to glyph mapping in one or more [Glyphs](../api/glyph.md#rich_typography.Glyphs) instances.
Each Glyphs instance accepts a string or list of characters and the lines of their rendered counterparts.
Individual glyphs are separated by a full column of the separator character (space by default).

Group glyphs by type (uppercase, lowercase, digits, punctuation, etc.) and split them into separate Glyph instances as needed. 
Use the constants from the `string` module (for example `string.ascii_lowercase`) to avoid typing out every single character. 
Ligatures are created the same way, but the input is a list of character sequences (e.g. ["ff", "fi"]) rather than single characters.

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

## Creating font files

The Textual Open Font Format (`.toff` ) used in rich-typography is based on the standard [config format](https://docs.python.org/3/library/configparser.html).
All font files have a **header** section that defines the basic attributes like the font name and the position of the baseline.
More complex line definitions, like in this example `underline2`, get their own section.

```config
[header]
name: My New Font
baseline: 3
underline: 4

[underline2]
index: 5
line: custom
char: ▔
```

As with Glyphs instances, glyph definitions can be grouped by category and split into multiple sections.
Sections that define any of the character sets in `string` just use that name (`lowercase`, `uppercase`, `digits`, `punctuation`) as their title.
Others that define a custom set of characters can have any name that best describes them.
The characters contained in these sections has to be listed under `chars`.
Any spaces in `chars` will be ignored, and can be used to improve the readability of the font file.
The length of spaces can be defined in the header instead.


```config
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
[german]
chars: äöü ß
glyphs:
  │ .. .. .. ╭╮
  │ ┌╮ ╭╮ ╷╷ │┤
  │ ╭┤ ││ ││ ││
  │ ╰┘ ╰╯ ╰╯ ╯╯
  │            
```

Ligatures get their own `ligatures` section. Instead of single characters, this section defines a set of `sequences`.
Here, spaces are mandatory to separate the individual sequences. 

```config
[ligatures] 
sequences: ff fi ft fff ffi fft
glyphs:
  │ ╭╭╮ ╭╮ ╭┐ ╭╭╭╮ ╭╭╮ ╭╭┐
  │ ┼┼  ┼┐ ┼┼ ┼┼┼  ┼┼┐ ┼┼┼
  │ ││  ││ ││ │││  │││ │││
  │ ╵╵  ╵╵ ╵╰ ╵╵╵  ╵╵╵ ╵╵╰
  │                       
```
