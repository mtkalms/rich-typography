from typing import Any, Optional
from rich.table import Table
from rich_typography.glyphs import Glyphs, Glyph


class Font:
    def __init__(
        self,
        name: str,
        glyphs: Glyphs,
        ligatures: Optional[Glyphs] = {},
        space_width: Optional[int] = 1,
    ):
        self._name = name
        self._line_height = len(list(glyphs.values())[0])
        self._glyphs = glyphs | Glyphs(self.space(space_width, self._line_height), " ")
        self._ligatures = ligatures

    @classmethod
    def space(cls, width: int, line_height: int) -> Glyph:
        return "\n".join([" " * width] * line_height)

    @classmethod
    def placeholder(cls, line_height: int) -> Glyph:
        return ["┌─┐"] + ["│ │"] * (line_height - 2) + ["└─┘"]

    def glyph(self, char: str) -> Glyph:
        return self._glyphs.get(char, self.placeholder(self._line_height))

    def ligature(self, char: str) -> Glyph:
        return self._ligatures.get(char, self.placeholder(self._line_height))

    def __contains__(self, other: Any) -> bool:
        if isinstance(other, str):
            return other in self._glyphs or other in self._ligatures
        else:
            raise ValueError

    def __str__(self):
        return "\n".join(
            f"{char}\n{'\n'.join(glyph)}"
            for char, glyph in (self._glyphs | self._ligatures).items()
        )

    def __repr__(self):
        return f"Font('{self._name}')"
