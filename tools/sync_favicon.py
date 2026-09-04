#!/usr/bin/env python3
"""Ensure every static HTML page loads the shared Options America favicon."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = '<script src="/favicon.js"></script>'
updated = 0
for path in ROOT.rglob('*.html'):
    if any(part in {'.git', 'node_modules'} for part in path.parts):
        continue
    text = path.read_text(encoding='utf-8')
    if '/favicon.js' in text:
        continue
    marker = '</head>'
    if marker not in text:
        continue
    text = text.replace(marker, SCRIPT + marker, 1)
    path.write_text(text, encoding='utf-8')
    updated += 1
print(f'Updated favicon loader in {updated} HTML files')
