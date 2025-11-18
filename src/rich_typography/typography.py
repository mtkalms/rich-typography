from rich_typography.fonts import Font, SEMISERIF
from rich.console import Console, ConsoleOptions, RenderResult
from rich.containers import Lines
from rich.control import strip_control_codes
from rich.segment import Segment
from rich.style import Style
from rich.text import Span, Text
from typing import Iterable, List, Tuple, Optional, Union
from rich.console import JustifyMethod, OverflowMethod
from rich_typography.glyphs import Glyph
import re


def _trailing(line: str):
    return len(line) - len(line.rstrip())


def _leading(line: str):
    return len(line) - len(line.lstrip())


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

    def split_glyphs(self, text: str) -> List[str]:
        if not self._use_ligartures:
            return list(text)
        glyphs = []
        last = 0
        ligatures = reversed(sorted(self._font.ligatures(), key=len))
        for ligature in re.finditer("|".join(ligatures), text):
            start, end = ligature.span()
            glyphs += list(text[last:start])
            glyphs += [text[start:end]]
            last = end
        glyphs += list(text[last:])
        return glyphs

    def __str__(self) -> str:
        return self._text

    def glyph_width(self, a: str):
        return len(self._font.get(a)[0])

    def rendered_width(self, text) -> int:
        if not text:
            return 0
        glyphs = self.split_glyphs(text)
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
    def from_text(cls, text: Text) -> "Typography":
        return Typography(
            text.plain,
            style=text.style,
            spans=text.spans[:],
            justify=text.justify,
            overflow=text.overflow,
            no_wrap=text.no_wrap,
            end=text.end,
            tab_size=text.tab_size,
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
        return [Typography.from_text(line) for line in lines]

    def divide(self, text: str, width: int) -> Tuple[Iterable[int], Iterable[int]]:
        offsets = []
        lengths = []
        space_length = self._font.space_width()
        offset = 0
        length = 0
        for word in text.split(" "):
            remaining = width - length
            word_length = self.rendered_width(word)
            if word_length > remaining:
                offsets.append(offset)
                lengths.append(length)
                length = 0
            if length > 0:
                length += space_length
            length += word_length
            offset += len(word) + 1
        offsets.append(offset)
        lengths.append(length)
        return offsets, lengths

    def render(self, console: "Console") -> Iterable["Segment"]:
        max_ligature = self._font.max_ligature_length()
        for line in self._text.splitlines():
            length = self.rendered_width(line)
            if self.justify == "right":
                indent = int(console.width - length)
            elif self.justify == "center":
                indent = int((console.width - length) // 2)
            else:
                indent = 0
            fragments = [" " * indent] * self._font._line_height
            ligature = 0
            for curr_idx, curr in enumerate(line):
                # TODO: Apply styles
                prv = line[curr_idx - 1] if curr_idx > 0 else " "
                if ligature > 0:
                    ligature -= 1
                    continue
                for offset in range(max_ligature, 1, -1):
                    substr = line[curr_idx : curr_idx + offset]
                    if self._use_ligartures and substr in self._font._ligatures:
                        ligature = offset - 1
                        letter = self._font.ligature(substr)
                        break
                else:
                    letter = self._font.glyph(curr)
                if all(fragments):
                    spacing = self._font.letter_spacing + self._adjust_spacing
                    if self._use_kerning and prv != " " and curr != " ":
                        spacing -= self.max_overlap(fragments, letter)
                    fragments = self.merge_glyphs(fragments, letter, spacing)
                else:
                    fragments = letter
            for fragment in fragments:
                yield Segment(fragment + "\n")

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        lines = self.wrap(console.width)
        for line in lines:
            yield from line.render(console)
