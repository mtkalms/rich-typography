from rich.text import Text

from rich_typography.typography import Typography

from tests.utilities.asserts import assert_markup
from tests.utilities.fonts import OVERLAP
from tests.utilities.markup import MarkupResult


def test_overlap() -> None:
    expected = MarkupResult(
        "╭╮   ╷  ",
        "┼╭╮┌╮┼╷╷",
        "││││ │││",
        "╵╰╯╵ ╰╰┤",
        "     ╰─╯",
    )
    assert_markup(Typography("forty", font=OVERLAP), expected)


def test_space_overlap() -> None:
    expected = MarkupResult(
        "╭╮   ╷    ",
        "┼╭╮┌╮┼  ╷╷",
        "││││ │  ││",
        "╵╰╯╵ ╰  ╰┤",
        "       ╰─╯",
    )
    assert_markup(Typography("fort y", font=OVERLAP), expected)


def test_justify_default() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                               .  ╷           .      ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌╮╷┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮ ",
        "││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤│ │╭┤││││  ││├┘│││╭┤│││ ",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵ ╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵ ",
        "       ╵                          ╵               ╵                           ",
        ".         .  ╷ .    ╷         ╷         .              .        ",
        "╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌╮╷┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐ ",
        "│││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘│ │╭┤│││ ││││╰╮╰╮││││││╰╮ ",
        "╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵ ╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯ ",
        " ╵                                ╵            ╵                ",
        "                  ╷      ╷  ╷    ╷        ╷.  .    .     ╷       .╷   ╷        ╷",
        "╭┐╭╮┌╮╭┐╭╮╭╮╷╷╷╷┌╮┼╷╷┌╮ ╭┤╭╮│╭╮╭┐┼╷╷╭┐ ┌╮╭┤╷╭╮╷╭┐╭┐╷ ┌╮┌╮┼╷╷╭┐ ╭┐╷┼ ╭╮│┌╮╭┐╭╮┌╮┼",
        "│ ││││╰╮├┘││││││││││││  ││├┘│├┘│ │││╰╮ ╭┤││││││╰╮│ │ ││╭┤│││╰╮ ╰╮││ │││╭┤│ ├┘╭┤│",
        "╰╴╰╯╵╵└╯╰╴╰┤╰╯╰╯╵╵╰╰╯╵  ╰┘╰╴╰╰╴╰╴╰╰╯└╯ ╰┘╰┘╵├╯╵└╯╰╴╵ ╵╵╰┘╰╰╯└╯ └╯╵╰ ├╯╰╰┘╰╴╰╴╰┘╰",
        "           ╵                                ╵                       ╵           ",
        "     ╷╷.╷.   ",
        "┌┬╮╭╮││╷┼╷┌╮ ",
        "││││││││││╭┤ ",
        "╵╵╵╰╯╰╰╵╰╵╰┘·",
        "             ",
    )
    assert_markup(Typography(text, font=OVERLAP, justify="default"), expected)


def test_justify_left() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                               .  ╷           .        ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌╮╷┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮   ",
        "││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤│ │╭┤││││  ││├┘│││╭┤│││   ",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵ ╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵   ",
        "       ╵                          ╵               ╵                             ",
        ".         .  ╷ .    ╷         ╷         .              .                        ",
        "╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌╮╷┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐                 ",
        "│││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘│ │╭┤│││ ││││╰╮╰╮││││││╰╮                 ",
        "╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵ ╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯                 ",
        " ╵                                ╵            ╵                                ",
        "                  ╷      ╷  ╷    ╷        ╷.  .    .     ╷       .╷   ╷        ╷",
        "╭┐╭╮┌╮╭┐╭╮╭╮╷╷╷╷┌╮┼╷╷┌╮ ╭┤╭╮│╭╮╭┐┼╷╷╭┐ ┌╮╭┤╷╭╮╷╭┐╭┐╷ ┌╮┌╮┼╷╷╭┐ ╭┐╷┼ ╭╮│┌╮╭┐╭╮┌╮┼",
        "│ ││││╰╮├┘││││││││││││  ││├┘│├┘│ │││╰╮ ╭┤││││││╰╮│ │ ││╭┤│││╰╮ ╰╮││ │││╭┤│ ├┘╭┤│",
        "╰╴╰╯╵╵└╯╰╴╰┤╰╯╰╯╵╵╰╰╯╵  ╰┘╰╴╰╰╴╰╴╰╰╯└╯ ╰┘╰┘╵├╯╵└╯╰╴╵ ╵╵╰┘╰╰╯└╯ └╯╵╰ ├╯╰╰┘╰╴╰╴╰┘╰",
        "           ╵                                ╵                       ╵           ",
        "     ╷╷.╷.                                                                      ",
        "┌┬╮╭╮││╷┼╷┌╮                                                                    ",
        "││││││││││╭┤                                                                    ",
        "╵╵╵╰╯╰╰╵╰╵╰┘·                                                                   ",
        "                                                                                ",
    )
    assert_markup(Typography(text, font=OVERLAP, justify="left"), expected)


def test_justify_right() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "   ╷╷  ╷    ╷  ╷       .╷ .╷                               .  ╷           .     ",
        "   ││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌╮╷┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮",
        "   ││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤│ │╭┤││││  ││├┘│││╭┤│││",
        "   ╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵ ╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵",
        "          ╵                          ╵               ╵                          ",
        "                 .         .  ╷ .    ╷         ╷         .              .       ",
        "                 ╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌╮╷┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐",
        "                 │││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘│ │╭┤│││ ││││╰╮╰╮││││││╰╮",
        "                 ╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵ ╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯",
        "                  ╵                                ╵            ╵               ",
        "                  ╷      ╷  ╷    ╷        ╷.  .    .     ╷       .╷   ╷        ╷",
        "╭┐╭╮┌╮╭┐╭╮╭╮╷╷╷╷┌╮┼╷╷┌╮ ╭┤╭╮│╭╮╭┐┼╷╷╭┐ ┌╮╭┤╷╭╮╷╭┐╭┐╷ ┌╮┌╮┼╷╷╭┐ ╭┐╷┼ ╭╮│┌╮╭┐╭╮┌╮┼",
        "│ ││││╰╮├┘││││││││││││  ││├┘│├┘│ │││╰╮ ╭┤││││││╰╮│ │ ││╭┤│││╰╮ ╰╮││ │││╭┤│ ├┘╭┤│",
        "╰╴╰╯╵╵└╯╰╴╰┤╰╯╰╯╵╵╰╰╯╵  ╰┘╰╴╰╰╴╰╴╰╰╯└╯ ╰┘╰┘╵├╯╵└╯╰╴╵ ╵╵╰┘╰╰╯└╯ └╯╵╰ ├╯╰╰┘╰╴╰╴╰┘╰",
        "           ╵                                ╵                       ╵           ",
        "                                                                        ╷╷.╷.   ",
        "                                                                   ┌┬╮╭╮││╷┼╷┌╮ ",
        "                                                                   ││││││││││╭┤ ",
        "                                                                   ╵╵╵╰╯╰╰╵╰╵╰┘·",
        "                                                                                ",
    )
    assert_markup(Typography(text, font=OVERLAP, justify="right"), expected)


def test_justify_center() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        " ╷╷  ╷    ╷  ╷       .╷ .╷                               .  ╷           .       ",
        " ││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌╮╷┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮  ",
        " ││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤│ │╭┤││││  ││├┘│││╭┤│││  ",
        " ╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵ ╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵  ",
        "        ╵                          ╵               ╵                            ",
        "        .         .  ╷ .    ╷         ╷         .              .                ",
        "        ╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌╮╷┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐         ",
        "        │││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘│ │╭┤│││ ││││╰╮╰╮││││││╰╮         ",
        "        ╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵ ╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯         ",
        "         ╵                                ╵            ╵                        ",
        "                  ╷      ╷  ╷    ╷        ╷.  .    .     ╷       .╷   ╷        ╷",
        "╭┐╭╮┌╮╭┐╭╮╭╮╷╷╷╷┌╮┼╷╷┌╮ ╭┤╭╮│╭╮╭┐┼╷╷╭┐ ┌╮╭┤╷╭╮╷╭┐╭┐╷ ┌╮┌╮┼╷╷╭┐ ╭┐╷┼ ╭╮│┌╮╭┐╭╮┌╮┼",
        "│ ││││╰╮├┘││││││││││││  ││├┘│├┘│ │││╰╮ ╭┤││││││╰╮│ │ ││╭┤│││╰╮ ╰╮││ │││╭┤│ ├┘╭┤│",
        "╰╴╰╯╵╵└╯╰╴╰┤╰╯╰╯╵╵╰╰╯╵  ╰┘╰╴╰╰╴╰╴╰╰╯└╯ ╰┘╰┘╵├╯╵└╯╰╴╵ ╵╵╰┘╰╰╯└╯ └╯╵╰ ├╯╰╰┘╰╴╰╴╰┘╰",
        "           ╵                                ╵                       ╵           ",
        "                                      ╷╷.╷.                                     ",
        "                                 ┌┬╮╭╮││╷┼╷┌╮                                   ",
        "                                 ││││││││││╭┤                                   ",
        "                                 ╵╵╵╰╯╰╰╵╰╵╰┘·                                  ",
        "                                                                                ",
    )
    assert_markup(Typography(text, font=OVERLAP, justify="center"), expected)


def test_justify_full() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                                 .  ╷            .     ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮  ┌╮╭╮┌┬╮╭╮  ╭╮┌╮┌╮╷┌╮┼╷╷┌╮  ╷╷╭╮┌╮╷┌╮┌┬╮",
        "││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘  ││├┘│││││  ││╭┤│ │╭┤││││   ││├┘│││╭┤│││",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴  ╵╵╰╴╵╵╵╰╯  ├╯╰┘╵ ╵╰┘╰╰╯╵   ╰┘╰╴╵╵╵╰┘╵╵╵",
        "       ╵                          ╵                 ╵                           ",
        ".            .  ╷    .    ╷            ╷             .                  .       ",
        "╷╭╮╭┐┌╮    ╭┐╷┌╮┼    ╷╷╷╭┐┼╭╮     ╭┐╭╮╭┤     ┌╮╭╮╭╮┌╮╷┌╮┌┬╮     ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐",
        "│││╰╮╭┤    ╰╮││││    │││╰╮│││     ╰╮├┘││     ╭┤││├┘│ │╭┤│││     ││││╰╮╰╮││││││╰╮",
        "╵├╯└╯╰┘    └╯╵╵╵╰    ╵╰╯└╯╰╰╯│    └╯╰╴╰┘     ╰┘├╯╰╴╵ ╵╰┘╵╵╵     ├╯╰╯└╯└╯╵╵╵╵╰╯└╯",
        " ╵                                             ╵                ╵               ",
        "                  ╷      ╷  ╷    ╷        ╷.  .    .     ╷       .╷   ╷        ╷",
        "╭┐╭╮┌╮╭┐╭╮╭╮╷╷╷╷┌╮┼╷╷┌╮ ╭┤╭╮│╭╮╭┐┼╷╷╭┐ ┌╮╭┤╷╭╮╷╭┐╭┐╷ ┌╮┌╮┼╷╷╭┐ ╭┐╷┼ ╭╮│┌╮╭┐╭╮┌╮┼",
        "│ ││││╰╮├┘││││││││││││  ││├┘│├┘│ │││╰╮ ╭┤││││││╰╮│ │ ││╭┤│││╰╮ ╰╮││ │││╭┤│ ├┘╭┤│",
        "╰╴╰╯╵╵└╯╰╴╰┤╰╯╰╯╵╵╰╰╯╵  ╰┘╰╴╰╰╴╰╴╰╰╯└╯ ╰┘╰┘╵├╯╵└╯╰╴╵ ╵╵╰┘╰╰╯└╯ └╯╵╰ ├╯╰╰┘╰╴╰╴╰┘╰",
        "           ╵                                ╵                       ╵           ",
        "     ╷╷.╷.                                                                      ",
        "┌┬╮╭╮││╷┼╷┌╮                                                                    ",
        "││││││││││╭┤                                                                    ",
        "╵╵╵╰╯╰╰╵╰╵╰┘·                                                                   ",
        "                                                                                ",
    )
    assert_markup(Typography(text, font=OVERLAP, justify="full"), expected)


def test_overlap_styles() -> None:
    markup = "[red on blue]f[/red on blue][purple on green]ort[/purple on green][red on blue]y[/red on blue]"
    expected = MarkupResult(
        "[red on blue]╭[/red on blue][red on green]╮[/red on green][purple on green]   ╷[/purple on green][red on blue]  [/red on blue]",
        "[red on blue]┼[/red on blue][purple on green]╭╮┌╮┼[/purple on green][red on blue]╷╷[/red on blue]",
        "[red on blue]│[/red on blue][purple on green]│││ │[/purple on green][red on blue]││[/red on blue]",
        "[red on blue]╵[/red on blue][purple on green]╰╯╵ ╰[/purple on green][red on blue]╰┤[/red on blue]",
        "[red on blue] [/red on blue][purple on green]    [/purple on green][red on green]╰[/red on green][red on blue]─╯[/red on blue]",
    )
    result = Typography.from_text(Text.from_markup(markup), font=OVERLAP)
    assert_markup(result, expected)
