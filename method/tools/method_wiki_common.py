from __future__ import annotations
from pathlib import Path
import re

METHOD_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_KEYS = {"id", "title", "type", "status", "version", "links"}


def md_files():
    return sorted(p for p in METHOD_ROOT.rglob("*.md") if "tools" not in p.parts)


def expected_id(path: Path) -> str:
    rel = path.relative_to(METHOD_ROOT).with_suffix("")
    parts = list(rel.parts)
    if parts == ["index"]:
        return "method.index"
    if parts == ["graph"]:
        return "method.graph"
    return ".".join(parts)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"MISSING FRONT MATTER: {path.relative_to(METHOD_ROOT)}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"BROKEN FRONT MATTER: {path.relative_to(METHOD_ROOT)}")
    block = text[4:end].splitlines()
    data = {}
    current_key = None
    current_subkey = None
    for raw in block:
        if not raw.strip():
            continue
        if not raw.startswith(" ") and ":" in raw:
            key, val = raw.split(":", 1)
            key, val = key.strip(), val.strip()
            current_key = key
            current_subkey = None
            if val == "":
                data[key] = {}
            elif val == "[]":
                data[key] = []
            else:
                data[key] = val
        elif raw.startswith("  ") and not raw.startswith("    ") and ":" in raw and isinstance(data.get(current_key), dict):
            sub, val = raw.strip().split(":", 1)
            sub, val = sub.strip(), val.strip()
            current_subkey = sub
            if val == "":
                data[current_key][sub] = []
            elif val == "[]":
                data[current_key][sub] = []
            else:
                data[current_key][sub] = val
        elif raw.startswith("    - ") and isinstance(data.get(current_key), dict):
            data[current_key].setdefault(current_subkey, []).append(raw.strip()[2:].strip())
        elif raw.startswith("  - "):
            data.setdefault(current_key, []).append(raw.strip()[2:].strip())
    return data


def collect_docs():
    docs = {}
    errors = []
    for p in md_files():
        try:
            fm = parse_frontmatter(p)
            docs[fm.get("id", "")] = {"path": p, "fm": fm}
        except Exception as e:
            errors.append(str(e))
    return docs, errors


def link_targets(fm: dict):
    links = fm.get("links") or {}
    targets = []
    parent = links.get("parent")
    if parent:
        targets.append(parent)
    for key in ("children", "related"):
        value = links.get(key) or []
        if isinstance(value, str):
            value = [value]
        targets.extend(value)
    return [t for t in targets if t]
