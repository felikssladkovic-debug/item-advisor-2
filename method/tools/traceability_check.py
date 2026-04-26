#!/usr/bin/env python3
from pathlib import Path
import sys
base = Path(sys.argv[1] if len(sys.argv) > 1 else 'project')
trace = base / 'spec' / '60-quality' / 'traceability.md'
if not trace.exists():
    print('Missing traceability.md')
    sys.exit(1)
text = trace.read_text(encoding='utf-8')
if '| Idea / Decision | Spec | Code | Tests | Status |' not in text:
    print('traceability.md does not contain the expected table header')
    sys.exit(1)
print('OK: traceability table exists')
