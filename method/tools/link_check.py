#!/usr/bin/env python3
from pathlib import Path
import re, sys
base = Path(sys.argv[1] if len(sys.argv) > 1 else 'project')
broken = []
pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for md in base.glob('**/*.md'):
    for link in pattern.findall(md.read_text(encoding='utf-8')):
        if '://' in link or link.startswith('#') or link.startswith('mailto:'):
            continue
        target = (md.parent / link.split('#')[0]).resolve()
        if link.split('#')[0] and not target.exists():
            broken.append((md, link))
if broken:
    for md, link in broken: print(f'Broken link in {md}: {link}')
    sys.exit(1)
print('OK: markdown links look valid')
