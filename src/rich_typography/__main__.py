from time import process_time
from rich_typography.typography import Typography
from rich.console import Console
from rich.table import Table
from rich.style import Style


if __name__ == "__main__":  # pragma: no cover
    start = process_time()
    console = Console()
    console.print(
        Typography.from_markup(
            "Most ansi styles: [bold]bold[/bold], [dim]dim[/dim], [underline]underline[/underline], [strike]strikethrough[/strike], [overline]overline[/overline], [reverse]reverse[/reverse], and even [blink]blink[/blink]."
        )
    )
    console.print(
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
    console.print(lorem_table)
    taken = round((process_time() - start) * 1000.0, 1)
    console.print(f"[dim]rendered in [not dim]{taken}ms[/]")
