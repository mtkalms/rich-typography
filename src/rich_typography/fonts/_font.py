from typing import Any, Dict, Iterable, List, Literal, Optional

from rich_typography.glyphs import Glyph, Glyphs

Variant = Optional[Literal["underline"]]


class Font:
    def __init__(
        self,
        name: str,
        glyphs: Dict[str, List[str]],
        ligatures: Optional[Glyphs] = None,
        letter_spacing: int = 0,
        space_width: int = 1,
        baseline: Optional[int] = None,
    ):
        self._name = name
        self._line_height = len(list(glyphs.values())[0])
        self.letter_spacing = letter_spacing
        self._glyphs = glyphs | Glyphs(self.space(space_width, self._line_height), " ")
        self._ligatures = ligatures or {}
        self._space_width = space_width
        self._baseline = baseline or self._line_height - 2

    def space_width(self):
        return self._space_width

    @classmethod
    def space(cls, width: int, line_height: int) -> str:
        return "\n".join([" " * width] * line_height)

    @classmethod
    def placeholder(cls, line_height: int) -> Glyph:
        return ["┌─┐"] + ["│ │"] * (line_height - 2) + ["└─┘"]

    @classmethod
    def underline(
        cls, glyph: Glyph, baseline: int, start: Optional[int], end: Optional[int]
    ):
        line = glyph[baseline - 1]
        start = start or 0
        end = start or len(line)
        _glyph = glyph[:]
        _glyph[baseline - 1] = (
            line[:start]
            + "".join("▔" if g == " " else g for g in line[start:end])
            + line[end:]
        )
        return _glyph

    def glyph(self, char: str, variant: Variant = None) -> Glyph:
        glyph = self._glyphs.get(char, self.placeholder(self._line_height))
        if variant == "underline":
            glyph = self.underline(glyph, self._baseline)
        return glyph

    def ligature(self, char: str, variant: Variant = None) -> Glyph:
        glyph = self._ligatures.get(char, self.placeholder(self._line_height))
        if variant == "underline":
            glyph = self.underline(glyph, self._baseline)
        return glyph

    def get(self, char: str, variant: Variant = None) -> Glyph:
        return (
            self.glyph(char, variant)
            if len(char) == 1
            else self.ligature(char, variant)
        )

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
