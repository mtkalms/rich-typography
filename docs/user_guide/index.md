# User Guide


=== "Output"

    ```rich
    from rich.console import Console
    from rich_typography import Typography

    console = Console()
    output = Typography.from_markup("Hello from [purple]rich-typography[/purple]")
    ```

=== "example"

    ```python
    from rich.console import Console
    from rich_typography import Typography

    console = Console()
    text = Typography.from_markup("Hello from [purple]rich-typography[/purple]")
    console.print(text)
    ```
