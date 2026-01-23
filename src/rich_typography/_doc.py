CODE_FORMAT = """\
<pre>
<code>
<svg class="rich-terminal" viewBox="0 0 {terminal_width} {terminal_height}" xmlns="http://www.w3.org/2000/svg">
    <!-- Generated with Rich https://www.textualize.io -->
    <style>
        @font-face {{
        font-family: "Cascadia Code";
        src: url(https://fonts.gstatic.com/s/cascadiacode/v5/qWcyB6-zq5zxD57cT5s916v3aD7rsBElg4M.woff2) format('woff2');
                <style>
@import url('https://fonts.googleapis.com/css2?family=Cascadia+Code:ital,wght@0,200..700;1,200..700&display=swap');
</style>
        font-style: normal;
        font-weight: 400;
    }}
    @font-face {{
        font-family: "Cascadia Code";
        src: url(https://fonts.gstatic.com/s/cascadiacode/v5/qWcyB6-zq5zxD57cT5s916v3aD7rsBElg4M.woff2) format('woff2');
        font-style: bold;
        font-weight: 700;
    }}

    .{unique_id}-matrix {{
        font-family: Cascadia Code, monospace;
        font-size: {char_height}px;
        line-height: {line_height}px;
        font-variant-east-asian: full-width;
        font-weight: bold;
    }}

    .{unique_id}-title {{
        font-size: 18px;
        font-weight: bold;
        font-family: arial;
    }}
    {styles}
    </style>
    <defs>
        <clipPath id="{unique_id}-clip-terminal">
            <rect x="0" y="0" width="{terminal_width}" height="{terminal_height}" />
        </clipPath>
        {lines}
    </defs>
    <g clip-path="url(#{unique_id}-clip-terminal)">
    {backgrounds}
    <g class="{unique_id}-matrix">
    {matrix}
    </g>
    </g>
</svg>
</code>
</pre>
"""

def rich(source, language, css_class, options, md, attrs, **kwargs) -> str:
    """A superfences formatter to insert an SVG screenshot."""

    import io

    from rich.console import Console

    title = attrs.get("title", "Rich")

    rows = int(attrs.get("lines", 24))
    columns = int(attrs.get("columns", 100))

    console = Console(
        file=io.StringIO(),
        record=True,
        force_terminal=True,
        color_system="truecolor",
        width=columns,
        height=rows,
    )
    error_console = Console(stderr=True)

    globals: dict = {}
    try:
        exec(source, globals)
    except Exception:
        error_console.print_exception()
        # console.bell()

    if "output" in globals:
        console.print(globals["output"])
    output_svg = console.export_svg(title=title, code_format=CODE_FORMAT)
    return output_svg
