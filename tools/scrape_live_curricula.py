#!/usr/bin/env python3
import json,re,time
from pathlib import Path
from urllib.parse import urljoin,urlparse

import requests
from bs4 import BeautifulSoup

CATALOG=Path('data/import/master-catalog.json')
OUT=Path('data/import/live-curricula.json')
UA='Mozilla/5.0 (compatible; OptionsAmericaMigration/1.0)'

LESSON_ID_PATTERNS=[
    re.compile(r'/courses/[^/]+/(\d+)/?'),
    re.compile(r'[?&](?:lesson_id|item_id)=(\d+)')
]

def lesson_id_from_href(href):
    for pattern in LESSON_ID_PATTERNS:
        m=pattern.search(href or '')
        if m:return int(m.group(1))
    return None

def clean(s):
    return ' '.join((s or '').split())

def scrape_course(session,course):
    url=course['url']
    r=session.get(url,timeout=30,allow_redirects=True)
    r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser')
    rows=[]; seen=set(); current_section='Course content'

    # MasterStudy has changed class names over versions, so use several signals.
    candidates=soup.select('a[href]')
    for a in candidates:
        href=urljoin(url,a.get('href',''))
        lid=lesson_id_from_href(href)
        if not lid or lid in seen: continue
        # Only keep links that belong to this course path when possible.
        p=urlparse(href).path
        course_path=urlparse(url).path.rstrip('/')+'/'
        if not p.startswith(course_path): continue
        seen.add(lid)
        title=clean(a.get_text(' ',strip=True))
        parent=a.parent
        # Look upward for a nearby section/chapter heading.
        for anc in list(a.parents)[:5]:
            heading=anc.find(['h2','h3','h4']) if hasattr(anc,'find') else None
            if heading:
                h=clean(heading.get_text(' ',strip=True))
                if h and h!=title:
                    current_section=h;break
        rows.append({'id':lid,'title':title,'url':href,'section':current_section})

    # Fallback for lesson IDs embedded in scripts/data attributes.
    if not rows:
        for m in re.finditer(r'"(?:lesson_id|item_id|post_id)"\s*:\s*"?(\d+)"?',r.text):
            lid=int(m.group(1))
            if lid not in seen:
                seen.add(lid);rows.append({'id':lid,'title':'','url':'','section':'Course content'})

    return {
        'courseId':course['id'],'slug':course['slug'],'title':course['title'],
        'sourceUrl':url,'httpStatus':r.status_code,'items':rows,'itemCount':len(rows)
    }

def main():
    catalog=json.loads(CATALOG.read_text(encoding='utf-8'))
    s=requests.Session();s.headers.update({'User-Agent':UA})
    result={'generatedFrom':'Rendered public course pages','courses':[],'errors':[]}
    for i,course in enumerate(catalog['courses'],1):
        try:
            data=scrape_course(s,course)
            result['courses'].append(data)
            print(f"[{i}/{len(catalog['courses'])}] {course['slug']}: {data['itemCount']} items")
        except Exception as e:
            result['errors'].append({'courseId':course['id'],'slug':course['slug'],'url':course['url'],'error':str(e)})
            print(f"[{i}/{len(catalog['courses'])}] ERROR {course['slug']}: {e}")
        time.sleep(.35)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f"Wrote {OUT} with {len(result['courses'])} courses and {len(result['errors'])} errors")

if __name__=='__main__':main()
