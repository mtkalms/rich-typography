import string

from rich_typography.fonts import Font
from rich_typography.glyphs import Glyphs


_upper = Glyphs(
    string.ascii_uppercase,
    "𜸚𜸤 𜸛𜸤 𜸚𜸤 𜸛𜸤 𜸛𜸥 𜸛𜸥 𜸚𜸤 𜸜𜸜 𜸜 𜸞𜸧 𜸜𜸜 𜸜  𜸛𜸠𜸤 𜸛𜸤 𜸚𜸤 𜸛𜸤 𜸚𜸤 𜸛𜸤 𜸚𜸤 𜸞𜸠𜸥 𜸜𜸜 𜸜𜸜 𜸜𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸞𜸤",
    "𜸨𜸶 𜸨𜸷 𜸩𜸼 𜸩𜸩 𜸨  𜸨  𜸩𜸼 𜸨𜸶 𜸩  𜸩 𜸨𜸷 𜸩  𜸩𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸨𜸷 𜸾𜸤  𜸩  𜸩𜸩 𜸩𜸩 𜸩𜸩𜸩 𜸮𜸷 𜸩𜸩 𜸚𜹃",
    "𜸩𜸩 𜸩𜸩 𜸩  𜸩𜸩 𜸩  𜸩  𜸩𜸧 𜸩𜸩 𜸩 𜸜𜸩 𜸩𜸩 𜸩  𜸩𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸨𜹃 𜸩𜸩 𜸩𜸩  𜸩  𜸩  𜸩𜸩 𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩 ",
    "𜸼𜸼 𜸽𜹃 𜸾𜹃 𜸽𜹃 𜸽𜸥 𜸼  𜸾𜹃 𜸼𜸼 𜸼 𜸾𜹃 𜸼𜸼 𜸽𜸥 𜸼𜸼𜸼 𜸼𜸼 𜸾𜹃 𜸼  𜸾𜹅 𜸼𜸼 𜸾𜹃  𜸼  𜸾𜹃 𜸾𜹄 𜸾𜹀𜹃 𜸼𜸼 𜸾𜸶 𜸾𜸥",
    "                                                                          𜸾𜹃   ",
)

_lower = Glyphs(
    string.ascii_lowercase,
    "   𜸜      𜸜    𜸚𜸤    𜸜  𜸣  𜸣 𜸜  𜸜                       𜸜                   ",
    "𜸚𜸤 𜸨𜸤 𜸚𜸤 𜸚𜸶 𜸚𜸤 𜸺  𜸚𜸧 𜸨𜸤 𜸜  𜸜 𜸩𜸜 𜸩 𜸛𜸠𜸤 𜸛𜸤 𜸚𜸤 𜸛𜸤 𜸚𜸤 𜸛𜸤 𜸚𜸤 𜸺 𜸜𜸜 𜸜𜸜 𜸜𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸞𜸤",
    "𜸚𜸶 𜸩𜸩 𜸩  𜸩𜸩 𜸨𜹄 𜸩  𜸩𜸩 𜸩𜸩 𜸩  𜸩 𜸨𜸷 𜸩 𜸩𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩  𜸾𜸤 𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸩𜸩 𜸮𜸷 𜸩𜸩 𜸚𜹃",
    "𜸾𜹃 𜸽𜹃 𜸾𜹃 𜸾𜹄 𜸾𜹃 𜸼  𜸾𜸶 𜸼𜸼 𜸼  𜸩 𜸼𜸼 𜸾 𜸼𜸼𜸼 𜸼𜸼 𜸾𜹃 𜸨𜹃 𜸾𜸶 𜸼  𜸾𜹃 𜸾 𜸾𜹃 𜸾𜹄 𜸾𜹀𜹃 𜸼𜸼 𜸾𜸶 𜸾𜸥",
    "                  𜸾𜹃      𜸾𜹃                𜸼   𜸼                      𜸾𜹃   ",
)

_digits = Glyphs(
    string.digits,
    "𜸚𜸤 𜸜 𜸚𜸤 𜸚𜸤 𜸜𜸜 𜸛𜸥 𜸚𜸥 𜸞𜸧 𜸚𜸤 𜸚𜸤",
    "𜸩𜸩 𜸩 𜸚𜹃  𜸷 𜸾𜸶 𜸽𜸤 𜸨𜸤 𜸚𜹃 𜸮𜸷 𜸾𜸶",
    "𜸩𜸹 𜸩 𜸩  𜸜𜸩  𜸩 𜸜𜸩 𜸩𜸩 𜸩  𜸩𜸩  𜸩",
    "𜸾𜹃 𜸼 𜸽𜸥 𜸾𜹃  𜸼 𜸾𜹃 𜸾𜹃 𜸼  𜸾𜹃 𜸾𜹃",
    "                            ",
)

_punctuation = Glyphs(
    string.punctuation,
    "𜸜 𜸜𜸜    𜸚𜸺𜸤 𜸚𜸤   𜸚𜸤𜸜 𜸜 𜸚 𜸤                    ╱      ╱    ╲  𜸚𜸤 𜸚𜸟𜸤 𜸛𜸥 ╲    𜸞𜸧 ╱╲    ╲ 𜸚𜸥 𜸜 𜸞𜸤    ",
    "𜸩    𜸺𜸺 𜸾𜸺𜸤 𜸾𜹃╱  𜸮𜸟𜸺   𜸩 𜸩 𜸪𜸲𜸸 𜸞𜸺𜸥   𜸞𜸟𜸥     ╱  𜹍   ╱  ══  ╲ 𜸚𜹃 𜸩𜸚𜸶 𜸩   ╲    𜸩         𜸺  𜸩  𜸺 𜸚𜸤 ",
    "𜸩    𜸺𜸺  𜸩𜸩  ╱𜸚𜸤 𜸩 𜸩   𜸩 𜸩                  ╱   𜹍 𜹍 ╲      ╱ 𜸩  𜸩𜸾𜹃 𜸩    ╲   𜸩         𜸩  𜸩  𜸩  𜸾𜹃",
    "𜹍       𜸾𜸺𜹃   𜸾𜹃 𜸾𜹃𜸾   𜸾 𜹃         𜸼     𜹍 ╱      𜸼  ╲    ╱  𜹍  𜸾𜸟𜹃 𜸽𜸥    ╲ 𜸞𜹄    𜸞𜸥   𜸾𜸥 𜸼 𜸞𜹃    ",
    "                                                                                                  ",
)

_ligatures = Glyphs(
    list(
        "re ra ri rj ro ru fb ff fh fi fj fk fl ft ffb fff ffh ffi ffj ffk ffl fft Th Ti Tj".split()
    ),
    "         .  .         𜸚𜸧  𜸚𜸚𜸤 𜸚𜸧  𜸚𜸤 𜸚𜸤 𜸚𜸧  𜸚𜸧 𜸚𜸧 𜸚𜸚𜸧  𜸚𜸚𜸚𜸤 𜸚𜸚𜸧  𜸚𜸚𜸤 𜸚𜸚𜸤 𜸚𜸚𜸧  𜸚𜸚𜸧 𜸚𜸚𜸧 𜸞𜸠𜸧  𜸞𜸠𜸧 𜸞𜸠𜸧",
    "𜸛𜸠𜸤 𜸛𜸤𜸤 𜸛𜸧 𜸛𜸧 𜸛𜸠𜸤 𜸛𜸧𜸜 𜸺𜸨𜸤 𜸺𜸺  𜸺𜸨𜸤 𜸺𜸧 𜸺𜸧 𜸺𜸩𜸜 𜸺𜸩 𜸺𜸺 𜸺𜸺𜸨𜸤 𜸺𜸺𜸺  𜸺𜸺𜸨𜸤 𜸺𜸺𜸧 𜸺𜸺𜸧 𜸺𜸺𜸩𜸜 𜸺𜸺𜸩 𜸺𜸺𜸺  𜸩𜸨𜸤  𜸩𜸜  𜸩𜸜",
    "𜸩𜸨𜹄 𜸩𜸚𜸶 𜸩𜸩 𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩  𜸩𜸩𜸩 𜸩𜸩 𜸩𜸩 𜸩𜸨𜸷 𜸩𜸩 𜸩𜸩 𜸩𜸩𜸩𜸩 𜸩𜸩𜸩  𜸩𜸩𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩𜸩 𜸩𜸩𜸨𜸷 𜸩𜸩𜸩 𜸩𜸩𜸩  𜸩𜸩𜸩  𜸩𜸩  𜸩𜸩",
    "𜸼𜸾𜹃 𜸼𜸾𜹃 𜸼𜸼 𜸼𜸩 𜸼𜸾𜹃 𜸼𜸾𜹃 𜸼𜸽𜹃 𜸼𜸼  𜸼𜸼𜸼 𜸼𜸼 𜸼𜸩 𜸼𜸼𜸼 𜸼𜸾 𜸼𜸾 𜸼𜸼𜸽𜹃 𜸼𜸼𜸼  𜸼𜸼𜸼𜸼 𜸼𜸼𜸼 𜸼𜸼𜸩 𜸼𜸼𜸼𜸼 𜸼𜸼𜸾 𜸼𜸼𜸾  𜸼𜸼𜸼  𜸼𜸼  𜸼𜸩",
    "           𜸾𜹃                        𜸾𜹃                               𜸾𜹃                        𜸾𜹃",
)

CONDENSED_SANS = Font(
    "Condensed Sans",
    _upper | _lower | _digits | _punctuation,
    ligatures=_ligatures,
    baseline=3,
)


if __name__ == "__main__":  # pragma: no cover
    from rich.console import Console
    from rich_typography.typography import Typography

    console = Console()
    console.print(
        Typography(
            CONDENSED_SANS.name,
            font=CONDENSED_SANS,
        )
    )
    console.print(str(_upper))
    console.print(str(_lower))
    console.print(str(_digits))
    console.print(str(_punctuation))
    console.print(str(_ligatures))
