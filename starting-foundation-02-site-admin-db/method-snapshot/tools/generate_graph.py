#!/usr/bin/env python3
from __future__ import annotations
import argparse
from method_wiki_common import METHOD_ROOT, collect_docs


def node_name(doc_id: str) -> str:
    return doc_id.replace(".", "_").replace("-", "_")


def generate() -> str:
    docs, errors = collect_docs()
    if errors:
        raise SystemExit("\n".join(errors))

    lines = [
        "---",
        "id: method.graph",
        "title: Method Graph",
        "type: generated",
        "status: generated",
        "version: 0.1",
        "links:",
        "  parent: method.index",
        "  children: []",
        "  related:",
        "    - rules.wiki-linking-rules",
        "---",
        "",
        "# Method Graph",
        "",
        "Generated from YAML front matter. Do not edit graph edges manually.",
        "",
        "```mermaid",
        "graph TD",
    ]

    # Declare nodes for stable labels.
    for doc_id in sorted(docs):
        title = docs[doc_id]["fm"].get("title", doc_id).replace('"', "'")
        lines.append(f'  {node_name(doc_id)}["{doc_id}<br/>{title}"]')

    lines.append("")

    for doc_id in sorted(docs):
        if doc_id == "method.graph":
            continue
        fm = docs[doc_id]["fm"]
        links = fm.get("links") or {}
        parent = links.get("parent")
        if parent and parent in docs:
            lines.append(f"  {node_name(parent)} --> {node_name(doc_id)}")
        for child in links.get("children") or []:
            if child in docs:
                lines.append(f"  {node_name(doc_id)} --> {node_name(child)}")
        for related in links.get("related") or []:
            if related in docs:
                lines.append(f"  {node_name(doc_id)} -. related .-> {node_name(related)}")

    lines += ["```", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = METHOD_ROOT / "graph.md"
    generated = generate()
    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != generated:
            print("GRAPH OUTDATED: method/graph.md differs from generated graph.")
            print("Run: python method/tools/generate_graph.py")
            return 1
        print("Method graph is up to date.")
        return 0
    target.write_text(generated, encoding="utf-8")
    print(f"Generated {target.relative_to(METHOD_ROOT.parent)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
