#!/usr/bin/env python3
import json,re,time
from pathlib import Path
from urllib.parse import urljoin,urlparse
import requests
from bs4 import BeautifulSoup

COURSE_URL='https://options-america.com/courses/options-trading-level-3-buying-put-option-strategy/'
OUT=Path('courses/options-trading-level-3-buying-put-option-strategy/course-data.json')
UA='Mozilla/5.0 (compatible; OptionsAmericaMigration/3.1)'
ID_PATTERNS=[re.compile(r'/courses/[^/]+/(\d+)/?'),re.compile(r'[?&](?:lesson_id|item_id)=(\d+)')]
VIMEO_PATTERNS=[re.compile(r'player\.vimeo\.com/video/(\d+)'),re.compile(r'vimeo\.com/(?:video/)?(\d{6,})')]

# Verified against the original WordPress WXR export.
WXR_VIMEO={50603:'932349422',50502:'935428450',50604:'933133568',50605:'933133500',50606:'933133552',50607:'933133513',50608:'933133465',50609:'933133441',50610:'933133488',50611:'933133418',50612:'933560920',50613:'933560824',50614:'933566459',50615:'933562452',50616:'933560647',50617:'933560716',50618:'933560758',50619:'933560686',50620:'933560797',50621:'934305498',50622:'934020397',50623:'934020409',50624:'934020651',50625:'934020252',50626:'934020107',50627:'934020374',50628:'934020533',50629:'934020235',50630:'934020525',50631:'934120460',50632:'934120344',50633:'934120212',50634:'934120220',50635:'934120421',50636:'934120097',50637:'934120233',50638:None,50639:None}

SECTIONS=[(10,'Part 1 — Introduction to Buying Put Options'),(19,'Part 2 — Put Option Chains'),(29,'Part 3 — Buying Put Option Analysis & T+0'),(36,'Part 4 — Put vs Call, Premium & Skew'),(999,'Course Transition & Case Studies')]

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

def section_for(n):
    for end,name in SECTIONS:
        if n<=end:return name
    return 'Course content'

def main():
    s=requests.Session();s.headers.update({'User-Agent':UA})
    r=s.get(COURSE_URL,timeout=30);r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser')
    rows=[];seen=set();course_path=urlparse(COURSE_URL).path.rstrip('/')+'/'
    for a in soup.select('a[href]'):
        href=urljoin(COURSE_URL,a.get('href',''))
        lid=lesson_id(href)
        if not lid or lid in seen or not urlparse(href).path.startswith(course_path): continue
        text=clean(a.get_text(' ',strip=True))
        if not text: continue
        seen.add(lid)
        dur,typ=parse_meta(text)
        title=re.sub(r'^\s*\d+\s*','',text)
        title=re.sub(r'\s+\d+\s*min\s*$','',title,flags=re.I)
        title=re.sub(r'\s+\d+\s+questions?\s*$','',title,flags=re.I)
        rows.append({'wpId':lid,'title':title,'duration':dur,'type':typ,'oldUrl':href})
    for i,row in enumerate(rows,1):
        row['number']=i
        row['section']=section_for(i)
        lid=row['wpId']
        if lid in (50638,50639):
            row['type']='text';row['duration']='Text lesson';row['vimeoId']=None
        elif row['type']=='video':
            row['vimeoId']=WXR_VIMEO.get(lid)
            if not row['vimeoId']:
                try:
                    rr=s.get(row['oldUrl'],timeout=30,allow_redirects=True)
                    row['vimeoId']=vimeo_id(rr.text)
                except Exception:
                    row['vimeoId']=None
                time.sleep(.15)
    # Restore authoritative WXR titles for the two text items.
    for row in rows:
        if row['wpId']==50638: row['title']='Call Option Case Studies'
        if row['wpId']==50639: row['title']='Transition from Level 3 to Level 4'
    data={'course':{'id':49881,'slug':'options-trading-level-3-buying-put-option-strategy','title':'Options Trading Course Level 3: Buying Put Option','level':'Beginner','previewVimeoId':'932349422','sourceUrl':COURSE_URL},'lessons':rows}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'lessons':len(rows),'videos':sum(1 for x in rows if x['type']=='video'),'videosWithVimeo':sum(1 for x in rows if x.get('vimeoId')),'quizzes':sum(1 for x in rows if x['type']=='quiz'),'text':sum(1 for x in rows if x['type']=='text')},indent=2))

if __name__=='__main__':main()
