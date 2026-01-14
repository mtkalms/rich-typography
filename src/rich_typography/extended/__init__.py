
from rich_typography.extended.condensed_sans import CONDENSED_SANS
from rich_typography.extended.sans import SANS

__all__ = [
    "CONDENSED_SANS",
    "SANS"
]


if __name__ == "__main__":  # pragma: no cover
    from rich.console import Console
    from rich_typography.typography import Typography

    text = "The quick brown fox jumps over the lazy dog"

    console = Console()
    for font in [CONDENSED_SANS, SANS]:
        console.print(
            Typography.from_markup(f"[purple]{font.name}[/] {text}", font=font)
        )
