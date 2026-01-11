from typing import Any, Dict, Iterable, List, Optional, Union

from rich_typography.fonts._line import LineStyle
from rich_typography.glyphs import Glyph, Glyphs

NON_OVERLAPPING = " \"'"


class Font:
    """A font.

    Args:
        name (str): Name of the font.
        glyphs (Dict[str, List[str]]): Glyphs for single chars.
        ligatures (Glyphs, optional): Glyphs for ligatures. Defaults to None.
        letter_spacing (int, optional): Spacing between glyphs in number of cells. Defaults to 0.
        space_width (int, optional): Width of space glyph in number of cells. Defaults to 1.
        baseline (Union[int, LineStyle], optional): Line index of baseline. Defaults to second to last line.
        underline (Union[int, LineStyle], optional): Line index or more complex style of underline. Defaults to line below baseline.
        underline2 (Union[int, LineStyle], optional): Line index or more complex style of underline2. Defaults to baseline.
        overline (Union[int, LineStyle], optional): Line index or more complex style of overline. Defaults to first line.
        strike (Union[int, LineStyle], optional): Line index or more complex style of strike. Defaults to middle line.
    """

    def __init__(
        self,
        name: str,
        glyphs: Dict[str, List[str]],
        *,
        ligatures: Optional[Glyphs] = None,
        letter_spacing: int = 0,
        space_width: int = 1,
        baseline: Optional[int] = None,
        underline: Optional[Union[int, LineStyle]] = None,
        underline2: Optional[Union[int, LineStyle]] = None,
        overline: Optional[Union[int, LineStyle]] = None,
        strike: Optional[Union[int, LineStyle]] = None,
    ):
        self._name = name
        self._line_height = len(list(glyphs.values())[0])
        self._glyphs = glyphs | Glyphs(" ", *self.space(space_width, self.line_height))
        self._ligatures = ligatures or {}
        self._letter_spacing = letter_spacing
        self._space_width = space_width
        self._baseline = baseline or self.line_height - 2
        self._underline = LineStyle(self._baseline, "underline") | underline
        self._underline2 = LineStyle(self._baseline + 1, "underline2") | underline2
        self._overline = LineStyle(0, "overline") | overline
        self._strike = LineStyle(self.line_height // 2, "strike") | strike
        self._placeholder = self.placeholder(self.line_height)

    @property
    def line_height(self) -> int:
        """Number of lines per glyph."""
        return self._line_height

    @property
    def letter_spacing(self) -> int:
        """Spacing between glyphs in number of cell"""
        return self._letter_spacing

    @property
    def space_width(self) -> int:
        """Width of space glyph in number of cells."""
        return self._space_width

    @property
    def baseline(self) -> int:
        """Line index of baseline."""
        return self._baseline

    @property
    def underline(self) -> LineStyle:
        """Style of underline."""
        return self._underline

    @property
    def underline2(self) -> LineStyle:
        """Style of underline2."""
        return self._underline2

    @property
    def overline(self) -> LineStyle:
        """Style of overline."""
        return self._overline

    @property
    def strike(self) -> LineStyle:
        """Style of strike."""
        return self._strike

    @property
    def ligatures(self) -> Iterable[str]:
        """All available ligatures."""
        return self._ligatures.keys()

    @classmethod
    def space(cls, width: int, line_height: int) -> Glyph:
        """Create space glyph.

        Args:
            width (int): Width in number of cells.
            line_height (int): Height in number of lines.

        Returns:
            Glyph: Space glyph.
        """
        return [" " * width] * line_height

    @classmethod
    def placeholder(cls, line_height: int) -> Glyph:
        """Create placeholder glyph.

        Args:
            line_height (int): Height in number of lines.

        Returns:
            Glyph: Placeholder glyph.
        """
        return ["┌─┐"] + ["│ │"] * (line_height - 2) + ["└─┘"]

    def get(self, char: str, *, underline: bool = False) -> Glyph:
        """Get glyph for char or ligature.

        Args:
            char (str): Char or group of chars (ligature).

        Returns:
            Glyph: Glyph for char.
        """
        if len(char) == 1:
            glyph = self._glyphs.get(char, self._placeholder)
        else:
            glyph = self._ligatures.get(char, self._placeholder)
        return glyph

    def __contains__(self, other: Any) -> bool:
        if isinstance(other, str):
            return (
                other in self._glyphs if len(other) == 1 else other in self._ligatures
            )
        else:
            raise ValueError

    def __str__(self):
        return "\n".join(
            char + "\n" + "\n".join(glyph)
            for char, glyph in (self._glyphs | self._ligatures).items()
        )

    def __repr__(self):
        return f"<Font: '{self._name}'>"
