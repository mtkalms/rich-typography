from rich_typography.typography import Typography
from rich.console import Console
from rich.text import Text

if __name__ == "__main__":  # pragma: no cover
    console = Console()
    console.print(
        Typography.from_text(
            Text.from_markup("Hello from [purple underline]rich-typography[/]!")
        )
    )
