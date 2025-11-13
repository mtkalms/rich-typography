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
        text = self._text
        result = [""] * self._font._line_height
        ligature = False
        for curr, prv, nxt in zip(text, " " + text[:-1], text[1:] + " "):
            if ligature:
                ligature = False
                continue
            if self._use_ligartures and curr + nxt in self._font:
                ligature = True
                letter = self._font.ligature(curr + nxt)
            else:
                letter = self._font.glyph(curr)
            if (
                self._use_kerning
                and prv != " "
                and curr != " "
                and all(result)
                and all(
                    result[d][-1] == " " or letter[d][0] == " "
                    for d in range(self._font._line_height)
                )
            ):
                # fix char spacing where possible
                result = [
                    r[:-1]
                    + (r[-1] if r[-1] != " " else letter[idx][0])
                    + letter[idx][1:]
                    for idx, r in enumerate(result)
                ]
            else:
                result = [r + letter[idx] for idx, r in enumerate(result)]
        for line in result:
            yield Segment(line + "\n")


if __name__ == "__main__":
    console = Console()
    console.print(Typography("textual/rich illumina", ILLUMINA))
    console.print(Typography("textual/rich semiserif", SEMISERIF))
