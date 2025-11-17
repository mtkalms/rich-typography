from typing import Any, Dict, Iterable, List, Optional
from rich_typography.glyphs import Glyphs, Glyph


class Font:
    def __init__(
        self,
        name: str,
        glyphs: Dict[str, List[str]],
        ligatures: Optional[Glyphs] = None,
        letter_spacing: int = 0,
        space_width: int = 1,
    ):
        self._name = name
        self._line_height = len(list(glyphs.values())[0])
        self.letter_spacing = letter_spacing
        self._glyphs = glyphs | Glyphs(self.space(space_width, self._line_height), " ")
        self._ligatures = ligatures or {}
        self._space_width = space_width

    def space_width(self):
        return self._space_width

    @classmethod
    def space(cls, width: int, line_height: int) -> str:
        return "\n".join([" " * width] * line_height)

    @classmethod
    def placeholder(cls, line_height: int) -> Glyph:
        return ["┌─┐"] + ["│ │"] * (line_height - 2) + ["└─┘"]

    def glyph(self, char: str) -> Glyph:
        return self._glyphs.get(char, self.placeholder(self._line_height))

    def ligature(self, char: str) -> Glyph:
        return self._ligatures.get(char, self.placeholder(self._line_height))

    def get(self, char: str) -> Glyph:
        return self.glyph(char) if len(char) == 1 else self.ligature(char)

    def max_ligature_length(self) -> int:
        return len(max(self._ligatures, key=len))

    def ligatures(self) -> Iterable[str]:
        return self._ligatures.keys()

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
        return f"Font('{self._name}')"
