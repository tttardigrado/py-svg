def render(canvas: list, html: bool = True, style_path: str = "", script_path: str = "", name: str = "output"):
    svg = ""
    for c in canvas:
        svg += c.render() + "\n"
    if html:
        write_html(style_path, script_path, svg, name)

    else:
        with open(f"{name}.svg", "w") as f:
            f.write(svg)


def write_html(style_path: str, script_path: str, svg: str, name: str):
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{name}</title>
            <link rel="stylesheet" href="{style_path}">
        </head>
        <body>
            {svg}

            <script src="{script_path}"></script>
        </body>
    </html>
    """
    with open(f"{name}.html", "w") as f:
        f.write(template)
