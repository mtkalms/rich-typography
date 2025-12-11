import re
from dataclasses import dataclass
from functools import partial
from typing import Dict, Iterable, List, Optional, Tuple, Union

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
from rich_typography.glyphs import Glyph


def _trailing(line: str):
    return len(line) - len(line.rstrip())


def _leading(line: str):
    return len(line) - len(line.lstrip())


@dataclass
class MutableSpan:
    start: int
    end: int
    style: Optional[Style]

    def __repr__(self) -> str:
        return f"<{self.start}, {self.end}>"

    def has_background(self):
        if not self.style or not self.style.bgcolor:
            return False
        return self.style.bgcolor != ColorType.STANDARD


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
        if not self._font.ligatures():
            return dict(enumerate(text))
        ligatures = reversed(sorted(self._font.ligatures(), key=len))
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
        )

    @classmethod
    def from_text(
        cls,
        text: Text,
        font: Font = SEMISERIF,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
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

    def wrap(
        self,
        width: int,
    ) -> Iterable["Typography"]:
        lines = Lines()
        text = self.to_text()
        for line in text.split(allow_blank=True):
            if "\t" in line:
                line.expand_tabs(self.tab_size)
            if self.no_wrap:
                new_lines = [line]
            else:
                offsets, _ = self.divide(str(line), width)
                new_lines = line.divide(offsets)
            for line in new_lines:
                line.rstrip_end(width)
            lines.extend(new_lines)
        return [
            Typography.from_text(
                line,
                self._font,
                self._adjust_spacing,
                self._use_kerning,
                self._use_ligartures,
            )
            for line in lines
        ]

    def divide(self, text: str, width: int) -> Tuple[Iterable[int], Iterable[int]]:
        offsets = []
        lengths = []
        space_length = self._font.space_width()
        offset = 0
        length = 0
        for word in text.split(" "):
            remaining = width - length
            word_length = self.rendered_width(word)
            if word_length >= remaining:
                offsets.append(offset)
                lengths.append(length)
                length = 0
            if length > 0:
                length += space_length
            length += word_length
            if offset > 0:
                offset += 1
            offset += len(word)
        offsets.append(offset)
        lengths.append(length)
        return offsets, lengths

    def flatten_spans(self, console: Console) -> List[MutableSpan]:
        def combine_styles(styles: Iterable[Union[Style, str]]) -> Optional[Style]:
            get_style = partial(console.get_style, default=Style.null())
            style_list = list(styles)
            if not style_list:
                return None
            return Style.combine(get_style(d) for d in style_list)

        spans = []
        styles: List[Union[Style, str]] = []
        for idx, span in enumerate(self._spans):
            spans.append((span.start, 1, idx))
            spans.append((span.end, -1, idx))
            styles.append(span.style)
        stack: List[int] = []
        result: List[MutableSpan] = []
        for pos, direction, idx in sorted(spans):
            if direction > 0:
                stack.append(idx)
            else:
                stack.remove(idx)
            if result and result[-1].start == result[-1].end:
                result[-1].end = pos
            style: Optional[Style] = combine_styles(
                styles[d] for d in stack if styles[d]
            )
            if style:
                result.append(MutableSpan(pos, pos, style))
        return result

    def expand_spans(self, spans: List[MutableSpan], width: int) -> List[MutableSpan]:
        if not spans:
            return [MutableSpan(0, width, None)]
        expanded_spans = []
        if spans[0].start != 0:
            expanded_spans.append(MutableSpan(0, spans[0].start, None))
        for first, second in zip(spans[:-1], spans[1:]):
            expanded_spans.append(first)
            expanded_spans.append(MutableSpan(first.end, second.start, None))
        expanded_spans.append(spans[-1])
        if expanded_spans[-1].end < width:
            expanded_spans.append(MutableSpan(expanded_spans[-1].end, width, None))
        return expanded_spans

    def resolve_spans(self, spans: List[MutableSpan]):
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

    def fg_offsets(self, spacing: int, fragment: Glyph, addition: Glyph) -> List[int]:
        return [
            min(
                min(0, spacing + _leading(addition[row])),
                max(spacing, -(_trailing(fragment[row]))),
            )
            for row in range(len(fragment))
        ]

    def bg_offsets(self, spacing: int, fragment: Glyph, addition: Glyph) -> List[int]:
        offsets = [0] * self._font._line_height
        for d in range(abs(spacing)):
            majority = sum(
                (1 if fragment[row][-(d + 1)] not in " " else 0)
                - (1 if addition[row][abs(spacing) - (d + 1)] not in " " else 0)
                for row in range(len(fragment))
            )
            if majority > 0:
                break
            else:
                offsets = [-(d + 1)] * self._font._line_height
        return offsets

    def overlay_styles(self, fg: Optional[Style], bg: Optional[Style]):
        _fg = fg or Style.null()
        _bg = bg or Style.null()
        return Style(
            color=_fg.color,
            blink=_fg.blink,
            bgcolor=_bg.bgcolor,
            underline=_bg.underline,
        )

    def render(self, console: "Console") -> Iterable["Segment"]:
        line_height = self._font._line_height
        letter_spacing = self._font.letter_spacing
        for line in self._text.splitlines():
            # Apply justification indents
            _width = self.rendered_width(line)
            if self.justify == "right":
                indent = int(console.width - _width)
            elif self.justify == "center":
                indent = int((console.width - _width) // 2)
            else:
                indent = 0
            row_chars = ["" + " " * indent] * line_height
            row_spans = [[MutableSpan(0, 0, None)] for _ in range(line_height)]
            _spans = self.flatten_spans(console)
            _spans = self.expand_spans(_spans, len(line))
            current_span: Optional[MutableSpan] = _spans[0]
            for pos, seg in self.split_glyphs(line).items():
                last_char = line[pos - 1] if pos else " "
                # Get rows
                letter = self._font.get(seg)
                # Calculate offset
                spacing = letter_spacing + self._adjust_spacing
                no_overlaps = ' "'
                if (
                    self._use_kerning
                    and last_char not in no_overlaps
                    and seg not in no_overlaps
                ):
                    spacing -= self.max_overlap(row_chars, letter)
                bg_offsets = self.bg_offsets(spacing, row_chars, letter)
                fg_offsets = self.fg_offsets(spacing, row_chars, letter)
                entering = [
                    span for span in _spans if pos <= span.start < pos + len(seg)
                ]
                entering_span = entering[-1] if entering else None
                split_styles = False
                if current_span:
                    leaving_span = pos <= current_span.end < pos + len(seg)
                    split_styles = (
                        leaving_span
                        and (
                            current_span.has_background()
                            or (entering_span and entering_span.has_background())
                        )
                        and spacing != 0
                    )
                    for d in range(len(row_spans)):
                        row_spans[d][-1].end = len(row_chars[d]) + fg_offsets[d]
                    if split_styles:
                        for d in range(len(row_spans)):
                            row_spans[d][-1].end = len(row_chars[d]) + fg_offsets[d]
                            if fg_offsets[d] > bg_offsets[d]:
                                row_spans[d].append(
                                    MutableSpan(
                                        len(row_chars[d]) + bg_offsets[d],
                                        len(row_chars[d]) + fg_offsets[d],
                                        current_span.style
                                        if not entering_span
                                        else self.overlay_styles(
                                            current_span.style, entering_span.style
                                        ),
                                    )
                                )
                            elif fg_offsets[d] < bg_offsets[d]:
                                row_spans[d].append(
                                    MutableSpan(
                                        len(row_chars[d]) + fg_offsets[d],
                                        len(row_chars[d]) + bg_offsets[d],
                                        current_span.style
                                        if not entering_span
                                        else self.overlay_styles(
                                            entering_span.style, current_span.style
                                        ),
                                    )
                                )

                    if leaving_span:
                        current_span = None
                if entering_span:
                    current_span = entering_span
                    for d in range(len(row_spans)):
                        row_spans[d].append(
                            MutableSpan(
                                len(row_chars[d])
                                + (
                                    max(bg_offsets[d], fg_offsets[d])
                                    if split_styles
                                    else fg_offsets[d]
                                ),
                                len(row_chars[d]) + len(letter[d]),
                                current_span.style,
                            )
                        )
                # Add current letter/ligature to result
                row_chars = self.merge_glyphs(row_chars, letter, spacing)
            if current_span:
                for row in row_spans:
                    row[-1].end = len(row_chars[0])
            row_spans = [self.resolve_spans(spans) for spans in row_spans]

            # Render result
            for row_num, (row, spans) in enumerate(zip(row_chars, row_spans)):
                is_underline_row = row_num == self._font._baseline + 1
                for span in spans:
                    style: Style = span.style
                    fragment = row[span.start : span.end]
                    if style and style.underline is True:
                        if is_underline_row:
                            fragment = "".join("▔" if f in " " else f for f in fragment)
                        style += Style(underline=False)
                    yield (Segment(fragment, style=style))
                yield Segment("\n")

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        lines = self.wrap(console.width)
        for line in lines:
            yield from line.render(console)
