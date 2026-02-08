---
title: "Typography"
---

Typography is meant as a drop-in replacement for `Text`. 
It largely implements the same interface, and follows the same conventions for styling, justification and overflow.
For all convenience methods that `Typography` does not implement, text and styles can be assembled as a `Text` instance, 
and then converted to a `Typography` instance using `Typography.from_text`.

### Kerning and Styles

Typography auto-adjusts the spacing between glyphs to create a more visually appealing image.
In some cases, kerning can cause glyphs to overlap. 
When this happens and a style change occurs between overlapping glyphs, foreground and background styles are handled differently:

- **Foreground styles** are applied to each individual glyph based on the cells it occupies
- **Background styles** are applied column-by-column, using whichever glyph occupies the majority of cells in that column

```python
Typography.from_markup("[magenta on blue]eff[/]ort")
```

```glyphs
┌~~~~~~~~~~~~~~~~~──~~~┐┌~~~~~~~~~~~~~~~~~───~~~┐┌──┐┌──┐┌─┐                                                
│[magenta on blue]  [/]││[magenta on blue]╭╭╮[/]││  ││  ││╷│      [magenta on blue]  ╭╭[/][magenta]╮[/]   ╷ 
│[magenta on blue]╭╮[/]││[magenta on blue]┼┼ [/]││╭╮││┬╮││┼│      [magenta on blue]╭╮┼┼[/]~~~~~~~~~╭~~~╮┬╮┼ 
│[magenta on blue]├┘[/]││[magenta on blue]││ [/]│││││││ ││││  ─→  [magenta on blue]├┘││[/]~~~~~~~~~│~~~││ │ 
│[magenta on blue]╰╴[/]││[magenta on blue]╵╵ [/]││╰╯││╵ ││╰│      [magenta on blue]╰╴╵╵[/]~~~~~~~~~╰~~~╯╵ ╰ 
│[magenta on blue]  [/]││[magenta on blue]   [/]││  ││  ││ │      [magenta on blue]    [/]~~~~~~~~~ ~~~     
└~~~~~~~~~~~~~~~~~──~~~┘└~~~~~~~~~~~~~~~~~───~~~┘└──┘└──┘└─┘                                                
```

### Ligatures and Styles

When a style border falls within a ligature, the entire ligature is rendered either with the closing (first) or the opening style (last).
```python
Typography.from_markup("[magenta]ef[/]fort", style_ligature="first")
```

```glyphs
┌──┐┌───┐┌──┐┌──┐┌─┐                     ┌~~~~~~~~~─╴fi~~~r~~~st╶──┐ ┌~~~~~~~~~──~~~╴last╶──┐  
│  ││╭╭╮││  ││  ││╷│        ╭╭╮   ╷      │[magenta]  ╭╭~~~╮[/]   ╷ │ │[magenta]  [/]╭╭╮   ╷ │
│╭╮││┼┼ ││╭╮││┬╮││┼│      ╭╮┼┼╭╮┬╮┼      │[magenta]╭╮┼┼[/]╭~~~╮┬╮┼ │ │[magenta]╭╮[/]┼┼╭╮┬╮┼ │
│├┘││││ │││││││ ││││  ─→  ├┘│││││ │  ─→  │[magenta]├┘││[/]│~~~││ │ │ │[magenta]├┘[/]│││││ │ │
│╰╴││╵╵ ││╰╯││╵ ││╰│      ╰╴╵╵╰╯╵ ╰      │[magenta]╰╴╵╵[/]╰~~~╯╵ ╰ │ │[magenta]╰╴[/]╵╵╰╯╵ ╰ │
│  ││   ││  ││  ││ │                     │[magenta]    [/] ~~~     │ │[magenta]  [/]        │
└──┘└───┘└──┘└──┘└─┘                     └~~~~~~~~~───~~~─~~~──────┘ └~~~~~~~~~──~~~────────┘
```   

::: rich_typography.Typography