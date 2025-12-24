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
    assert_markup(Typography(text, font=OVERLAP, justify="default"), expected)


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
    assert_markup(Typography(text, font=OVERLAP, justify="left"), expected)


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
    assert_markup(Typography(text, font=OVERLAP, justify="right"), expected)


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
    assert_markup(Typography(text, font=OVERLAP, justify="center"), expected)


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
    assert_markup(Typography(text, font=OVERLAP, justify="full"), expected)


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
    assert_markup(result, expected, True)


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
    assert_markup(result, expected, True)


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
