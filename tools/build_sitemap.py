#!/usr/bin/env python3
"""Generate the public XML sitemap from static index pages."""

from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://options-america.onrender.com"
EXCLUDED_PARTS = {".git", "dashboard", "player"}


def public_url(page: Path) -> str | None:
    relative = page.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return None
    directory = relative.parent.as_posix()
    path = "/" if directory == "." else f"/{quote(directory, safe='/')}/"
    return f"{BASE_URL}{path}"


urls = sorted(filter(None, (public_url(page) for page in ROOT.rglob("index.html"))))
rows = "\n".join(f"  <url><loc>{escape(url)}</loc></url>" for url in urls)
xml = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
       "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
       f"{rows}\n"
       "</urlset>\n")
(ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
print(f"Generated sitemap.xml with {len(urls)} public URLs")
