#!/usr/bin/env python3
"""
Wiki Search Engine: Full-text search over the knowledge base.
Usage:
  python search.py "PDH margin"              # keyword search
  python search.py --tag risk                 # filter by tag
  python search.py "freight" --dir 22_Physical_Logistics
  python search.py "arbitrage" --top 5
"""
import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

VAULT = Path(r"C:\Users\chenx\Desktop\my_knowledge_base")

SCAN_DIRS = [
    "10_Atlas",
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]


def parse_yaml(content):
    """Extract YAML frontmatter fields."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fields = {}
    for line in content[3:end].strip().split("\n"):
        if ":" in line:
            key = line.split(":")[0].strip()
            val = line.split(":", 1)[1].strip()
            fields[key] = val
    return fields


def load_notes(scan_dirs=None, vault=None):
    """Load all markdown notes from scan directories."""
    vault = vault or VAULT
    dirs = scan_dirs or SCAN_DIRS
    notes = []
    for d in dirs:
        dirpath = vault / d
        if not dirpath.exists():
            continue
        for f in dirpath.glob("*.md"):
            content = f.read_text(encoding="utf-8", errors="replace")
            yaml = parse_yaml(content)
            notes.append({
                "path": f,
                "stem": f.stem,
                "dir": d,
                "content": content,
                "yaml": yaml,
                "title": f.stem.replace("_", " "),
            })
    return notes


def search(query, notes, tag_filter=None, dir_filter=None, top_n=10):
    """Search notes by keyword with optional filters. Returns ranked results."""
    query_lower = query.lower()
    query_words = query_lower.split()
    results = []

    for note in notes:
        # Apply filters
        if tag_filter:
            tags_str = note["yaml"].get("tags", "")
            if tag_filter.lower() not in tags_str.lower():
                continue
        if dir_filter:
            if dir_filter.lower() not in note["dir"].lower():
                continue

        content_lower = note["content"].lower()
        title_lower = note["title"].lower()

        # Score: title match (high weight) + content frequency
        score = 0

        # Exact phrase match in title
        if query_lower in title_lower:
            score += 100

        # Exact phrase match in content
        phrase_count = content_lower.count(query_lower)
        score += phrase_count * 10

        # Individual word matches
        for word in query_words:
            if word in title_lower:
                score += 30
            word_count = content_lower.count(word)
            score += word_count * 2

        # YAML field matches (tags, aliases)
        for field in ["tags", "aliases"]:
            val = note["yaml"].get(field, "")
            if query_lower in val.lower():
                score += 50

        if score > 0:
            # Extract context snippet around first match
            idx = content_lower.find(query_lower)
            if idx == -1:
                # Try first word
                for w in query_words:
                    idx = content_lower.find(w)
                    if idx != -1:
                        break
            snippet = ""
            if idx != -1:
                start = max(0, idx - 60)
                end = min(len(note["content"]), idx + len(query) + 60)
                snippet = note["content"][start:end].replace("\n", " ").strip()
                if start > 0:
                    snippet = "..." + snippet
                if end < len(note["content"]):
                    snippet = snippet + "..."

            results.append({
                "path": note["path"],
                "title": note["title"],
                "dir": note["dir"],
                "score": score,
                "snippet": snippet,
                "status": note["yaml"].get("status", "?"),
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]


def print_results(results, query):
    """Pretty-print search results."""
    if not results:
        print(f"No results for: \"{query}\"")
        return

    print(f"\n{'='*60}")
    print(f"  Search: \"{query}\"  ({len(results)} results)")
    print(f"{'='*60}\n")

    for i, r in enumerate(results, 1):
        rel = f"{r['dir']}/{r['path'].name}"
        print(f"  {i}. [{r['status']}] {r['title']}")
        print(f"     {rel}  (score: {r['score']})")
        if r["snippet"]:
            print(f"     > {r['snippet']}")
        print()


def interactive_mode(notes):
    """Interactive search REPL."""
    print("Wiki Search Engine — type a query, or 'q' to quit")
    print("Filters: --tag <tag>, --dir <dir>, --top <n>\n")
    while True:
        try:
            raw = input("search> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw.lower() in ("q", "quit", "exit"):
            break
        # Parse inline flags
        tag = dir_f = None
        top_n = 10
        parts = raw.split("--")
        query = parts[0].strip()
        for part in parts[1:]:
            part = part.strip()
            if part.startswith("tag "):
                tag = part[4:].strip()
            elif part.startswith("dir "):
                dir_f = part[4:].strip()
            elif part.startswith("top "):
                try:
                    top_n = int(part[4:].strip())
                except ValueError:
                    pass
        if query:
            results = search(query, notes, tag_filter=tag, dir_filter=dir_f, top_n=top_n)
            print_results(results, query)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search the LPG knowledge base")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--dir", help="Filter by directory")
    parser.add_argument("--top", type=int, default=10, help="Number of results")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    args = parser.parse_args()

    notes = load_notes()
    print(f"Loaded {len(notes)} notes from {len(SCAN_DIRS)} directories")

    if args.interactive or not args.query:
        interactive_mode(notes)
    else:
        results = search(args.query, notes, tag_filter=args.tag, dir_filter=args.dir, top_n=args.top)
        print_results(results, args.query)
