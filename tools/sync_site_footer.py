#!/usr/bin/env python3
import re
from pathlib import Path

FOOTER='''<footer>
  <div class="container footer-grid">
    <div><a class="brand" href="/"><span class="brand-icon">↗</span><span>Options <b>America</b></span></a><p>The free resource for learning options trading from beginner to advanced.</p></div>
    <div><h4>Learn</h4><a href="/courses/">Courses</a><a href="/#paths">Learning Paths</a><a href="/courses/?level=Beginner">Beginner Courses</a><a href="/courses/?category=Option%20Greeks">Options Greeks</a></div>
    <div><h4>Strategies</h4><a href="/#strategies">All Strategies</a><a href="/courses/?category=Options%20Strategies">Income Strategies</a><a href="/courses/?category=Options%20Strategies">Neutral Strategies</a><a href="/courses/?category=Options%20Adjustments">Adjustments</a></div>
    <div><h4>Futures</h4><a href="/#futures">Options on Futures</a><a href="/courses/?category=Options%20on%20Futures">Gold Options</a><a href="/courses/?category=Options%20on%20Futures">Crude Oil Options</a><a href="/courses/?category=Options%20on%20Futures">Natural Gas Options</a></div>
    <div><h4>Resources</h4><a href="/#blog">Blog</a><a href="/#resources">Resources</a><a href="/courses/?category=Case%20Studies">Case Studies</a><a href="/courses/">Course Library</a></div>
  </div>
  <div class="container copyright">© <span data-current-year></span> Options America · Educational content only — not financial advice.</div>
</footer>'''
YEAR_SCRIPT='<script>document.querySelectorAll("[data-current-year]").forEach(el=>el.textContent=new Date().getFullYear());</script>'

changed=[]
for path in [Path('index.html'), Path('courses/index.html'), *Path('courses').glob('*/index.html')]:
    if 'player' in path.parts or not path.exists():
        continue
    text=path.read_text(encoding='utf-8')
    if '<footer' not in text:
        continue
    new=re.sub(r'<footer\b[^>]*>.*?</footer>', FOOTER, text, flags=re.S|re.I)
    new=re.sub(r'<script>document\.querySelectorAll\([\'\"]\.current-year[\'\"]\).*?</script>', '', new, flags=re.S)
    if 'data-current-year' in new and YEAR_SCRIPT not in new:
        new=new.replace('</body>', YEAR_SCRIPT+'\n</body>')
    if new!=text:
        path.write_text(new,encoding='utf-8')
        changed.append(str(path))
print(f'Updated {len(changed)} pages')
for p in changed: print(p)
