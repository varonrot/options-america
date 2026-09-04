#!/usr/bin/env python3
import json,re,time
from pathlib import Path
from urllib.parse import urljoin,urlparse
import requests
from bs4 import BeautifulSoup

COURSE_URL='https://options-america.com/courses/options-trading-level-2-selling-call-option-strategy-2/'
OUT=Path('courses/options-trading-level-2-selling-call-option-strategy-2/course-data.json')
UA='Mozilla/5.0 (compatible; OptionsAmericaMigration/2.0)'

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
    r=s.get(COURSE_URL,timeout=30);r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser')
    rows=[];seen=set();section='Course Start'
    course_path=urlparse(COURSE_URL).path.rstrip('/')+'/'
    for a in soup.select('a[href]'):
        href=urljoin(COURSE_URL,a.get('href',''))
        lid=lesson_id(href)
        if not lid or lid in seen or not urlparse(href).path.startswith(course_path): continue
        text=clean(a.get_text(' ',strip=True))
        if not text: continue
        seen.add(lid)
        for anc in list(a.parents)[:6]:
            h=anc.find(['h2','h3','h4']) if hasattr(anc,'find') else None
            if h:
                ht=clean(h.get_text(' ',strip=True))
                if ht and ht!=text and len(ht)<180:
                    section=ht;break
        dur,typ=parse_meta(text)
        # remove leading lesson number and trailing duration from title
        title=re.sub(r'^\s*\d+\s*','',text)
        title=re.sub(r'\s+\d+\s*min\s*$','',title,flags=re.I)
        title=re.sub(r'\s+\d+\s+questions?\s*$','',title,flags=re.I)
        rows.append({'wpId':lid,'title':title,'duration':dur,'type':typ,'section':section,'oldUrl':href})
    for i,row in enumerate(rows,1):
        row['number']=i
        if row['type']=='video':
            try:
                rr=s.get(row['oldUrl'],timeout=30,allow_redirects=True)
                row['vimeoId']=vimeo_id(rr.text)
            except Exception:
                row['vimeoId']=None
            time.sleep(.15)
    data={'course':{'id':50159,'slug':'options-trading-level-2-selling-call-option-strategy-2','title':'Options Trading Course Level 2: Selling Call Option','level':'Beginner','sourceUrl':COURSE_URL},'lessons':rows}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'lessons':len(rows),'videos':sum(1 for x in rows if x['type']=='video'),'videosWithVimeo':sum(1 for x in rows if x.get('vimeoId')),'quizzes':sum(1 for x in rows if x['type']=='quiz')},indent=2))

if __name__=='__main__':main()
