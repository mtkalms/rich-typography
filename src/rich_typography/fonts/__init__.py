from rich_typography.fonts._font import Font, NON_OVERLAPPING
from rich_typography.fonts._line import LineType, LineStyle
from rich_typography.fonts.semiserif import SEMISERIF
from rich_typography.fonts.sansserif import SANSSERIF
from rich_typography.fonts.serif import SERIF

__all__ = [
    "Font",
    "LineType",
    "LineStyle",
    "NON_OVERLAPPING",
    # FONTS
    "SANSSERIF",
    "SEMISERIF",
    "SERIF",
]


if __name__ == "__main__":  # pragma: no cover
    from rich.console import Console
    from rich_typography.typography import Typography

    text = "The quick brown fox jumps over the lazy dog"

    console = Console()
    for font in [SANSSERIF, SEMISERIF, SERIF]:
        console.print(
            Typography.from_markup(f"[purple]{font.name}[/] {text}", font=font)
        )
