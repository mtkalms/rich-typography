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


def test_tabs() -> None:
    expected = MarkupResult(
        "╭╮   ╷       ",
        "┼╭╮┌╮┼     ╷╷",
        "││││ │     ││",
        "╵╰╯╵ ╰     ╰┤",
        "          ╰─╯",
    )
    assert_markup(Typography("fort\ty", font=OVERLAP), expected)


def test_overflow_fold() -> None:
    text = "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto"
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷",
        "││││││││││╭┤│├┘╰╮ │││",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵",
        "       ╵             ",
        "╷ .╷                 ",
        "├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮",
        "││││ │ │││││││││├┘ ││",
        "╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵",
        "             ╵       ",
        "             .  ╷    ",
        "╭╮┌┬╮╭╮ ╭╮┌╮┌┐┌╮┼╷╷┌╮",
        "├┘│││││ ││╭┤││╭┤││││ ",
        "╰╴╵╵╵╰╯ ├╯╰┘╵╵╰┘╰╰╯╵ ",
        "        ╵            ",
        "      .      .       ",
        "╷╷╭╮┌╮╷┌╮┌┬╮ ╷╭╮╭┐┌╮ ",
        "││├┘│││╭┤│││ │││╰╮╭┤ ",
        "╰┘╰╴╵╵╵╰┘╵╵╵ ╵├╯└╯╰┘ ",
        "              ╵      ",
        "  .  ╷ .    ╷  ",
        "╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮",
        "╰╮││││ │││╰╮│││",
        "└╯╵╵╵╰ ╵╰╯└╯╰╰╯",
        "               ",
    )
    assert_markup(
        Typography(text, font=OVERLAP, overflow="fold"),
        expected,
        "Overflow fold through Typogrpahy failed.",
        preview=True,
        width=21,
    )


def test_justify_default() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                              .  ╷           .      ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌┐┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮ ",
        "││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤││╭┤││││  ││├┘│││╭┤│││ ",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵ ",
        "       ╵                          ╵               ╵                          ",
        ".         .  ╷ .    ╷         ╷        .              .        ",
        "╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌┐┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐ ",
        "│││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘││╭┤│││ ││││╰╮╰╮││││││╰╮ ",
        "╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯ ",
        " ╵                                ╵           ╵                ",
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
    assert_markup(
        Typography(text, font=OVERLAP, justify="default"),
        expected,
        "Justify default through Typogrpahy failed.",
    )
    assert_markup(
        Typography(text, font=OVERLAP),
        expected,
        "Justify default through console failed.",
        justify="default",
    )


def test_justify_left() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                              .  ╷           .         ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌┐┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮    ",
        "││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤││╭┤││││  ││├┘│││╭┤│││    ",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵    ",
        "       ╵                          ╵               ╵                             ",
        ".         .  ╷ .    ╷         ╷        .              .                         ",
        "╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌┐┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐                  ",
        "│││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘││╭┤│││ ││││╰╮╰╮││││││╰╮                  ",
        "╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯                  ",
        " ╵                                ╵           ╵                                 ",
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
    assert_markup(
        Typography(text, font=OVERLAP, justify="left"),
        expected,
        "Justify left through Typogrpahy failed.",
    )
    assert_markup(
        Typography(text, font=OVERLAP),
        expected,
        "Justify left through console failed.",
        justify="left",
    )


def test_justify_right() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "    ╷╷  ╷    ╷  ╷       .╷ .╷                              .  ╷           .     ",
        "    ││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌┐┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮",
        "    ││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤││╭┤││││  ││├┘│││╭┤│││",
        "    ╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵",
        "           ╵                          ╵               ╵                         ",
        "                  .         .  ╷ .    ╷         ╷        .              .       ",
        "                  ╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌┐┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐",
        "                  │││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘││╭┤│││ ││││╰╮╰╮││││││╰╮",
        "                  ╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯",
        "                   ╵                                ╵           ╵               ",
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
    assert_markup(
        Typography(text, font=OVERLAP, justify="right"),
        expected,
        "Justify right through Typogrpahy failed.",
    )
    assert_markup(
        Typography(text, font=OVERLAP),
        expected,
        "Justify right through console failed.",
        justify="right",
    )


def test_justify_center() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "  ╷╷  ╷    ╷  ╷       .╷ .╷                              .  ╷           .       ",
        "  ││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│ ╭┐╷╷┌┬╮╭╮╷╷╭╮ ┌╮╭╮┌┬╮╭╮ ╭╮┌╮┌┐┌╮┼╷╷┌╮ ╷╷╭╮┌╮╷┌╮┌┬╮  ",
        "  ││││││││││╭┤│├┘╰╮ │││││││ │ │││││││││├┘ ││├┘│││││ ││╭┤││╭┤││││  ││├┘│││╭┤│││  ",
        "  ╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰ ╰╴╰╯╵╵╵╰┤╰╯╰╴ ╵╵╰╴╵╵╵╰╯ ├╯╰┘╵╵╰┘╰╰╯╵  ╰┘╰╴╵╵╵╰┘╵╵╵  ",
        "         ╵                          ╵               ╵                           ",
        "         .         .  ╷ .    ╷         ╷        .              .                ",
        "         ╷╭╮╭┐┌╮ ╭┐╷┌╮┼ ╷╷╷╭┐┼╭╮  ╭┐╭╮╭┤ ┌╮╭╮╭╮┌┐┌╮┌┬╮ ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐         ",
        "         │││╰╮╭┤ ╰╮││││ │││╰╮│││  ╰╮├┘││ ╭┤││├┘││╭┤│││ ││││╰╮╰╮││││││╰╮         ",
        "         ╵├╯└╯╰┘ └╯╵╵╵╰ ╵╰╯└╯╰╰╯│ └╯╰╴╰┘ ╰┘├╯╰╴╵╵╰┘╵╵╵ ├╯╰╯└╯└╯╵╵╵╵╰╯└╯         ",
        "          ╵                                ╵           ╵                        ",
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
    assert_markup(
        Typography(text, font=OVERLAP, justify="center"),
        expected,
        "Justify center through Typography failed.",
    )
    assert_markup(
        Typography(text, font=OVERLAP),
        expected,
        "Justify center through console failed.",
        justify="center",
    )


def test_justify_full() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "sed aperiam possimus consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                                 .  ╷            .     ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│  ╭┐╷╷┌┬╮╭╮╷╷╭╮  ┌╮╭╮┌┬╮╭╮  ╭╮┌╮┌┐┌╮┼╷╷┌╮  ╷╷╭╮┌╮╷┌╮┌┬╮",
        "││││││││││╭┤│├┘╰╮ │││││││  │ │││││││││├┘  ││├┘│││││  ││╭┤││╭┤││││   ││├┘│││╭┤│││",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰  ╰╴╰╯╵╵╵╰┤╰╯╰╴  ╵╵╰╴╵╵╵╰╯  ├╯╰┘╵╵╰┘╰╰╯╵   ╰┘╰╴╵╵╵╰┘╵╵╵",
        "       ╵                           ╵                 ╵                          ",
        ".            .  ╷    .    ╷             ╷            .                  .       ",
        "╷╭╮╭┐┌╮    ╭┐╷┌╮┼    ╷╷╷╭┐┼╭╮      ╭┐╭╮╭┤     ┌╮╭╮╭╮┌┐┌╮┌┬╮     ╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐",
        "│││╰╮╭┤    ╰╮││││    │││╰╮│││      ╰╮├┘││     ╭┤││├┘││╭┤│││     ││││╰╮╰╮││││││╰╮",
        "╵├╯└╯╰┘    └╯╵╵╵╰    ╵╰╯└╯╰╰╯│     └╯╰╴╰┘     ╰┘├╯╰╴╵╵╰┘╵╵╵     ├╯╰╯└╯└╯╵╵╵╵╰╯└╯",
        " ╵                                              ╵               ╵               ",
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
    assert_markup(
        Typography(text, font=OVERLAP, justify="full"),
        expected,
        "Justify full through Typogrpahy failed.",
    )
    assert_markup(
        Typography(text, font=OVERLAP),
        expected,
        "Justify full through console failed.",
        justify="full",
    )


def test_justify_full_with_styles() -> None:
    text = (
        "Voluptates nihil cumque nemo pariatur veniam ipsa sint iusto, "
        + "[red]sed[/red] [on blue]aperiam [/on blue][green]possimus[/green] consequuntur delectus adipisci natus sit placeat mollitia."
    )
    expected = MarkupResult(
        "╷╷  ╷    ╷  ╷       .╷ .╷                                 .  ╷            .     ",
        "││╭╮│╷╷╭╮┼┌╮┼╭╮╭┐ ┌╮╷├╮╷│  ╭┐╷╷┌┬╮╭╮╷╷╭╮  ┌╮╭╮┌┬╮╭╮  ╭╮┌╮┌┐┌╮┼╷╷┌╮  ╷╷╭╮┌╮╷┌╮┌┬╮",
        "││││││││││╭┤│├┘╰╮ │││││││  │ │││││││││├┘  ││├┘│││││  ││╭┤││╭┤││││   ││├┘│││╭┤│││",
        "╰┘╰╯╰╰╯├╯╰╰┘╰╰╴└╯ ╵╵╵╵╵╵╰  ╰╴╰╯╵╵╵╰┤╰╯╰╴  ╵╵╰╴╵╵╵╰╯  ├╯╰┘╵╵╰┘╰╰╯╵   ╰┘╰╴╵╵╵╰┘╵╵╵",
        "       ╵                           ╵                 ╵                          ",
        ".            .  ╷    .    ╷        [red]     ╷[/red]     [on blue]       .          [/on blue][green]        .       [/green]",
        "╷╭╮╭┐┌╮    ╭┐╷┌╮┼    ╷╷╷╭┐┼╭╮      [red]╭┐╭╮╭┤[/red]     [on blue]┌╮╭╮╭╮┌┐┌╮┌┬╮     [/on blue][green]╭╮╭╮╭┐╭┐╷┌┬╮╷╷╭┐[/green]",
        "│││╰╮╭┤    ╰╮││││    │││╰╮│││      [red]╰╮├┘││[/red]     [on blue]╭┤││├┘││╭┤│││     [/on blue][green]││││╰╮╰╮││││││╰╮[/green]",
        "╵├╯└╯╰┘    └╯╵╵╵╰    ╵╰╯└╯╰╰╯│     [red]└╯╰╴╰┘[/red]     [on blue]╰┘├╯╰╴╵╵╰┘╵╵╵     [/on blue][green]├╯╰╯└╯└╯╵╵╵╵╰╯└╯[/green]",
        " ╵                                 [red]      [/red]     [on blue]  ╵               [/on blue][green]╵               [/green]",
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
    assert_markup(
        Typography.from_text(Text.from_markup(text, justify="full"), font=OVERLAP),
        expected,
        "Justify full through Text failed.",
    )
    assert_markup(
        Typography.from_text(Text.from_markup(text), font=OVERLAP),
        expected,
        "Justify full through console failed.",
        justify="full",
    )


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


def test_mask_styles() -> None:
    markup = "[red]i[/red][blue]i[/blue][green]g[/green]"
    expected = MarkupResult(
        "[red].[/red][blue].[/blue][green]  [/green]",
        "[red]╷[/red][blue]╷[/blue][green]╭┐[/green]",
        "[red]│[/red][blue]│[/blue][green]││[/green]",
        "[red]╵[/red][blue]╵[/blue][green]╰┤[/green]",
        "[green]╰──╯[/green]",
    )
    result = Typography.from_text(Text.from_markup(markup), font=OVERLAP)
    assert_markup(result, expected)


def test_underline_style() -> None:
    markup = "m[underline]ini cigar[/underline]s"
    expected = MarkupResult(
        "   .  .   .        ",
        "┌┬╮╷┌╮╷ ╭┐╷╭┐┌╮┌╮╭┐",
        "│││││││ │ │││╭┤│ ╰╮",
        "╵╵╵╵╵╵╵ ╰╴╵╰┤╰┘╵ └╯",
        "   ▔▔▔▔▔▔╰──╯▔▔▔▔  ",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, use_ligatures=False
    )
    assert_markup(result, expected)


def test_underline_ligatures_style() -> None:
    markup = "f[underline]ini figar[/underline]o"
    expected = MarkupResult(
        "╭╮  . ╭╮       ",
        "┼┐┌╮╷ ┼┐╭┐┌╮┌┬╮",
        "│││││ ││││╭┤│││",
        "╵╵╵╵╵ ╵╵╰┤╰┘╵╰╯",
        "  ▔▔▔▔╰──╯▔▔▔▔▔",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, use_ligatures=True
    )
    assert_markup(result, expected)


def test_ligatures_enabled() -> None:
    markup = "fira"
    expected = MarkupResult(
        "╭╮   ",
        "┼┐┌╮╮",
        "│││╭┤",
        "╵╵╵╰┘",
        "     ",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, use_ligatures=True
    )
    assert_markup(result, expected)


def test_ligatures_disabled() -> None:
    markup = "fira"
    expected = MarkupResult(
        "╭╮.    ",
        "┼ ╷┌╮┌╮",
        "│ ││ ╭┤",
        "╵ ╵╵ ╰┘",
        "       ",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, use_ligatures=False
    )
    assert_markup(result, expected)


def test_ligature_style_first() -> None:
    markup = "[red]f[/red][blue]ir[/blue][green]a[/green]"
    expected = MarkupResult(
        "[red]╭╮[/red][blue]   [/blue]",
        "[red]┼┐[/red][blue]┌╮╮[/blue]",
        "[red]││[/red][blue]│╭┤[/blue]",
        "[red]╵╵[/red][blue]╵╰┘[/blue]",
        "[red]  [/red][blue]   [/blue]",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, style_ligatures="first"
    )
    assert_markup(result, expected)


def test_ligature_style_last() -> None:
    markup = "[red]f[/red][blue]ir[/blue][green]a[/green]"
    expected = MarkupResult(
        "[blue]╭╮[/blue][green]   [/green]",
        "[blue]┼┐[/blue][green]┌╮╮[/green]",
        "[blue]││[/blue][green]│╭┤[/green]",
        "[blue]╵╵[/blue][green]╵╰┘[/green]",
        "[blue]  [/blue][green]   [/green]",
    )
    result = Typography.from_text(
        Text.from_markup(markup), font=OVERLAP, style_ligatures="last"
    )
    assert_markup(result, expected)
