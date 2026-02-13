from itertools import zip_longest
from typing import Dict, List, Optional, Union

Glyph = List[str]
"""A single glyph represented by lines of text."""


class Glyphs(dict):
    """A glyph dictionary, mapping single chars or groups of chars (ligatures) to glyphs."""

    @classmethod
    def from_lines(
        cls,
        chars: Union[List[str], str],
        *glyphs: str,
        separator: Optional[str] = None,
    ) -> "Glyphs":
        """Create a Glyphs instance from lines.

        Args:
            chars (Union[str, List[str]]): String of chars or list of char groups in the same order as glyphs.
            *glyphs (str): Lines of concatenated glyphs, delimited by full column of separator char.
            separator (str): Separator char used to separate individual glyphs. Defaults to space.

        Raises:
            ValueError: Glyph lines are of unequal length.
            ValueError: Number of glyphs does not match number of chars.
        """
        if not all(len(line) == len(glyphs[0]) for line in glyphs):
            raise ValueError("Line length missmatch.")
        if len(chars) == 0:
            return Glyphs({})
        elif len(chars) == 1:
            return Glyphs({chars[0]: list(glyphs)})
        else:
            return Glyphs(cls.get_char_map(chars, *glyphs, separator=separator))

    @property
    def line_height(self) -> int:
        """Line height of glyphs."""
        return len(list(self.values())[0]) if self else 0

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
            chars (Union[List[str], str]): String or List of chars.
            glyphs (List[str]): Lines of concatenated glyphs, delimited by full column of separator.
            separator (Optional[str], optional): _description_. Defaults to None.

        Raises:
            ValueError: Number of glyphs does not match number of chars.

        Returns:
            Dict[str, List[str]]: Char to glyph map.
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

    @classmethod
    def line_trail(cls, line: str) -> int:
        """Get number of trailing whitespace.

        Args:
            line (str): Line of text.

        Returns:
            int: Trailing whitespace count.
        """
        return len(line) - len(line.rstrip())

    @classmethod
    def line_lead(cls, line: str) -> int:
        """Get number of leading whitespace.

        Args:
            line (str): Line of text.

        Returns:
            int: Leading whitespace count.
        """
        return len(line) - len(line.lstrip())

    @classmethod
    def max_overlap(cls, left: Glyph, right: Glyph) -> int:
        """Calculates the maximum number of cells two glyphs can overlap without occluding each other.

        Args:
            left (List[str]): Left glyph.
            right (List[str]): Right glyph.

        Returns:
            int: Max overlap in number of cells.
        """
        return min(
            cls.line_trail(ll) + cls.line_lead(lr) for ll, lr in zip(left, right)
        )

    @classmethod
    def merge_line(cls, left: str, right: str, spacing: int = 0) -> str:
        """Merge two lines. In case of overlapping non-space characters, the right line will occlude the left line.

        Args:
            left (str): Left line.
            right (str): Right line.
            spacing (int): Space between left and right in number of cells. Defaults to 0.

        Returns:
            str: Merged line.
        """
        if spacing >= 0:
            return left + (" " * spacing) + right
        else:
            return (
                left[:spacing]
                + "".join(
                    ll if lr.isspace() else lr
                    for ll, lr in zip(left[spacing:], right[:-spacing])
                )
                + right[-spacing:]
            )

    @classmethod
    def merge(cls, left: Glyph, right: Glyph, spacing: int = 0) -> Glyph:
        """Merges two glyphs. In case of overlapping non-space characters, the right glyph will occlude the left glyph.

        Args:
            left (List[str]): Left glyph.
            right (List[str]): Right glyph.
            spacing (int): Space between left and right in number of cells. Defaults to 0.

        Returns:
            Glyph: Merged glyph.
        """
        return [cls.merge_line(ll, lr, spacing) for ll, lr in zip(left, right)]

    @classmethod
    def boundary(cls, left: Glyph, right: Glyph, spacing: int) -> List[int]:
        """Calculates the boundary between two glyphs.

        Args:
            left (List[str]): Left glyph.
            right (List[str]): Right glyph.
            spacing (int): Space between left and right in number of cells.

        Returns:
            List[int]: Boundary in offsets from the end of the left glyph.
        """
        line_height = len(left)
        return [
            min(
                min(0, spacing + Glyphs.line_lead(right[row])),
                max(spacing, -Glyphs.line_trail(left[row])),
            )
            for row in range(line_height)
        ]

    @classmethod
    def bg_boundary(cls, left: Glyph, right: Glyph, spacing: int) -> List[int]:
        """Calculates the background boundary between two glyphs.

        Args:
            left (List[str]): Left glyph.
            right (List[str]): Right glyph.
            spacing (int): Space between left and right in number of cells.

        Returns:
            List[int]: Boundary in offsets from the end of the left glyph.
        """
        line_height = len(left)
        offsets = [0] * line_height
        for d in range(abs(spacing)):
            majority = sum(
                (1 if left[row][-(d + 1)] not in " " else 0)
                - (1 if right[row][abs(spacing) - (d + 1)] not in " " else 0)
                for row in range(line_height)
            )
            if majority > 0:
                break
            else:
                offsets = [-(d + 1)] * line_height
        return offsets
