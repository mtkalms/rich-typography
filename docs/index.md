# Welcome

Welcome to the rich-typography documentation.

```{.rich columns=155 transparent=True}
from rich_typography import Typography
from rich.containers import Renderables
from rich.table import Table
from rich.style import Style

output = Renderables()

output.append(
    Typography.from_markup(
        "Most ansi styles: [bold]bold[/bold], [dim]dim[/dim], [underline]underline[/underline], [strike]strikethrough[/strike], [overline]overline[/overline], [reverse]reverse[/reverse], and even [blink]blink[/blink]."
    )
)
output.append(
    Typography.from_markup(
        """Word wrap text. Justify [green]left[/], [yellow]center[/], [blue]right[/] or [red]full[/].\n"""
    ),
)
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque in metus sed sapien ultricies pretium a at justo. Maecenas luctus velit et auctor maximus."
lorem_table = Table.grid(padding=3)
lorem_table.add_row(
    Typography(lorem, justify="left", style=Style(color="green")),
    Typography(lorem, justify="center", style=Style(color="yellow")),
)
lorem_table.add_row(
    Typography(lorem, justify="right", style=Style(color="blue")),
    Typography(lorem, justify="full", style=Style(color="red")),
)
output.append(lorem_table)
```
