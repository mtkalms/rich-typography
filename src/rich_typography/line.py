from typing import Literal, Optional


LineType = Literal["underline", "underline2", "strike", "overline", "custom"]
"""Type of line. Either ansi styles "underline", "underline2", "overline", "strike", or "custom"."""


class LineStyle:
    """Style of underline, overline or strike.

    Args:
        index (int): Line index.
        line (str): Line type. Either ansi styles "underline", "underline2", "overline", "strike", or "custom". Defaults to None.
        char (str, optional): Line char. Only used when line is "custom". Defaults to None.
    """

    def __init__(self, index: int, line: LineType, char: Optional[str] = None) -> None:
        self._index = index
        self._line: LineType = line
        self._char = char

    @property
    def index(self) -> int:
        """Line index.

        Returns:
            int: Line index.
        """
        return self._index

    @property
    def line(self) -> LineType:
        """Line type. Either ansi styles "underline", "underline2", "overline", "strike", or "custom".

        Returns:
            LineType: Line type.
        """
        return self._line

    @property
    def char(self) -> Optional[str]:
        """Line char. Only used when line is "custom".

        Returns:
            Optional[str]: Line char.
        """
        return self._char

    def __or__(self, other):
        if isinstance(other, int):
            return LineStyle(
                other,
                self.line,
                self.char,
            )
        elif isinstance(other, LineStyle):
            return LineStyle(
                other.index or self.index,
                other.line or self.line,
                other.char or self.char,
            )
        else:
            return self

    def __eq__(self, value: object) -> bool:
        if isinstance(value, LineStyle):
            return (
                self.index == value.index
                and self.line == value.line
                and self.char == value.char
            )
        return NotImplemented
