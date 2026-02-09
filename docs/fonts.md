# Fonts

The font collection in rich-typography focuses on clean, clearly readable versions of basic
font styles.


## Regular

**Condensed Sans** (condensedsans)
```{.rich columns="120"}
from rich_typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog."
output=Typography.from_markup(text, font="condensedsans")
```

**Condensed Semi** (condensedsemi)
```{.rich columns="120"}
from rich_typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog."
output=Typography.from_markup(text, font="condensedsemi")
```

**Condensed Serif** (condensedserif)
```{.rich columns="120"}
from rich_typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog."
output=Typography.from_markup(text, font="condensedserif")
```

## Extended

!!! warning "Unicode Compatibility"
    Fonts in the extended namespace use uncommon unicode characters, specifically
    from the [Symbols for Legacy Computing][LegacyComputing] block introduced in
    [Unicode 16.0][Unicode16]. Using these fonts might severely limit the 
    compatibility of your application with different terminal setups.

**Condensed Sans** (extended.condensedsans)
```{.rich columns="120"}
from rich_typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog."
output=Typography.from_markup(text, font="extended.condensedsans")
```

**Sans** (extended.sans)
```{.rich columns="120"}
from rich_typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog."
output=Typography.from_markup(text, font="extended.sans")
```


[LegacyComputing]: https://en.wikipedia.org/wiki/Symbols_for_Legacy_Computing
[Unicode16]: https://www.unicode.org/charts/PDF/U1FB00.pdf