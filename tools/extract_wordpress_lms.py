#!/usr/bin/env python3
import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter

NS={'wp':'http://wordpress.org/export/1.2/','content':'http://purl.org/rss/1.0/modules/content/'}

def text(el,path,ns=None,default=''):
    node=el.find(path,ns or {})
    return default if node is None or node.text is None else node.text

def meta(item):
    out={}
    for pm in item.findall('wp:postmeta',NS):
        k=text(pm,'wp:meta_key',NS)
        v=text(pm,'wp:meta_value',NS)
        if k: out[k]=v
    return out

def vimeo_id(content,m):
    candidates=[]
    for k,v in m.items():
        if 'vimeo' in k.lower() and v: candidates.append(v)
        if 'vimeo.com' in v: candidates.append(v)
    if content: candidates.append(content)
    for value in candidates:
        hit=re.search(r'(?:player\.)?vimeo\.com/(?:video/)?(\d+)',value)
        if hit:return hit.group(1)
    return None

def parse(path):
    root=ET.parse(path).getroot()
    rows=[]
    for item in root.findall('./channel/item'):
        pt=text(item,'wp:post_type',NS)
        if not pt: continue
        m=meta(item)
        rows.append({
            'id':int(text(item,'wp:post_id',NS,'0')),
            'type':pt,
            'title':text(item,'title'),
            'slug':text(item,'wp:post_name',NS),
            'url':text(item,'link'),
            'content':text(item,'content:encoded',NS),
            'meta':m,
            'vimeoId':vimeo_id(text(item,'content:encoded',NS),m)
        })
    return rows

def main():
    if len(sys.argv)<2:
        raise SystemExit('Usage: extract_wordpress_lms.py export1.xml [export2.xml ...]')
    rows=[]
    for p in sys.argv[1:]: rows.extend(parse(p))
    by_type={}
    for r in rows: by_type.setdefault(r['type'],{})[r['id']]=r
    out=Path('data/import');out.mkdir(parents=True,exist_ok=True)

    courses=[]
    for r in by_type.get('stm-courses',{}).values():
        m=r['meta']
        courses.append({
            'id':r['id'],'title':r['title'],'slug':r['slug'],'url':r['url'],
            'level':m.get('level',''),'duration':m.get('duration_info',''),
            'skillLevel':m.get('skill_level',''),'previewVimeoId':r['vimeoId'],
            'thumbnailId':m.get('_thumbnail_id',''),'curriculumRaw':m.get('curriculum','')
        })

    lessons=[]
    for r in by_type.get('stm-lessons',{}).values():
        m=r['meta']
        lessons.append({
            'id':r['id'],'title':r['title'],'slug':r['slug'],'url':r['url'],
            'duration':m.get('duration',''),'type':m.get('type',''),
            'preview':m.get('preview',''),'vimeoId':r['vimeoId']
        })

    quizzes=[]
    for r in by_type.get('stm-quizzes',{}).values():
        m=r['meta']; ids=[int(x) for x in re.findall(r'\d+',m.get('questions',''))]
        quizzes.append({
            'id':r['id'],'title':r['title'],'slug':r['slug'],'url':r['url'],
            'questions':ids,'duration':m.get('duration',''),
            'durationMeasure':m.get('duration_measure',''),'passingGrade':m.get('passing_grade','')
        })

    questions=[]
    for r in by_type.get('stm-questions',{}).values():
        m=r['meta']
        questions.append({
            'id':r['id'],'title':r['title'],'slug':r['slug'],'url':r['url'],
            'question':m.get('question','') or r['title'],'questionType':m.get('type',''),
            'answersSerialized':m.get('answers',''),'hint':m.get('question_hint',''),
            'explanation':m.get('question_explanation','')
        })

    payloads={
        'courses-index.json':sorted(courses,key=lambda x:x['id']),
        'lessons-index.json':sorted(lessons,key=lambda x:x['id']),
        'quizzes-index.json':sorted(quizzes,key=lambda x:x['id']),
        'questions-index.json':sorted(questions,key=lambda x:x['id'])
    }
    for name,data in payloads.items():
        (out/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    summary={
        'counts':dict(Counter(r['type'] for r in rows)),
        'lessonsWithVimeo':sum(1 for l in lessons if l['vimeoId']),
        'warning':'MasterStudy WXR curriculum metadata may be stale and is not sufficient by itself to reconstruct current course-to-lesson ordering. Use rendered curriculum HTML or another relationship source for exact mappings.'
    }
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
