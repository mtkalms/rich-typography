import string

from rich_typography.fonts import Font
from rich_typography.glyphs import Glyphs

LOWER = Glyphs(
    """
   ┐      ┐    ╭╮    ┐  .  . ┐  ┐                       ╷                   
┌╮ ├╮ ╭┐ ╭┤ ╭╮ ┼  ╭┬ ├╮ ┐  ┐ │╷ │ ┬┬╮ ┬╮ ╭╮ ┬╮ ┬╮ ┬╮ ╭┐ ┼ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
╭┤ ││ │  ││ ├┘ │  ││ ││ │  │ ├╮ │ │││ ││ ││ ││ ││ │  ╰╮ │ ││ ││ │││ ╭╯ ││ ╭╯
╰┘ └╯ ╰╴ ╰┘ ╰╴ ╵  ╰┤ ╵╵ ╵  │ ╵╵ ╰ ╵╵╵ ╵╵ ╰╯ ├╯ ╰┤ ╵  └╯ ╰ ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                  └╯      └╯                ╵   ╵                      └╯   
""",
    string.ascii_lowercase,
)

UPPER = Glyphs(
    """
┬╮ ┬╮ ╭╮ ┬╮ ┬╴ ┬╴ ╭╮ ┐╷ ┐  ┐ ┐╷ ┐  ┬┬╮ ┬╮ ╭╮ ┬╮ ╭╮  ┬╮ ╭┐ ┌┬┐ ┐╷ ┐╷ ┐╷╷ ┐╷ ┐╷ ┌╮
├┤ ├┤ │╵ ││ ├  ├  │╵ ├┤ │  │ ├╯ │  │││ ││ ││ ││ ││  ├╯ ╰╮  │  ││ ││ │││ ╭╯ ││ ╭╯
││ ││ │  ││ │  │  │┐ ││ │ ╷│ ││ │  │││ ││ ││ ├╯ ││  ││  │  │  ││ ││ │││ ││ ││ │ 
╵╵ └╯ ╰╯ └╯ └╴ ╵  ╰╯ ╵╵ ╵ ╰╯ ╵╵ └┘ ╵╵╵ ╵╵ ╰╯ ╵  ╰┤  ╵╵ └╯  ╵  ╰╯ ╰┘ ╰┴╯ ╵╵ ╰┤ ╰┘
                                                 ╰╯                        └╯   
""",
    string.ascii_uppercase,
)

DIGITS = Glyphs(
    """
╭╮ ┐ ╭╮ ╭╮ ╷╷ ┌╴ ╭╴ ┌┐ ╭╮ ╭╮
││ │ ╭╯  ┤ ╰┼ └╮ ├╮ ╭╯ ╭╯ ╰┤
││ │ │  ╷│  │ ╷│ ││ │  ││  │
╰╯ ╵ └┘ ╰╯  ╵ ╰╯ ╰╯ ╵  ╰╯ ╰╯
                            
""",
    string.digits,
)

PUNCTUATION = Glyphs(
    """
╷ ╷╷    ╭┼╮ ◯  ╱ ╭╮╷ ╷ ╭ ╮                   ╱      ╱    ╲  ╭╮     ┌╴ ╲    ╶┐ ╱╲    ╲ ╭╴ ╷ ╶╮    
│    ┼┼ ╰┼╮   ╱  ├─┼   │ │                  ╱  ·   ╱  ╶╴  ╲ ╭╯ ╭─╮ │   ╲    │         ┼  │  ┼ ╭╮ 
│    ┼┼   │  ╱   │ │   │ │ ╶╳╴ ╶┼╴   ╶╴    ╱   · · ╲  ╶╴  ╱ │  │╭┤ │    ╲   │         │  │  │  ╰╯
·       └┼╯ ╱  ◯ ╰╯╰   ╰ ╯         │    · ╱      │  ╲    ╱  ·  │╰╯ └╴    ╲ ╶┙    ╶╴   ╰╴ ╵ ╶╯    
                                                               ╰─╯                               
""",
    string.punctuation,
)

LIGATURES = Glyphs(
    """
         .         ╭╮ ╭╭╮ ╭╷ ╭╭╮
┬┬╮ ┬╮╮ ┬┐ ┬┬╮ ┬┐╷ ┼┐ ┼┼  ┼┼ ┼┼┐
│├┘ │╭┤ ││ │││ │││ ││ ││  ││ │││
╵╰╴ ╵╰┘ ╵╵ ╵╰╯ ╵╰╯ ╵╵ ╵╵  ╵╰ ╵╵╵
                                
""",
    ["re", "ra", "ri", "ro", "ru", "fi", "ff", "ft", "ffi"],
)

SEMISERIF = Font(
    "Semi Serif", UPPER | LOWER | DIGITS | PUNCTUATION, LIGATURES, baseline=3
)


if __name__ == "__main__":
    from rich.console import Console
    from rich.text import Text

    from rich_typography.typography import Typography

    lorem_markup = """[red]Lorem ipsum[/red] dolor sit amet, consectetur adipiscing elit. Nam sed arcu id quam venenatis cursus et vitae quam. Sed non diam ut leo efficitur semper sit amet eget dui. Etiam venenatis nisi ex, vitae egestas velit porta sit amet. Morbi posuere id urna in feugiat. [red]Pr[/red][green]aesent[/green] tristique tellus mauris, vitae sodales lacus pretium eu. Nulla sagittis, [on green]ipsum rhoncus varius[/on green] sollicitudin, dui mi facilisis dui, quis volutpat neque ante nec lectus. Nam sagittis, enim at bibendum fringilla, justo sapien tempor nibh, eget gravida felis quam at urna. Donec convallis accumsan tellus, vitae dictum ligula vulputate et. Vestibulum faucibus sem mauris, ac semper mi congue vitae. Proin dapibus vel ligula et finibus. Sed at rhoncus nunc, eu mollis arcu.
Suspendisse consequat, nisl sed finibus varius, libero libero [on red]f[/on red][on green]eugiat nibh[/on green], a blandit ipsum ipsum ut ante. Curabitur malesuada posuere elit, porta volutpat sapien pretium ut. Quisque neque erat, viverra sit amet lacinia ac, aliquet aliquam urna. Phasellus egestas nibh eu semper lobortis. Sed risus metus, ullamcorper vitae fringilla quis, tempor eu metus. Donec ultrices commodo nisi, eu sollicitudin nisl malesuada sed. Ut scelerisque nec odio eget ullamcorper. Cras a laoreet mi. Vestibulum a volutpat lacus. Mauris consequat lacinia luctus. Aliquam et erat non ligula varius dignissim. Mauris pellentesque, odio et molestie tempor, dolor nibh pretium dui, viverra feugiat orci massa vel felis. Pellentesque vehicula, neque at molestie maximus, ante lacus dignissim mauris, eget tempor enim leo nec tortor.
Donec maximus velit diam. Vestibulum ac nulla vitae justo laoreet [underline]consequat facilisis[/underline] et ligula. Phasellus vestibulum magna id velit luctus, et consectetur ante venenatis. Nam sed arcu sed ipsum fringilla laoreet ac ornare metus. Maecenas rhoncus justo consequat pellentesque hendrerit. Pellentesque bibendum neque ullamcorper, ornare velit eget, mollis velit. Aenean id erat eu erat sagittis tristique.
Vestibulum gravida euismod viverra. [bold]Pellentesque[/bold] habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin at metus eget turpis suscipit semper eget ut dui. Cras volutpat diam ut dui posuere, at malesuada quam congue. Ut scelerisque pharetra ipsum, eget convallis dolor accumsan quis. Integer vitae nibh erat. Curabitur eget sagittis eros. Nulla congue luctus magna v[blue]itae ef[/blue]f[red]ici[/red]tur. Praesent sit amet leo tellus. Nam nisl enim, rutrum vel porta dapibus, pharetra eget odio.
Suspendisse vel blandit enim. Sed id [red]f[/red][blue]elis sed[/blue] [blue on yellow]sapien mattis feugiat aliquam[/] imperdiet quam. Praesent congue nibh id laoreet accumsan. Vivamus tincidunt turpis sit amet leo varius, vitae convallis dolor dictum. Fusce posuere eget nisl et lacinia. Suspendisse est sem, venenatis eget lacus a, laoreet accumsan [on red]er[/on red][on blue]at. [/on blue]Vivamus vehicula nulla a tellus rhoncus dictum. Nulla eget fringilla justo, vitae vehicula nulla. Donec urna risus, aliquam non sapien vitae, pretium venenatis lacus.
"""

    console = Console()
    markup = Text.from_markup(lorem_markup)
    text = Text(markup.plain, spans=markup.spans, justify="right")
    typography = Typography.from_text(text)
    console.print(text, justify="right")
    console.print(typography)
