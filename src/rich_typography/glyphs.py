from itertools import zip_longest
from typing import Dict, List, Optional, Union

Glyph = List[str]
"""A single glyph represented by lines of text."""


class Glyphs(dict):
    """A glyph dictionary mapping single chars or groups of chars (ligatures) to glyphs.

    Args:
        chars (Union[List[str], str]): String of chars or list of char groups in the same order as glyphs.
        *glyphs (str): Lines of concatenated glyphs, delimited by full column of separator char.
        separator (str): Separator char used to separate individual glyphs. Defaults to space.

    Raises:
        ValueError: Glyph lines are of unequal length.
        ValueError: Number of glyphs does not match number of chars.
    """

    def __init__(
        self,
        chars: Union[List[str], str],
        *glyphs: str,
        separator: Optional[str] = None,
    ):
        self._line_height = len(glyphs)
        if not all(len(line) == len(glyphs[0]) for line in glyphs):
            raise ValueError("Glyphs has lines of unqual length.")
        if len(chars) == 1:
            super().__init__({chars[0]: list(glyphs)})
        else:
            super().__init__(self.get_char_map(chars, *glyphs, separator=separator))

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

    def __repr__(self) -> str:
        return f"<Glyphs: {' '.join(self.keys())}>"

    @classmethod
    def get_char_map(
        cls,
        chars: Union[List[str], str],
        *glyphs: str,
        separator: Optional[str] = None,
    ) -> Dict[str, Glyph]:
        """Map chars to split glyphs. Glyphs are split at every full column of the separator char.

        Args:
            lines (List[str]): Lines of concatenated glyphs, delimited by full column of separator.
            chars (Union[List[str], str]): String or List of chars.
            separator (Optional[str], optional): _description_. Defaults to None.

        Raises:
            ValueError: Number of glyphs does not match number of chars.

        Returns:
            Dict[str, Glyph]: Char to glyph map.
        """
        _separator = separator or " "
        columns = zip(*glyphs)
        breaks = [i for i, d in enumerate(columns) if all(c == _separator for c in d)]
        result = {}
        for idx, pos in enumerate(zip([-1] + breaks, breaks + [len(glyphs[0])])):
            start, end = pos
            result[chars[idx]] = ["".join(line[(start + 1) : end]) for line in glyphs]
        if len(result) != len(chars):
            raise ValueError("Number of glyphs does not match number of chars.")
        return result
