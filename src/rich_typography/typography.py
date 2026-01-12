import re
from dataclasses import dataclass
from functools import partial
from typing import Dict, Iterable, List, Literal, Optional, Tuple, Union

from rich.color import ColorType
from rich.console import (
    Console,
    ConsoleOptions,
    JustifyMethod,
    OverflowMethod,
    RenderResult,
)
from rich.containers import Lines
from rich.control import strip_control_codes
from rich.segment import Segment
from rich.style import Style
from rich.text import Span, Text
from rich.emoji import EmojiVariant
from rich.jupyter import JupyterMixin
from rich.measure import Measurement

from rich_typography.fonts import SEMISERIF, Font, NON_OVERLAPPING, LineStyle
from rich_typography.glyphs import Glyphs
import bisect

LigatureStyleMethod = Literal["first", "last"]

DEFAULT_JUSTIFY: "JustifyMethod" = "default"
DEFAULT_OVERFLOW: "OverflowMethod" = "fold"
LINE_STYLE_RESET = Style(
    underline=False,
    underline2=False,
    overline=False,
    strike=False,
)


@dataclass
class MutableSpan:
    start: int
    end: int
    style: Optional[Style]

    def __repr__(self) -> str:
        return f"<{self.start}, {self.end}>"

    @classmethod
    def resolve(
        cls,
        spans: List["MutableSpan"],
    ) -> List["MutableSpan"]:
        """Resolve overlaping spans in a list of spans.
        In case of an overlap a span takes precident over any previous spans in the list.
        Previous spans either have their end readjusted or are removed if fully overlapped.

        Args:
            spans (List[MutableSpan]): A list of style spans.

        Returns:
            List[MutableSpan]: Resolved list of style spans.
        """
        last = None
        result = []
        for span in reversed(spans):
            if span.start > span.end:
                continue
            if last is None:
                result.append(span)
                last = span
            elif span.start < last.start:
                span.end = last.start
                result.append(span)
                last = span
        return list(reversed(result))


class Typography(JupyterMixin):
    """Large text with color and style.

    Args:
        text (str, optional): Default unstyled text. Defaults to "".
        style (Union[str, Style], optional): Base style for text. Defaults to "".
        justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
        overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
        no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
        tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        spans (List[Span], optional): A list of predefined style spans. Defaults to None.
        font (Font, optional): Font used to render text. Defaults to SEMISERIF.
        adjust_spacing (int, optional): Adjust letter spacing. Defaults to 0.
        use_kerning (bool, optional): Enable automatic kerning. Defaults to True.
        use_ligatures (bool, optional): Enable all ligatures the font provides. Defaults to True.
        style_ligatures (str, optional): Ligature style method: "first", "last". Defaults to None.
    """

    __slots__ = [
        "_text",
        "style",
        "justify",
        "overflow",
        "no_wrap",
        "end",
        "tab_size",
        "_spans",
        "_length",
        "font",
        "adjust_spacing",
        "use_kerning",
        "use_ligatures",
        "style_ligatures",
    ]

    def __init__(
        self,
        text: str = "",
        style: Union[str, Style] = "",
        *,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
        no_wrap: Optional[bool] = None,
        tab_size: Optional[int] = None,
        spans: Optional[List[Span]] = None,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
        style_ligatures: Optional["LigatureStyleMethod"] = None,
    ):
        sanitized_text = strip_control_codes(text)
        self._text = [sanitized_text]
        self._length = len(sanitized_text)
        self.style = style
        self.justify: Optional["JustifyMethod"] = justify
        self.overflow: Optional["OverflowMethod"] = overflow
        self.no_wrap = no_wrap
        self.tab_size = tab_size
        self._spans: List[Span] = spans or []
        self.font = font
        self.adjust_spacing = adjust_spacing
        self.use_kerning = use_kerning
        self.use_ligatures = use_ligatures
        self.style_ligatures: Optional["LigatureStyleMethod"] = style_ligatures

    # PROPERTIES

    @property
    def plain(self) -> str:
        """Get the text as a single string."""
        if len(self._text) != 1:
            self._text[:] = ["".join(self._text)]
        return self._text[0]

    @plain.setter
    def plain(self, new_text: str) -> None:
        """Set the text to a new value."""
        if new_text != self.plain:
            sanitized_text = strip_control_codes(new_text)
            self._text[:] = [sanitized_text]
            old_length = self._length
            self._length = len(sanitized_text)
            if old_length > self._length:
                self._spans[:] = [
                    (
                        span
                        if span.end < self._length
                        else Span(span.start, min(self._length, span.end), span.style)
                    )
                    for span in self._spans
                    if span.start < self._length
                ]

    @property
    def spans(self) -> List[Span]:
        """Get a reference to the internal list of spans."""
        return self._spans

    @spans.setter
    def spans(self, spans: List[Span]) -> None:
        """Set spans."""
        self._spans = spans[:]

    def letter_adjust(self, left: str, right: str) -> int:
        """Calculates the spacing between two glyphs.

        Args:
            left (str): Left character or ligature.
            right (str): Right character or ligature.

        Returns:
            int: Spacing in number of cells.
        """
        value = self.font.letter_spacing + self.adjust_spacing
        if self.use_kerning and left != " " and right != " ":
            value -= Glyphs.max_overlap(*map(self.font.get, [left, right]))
        return value

    # OPERATOR OVERRIDES

    def __len__(self) -> int:
        return self._length

    def __bool__(self) -> bool:
        return bool(self._length)

    def __repr__(self) -> str:
        return f"<typography {self.plain!r} {self._spans!r} {self.style!r}>"

    def __str__(self) -> str:
        return self.plain

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Typography):
            return NotImplemented
        return self.plain == other.plain and self._spans == other._spans

    def __contains__(self, other: object) -> bool:
        if isinstance(other, str):
            return other in self.plain
        elif isinstance(other, Text):
            return other.plain in self.plain
        return False

    # CONVERTERS

    def copy(self) -> "Typography":
        """Return a copy of this instance."""
        return Typography(
            self.plain,
            style=self.style,
            justify=self.justify,
            overflow=self.overflow,
            no_wrap=self.no_wrap,
            tab_size=self.tab_size,
            spans=self._spans[:],
            font=self.font,
            adjust_spacing=self.adjust_spacing,
            use_kerning=self.use_kerning,
            use_ligatures=self.use_ligatures,
            style_ligatures=self.style_ligatures,
        )

    @classmethod
    def from_text(
        cls,
        text: Text,
        *,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
        style_ligatures: Optional[LigatureStyleMethod] = None,
    ) -> "Typography":
        """Create Typography instance from Text.

        Args:
            text (Text): Text instance.
            font (Font, optional): Font used to render text. Defaults to SEMISERIF.
            adjust_spacing (int, optional): Adjust letter spacing. Defaults to 0.
            use_kerning (bool, optional): Enable automatic kerning. Defaults to True.
            use_ligatures (bool, optional): Enable all ligatures the font provides. Defaults to True.
            style_ligatures (str, optional): Ligature style method: "first", "last". Defaults to None.

        Returns:
            Typography: A Typography instance based on Text.
        """
        return Typography(
            text.plain,
            style=text.style,
            spans=text.spans[:],
            justify=text.justify,
            overflow=text.overflow,
            no_wrap=text.no_wrap,
            tab_size=text.tab_size,
            font=font,
            adjust_spacing=adjust_spacing,
            use_kerning=use_kerning,
            use_ligatures=use_ligatures,
            style_ligatures=style_ligatures,
        )

    @classmethod
    def from_markup(
        cls,
        text: str,
        *,
        style: Union[str, Style] = "",
        emoji: bool = True,
        emoji_variant: Optional[EmojiVariant] = None,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
        style_ligatures: Optional[LigatureStyleMethod] = None,
    ) -> "Typography":
        """Create Typography instance from markup.

        Args:
            text (str): A string containing console markup.
            style (Union[str, Style], optional): Base style for text. Defaults to "".
            emoji (bool, optional): Also render emoji code. Defaults to True.
            emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
            justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
            overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
            end (str, optional): Character to end text with. Defaults to "\\\\n".
            font (Font, optional): Font used to render text. Defaults to SEMISERIF.
            adjust_spacing (int, optional): Adjust letter spacing. Defaults to 0.
            use_kerning (bool, optional): Enable automatic kerning. Defaults to True.
            use_ligatures (bool, optional): Enable all ligatures the font provides. Defaults to True.
            style_ligatures (str, optional): Ligature style method: "first", "last". Defaults to None.

        Returns:
            Typography: A Typography instance with markup rendered.
        """
        return cls.from_text(
            Text.from_markup(
                text,
                style=style,
                emoji=emoji,
                emoji_variant=emoji_variant,
                justify=justify,
                overflow=overflow,
            ),
            font=font,
            adjust_spacing=adjust_spacing,
            use_kerning=use_kerning,
            use_ligatures=use_ligatures,
            style_ligatures=style_ligatures,
        )

    def to_text(self) -> Text:
        """Create Text instance from Typography.

        Returns:
            Text: A Text instance based on Typography.
        """
        return Text(
            self.plain,
            style=self.style,
            justify=self.justify,
            overflow=self.overflow,
            no_wrap=self.no_wrap,
            tab_size=self.tab_size,
            spans=self._spans[:],
        )

    def rendered_width(self, text: str) -> int:
        """Get length of rendered text with current settings.

        Args:
            text (str): Text.

        Returns:
            int: Length of rendered text.
        """

        def glyph_width(c: str) -> int:
            return len(self.font.get(c)[0])

        if not text:
            return 0
        glyphs = list(self.split_glyphs(text).values())
        width = glyph_width(glyphs[0])
        for a, b in zip(glyphs[:-1], glyphs[1:]):
            width += glyph_width(b) + self.letter_adjust(a, b)
        return width

    def split_glyphs(self, text: str) -> Dict[int, str]:
        """Splits text into individual glyphs, based on the available ligatures in the font.

        Args:
            text (str): _description_

        Returns:
            Dict[int, str]: _description_
        """
        if not self.use_ligatures:
            return dict(enumerate(text))
        glyphs: Dict[int, str] = {}
        last = 0
        if not self.font.ligatures:
            return dict(enumerate(text))
        ligatures = reversed(sorted(self.font.ligatures, key=len))
        for ligature in re.finditer("|".join(ligatures), text):
            start, end = ligature.span()
            glyphs |= dict(enumerate(text[last:start], last))
            glyphs[start] = text[start:end]
            last = end
        glyphs |= dict(enumerate(text[last:], last))
        return glyphs

    def truncate(
        self,
        max_width: int,
        *,
        overflow: Optional[OverflowMethod],
    ) -> None:
        """Truncate text if it is longer than a given width.

        Args:
            max_width (int): Maximum number of characters in text.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None, to use self.overflow.
        """

        def set_cell_size(text: str, width: int) -> str:
            while self.rendered_width(text) > width:
                text = text[:-1]
            return text

        _overflow = overflow or self.overflow or DEFAULT_OVERFLOW
        length = self.rendered_width(self.plain)
        if _overflow == "ignore" or length <= max_width:
            return
        if _overflow == "ellipsis":
            ellipsis = "…" if "…" in self.font else "..."
            max_width -= self.rendered_width(ellipsis)
            self.plain = set_cell_size(self.plain, max_width) + ellipsis
        else:
            self.plain = set_cell_size(self.plain, max_width)

    def wrap(
        self,
        width: int,
        *,
        overflow: Optional["OverflowMethod"] = None,
        tab_size: int = 8,
        no_wrap: Optional[bool] = None,
    ) -> Iterable["Typography"]:
        """Word wrap the text.

        Args:
            console (Console): Console instance.
            width (int): Number of cells available per line.
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None.
            tab_size (int, optional): Default tab size. Defaults to 8.
            no_wrap (bool, optional): Disable wrapping, Defaults to False.

        Returns:
            Iterable[Typography]: Typography for each line.
        """
        wrap_overflow = overflow or self.overflow or DEFAULT_OVERFLOW
        no_wrap = bool(no_wrap or self.no_wrap) or wrap_overflow == "ignore"
        lines = Lines()
        text = self.to_text()
        for line in text.split(allow_blank=True):
            if "\t" in line:
                line.expand_tabs(tab_size)
            if no_wrap:
                new_lines = [line]
            else:
                offsets = self._divide_offsets(
                    str(line), width, wrap_overflow == "fold"
                )
                new_lines = line.divide(offsets)
            lines.extend(new_lines)
        typography_lines = [
            Typography.from_text(
                line,
                font=self.font,
                adjust_spacing=self.adjust_spacing,
                use_kerning=self.use_kerning,
                use_ligatures=self.use_ligatures,
                style_ligatures=self.style_ligatures,
            )
            for line in lines
        ]
        for line in typography_lines:
            line.truncate(width, overflow=overflow)
        return typography_lines

    # RENDERING

    def render(
        self,
        console: "Console",
        width: int,
        *,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
    ) -> Iterable["Segment"]:
        """Render as Segments.

        Args:
            console (Console): Console instance.
            width (int): Number of cells available.
            justify (str, optional): Justify method: "default", "left", "center", "full", "right". Defaults to "default".
            overflow (str, optional): Overflow method: "crop", "fold", or "ellipsis". Defaults to None.


        Returns:
            Iterable[Segment]: Result of render that may be written to the console.
        """

        def has_background(style: Optional[Style]):
            if not style or not style.bgcolor:
                return False
            return style.bgcolor != ColorType.STANDARD

        wrap_justify = justify or self.justify or DEFAULT_JUSTIFY
        # wrap_overflow = overflow or self.overflow or DEFAULT_OVERFLOW
        line_height = self.font.line_height
        letter_spacing = self.font.letter_spacing
        for line in self.plain.splitlines():
            # Align style borders to glyphs
            fragments = self._style_fragments(line, console)
            # Right-strip if appropriate for justify method
            if wrap_justify in ["right", "center", "justify"]:
                line = line.rstrip()
            # Apply justify
            # Note: we do this here, because the length of a rendered space can
            # be other than 1, and indents cannot be expressed in text spaces.
            line_width = self.rendered_width(line)
            if wrap_justify == "right":
                indent = int(width - line_width)
            elif wrap_justify == "center":
                indent = int((width - line_width) // 2)
            else:
                indent = 0
            # Adjust style borders
            if wrap_justify == "full":
                fragments = self._justify_full(width, line, fragments)
            # Prepapre accumulators and apply indents
            row_spans = [[MutableSpan(0, 0, None)] for _ in range(line_height)]
            row_chars = ["" + " " * indent] * line_height
            last_char = ""
            last_style = None
            for fragment_text, fragment_style in fragments:
                if not fragment_text:
                    continue
                if self.use_ligatures:
                    segment_chars = list(self.split_glyphs(fragment_text).values())
                else:
                    segment_chars = list(fragment_text)
                # Render fragment
                fragment = []
                fragment_char = None
                for char in segment_chars:
                    letter = self.font.get(char)
                    if fragment_char is None:
                        fragment = letter
                    else:
                        spacing = letter_spacing + self.adjust_spacing
                        if self._should_overlap(fragment_char, char):
                            spacing -= Glyphs.max_overlap(fragment, letter)
                        fragment = Glyphs.merge(fragment, letter, spacing)
                    fragment_char = char
                fragment_spacing = letter_spacing + self.adjust_spacing
                if self._should_overlap(last_char, fragment_text[0]):
                    fragment_spacing -= Glyphs.max_overlap(row_chars, fragment)
                last_char = fragment_char
                # Determine if styles overlap
                split_styles = (
                    has_background(fragment_style) or has_background(last_style)
                ) and fragment_spacing != 0
                # Calculate offsets
                fg_offsets = Glyphs.boundary(row_chars, fragment, fragment_spacing)
                bg_offsets = Glyphs.bg_boundary(row_chars, fragment, fragment_spacing)
                if split_styles:
                    # Add mixed styles for overlap
                    for d in range(len(row_spans)):
                        row_spans[d][-1].end = len(row_chars[d]) + min(
                            fg_offsets[d], bg_offsets[d]
                        )
                        # Row overlaps segment
                        if fg_offsets[d] > bg_offsets[d]:
                            row_spans[d].append(
                                MutableSpan(
                                    len(row_chars[d]) + bg_offsets[d],
                                    len(row_chars[d]) + fg_offsets[d],
                                    self._overlay_styles(last_style, fragment_style),
                                )
                            )
                        # Fragment overlaps row
                        elif fg_offsets[d] < bg_offsets[d]:
                            row_spans[d].append(
                                MutableSpan(
                                    len(row_chars[d]) + fg_offsets[d],
                                    len(row_chars[d]) + bg_offsets[d],
                                    self._overlay_styles(fragment_style, last_style),
                                )
                            )
                else:
                    for d in range(len(row_spans)):
                        row_spans[d][-1].end = len(row_chars[d]) + fg_offsets[d]
                for d in range(len(row_spans)):
                    row_spans[d].append(
                        MutableSpan(
                            len(row_chars[d])
                            + (
                                max(bg_offsets[d], fg_offsets[d])
                                if split_styles
                                else fg_offsets[d]
                            ),
                            len(row_chars[d]) + len(fragment[d]),
                            fragment_style,
                        )
                    )
                # Add current letter/ligature to result
                row_chars = Glyphs.merge(row_chars, fragment, fragment_spacing)
                last_style = fragment_style
            # Truncate
            row_chars = [row[:width] for row in row_chars]
            # Right-pad if appropriate for justify method
            if wrap_justify and wrap_justify != "default":
                row_chars = [row + " " * (width - len(row)) for row in row_chars]
            # Adjust last style spans
            for row in row_spans:
                row[-1].end = len(row_chars[0])
            # Resolve span overlap
            row_spans = [MutableSpan.resolve(spans) for spans in row_spans]
            # Render result
            for row_num, (row, spans) in enumerate(zip(row_chars, row_spans)):
                for span in spans:
                    style: Optional[Style] = span.style
                    fragment = row[span.start : span.end]
                    if style:
                        style_override = LINE_STYLE_RESET
                        for line in ["underline", "underline2", "overline", "strike"]:
                            line_style: LineStyle = getattr(self.font, line)
                            if not getattr(style, line) or line_style.index != row_num:
                                continue
                            if line_style.line == "custom" and line_style.char:
                                fragment = fragment.replace(" ", line_style.char)
                            else:
                                _line = (
                                    line
                                    if line_style.line == "custom"
                                    else line_style.line
                                )
                                override = {_line: True}
                                style_override += Style(*{}, **override)
                        style += style_override
                    yield (Segment(fragment, style=style))
                yield Segment("\n")

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        tab_size = console.tab_size if self.tab_size is None else self.tab_size
        no_wrap = bool(self.no_wrap or options.no_wrap)
        justify = self.justify or options.justify or DEFAULT_JUSTIFY
        overflow = self.overflow or options.overflow or DEFAULT_OVERFLOW
        lines: Iterable["Typography"] = self.wrap(
            width=options.max_width,
            tab_size=tab_size or 8,
            no_wrap=no_wrap,
            overflow=overflow,
        )
        for line in lines:
            yield from line.render(
                console=console,
                width=options.max_width,
                justify=justify,
                overflow=overflow,
            )

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> Measurement:
        glyphs = set(
            re.findall("|".join(self.font.ligatures), self.plain) + list(self.plain)
        )
        minimum = max(self.rendered_width(g) for g in glyphs)
        return Measurement(minimum, self.rendered_width(self.plain))

    # PRIVATE

    def _chop_cells(self, text: str, width: int) -> Iterable[str]:
        result = []
        lst, curr = 0, 1
        while curr < len(text):
            while curr < len(text) and self.rendered_width(text[lst:curr]) <= width:
                curr += 1
            result.append(text[lst:curr])
            lst = curr
        if lst < curr:
            result.append(text[lst:curr])
        return result

    def _divide_offsets(
        self,
        text: str,
        width: int,
        fold: bool,
    ) -> Iterable[int]:
        offsets = []
        space_length = self.font.space_width
        offset = 0
        length = 0
        for word in text.split(" "):
            remaining = width - length - space_length
            word_length = self.rendered_width(word)
            if word_length > remaining:
                if (
                    fold
                    and word_length > width
                    and self.rendered_width(word[0]) <= remaining
                ):
                    fold_offset = 1
                    while self.rendered_width(word[: fold_offset + 1]) <= remaining:
                        fold_offset += 1
                    part = word[:fold_offset]
                    part_length = self.rendered_width(part)
                    if offset > 0:
                        offset += 1
                    offset += fold_offset
                    if length > 0:
                        length += space_length
                    length += part_length
                    for part in self._chop_cells(word[fold_offset:], width):
                        offsets.append(offset)
                        offset += len(part)
                        length = self.rendered_width(part)
                else:
                    if length > 0 or not word:
                        length += space_length
                    length = word_length
                    if offset > 0 or not word:
                        offset += 1
                    offsets.append(offset)
                    offset += len(word)
            else:
                if length > 0 or not word:
                    length += space_length
                length += word_length
                if offset > 0 or not word:
                    offset += 1
                offset += len(word)
        offsets.append(offset)
        return offsets

    def _glyph_borders(self, text: str) -> List[int]:
        result = list(range(len(text)))
        if not (self.use_ligatures and self.font.ligatures):
            return result
        ligatures = reversed(sorted(self.font.ligatures, key=len))
        for ligature in re.finditer("|".join(ligatures), text):
            start, end = ligature.span()
            for d in range(start + 1, end):
                result.remove(d)
        return result

    def _style_borders(
        self,
        console: Console,
        width: int,
    ) -> List[Tuple[int, Optional[Style]]]:
        def combine_styles(styles: Iterable[Union[Style, str]]) -> Optional[Style]:
            get_style = partial(console.get_style, default=Style.null())
            style_list = list(styles)
            if not style_list:
                return None
            return Style.combine(get_style(d) for d in style_list)

        styles: List[Union[Style, str]] = [console.get_style(self.style)]
        borders: Dict[int, List[Tuple[int, int]]] = {
            0: [(1, 0)],
            len(self.plain): [(-1, 0)],
        }
        for idx, span in enumerate(self.spans, 1):
            borders[span.start] = borders.get(span.start, []) + [(1, idx)]
            borders[span.end] = borders.get(span.end, []) + [(-1, idx)]
            styles.append(span.style)

        stack: List[int] = []
        result: List[Tuple[int, Optional[Style]]] = []
        for pos in sorted(borders):
            for direction, idx in sorted(borders[pos]):
                if direction > 0:
                    stack.append(idx)
                else:
                    stack.remove(idx)
            if pos < width:
                result.append(
                    (pos, combine_styles(styles[d] for d in stack if styles[d]))
                )
        if 0 not in borders:
            result.insert(0, (0, None))
        return result

    def _style_fragments(
        self, text: str, console: Console
    ) -> List[Tuple[str, Optional[Style]]]:
        def neighbours(
            numbers: List[int], target: int
        ) -> Tuple[Optional[int], Optional[int]]:
            right = bisect.bisect_right(numbers, target)
            left = right - 1
            return (
                numbers[left] if left >= 0 else None,
                numbers[right] if right < len(numbers) else None,
            )

        glyphs = self._glyph_borders(text)
        styles = self._style_borders(console, len(text))
        if self.use_ligatures:
            corrected = {}
            for pos, style in styles:
                if pos in glyphs:
                    corrected[pos] = style
                else:
                    prv, nxt = neighbours(glyphs, pos)
                    if prv is not None and self.style_ligatures == "last":
                        corrected[prv] = style
                    elif nxt is not None:
                        corrected[nxt] = style
        else:
            corrected = dict(styles)
        result = []
        segment_ends = list(corrected.keys())[1:] + [(len(text))]
        for (start, style), end in zip(corrected.items(), segment_ends):
            result.append((text[start:end], style))
        return result

    def _overlay_styles(self, fg: Optional[Style], bg: Optional[Style]):
        _fg = fg or Style.null()
        _bg = bg or Style.null()
        return Style(
            color=_fg.color,
            blink=_fg.blink,
            strike=_fg.strike,
            bgcolor=_bg.bgcolor,
            underline=_bg.underline,
            underline2=_bg.underline2,
            overline=_bg.overline,
        )

    def _justify_full(
        self, width: int, line: str, spans: List[Tuple[str, Optional[Style]]]
    ) -> List[Tuple[str, Optional[Style]]]:
        space_width = self.font.space_width
        line = line.rstrip()
        line_width = self.rendered_width(line)
        words = line.split(" ")
        num_spaces = len(words) - 1
        words_size = line_width - (num_spaces * space_width)
        spaces = [1 for d in range(num_spaces)]
        index = 0
        if spaces:
            while words_size + num_spaces * space_width < width:
                spaces[len(spaces) - index - 1] += 1
                num_spaces += 1
                index = (index + 1) % len(spaces)
        adjusted_line = "".join(
            word + (" " * space) for word, space in zip(words, spaces + [0])
        )
        result = []
        pos = 0
        for txt, style in spans:
            end = pos + len(txt)
            spaces_before_pos = line[:pos].count(" ")
            spaces_before_end = line[:end].count(" ")
            _pos = pos + sum(spaces[:spaces_before_pos]) - spaces_before_pos
            _end = end + sum(spaces[:spaces_before_end]) - spaces_before_end
            result.append((adjusted_line[_pos:_end], style))
            pos = end
        return result

    def _should_overlap(self, a: Optional[str], b: Optional[str]) -> bool:
        if not a or not b:
            return False
        return self.use_kerning and not any(c in NON_OVERLAPPING for c in [a, b])
