import string

from rich_typography.glyphs import Glyphs
from rich_typography.fonts import Font

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
         . ╭╮
┬┬╮ ┬╮╮ ┬┐ ┼┐
│├┘ │╭┤ ││ ││
╵╰╴ ╵╰┘ ╵╵ ╵╵
             
""",
    ["re", "ra", "ri", "fi"],
)

SEMISERIF = Font("Semi Serif", UPPER | LOWER | DIGITS | PUNCTUATION, LIGATURES)


if __name__ == "__main__":
    from rich.console import Console
    from rich_typography.typography import Typography
    from rich.text import Text

    lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sed arcu id quam venenatis cursus et vitae quam. Sed non diam ut leo efficitur semper sit amet eget dui. Etiam venenatis nisi ex, vitae egestas velit porta sit amet. Morbi posuere id urna in feugiat. Praesent tristique tellus mauris, vitae sodales lacus pretium eu. Nulla sagittis, ipsum rhoncus varius sollicitudin, dui mi facilisis dui, quis volutpat neque ante nec lectus. Nam sagittis, enim at bibendum fringilla, justo sapien tempor nibh, eget gravida felis quam at urna. Donec convallis accumsan tellus, vitae dictum ligula vulputate et. Vestibulum faucibus sem mauris, ac semper mi congue vitae. Proin dapibus vel ligula et finibus. Sed at rhoncus nunc, eu mollis arcu.
Suspendisse consequat, nisl sed finibus varius, libero libero feugiat nibh, a blandit ipsum ipsum ut ante. Curabitur malesuada posuere elit, porta volutpat sapien pretium ut. Quisque neque erat, viverra sit amet lacinia ac, aliquet aliquam urna. Phasellus egestas nibh eu semper lobortis. Sed risus metus, ullamcorper vitae fringilla quis, tempor eu metus. Donec ultrices commodo nisi, eu sollicitudin nisl malesuada sed. Ut scelerisque nec odio eget ullamcorper. Cras a laoreet mi. Vestibulum a volutpat lacus. Mauris consequat lacinia luctus. Aliquam et erat non ligula varius dignissim. Mauris pellentesque, odio et molestie tempor, dolor nibh pretium dui, viverra feugiat orci massa vel felis. Pellentesque vehicula, neque at molestie maximus, ante lacus dignissim mauris, eget tempor enim leo nec tortor.
Donec maximus velit diam. Vestibulum ac nulla vitae justo laoreet consequat facilisis et ligula. Phasellus vestibulum magna id velit luctus, et consectetur ante venenatis. Nam sed arcu sed ipsum fringilla laoreet ac ornare metus. Maecenas rhoncus justo consequat pellentesque hendrerit. Pellentesque bibendum neque ullamcorper, ornare velit eget, mollis velit. Aenean id erat eu erat sagittis tristique.
Vestibulum gravida euismod viverra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin at metus eget turpis suscipit semper eget ut dui. Cras volutpat diam ut dui posuere, at malesuada quam congue. Ut scelerisque pharetra ipsum, eget convallis dolor accumsan quis. Integer vitae nibh erat. Curabitur eget sagittis eros. Nulla congue luctus magna vitae efficitur. Praesent sit amet leo tellus. Nam nisl enim, rutrum vel porta dapibus, pharetra eget odio.
Suspendisse vel blandit enim. Sed id felis sed sapien mattis feugiat aliquam imperdiet quam. Praesent congue nibh id laoreet accumsan. Vivamus tincidunt turpis sit amet leo varius, vitae convallis dolor dictum. Fusce posuere eget nisl et lacinia. Suspendisse est sem, venenatis eget lacus a, laoreet accumsan erat. Vivamus vehicula nulla a tellus rhoncus dictum. Nulla eget fringilla justo, vitae vehicula nulla. Donec urna risus, aliquam non sapien vitae, pretium venenatis lacus.
"""

    console = Console()
    console.print(
        Typography(
            '"The quick brown fox jumps over the lazy dog," which contains every letter of the alphabet. ',
            SEMISERIF,
        )
    )
    console.print(Typography("You are rad! Just right, figuretively. Qualification", SEMISERIF))
    console.print(Typography("You are rad! Just right, figuretively. Qualification", SEMISERIF, use_ligatures=False))
    console.print(Text(lorem))
    console.print(Typography(lorem, SEMISERIF))
    console.print()
