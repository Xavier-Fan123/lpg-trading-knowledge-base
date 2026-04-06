#!/usr/bin/env python3
"""Batch download all NotebookLM source full texts."""
import subprocess
import json
import re
import os
import sys
import time

OUTDIR = r"C:\Users\chenx\Desktop\my_knowledge_base\00_Inbox\sources"
os.makedirs(OUTDIR, exist_ok=True)

# Step 1: Get source list as raw text and extract IDs
print("Fetching source list...")
result = subprocess.run(
    ["notebooklm", "source", "list"],
    capture_output=True, text=True, encoding="utf-8", errors="replace"
)

# Extract all partial UUIDs (8-char prefix with dash pattern)
# The table shows IDs like "75ab983d-bfe4-…"
raw = result.stdout + result.stderr
id_pattern = re.compile(r'([0-9a-f]{8}-[0-9a-f]{4}-)')
matches = id_pattern.findall(raw)
# Deduplicate while preserving order, use first 8 chars as partial ID
seen = set()
source_ids = []
for m in matches:
    prefix = m[:8]
    if prefix not in seen:
        seen.add(prefix)
        source_ids.append(prefix)

print(f"Found {len(source_ids)} sources")

# Step 2: Download each source fulltext
success = 0
failed = 0
for i, sid in enumerate(source_ids):
    outfile = os.path.join(OUTDIR, f"{sid}.txt")
    if os.path.exists(outfile) and os.path.getsize(outfile) > 0:
        print(f"[{i+1}/{len(source_ids)}] SKIP {sid} (already exists)")
        success += 1
        continue

    print(f"[{i+1}/{len(source_ids)}] Downloading {sid}...")
    try:
        r = subprocess.run(
            ["notebooklm", "source", "fulltext", sid, "-o", outfile],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=60
        )
        if r.returncode == 0 and os.path.exists(outfile) and os.path.getsize(outfile) > 0:
            size = os.path.getsize(outfile)
            print(f"  OK ({size} bytes)")
            success += 1
        else:
            print(f"  FAILED: {r.stderr[:200] if r.stderr else 'empty output'}")
            failed += 1
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT")
        failed += 1
    except Exception as e:
        print(f"  ERROR: {e}")
        failed += 1

print(f"\nDone: {success} success, {failed} failed, {len(source_ids)} total")
