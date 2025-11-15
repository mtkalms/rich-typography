from rich_typography.fonts._font import Font
from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment

from rich_typography.fonts import ILLUMINA, SEMISERIF


class Typography:
    def __init__(
        self,
        text: str,
        font: Font,
        use_kerning: bool = True,
        use_ligatures: bool = True,
    ):
        self._text = text
        self._font = font
        self._use_kerning = use_kerning
        self._use_ligartures = use_ligatures

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        max_ligature = max(len(l) for l in self._font._ligatures)
        for line in self._text.splitlines():
            fragments = [""] * self._font._line_height
            ligature = 0
            for curr_idx, curr in enumerate(line):
                prv = line[curr_idx - 1] if curr_idx > 0 else None
                if ligature > 0:
                    ligature -= 1
                    continue
                for offset in range(max_ligature, 1, -1):
                    substr = line[curr_idx:curr_idx + offset]
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
                if (
                    self._use_kerning
                    and prv != " "
                    and curr != " "
                    and all(fragments)
                    and all(
                        fragments[d][-1] == " " or letter[d][0] == " "
                        for d in range(self._font._line_height)
                    )
                ):
                    # fix char spacing where possible
                    fragments = [
                        r[:-1]
                        + (r[-1] if r[-1] != " " else letter[idx][0])
                        + letter[idx][1:]
                        for idx, r in enumerate(fragments)
                    ]
                else:
                    fragments = [r + letter[idx] for idx, r in enumerate(fragments)]
            for fragment in fragments:
                yield Segment(fragment + "\n")


if __name__ == "__main__":
    console = Console()
    console.print(Typography("textual/rich illumina", ILLUMINA))
    console.print(Typography("textual/rich semiserif", SEMISERIF))
