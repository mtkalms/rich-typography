from itertools import zip_longest
from typing import Dict, List, Union

Glyph = List[str]


class Glyphs(dict):
    def __init__(self, chars: Union[List[str], str], *glyphs: str):
        # Ignore leading/trailing line breaks
        _glyphs = [g for g in glyphs if g]
        self._line_height = len(_glyphs)
        if len(chars) == 1:
            super().__init__({chars[0]: _glyphs})
        else:
            super().__init__(self.get_char_map(_glyphs, chars))
        # Preflight Checks
        for char, glyph in self.items():
            if not all(len(line) == len(glyph[0]) for line in glyph):
                raise ValueError(f"Glyph {char} has lines of unqual length.")

    def __or__(self, other):
        if not isinstance(other, Glyphs):
            raise TypeError(f"Unsupported operand type for |: {type(other)}")
        if other._line_height != self._line_height:
            raise ValueError(
                f"Line height missmatch: {other._line_height} != {self._line_height}"
            )
        return super().__or__(other)

    def __str__(self) -> str:
        result = " ".join(c.ljust(len(g[0])) for c, g in self.items())
        for line in zip_longest(*self.values()):
            result += "\n" + " ".join(line)
        return result

    @classmethod
    def get_char_map(
        cls, lines: List[str], chars: Union[List[str], str]
    ) -> Dict[str, Glyph]:
        columns = zip(*lines)
        breaks = [i for i, d in enumerate(columns) if all(c == " " for c in d)]
        result = {}
        for idx, pos in enumerate(zip([-1] + breaks, breaks + [len(lines[0])])):
            start, end = pos
            result[chars[idx]] = ["".join(line[(start + 1) : end]) for line in lines]
        return result
