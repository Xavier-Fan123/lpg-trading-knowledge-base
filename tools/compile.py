#!/usr/bin/env python3
"""
Incremental Compilation Pipeline: Process raw data in 00_Inbox/ into structured wiki notes.
Usage:
  python compile.py                    # scan and list unprocessed files
  python compile.py --process          # generate note templates for unprocessed files
  python compile.py --process --auto   # auto-compile (uses heuristic classification)
"""
import os
import re
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

VAULT = Path(r"C:\Users\chenx\Desktop\my_knowledge_base")
INBOX = VAULT / "00_Inbox"
PROCESSED_LOG = INBOX / ".processed.json"

TARGET_DIRS = {
    "market": "20_Market_Fundamentals",
    "supply": "20_Market_Fundamentals",
    "demand": "20_Market_Fundamentals",
    "price": "21_Pricing_and_Valuation",
    "pricing": "21_Pricing_and_Valuation",
    "benchmark": "21_Pricing_and_Valuation",
    "hedging": "21_Pricing_and_Valuation",
    "spread": "21_Pricing_and_Valuation",
    "valuation": "21_Pricing_and_Valuation",
    "freight": "22_Physical_Logistics",
    "shipping": "22_Physical_Logistics",
    "vessel": "22_Physical_Logistics",
    "terminal": "22_Physical_Logistics",
    "logistics": "22_Physical_Logistics",
    "demurrage": "22_Physical_Logistics",
    "incoterm": "22_Physical_Logistics",
    "arbitrage": "30_Trading_Strategies",
    "strategy": "30_Trading_Strategies",
    "trading": "30_Trading_Strategies",
    "company": "40_Entities",
    "entity": "40_Entities",
    "exchange": "40_Entities",
    "aramco": "40_Entities",
    "platts": "40_Entities",
}

CONCEPT_TEMPLATE = """---
aliases: []
tags: [{tags}]
date: {date}
status: seed
source_file: {source}
---

# {title}

> Compiled from `{source}` on {date}

---

## Key Points

{summary}

## Empirical Facts vs Analytical Assumptions

### Empirical Facts (verifiable)
- [ ] TODO: Extract from source

### Analytical Assumptions (interpretive)
- [ ] TODO: Extract from source

## Scenario Analysis

| Scenario | Condition | Outcome |
|----------|-----------|---------|
| Base     |           |         |
| Bull     |           |         |
| Bear     |           |         |
| Invalidation |       |         |

## Downside Risks

- [ ] TODO: Identify and WikiLink risks

---
*Source: `{source}`*
"""

ENTITY_TEMPLATE = """---
aliases: []
tags: [entity, {tags}]
date: {date}
status: seed
source_file: {source}
---

# {title}

> Compiled from `{source}` on {date}

---

## Overview

{summary}

## Key Data Points

- [ ] TODO: Extract from source

## Associated Risks

| Risk Category | Description | WikiLink |
|---------------|-------------|----------|
|               |             |          |

---
*Source: `{source}`*
"""


def load_processed_log():
    """Load the log of already-processed files."""
    if PROCESSED_LOG.exists():
        return json.loads(PROCESSED_LOG.read_text(encoding="utf-8"))
    return {"processed": [], "skipped": []}


def save_processed_log(log):
    """Save the processed file log."""
    PROCESSED_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")


def classify_content(text, filename=""):
    """Heuristic classification of content into target directory."""
    text_lower = (text + " " + filename).lower()
    scores = defaultdict(int)
    for keyword, target_dir in TARGET_DIRS.items():
        count = text_lower.count(keyword)
        if count > 0:
            scores[target_dir] += count
    if not scores:
        return "20_Market_Fundamentals"  # default
    return max(scores, key=scores.get)


def extract_title(text, filename):
    """Extract a title from content or filename."""
    # Try first heading
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Try first non-empty line
    for line in text.split("\n"):
        line = line.strip()
        if line and len(line) > 5 and len(line) < 200:
            return line[:80]
    # Fall back to filename
    return filename.replace("_", " ").replace("-", " ").rsplit(".", 1)[0]


def extract_summary(text, max_lines=10):
    """Extract first meaningful lines as summary."""
    lines = []
    in_yaml = False
    for line in text.split("\n"):
        if line.strip() == "---":
            in_yaml = not in_yaml
            continue
        if in_yaml:
            continue
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
            if len(lines) >= max_lines:
                break
    return "\n".join(lines) if lines else "(No summary extracted)"


def sanitize_filename(title, max_len=80):
    """Clean title for use as filename."""
    clean = re.sub(r'[<>:"/\\|?*]', '', title)
    clean = re.sub(r'\s+', '_', clean.strip())
    return clean[:max_len]


def scan_inbox():
    """Scan 00_Inbox for unprocessed files."""
    log = load_processed_log()
    processed_set = set(log["processed"])

    unprocessed = []

    # Scan raw notes
    notes_dir = INBOX / "notes"
    if notes_dir.exists():
        for f in notes_dir.glob("*.md"):
            if str(f) not in processed_set:
                unprocessed.append(("note", f))

    # Scan web clips
    clips_dir = INBOX / "web_clips"
    if clips_dir.exists():
        for f in clips_dir.glob("*.md"):
            if str(f) not in processed_set:
                unprocessed.append(("clip", f))

    # Scan source texts (only .txt with substantial content)
    sources_dir = INBOX / "sources"
    if sources_dir.exists():
        for f in sources_dir.glob("*.txt"):
            if str(f) not in processed_set and f.stat().st_size > 500:
                unprocessed.append(("source", f))

    return unprocessed


def compile_file(file_type, filepath, auto=False):
    """Compile a raw file into a structured note template."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    title = extract_title(content, filepath.name)
    summary = extract_summary(content)
    target_dir = classify_content(content, filepath.name)
    date = datetime.now().strftime("%Y-%m-%d")

    is_entity = target_dir == "40_Entities"
    template = ENTITY_TEMPLATE if is_entity else CONCEPT_TEMPLATE
    tags = "entity" if is_entity else "concept"

    note_content = template.format(
        title=title,
        tags=tags,
        date=date,
        source=filepath.name,
        summary=summary,
    )

    slug = sanitize_filename(title)
    out_dir = VAULT / target_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    outfile = out_dir / f"{slug}.md"

    # Avoid overwriting existing notes
    if outfile.exists():
        outfile = out_dir / f"{slug}_{datetime.now().strftime('%H%M%S')}.md"

    return {
        "source": filepath,
        "target": outfile,
        "target_dir": target_dir,
        "title": title,
        "content": note_content,
        "file_type": file_type,
    }


def process_files(unprocessed, auto=False, dry_run=False):
    """Process unprocessed files and generate note templates."""
    log = load_processed_log()
    results = []

    for file_type, filepath in unprocessed:
        try:
            compiled = compile_file(file_type, filepath, auto=auto)
            if not dry_run:
                compiled["target"].write_text(compiled["content"], encoding="utf-8")
                log["processed"].append(str(filepath))
            results.append({
                "status": "OK" if not dry_run else "DRY_RUN",
                "source": str(filepath.name),
                "target": str(compiled["target"].relative_to(VAULT)),
                "title": compiled["title"],
            })
        except Exception as e:
            results.append({
                "status": "FAIL",
                "source": str(filepath.name),
                "error": str(e),
            })

    if not dry_run:
        save_processed_log(log)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Incremental compilation pipeline")
    parser.add_argument("--process", action="store_true", help="Process unprocessed files")
    parser.add_argument("--auto", action="store_true", help="Auto-classify and compile")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--reset", action="store_true", help="Reset processed log")
    args = parser.parse_args()

    if args.reset:
        if PROCESSED_LOG.exists():
            PROCESSED_LOG.unlink()
        print("Processed log reset.")
        sys.exit(0)

    print("Scanning 00_Inbox/ for unprocessed files...")
    unprocessed = scan_inbox()

    if not unprocessed:
        print("All files have been processed. Nothing to do.")
        sys.exit(0)

    print(f"\nFound {len(unprocessed)} unprocessed files:")
    by_type = defaultdict(int)
    for ft, fp in unprocessed:
        by_type[ft] += 1
    for ft, count in sorted(by_type.items()):
        print(f"  {ft}: {count}")

    if not args.process:
        print("\nRun with --process to compile them.")
        print("  --dry-run  Preview without writing")
        print("  --auto     Auto-classify content")
        sys.exit(0)

    results = process_files(unprocessed, auto=args.auto, dry_run=args.dry_run)

    ok = sum(1 for r in results if r["status"] in ("OK", "DRY_RUN"))
    fail = sum(1 for r in results if r["status"] == "FAIL")
    print(f"\nResults: {ok} compiled, {fail} failed")
    for r in results[:20]:
        status = r["status"]
        if status == "FAIL":
            print(f"  FAIL: {r['source']} — {r.get('error', '?')}")
        else:
            print(f"  {status}: {r['source']} → {r.get('target', '?')}")
    if len(results) > 20:
        print(f"  ... and {len(results)-20} more")
