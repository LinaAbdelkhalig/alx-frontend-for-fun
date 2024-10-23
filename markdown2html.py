#!/usr/bin/python3
import sys
import os
import markdown

if __name__ == "__main__":
    # check if the correct number of arguments have been passed
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    # Assign arguments to file names
    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        exit(1)

    # Convert Markdown to HTML
    with open(md_file, 'r') as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content)

    # Write the HTML content to the output file
    with open(html_file, 'w') as f:
        f.write(html_content)

    # Successful completion
    exit(0)
