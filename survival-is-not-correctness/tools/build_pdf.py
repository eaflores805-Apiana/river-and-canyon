#!/usr/bin/env python3
"""Rebuild the manuscript PDF from the Markdown source + figure PNGs.

Requirements:
  python -m pip install markdown
  wkhtmltopdf on PATH  (https://wkhtmltopdf.org/)

Usage (from anywhere):
  python tools/build_pdf.py

Outputs (at the repo root):
  build/paper.html
  survival-is-not-correctness.pdf

The figures are shipped as final PNGs and are NOT regenerated here.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent  # repo root
MD = ROOT / "survival-is-not-correctness.md"
HTML = ROOT / "build" / "paper.html"
PDF = ROOT / "survival-is-not-correctness.pdf"

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency: pip install markdown")

src = MD.read_text(encoding="utf-8")

# Resolve relative figure references to absolute file:// URIs so the renderer finds them.
src = re.sub(
    r"\]\((assets/fig_[A-Za-z0-9_]+\.png)\)",
    lambda m: f"]({(ROOT / m.group(1)).as_uri()})",
    src,
)

html_body = markdown.markdown(
    src,
    extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    output_format="html5",
)

CSS = """
@page { size: Letter; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 10.5pt; line-height: 1.5; color: #1a1a1a;
  max-width: 100%;
}
h1 {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 18pt; line-height: 1.25; color: #111;
  border-bottom: 2px solid #333; padding-bottom: 8px; margin: 0 0 12px 0;
}
h2 {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 13.5pt; color: #111; margin: 22px 0 8px 0;
  border-bottom: 1px solid #ccc; padding-bottom: 3px;
  page-break-after: avoid;
}
h3 {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 11pt; color: #222; margin: 16px 0 5px 0; page-break-after: avoid;
}
p { margin: 0.5em 0; text-align: justify; }
em { color: #333; }
strong { color: #000; }
ul, ol { margin: 0.4em 0 0.6em 0; padding-left: 1.4em; }
li { margin: 0.2em 0; text-align: justify; }
blockquote {
  margin: 0.8em 0; padding: 6px 12px; border-left: 3px solid #888;
  background: #f7f7f7; font-style: italic;
}
blockquote p { margin: 0.2em 0; }
code {
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
  font-size: 8.8pt; background: #f0f0f0; padding: 0 2px; border-radius: 2px;
}
pre {
  background: #f5f5f5; border: 1px solid #ddd; border-radius: 3px;
  padding: 8px 10px; font-size: 8.6pt; line-height: 1.35; overflow-x: hidden;
  white-space: pre-wrap; word-wrap: break-word;
  page-break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: 8.6pt; }
hr { border: none; border-top: 1px solid #bbb; margin: 18px 0; }
table {
  border-collapse: collapse; width: 100%; margin: 10px 0 14px 0;
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 8pt;
  line-height: 1.3;
}
th, td {
  border: 1px solid #b8b8b8; padding: 4px 5px; vertical-align: top;
  text-align: left; word-wrap: break-word; overflow-wrap: break-word;
}
th { background: #ececec; font-weight: bold; color: #111; }
tr { page-break-inside: avoid; }
td code, th code { font-size: 7.6pt; background: #e6e6e6; }
img {
  display: block; margin: 14px auto 4px auto; max-width: 86%; height: auto;
  page-break-inside: avoid;
}
img + p, p > img { page-break-before: avoid; }
"""

doc = (
    "<!DOCTYPE html>\n"
    '<html lang="en"><head><meta charset="utf-8"><style>'
    + CSS
    + "</style></head>\n<body>"
    + html_body
    + "</body></html>"
)

HTML.parent.mkdir(exist_ok=True)
HTML.write_text(doc, encoding="utf-8")
print(f"HTML written: {len(doc)} chars; tables: {html_body.count('<table>')}")

cmd = [
    "wkhtmltopdf", "--encoding", "utf-8", "--enable-local-file-access",
    "--page-size", "Letter",
    "--margin-top", "16mm", "--margin-bottom", "16mm",
    "--margin-left", "15mm", "--margin-right", "15mm",
    "--footer-center", "[page] / [topage]", "--footer-font-size", "8",
    "--footer-spacing", "5", "--footer-font-name", "Helvetica",
    "--quiet", str(HTML), str(PDF),
]
try:
    subprocess.run(cmd, check=True)
except FileNotFoundError:
    sys.exit("Missing dependency: install wkhtmltopdf and ensure it is on PATH.")
print(f"PDF written: {PDF}")
