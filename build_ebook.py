import markdown
import os
import base64
import re

def get_base64_image(filepath):
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    return ""

files_to_include = [
    "ebook-draft.md",
    "content md/excel-basics.md",
    "content md/sql-fundamentals.md",
    "content md/python-for-data.md"
]

combined_markdown = ""
for file in files_to_include:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            combined_markdown += f.read() + "\n\n"

html_body = markdown.markdown(combined_markdown)

# Base64 encode all referenced images so the HTML is completely portable
def replace_img(match):
    img_path = match.group(1).replace('../', '')
    b64_src = get_base64_image(img_path)
    if b64_src:
         return f'src="{b64_src}"'
    return match.group(0)

html_body = re.sub(r'src="([^"]+)"', replace_img, html_body)

# Get base64 for the background image
bg_image = get_base64_image("assets/ebook_cover.png")

# Wrap in a beautiful HTML template
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analysis Basics eBook</title>
    <style>
        body {{
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.8;
            color: #e0e0e0;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #121212;
            background-image: url('{bg_image}');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            /* Blend the image with the dark background color to make it a subtle watermark */
            background-blend-mode: multiply;
        }}
        .book-container {{
            background: rgba(25, 25, 25, 0.95);
            padding: 50px 80px;
            border-radius: 8px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.8);
            position: relative;
            z-index: 1;
            /* Create a slight blur effect behind the container */
            backdrop-filter: blur(5px);
        }}
        h1, h2, h3 {{
            color: #ffffff;
            margin-top: 2em;
            margin-bottom: 0.5em;
        }}
        h1 {{
            font-size: 2.5em;
            text-align: center;
            border-bottom: 2px solid #333333;
            padding-bottom: 10px;
        }}
        h2 {{
            border-bottom: 1px solid #333333;
            padding-bottom: 5px;
            color: #90caf9;
        }}
        code {{
            background-color: #2d2d2d;
            color: #ffb74d;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #000000;
            color: #d4d4d4;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
            color: inherit;
        }}
        blockquote {{
            border-left: 4px solid #3b82f6;
            margin: 0;
            padding: 10px 20px;
            background-color: #1a2639;
            border-radius: 0 8px 8px 0;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.5);
            margin: 20px 0;
        }}
        hr {{
            border: 0;
            height: 1px;
            background: #333333;
            margin: 40px 0;
        }}
        @media (max-width: 768px) {{
            .book-container {{
                padding: 30px 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="book-container">
        {html_body}
    </div>
</body>
</html>
"""

with open("Data_Analysis_Basics_eBook.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("eBook HTML generated successfully with embedded images and background!")
