#!/usr/bin/env python3
from pathlib import Path
import sys
base = Path(sys.argv[1] if len(sys.argv) > 1 else 'project')
required = ['ideas', 'spec', 'method.lock.json']
missing = [p for p in required if not (base / p).exists()]
md_without_h1 = []
for p in list((base/'ideas').glob('*.md')) + list((base/'spec').glob('**/*.md')):
    text = p.read_text(encoding='utf-8')
    if not text.lstrip().startswith('# '):
        md_without_h1.append(str(p))
if missing or md_without_h1:
    if missing: print('Missing:', ', '.join(missing))
    if md_without_h1: print('Markdown files without H1:', *md_without_h1, sep='
- ')
    sys.exit(1)
print('OK: spec structure looks valid')
