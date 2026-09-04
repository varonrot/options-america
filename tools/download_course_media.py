#!/usr/bin/env python3
import json
import mimetypes
from pathlib import Path
from urllib.parse import urlparse

import requests

MAP_PATH = Path('data/import/course-media-map.json')
OUT_DIR = Path('assets/images/courses/legacy')
TIMEOUT = 30


def extension_from(url, content_type=''):
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg'}:
        return suffix
    guessed = mimetypes.guess_extension((content_type or '').split(';')[0].strip())
    return guessed or '.img'


def main():
    data = json.loads(MAP_PATH.read_text(encoding='utf-8'))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({'User-Agent': 'Options-America-Migration/1.0'})

    results = []
    for idx, course in enumerate(data['courses'], start=1):
        url = course['sourceUrl']
        slug = course['slug']
        try:
            response = session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            ext = extension_from(url, response.headers.get('content-type', ''))
            dest = OUT_DIR / f'{slug}{ext}'
            dest.write_bytes(response.content)
            results.append({'courseId': course['courseId'], 'slug': slug, 'path': str(dest), 'bytes': len(response.content), 'status': 'ok'})
            print(f'[{idx}/{len(data["courses"])}] {slug}: {len(response.content)} bytes')
        except Exception as exc:
            results.append({'courseId': course['courseId'], 'slug': slug, 'sourceUrl': url, 'status': 'error', 'error': str(exc)})
            print(f'[{idx}/{len(data["courses"])}] ERROR {slug}: {exc}')

    report = {
        'total': len(results),
        'downloaded': sum(1 for r in results if r['status'] == 'ok'),
        'errors': sum(1 for r in results if r['status'] == 'error'),
        'items': results,
    }
    Path('data/import/course-media-download-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('total', 'downloaded', 'errors')}, indent=2))


if __name__ == '__main__':
    main()
