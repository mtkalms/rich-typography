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

from rich_typography.fonts import SEMISERIF, Font
from rich_typography.fonts._font import NON_OVERLAPPING
from rich_typography.glyphs import Glyph
import bisect

LigatureStyleMethod = Literal["first", "last"]

DEFAULT_JUSTIFY: "JustifyMethod" = "default"
DEFAULT_OVERFLOW: "OverflowMethod" = "fold"


def _trailing(line: str):
    return len(line) - len(line.rstrip())


def _leading(line: str):
    return len(line) - len(line.lstrip())


def neighbours(numbers: List[int], target: int) -> Tuple[Optional[int], Optional[int]]:
    right = bisect.bisect_right(numbers, target)
    left = right - 1
    return (
        numbers[left] if left >= 0 else None,
        numbers[right] if right < len(numbers) else None,
    )


def has_background(style: Optional[Style]):
    if not style or not style.bgcolor:
        return False
    return style.bgcolor != ColorType.STANDARD


@dataclass
class MutableSpan:
    start: int
    end: int
    style: Optional[Style]

    def __repr__(self) -> str:
        return f"<{self.start}, {self.end}>"


class Typography:
    def __init__(
        self,
        text: str = "",
        style: Union[str, Style] = "",
        *,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
        no_wrap: Optional[bool] = None,
        end: str = "\n",
        tab_size: Optional[int] = None,
        spans: Optional[List[Span]] = None,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
        style_ligatures: Optional["LigatureStyleMethod"] = None,
    ):
        sanitized_text = strip_control_codes(text)
        self._text = sanitized_text
        self.style = style
        self.justify: Optional["JustifyMethod"] = justify
        self.overflow: Optional["OverflowMethod"] = overflow
        self.no_wrap = no_wrap
        self.end = end
        self.tab_size = tab_size
        self._spans: List[Span] = spans or []
        self._font = font
        self._adjust_spacing = adjust_spacing
        self._use_kerning = use_kerning
        self._use_ligartures = use_ligatures
        self._style_ligatures: Optional["LigatureStyleMethod"] = style_ligatures

    @classmethod
    def max_overlap(cls, a: Glyph, b: Glyph) -> int:
        return min(_trailing(la) + _leading(lb) for la, lb in zip(a, b))

    @classmethod
    def merge_lines(cls, a: str, b: str) -> str:
        return "".join(rlb if rlb != " " else rla for rla, rlb in zip(a, b))

    @classmethod
    def merge_glyphs(cls, a: Glyph, b: Glyph, offset: int) -> Glyph:
        if offset >= 0:
            return [la + (" " * offset) + lb for la, lb in zip(a, b)]
        else:
            return [
                la[:offset] + cls.merge_lines(la[offset:], lb[:-offset]) + lb[-offset:]
                for la, lb in zip(a, b)
            ]

    def letter_adjust(self, a: str, b: str) -> int:
        value = self._font.letter_spacing + self._adjust_spacing
        if self._use_kerning and a != " " and b != " ":
            value -= self.max_overlap(*map(self._font.get, [a, b]))
        return value

    def split_glyphs(self, text: str) -> Dict[int, str]:
        if not self._use_ligartures:
            return dict(enumerate(text))
        glyphs: Dict[int, str] = {}
        last = 0
        if not self._font.ligatures:
            return dict(enumerate(text))
        ligatures = reversed(sorted(self._font.ligatures, key=len))
        for ligature in re.finditer("|".join(ligatures), text):
            start, end = ligature.span()
            glyphs |= dict(enumerate(text[last:start], last))
            glyphs[start] = text[start:end]
            last = end
        glyphs |= dict(enumerate(text[last:], last))
        return glyphs

    def __str__(self) -> str:
        return self._text

    def glyph_width(self, a: str):
        return len(self._font.get(a)[0])

    def rendered_width(self, text) -> int:
        if not text:
            return 0
        glyphs = list(self.split_glyphs(text).values())
        width = self.glyph_width(glyphs[0])
        for a, b in zip(glyphs[:-1], glyphs[1:]):
            width += self.glyph_width(b) + self.letter_adjust(a, b)
        return width

    def copy(self) -> "Typography":
        return Typography(
            self._text,
            style=self.style,
            justify=self.justify,
            overflow=self.overflow,
            no_wrap=self.no_wrap,
            end=self.end,
            tab_size=self.tab_size,
            spans=self._spans[:],
            font=self._font,
            adjust_spacing=self._adjust_spacing,
            use_kerning=self._use_kerning,
            use_ligatures=self._use_ligartures,
            style_ligatures=self._style_ligatures,
        )

    @classmethod
    def from_text(
        cls,
        text: Text,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
        style_ligatures: Optional[LigatureStyleMethod] = None,
    ) -> "Typography":
        return Typography(
            text.plain,
            style=text.style,
            spans=text.spans[:],
            justify=text.justify,
            overflow=text.overflow,
            no_wrap=text.no_wrap,
            end=text.end,
            tab_size=text.tab_size,
            font=font,
            adjust_spacing=adjust_spacing,
            use_kerning=use_kerning,
            use_ligatures=use_ligatures,
            style_ligatures=style_ligatures,
        )

    def to_text(self) -> Text:
        return Text(
            self._text,
            style=self.style,
            justify=self.justify,
            overflow=self.overflow,
            no_wrap=self.no_wrap,
            end=self.end,
            tab_size=self.tab_size,
            spans=self._spans[:],
        )

    def set_cell_size(self, text: str, width: int) -> str:
        while self.rendered_width(text) > width:
            text = text[:-1]
        return text

    def truncate(self, max_width: int, *, overflow: Optional[OverflowMethod]) -> None:
        _overflow = overflow or self.overflow or DEFAULT_OVERFLOW
        if _overflow != "ignore":
            length = self.rendered_width(self._text)
            if length > max_width:
                if _overflow == "ellipsis":
                    ellipsis = "…" if "…" in self._font else "..."
                    max_width -= self.rendered_width(ellipsis)
                    self._text = self.set_cell_size(self._text, max_width) + ellipsis
                else:
                    self._text = self.set_cell_size(self._text, max_width)

    def wrap(
        self,
        width: int,
        *,
        tab_size: int = 8,
        overflow: Optional["OverflowMethod"] = None,
        no_wrap: Optional[bool] = None,
    ) -> Iterable["Typography"]:
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
                offsets = self.divide(str(line), width, wrap_overflow == "fold")
                new_lines = line.divide(offsets)
            # for line in new_lines:
            #     line.rstrip_end(width)
            lines.extend(new_lines)
        typography_lines = [
            Typography.from_text(
                line,
                self._font,
                self._adjust_spacing,
                self._use_kerning,
                self._use_ligartures,
                self._style_ligatures,
            )
            for line in lines
        ]
        for line in typography_lines:
            line.truncate(width, overflow=overflow)
        return typography_lines

    def chop_cells(self, text: str, width: int) -> Iterable[str]:
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

    def divide(self, text: str, width: int, fold: bool) -> Iterable[int]:
        offsets = []
        space_length = self._font.space_width
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
                    for part in self.chop_cells(word[fold_offset:], width):
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

    def glyph_borders(self, text: str) -> List[int]:
        result = list(range(len(text)))
        if not (self._use_ligartures and self._font.ligatures):
            return result
        ligatures = reversed(sorted(self._font.ligatures, key=len))
        for ligature in re.finditer("|".join(ligatures), text):
            start, end = ligature.span()
            for d in range(start + 1, end):
                result.remove(d)
        return result

    def style_borders(
        self, console: Console, width: int
    ) -> List[Tuple[int, Optional[Style]]]:
        def combine_styles(styles: Iterable[Union[Style, str]]) -> Optional[Style]:
            get_style = partial(console.get_style, default=Style.null())
            style_list = list(styles)
            if not style_list:
                return None
            return Style.combine(get_style(d) for d in style_list)

        styles: List[Union[Style, str]] = []
        borders: Dict[int, List[Tuple[int, int]]] = {}
        for idx, span in enumerate(self._spans):
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

    def style_fragments(
        self, text: str, console: Console
    ) -> List[Tuple[str, Optional[Style]]]:
        glyphs = self.glyph_borders(text)
        styles = self.style_borders(console, len(text))
        if self._use_ligartures:
            corrected = {}
            for pos, style in styles:
                if pos in glyphs:
                    corrected[pos] = style
                else:
                    prv, nxt = neighbours(glyphs, pos)
                    if prv is not None and self._style_ligatures == "last":
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

    def resolve_spans(self, spans: List[MutableSpan]) -> List[MutableSpan]:
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

    def _fg_offsets(self, spacing: int, fragment: Glyph, addition: Glyph) -> List[int]:
        return [
            min(
                min(0, spacing + _leading(addition[row])),
                max(spacing, -_trailing(fragment[row])),
            )
            for row in range(len(fragment))
        ]

    def _bg_offsets(self, spacing: int, fragment: Glyph, addition: Glyph) -> List[int]:
        offsets = [0] * self._font.line_height
        for d in range(abs(spacing)):
            majority = sum(
                (1 if fragment[row][-(d + 1)] not in " " else 0)
                - (1 if addition[row][abs(spacing) - (d + 1)] not in " " else 0)
                for row in range(len(fragment))
            )
            if majority > 0:
                break
            else:
                offsets = [-(d + 1)] * self._font.line_height
        return offsets

    def _overlay_styles(self, fg: Optional[Style], bg: Optional[Style]):
        _fg = fg or Style.null()
        _bg = bg or Style.null()
        return Style(
            color=_fg.color,
            blink=_fg.blink,
            bgcolor=_bg.bgcolor,
            underline=_bg.underline,
        )

    def _justify_full(
        self, width: int, line: str, spans: List[Tuple[str, Optional[Style]]]
    ) -> List[Tuple[str, Optional[Style]]]:
        space_width = self._font.space_width
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

    def should_overlap(self, a: Optional[str], b: Optional[str]) -> bool:
        if not a or not b:
            return False
        return (
            self._use_kerning and a not in NON_OVERLAPPING and b not in NON_OVERLAPPING
        )

    def render(
        self,
        console: "Console",
        *,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
    ) -> Iterable["Segment"]:
        wrap_justify = justify or self.justify or DEFAULT_JUSTIFY
        # wrap_overflow = overflow or self.overflow or DEFAULT_OVERFLOW
        line_height = self._font.line_height
        letter_spacing = self._font.letter_spacing
        for line in self._text.splitlines():
            # Align style borders to glyphs
            fragments = self.style_fragments(line, console)
            # Right-strip if appropriate for justify method
            if wrap_justify in ["right", "center", "justify"]:
                line = line.rstrip()
            # Apply justify
            # Note: we do this here, because the length of a rendered space can
            # be other than 1, and indents cannot be expressed in text spaces.
            line_width = self.rendered_width(line)
            if wrap_justify == "right":
                indent = int(console.width - line_width)
            elif wrap_justify == "center":
                indent = int((console.width - line_width) // 2)
            else:
                indent = 0
            # Adjust style borders
            if wrap_justify == "full":
                fragments = self._justify_full(console.width, line, fragments)
            # Prepapre accumulators and apply indents
            row_spans = [[MutableSpan(0, 0, None)] for _ in range(line_height)]
            row_chars = ["" + " " * indent] * line_height
            last_char = ""
            last_style = None
            for fragment_text, fragment_style in fragments:
                if not fragment_text:
                    continue
                if self._use_ligartures:
                    segment_chars = list(self.split_glyphs(fragment_text).values())
                else:
                    segment_chars = list(fragment_text)
                # Render fragment
                fragment = []
                fragment_char = None
                for char in segment_chars:
                    letter = self._font.get(char)
                    if fragment_char is None:
                        fragment = letter
                    else:
                        spacing = letter_spacing + self._adjust_spacing
                        if self.should_overlap(fragment_char, char):
                            spacing -= self.max_overlap(fragment, letter)
                        fragment = self.merge_glyphs(fragment, letter, spacing)
                    fragment_char = char
                fragment_spacing = letter_spacing + self._adjust_spacing
                if self.should_overlap(last_char, fragment_text[0]):
                    fragment_spacing -= self.max_overlap(row_chars, fragment)
                last_char = fragment_char
                # Determine if styles overlap
                split_styles = (
                    has_background(fragment_style) or has_background(last_style)
                ) and fragment_spacing != 0
                # Calculate offsets
                bg_offsets = self._bg_offsets(fragment_spacing, row_chars, fragment)
                fg_offsets = self._fg_offsets(fragment_spacing, row_chars, fragment)
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
                row_chars = self.merge_glyphs(row_chars, fragment, fragment_spacing)
                last_style = fragment_style
            # Truncate
            row_chars = [row[: console.width] for row in row_chars]
            # Right-pad if appropriate for justify method
            if wrap_justify and wrap_justify != "default":
                row_chars = [
                    row + " " * (console.width - len(row)) for row in row_chars
                ]
            # Adjust last style spans
            for row in row_spans:
                row[-1].end = len(row_chars[0])
            # Resolve span overlay
            row_spans = [self.resolve_spans(spans) for spans in row_spans]
            # Render result
            for row_num, (row, spans) in enumerate(zip(row_chars, row_spans)):
                is_underline_row = row_num == self._font.underline
                underline_char = self._font.underline_char
                for span in spans:
                    style: Optional[Style] = span.style
                    fragment = row[span.start : span.end]
                    if style and style.underline is True:
                        if is_underline_row:
                            fragment = fragment.replace(" ", underline_char)
                        style += Style(underline=False)
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
            width=console.width,
            tab_size=tab_size or 8,
            no_wrap=no_wrap,
            overflow=overflow,
        )
        for line in lines:
            yield from line.render(console=console, justify=justify, overflow=overflow)
