from rich_typography.fonts._font import Font
from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment

from rich_typography.fonts import ILLUMINA, SEMISERIF
from rich_typography.glyphs import Glyph


def len_trailing(line: str):
    return len(line) - len(line.rstrip())


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
        self._spacing = adjust_spacing
        self._use_kerning = use_kerning
        self._use_ligartures = use_ligatures

    @classmethod
    def max_overlap(cls, a: Glyph, b: Glyph) -> int:
        return min(len_trailing(la) + len_trailing(lb) for la, lb in zip(a, b))

    @classmethod
    def merge_glyphs(cls, a: Glyph, b: Glyph, overlap: int) -> Glyph:
        return [
            la[:-overlap]
            + "".join(
                rlb if rlb != " " else rla
                for rla, rlb in zip(la[-overlap:], lb[:overlap])
            )
            + lb[overlap:]
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
                spacing = self.max_overlap(fragments, letter) - self._spacing
                if (
                    self._use_kerning
                    and prv != " "
                    and curr != " "
                    and all(fragments)
                    and spacing > 0
                ):
                    # fix char spacing where possible
                    fragments = self.merge_glyphs(fragments, letter, spacing)
                else:
                    fragments = [r + letter[idx] for idx, r in enumerate(fragments)]
            for fragment in fragments:
                yield Segment(fragment + "\n")


if __name__ == "__main__":
    console = Console()
    console.print(Typography("textual/rich illumina", ILLUMINA))
    console.print(Typography("textual/rich semiserif", SEMISERIF))
