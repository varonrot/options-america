#!/usr/bin/env python3
import json,re,time
from pathlib import Path
from urllib.parse import urljoin,urlparse
import requests
from bs4 import BeautifulSoup

COURSE_URL='https://options-america.com/courses/options-trading-level-4-selling-put-option-strategy/'
SLUG='options-trading-level-4-selling-put-option-strategy'
OUT=Path(f'courses/{SLUG}/course-data.json')
UA='Mozilla/5.0 (compatible; OptionsAmericaMigration/4.0)'
ID_PATTERNS=[re.compile(r'/courses/[^/]+/(\d+)/?'),re.compile(r'[?&](?:lesson_id|item_id)=(\d+)')]
VIMEO_PATTERNS=[re.compile(r'player\.vimeo\.com/video/(\d+)'),re.compile(r'vimeo\.com/(?:video/)?(\d{6,})')]

def clean(s): return ' '.join((s or '').split())
def lesson_id(href):
    for p in ID_PATTERNS:
        m=p.search(href or '')
        if m:return int(m.group(1))
    return None

def vimeo_id(text):
    for p in VIMEO_PATTERNS:
        m=p.search(text or '')
        if m:return m.group(1)
    return None

def parse_meta(text):
    text=clean(text)
    q=re.search(r'(\d+)\s+questions?',text,re.I)
    if q:return f'{q.group(1)} questions','quiz'
    m=re.search(r'(\d+)\s*min',text,re.I)
    return (f'{m.group(1)} min' if m else 'Video lesson'),'video'

def main():
    s=requests.Session();s.headers.update({'User-Agent':UA})
    r=s.get(COURSE_URL,timeout=30);r.raise_for_status(); soup=BeautifulSoup(r.text,'html.parser')
    rows=[];seen=set();section='Course Start'; course_path=urlparse(COURSE_URL).path.rstrip('/')+'/'
    for a in soup.select('a[href]'):
        href=urljoin(COURSE_URL,a.get('href','')); lid=lesson_id(href)
        if not lid or lid in seen or not urlparse(href).path.startswith(course_path):continue
        text=clean(a.get_text(' ',strip=True))
        if not text:continue
        seen.add(lid); dur,typ=parse_meta(text)
        title=re.sub(r'^\s*\d+\s*','',text); title=re.sub(r'\s+\d+\s*min\s*$','',title,flags=re.I); title=re.sub(r'\s+\d+\s+questions?\s*$','',title,flags=re.I)
        rows.append({'wpId':lid,'title':title,'duration':dur,'type':typ,'oldUrl':href})
    # Infer chapter boundaries from intro/summary wording while preserving exact lesson order.
    part=1
    for i,row in enumerate(rows,1):
        row['number']=i
        t=row['title'].lower()
        if i>1 and ('what will we learn' in t or 'what we will learn' in t or 'introduction to' in t) and rows[i-2].get('section'):
            if 'summary' in rows[i-2]['title'].lower(): part+=1
        row['section']=f'Part {part} — Selling Put Options'
        if 'text lesson' in t:
            row['title']=re.sub(r'\s*text lesson\s*$','',row['title'],flags=re.I); row['type']='text'; row['duration']='Text lesson'
        if row['type']=='video':
            try:
                rr=s.get(row['oldUrl'],timeout=30,allow_redirects=True); row['vimeoId']=vimeo_id(rr.text)
            except Exception: row['vimeoId']=None
            time.sleep(.1)
    data={'course':{'slug':SLUG,'title':'Options Trading Course Level 4: Selling Put Option','level':'Beginner','previewVimeoId':next((x.get('vimeoId') for x in rows if x.get('vimeoId')),None),'sourceUrl':COURSE_URL},'lessons':rows}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'lessons':len(rows),'videos':sum(x['type']=='video' for x in rows),'videosWithVimeo':sum(bool(x.get('vimeoId')) for x in rows),'quizzes':sum(x['type']=='quiz' for x in rows),'text':sum(x['type']=='text' for x in rows)},indent=2))
if __name__=='__main__':main()
