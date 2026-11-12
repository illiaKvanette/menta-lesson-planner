#!/usr/bin/env python3
"""Builds a lesson (or unit-test) page from the lesson JSON, so Claude never copies the page code.

    python3 build_page.py lesson.json [out.html]

Writes the page (templates/lesson-page.md with the JSON inside) and prints the menta-lms.com/play link: the same
lesson opened with Menta's own exercises, where print and PDF work. Python standard library only.
"""
import base64, json, pathlib, re, sys, zlib

here = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".html")

lesson = json.loads(src.read_text(encoding="utf-8"))  # fails loudly on a JSON mistake: fix the JSON and run again
data = json.dumps(lesson, ensure_ascii=False).replace("</", "<\\/")

template = (here / "templates" / ("test-page.md" if lesson.get("mode") == "test" else "lesson-page.md")).read_text(encoding="utf-8")
html = re.search(r"````html\n(.*?)````", template, re.S).group(1)
html = re.sub(r'(<script id="lesson-data" type="application/json">\n).*?(\n</script>)', lambda m: m.group(1) + data + m.group(2), html, count=1, flags=re.S)
out.write_text(html, encoding="utf-8")

z = zlib.compressobj(9, zlib.DEFLATED, -15)
packed = z.compress(json.dumps(lesson, ensure_ascii=False).encode("utf-8")) + z.flush()
link = "https://menta-lms.com/play#" + base64.urlsafe_b64encode(packed).decode().rstrip("=")
print(f"page: {out}  ({len(html) // 1024} KB)")
print(f"menta: {link}")
if len(link) > 60000:
    print("warning: the link is long (big pictures); it opens in Chrome, Edge and Firefox, maybe not in old Safari")
