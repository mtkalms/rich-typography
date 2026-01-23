# Fonts

## Regular

Condensed Sans
```{.rich columns="120"}
from rich_typography.typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog"
output=Typography.from_markup(text, font="condensedsans")
```

Condensed Semi
```{.rich columns="120"}
from rich_typography.typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog"
output=Typography.from_markup(text, font="condensedsemi")
```

Condensed Serif
```{.rich columns="120"}
from rich_typography.typography import Typography
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog"
output=Typography.from_markup(text, font="condensedserif")
```

## Extended

Condensed Sans
```{.rich columns="120"}
from rich_typography.typography import Typography
from rich_typography.extended import CONDENSED_SANS
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog"
output=Typography.from_markup(text, font=CONDENSED_SANS)
```

Sans
```{.rich columns="120"}
from rich_typography.typography import Typography
from rich_typography.extended import SANS
text = "The quick brown fox [underline]jumps[/underline] over the lazy dog"
output=Typography.from_markup(text, font=SANS)
```
