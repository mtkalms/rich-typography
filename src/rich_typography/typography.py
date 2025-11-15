from rich_typography.fonts._font import Font
from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment

from rich_typography.fonts import ILLUMINA, SEMISERIF
from rich_typography.glyphs import Glyph


def _trailing(line: str):
    return len(line) - len(line.rstrip())


def _leading(line: str):
    return len(line) - len(line.lstrip())


class Typography:
    def __init__(
        self,
        text: str,
        font: Font,
        adjust_spacing: int = 0,
        use_kerning: bool = True,
        use_ligatures: bool = True,
    ):
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

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        max_ligature = self._font.max_ligature_length()
        for line in self._text.splitlines():
            fragments = [""] * self._font._line_height
            ligature = 0
            for curr_idx, curr in enumerate(line):
                prv = line[curr_idx - 1] if curr_idx > 0 else None
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
                if len(fragments[0]) + len(letter[0]) > console.width:
                    for fragment in fragments:
                        yield Segment(fragment + "\n")
                    fragments = [""] * self._font._line_height
                if all(fragments):
                    spacing = self._font.letter_spacing + self._adjust_spacing
                    if self._use_kerning and prv != " " and curr != " ":
                        spacing -= self.max_overlap(fragments, letter)
                    fragments = self.merge_glyphs(fragments, letter, spacing)
                else:
                    fragments = letter
            for fragment in fragments:
                yield Segment(fragment + "\n")


if __name__ == "__main__":
    console = Console()

    console.print(Typography("textual/rich illumina", ILLUMINA))
    console.print(Typography("textual/rich semiserif", SEMISERIF))
