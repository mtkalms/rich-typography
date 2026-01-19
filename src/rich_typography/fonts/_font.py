from functools import lru_cache
from glob import glob
from pathlib import Path
import string
from typing import Any, Dict, Iterable, List, Optional, Union

from configparser import ConfigParser

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
        baseline (int, optional): Line index of baseline. Defaults to second to last line.
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
        space = Glyphs.from_lines(" ", *self.space(space_width, self.line_height))
        self._glyphs = glyphs | space
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
    def name(self) -> str:
        """Name of the Font."""
        return self._name

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
        return list(self._ligatures.keys())

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

    @classmethod
    @lru_cache
    def _builtin_fonts(cls):
        parent_folder = Path(__file__).resolve().parent / "files"
        return {
            Path(d).stem: parent_folder / d
            for d in glob(str(parent_folder / "*.glyphs"))
        }

    @classmethod
    def get_font_names(cls):
        """Return list of builtin font names."""
        return list(cls._builtin_fonts().keys())

    @classmethod
    @lru_cache
    def from_file(cls, path: Union[Path, str]) -> "Font":
        """Load from glyphs file.

        Args:
            path (Union[Path, str]): Path to glyphs file.

        Returns:
            Font: Loaded font.
        """

        def split(text: str):
            lines = [line[2:] for line in text.splitlines() if line]
            length = max(len(line) for line in lines)
            return [line.ljust(length) for line in lines]

        builtin_fonts = cls._builtin_fonts()
        if isinstance(path, str) and path in builtin_fonts:
            path = builtin_fonts[path]
        else:
            path = Path(path)
        if not path.exists():
            raise FileNotFoundError("Font file not found.")
        config = ConfigParser()
        config.read(path)
        if "header" not in config:
            raise KeyError("Font file header missing.")
        header = {}
        glyphs = Glyphs()
        ligatures = Glyphs()
        for section, data in config.items():
            if section == "header":
                header |= {k: (d if k in ["name"] else int(d)) for k, d in data.items()}
            elif section == "ligatures":
                ligatures |= Glyphs.from_lines(
                    data["sequences"].split(),
                    *split(data["glyphs"]),
                )
            elif section in dir(string):
                glyphs |= Glyphs.from_lines(
                    getattr(string, section),
                    *split(data["glyphs"]),
                )
        return Font(**header, glyphs=glyphs, ligatures=ligatures)

    def get(self, char: str) -> Glyph:
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
