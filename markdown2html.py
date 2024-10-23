#!/usr/bin/python3
"""
markdown2html.py: A script to convert a Markdown file to an HTML file.

Usage:
    ./markdown2html.py README.md README.html

Arguments:
    - First argument: Input Markdown file
    - Second argument: Output HTML file

Exits:
    - Exit 1 if there are not enough arguments
    - Exit 1 if the Markdown file does not exist
    - Exit 0 on successful completion
"""

import sys
import os
import markdown

def convert_md_to_html(md_file, html_file):
    """
    Converts a Markdown file to an HTML file.

    Parameters:
    - md_file (str): The path to the input Markdown file.
    - html_file (str): The path to the output HTML file.

    Returns:
    - None
    """
    with open(md_file, 'r') as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content)

    with open(html_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        exit(1)

    # Convert Markdown to HTML
    convert_md_to_html(md_file, html_file)

    # Successful completion
    exit(0)

