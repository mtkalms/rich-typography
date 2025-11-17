from rich_typography.fonts._font import Font
from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment
from typing import Iterable, List, Tuple, Optional
from rich.console import JustifyMethod
from rich_typography.glyphs import Glyph
import re


def _trailing(line: str):
    return len(line) - len(line.rstrip())


def _leading(line: str):
    return len(line) - len(line.lstrip())


class Typography:
    def __init__(
        self,
        text: str,
        font: Font,
        justify: Optional[JustifyMethod] = None,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
    ):
        self.justify = justify
        self._text = text
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

    def wrap(self, text: str, max_width: int) -> Iterable[Tuple[str, int]]:
        lines = []
        lengths = []
        space_width = self._font.space_width()
        for line in text.splitlines():
            cumm_length = 0
            words = []
            for word in line.split(" "):
                word_length = self.rendered_width(word)
                length = word_length
                if cumm_length > 0:
                    length += space_width
                if cumm_length + length > max_width:
                    lines.append(" ".join(words))
                    lengths.append(cumm_length)
                    words = []
                    cumm_length = 0
                words.append(word)
                if cumm_length > 0:
                    cumm_length += length
                else:
                    cumm_length += word_length
            lines.append(" ".join(words))
            lengths.append(cumm_length)
        return zip(lines, lengths)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        max_ligature = self._font.max_ligature_length()
        for line, length in self.wrap(self._text, console.width):
            if self.justify == "right":
                indent = int(console.width - length)
            elif self.justify == "center":
                indent = int((console.width - length) // 2)
            else:
                indent = 0
            fragments = [" " * indent] * self._font._line_height
            ligature = 0
            for curr_idx, curr in enumerate(line):
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
