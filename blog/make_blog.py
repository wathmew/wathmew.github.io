import markdown
from pathlib import Path

path = Path(__file__).parent / "posts"

blog_page = """
<!DOCTYPE html>

<html>
    <head>
        <title>wathmusings</title>
        <link rel="stylesheet" href="styles.css">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <article>
            <h1>Blog</h1>
            <p>This is in chronological order from latest to earliest</p>
            <br>
"""

for md_file in sorted(path.glob("*.md"), key=lambda f: int(f.stem.split("-", 1)[0]), reverse=True):
    with md_file.open("r", encoding="utf-8") as f:
        content = f.read()
        post_html = markdown.markdown(content)

        blog_post = f"""
        <!DOCTYPE html>

        <html>
            <head>
                <title>{md_file.stem.split("-",1)[1]}</title>
                <link rel="stylesheet" href="styles.css">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <article>
                {post_html}
                </article>
            </body>
        </html>
        """

        blog_page += f"""
        <p><a href=./blog/posts/{md_file.stem}.html>{md_file.stem.split("-",1)[1]}</a></p>
        """

        with open(f"blog/posts/{md_file.stem}.html", "w", encoding="utf-8") as f:
            f.write(blog_post)
        
        





blog_page += """
       </article>
    </body>
</html>
"""

output_file = Path(__file__).parent.parent / "blog.html"
with output_file.open("w", encoding="utf-8") as f:
    f.write(blog_page)