#!/usr/bin/env python3
from __future__ import annotations
from collections import defaultdict, deque
import subprocess
import sys
from pathlib import Path
from method_wiki_common import METHOD_ROOT, REQUIRED_KEYS, collect_docs, expected_id, link_targets


def main() -> int:
    docs, errors = collect_docs()

    for doc_id, item in docs.items():
        fm = item["fm"]
        path = item["path"]
        missing = REQUIRED_KEYS - set(fm.keys())
        if missing:
            errors.append(f"MISSING KEYS in {path.relative_to(METHOD_ROOT)}: {sorted(missing)}")
        exp = expected_id(path)
        if doc_id != exp:
            errors.append(f"ID MISMATCH in {path.relative_to(METHOD_ROOT)}: expected {exp}, got {doc_id}")
        links = fm.get("links") or {}
        for required in ("parent", "children", "related"):
            if required not in links:
                errors.append(f"MISSING links.{required} in {path.relative_to(METHOD_ROOT)}")

    ids = set(docs.keys())
    incoming = defaultdict(set)
    adjacency = defaultdict(set)
    for doc_id, item in docs.items():
        for target in link_targets(item["fm"]):
            if target not in ids:
                errors.append(f"BROKEN LINK in {item['path'].relative_to(METHOD_ROOT)}: {target}")
            else:
                adjacency[doc_id].add(target)
                incoming[target].add(doc_id)
                # Treat parent/child/related links as graph edges for reachability.
                adjacency[target].add(doc_id)

    for doc_id in ids:
        if doc_id != "method.index" and not incoming[doc_id]:
            errors.append(f"ORPHAN: {docs[doc_id]['path'].relative_to(METHOD_ROOT)} has no incoming links")

    if "method.index" not in ids:
        errors.append("MISSING ROOT: method.index")
    else:
        seen = set(["method.index"])
        q = deque(["method.index"])
        while q:
            current = q.popleft()
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        for doc_id in sorted(ids - seen):
            errors.append(f"UNREACHABLE FROM method.index: {docs[doc_id]['path'].relative_to(METHOD_ROOT)}")

    graph_check = subprocess.run([sys.executable, "-S", str(METHOD_ROOT / "tools" / "generate_graph.py"), "--check"], text=True, capture_output=True)
    if graph_check.returncode != 0:
        errors.append(graph_check.stdout.strip() or graph_check.stderr.strip())

    if errors:
        print("Method-wiki validation failed:\n")
        for e in errors:
            print(f"- {e}")
        return 1
    print("Method-wiki validation OK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
