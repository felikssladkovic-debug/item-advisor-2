#!/usr/bin/env python3
from pathlib import Path
import sys
base = Path(sys.argv[1] if len(sys.argv) > 1 else 'project')
allowed = {'ideas', 'spec', 'method.lock.json', 'README.md', '.gitkeep'}
extra = [p for p in base.iterdir() if p.name not in allowed]
if extra:
    print('Extra top-level project entries:')
    for p in extra: print('-', p)
    print('This may be OK after implementation starts, but for barebone start it should be intentional.')
else:
    print('OK: no unexpected top-level project entries')
