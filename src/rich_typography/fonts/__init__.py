from rich_typography.fonts._font import Font, NON_OVERLAPPING
from rich_typography.fonts._line import LineType, LineStyle

__all__ = [
    "Font",
    "LineType",
    "LineStyle",
    "NON_OVERLAPPING",
]


if __name__ == "__main__":  # pragma: no cover
    from rich.console import Console
    from rich_typography.typography import Typography

    text = "The quick brown fox jumps over the lazy dog"

    console = Console()
    for font in Font.get_font_names():
        Font.from_file
        console.print(Typography.from_markup(f"[purple]{font}[/] {text}", font=font))
