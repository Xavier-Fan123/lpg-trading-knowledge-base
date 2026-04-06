#!/usr/bin/env python3
"""
Web Clipper: Fetch any URL via agent-browser, extract text, save as Markdown to 00_Inbox/sources/.
Usage: python web_clip.py <url> [--title "Custom Title"]
"""
import subprocess
import sys
import os
import re
import json
import hashlib
from datetime import datetime
from pathlib import Path

VAULT = Path(r"C:\Users\chenx\Desktop\my_knowledge_base")
INBOX = VAULT / "00_Inbox" / "web_clips"
INBOX.mkdir(parents=True, exist_ok=True)


def sanitize_filename(title: str, max_len: int = 80) -> str:
    """Clean title for use as filename."""
    clean = re.sub(r'[<>:"/\\|?*]', '', title)
    clean = re.sub(r'\s+', '_', clean.strip())
    return clean[:max_len]


def clip_url(url: str, custom_title: str = None) -> Path:
    """Fetch URL content via agent-browser and save as markdown."""
    print(f"Opening: {url}")

    # Open the URL
    subprocess.run(
        ["agent-browser", "open", url],
        capture_output=True, text=True, timeout=30
    )

    # Wait for page to load
    subprocess.run(
        ["agent-browser", "wait", "3000"],
        capture_output=True, text=True, timeout=10
    )

    # Get page title
    title_result = subprocess.run(
        ["agent-browser", "get", "title"],
        capture_output=True, text=True, timeout=10
    )
    page_title = title_result.stdout.strip() or "Untitled"
    if custom_title:
        page_title = custom_title

    # Get full page text
    text_result = subprocess.run(
        ["agent-browser", "get", "text", "body"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30
    )
    body_text = text_result.stdout.strip()

    # Get page URL (in case of redirects)
    url_result = subprocess.run(
        ["agent-browser", "get", "url"],
        capture_output=True, text=True, timeout=10
    )
    final_url = url_result.stdout.strip() or url

    # Take screenshot
    screenshot_dir = INBOX / "screenshots"
    screenshot_dir.mkdir(exist_ok=True)
    slug = sanitize_filename(page_title)
    screenshot_path = screenshot_dir / f"{slug}.png"
    subprocess.run(
        ["agent-browser", "screenshot", str(screenshot_path)],
        capture_output=True, text=True, timeout=15
    )

    # Build markdown
    now = datetime.now().strftime("%Y-%m-%d")
    md_content = f"""---
aliases: []
tags: [raw-clip, web-source]
date: {now}
source_url: {final_url}
status: seed
clip_method: agent-browser
---

# {page_title}

> Clipped from [{final_url}]({final_url}) on {now}

---

{body_text}

---
*Screenshot: [[{screenshot_path.name}]]*
"""

    # Save
    outfile = INBOX / f"{slug}.md"
    outfile.write_text(md_content, encoding="utf-8")
    print(f"Saved: {outfile}")
    print(f"Screenshot: {screenshot_path}")
    print(f"Title: {page_title}")
    print(f"Content: {len(body_text)} chars")

    # Close browser
    subprocess.run(
        ["agent-browser", "close"],
        capture_output=True, text=True, timeout=10
    )

    return outfile


def batch_clip(urls: list):
    """Clip multiple URLs."""
    results = []
    for url in urls:
        try:
            path = clip_url(url)
            results.append((url, str(path), "OK"))
        except Exception as e:
            results.append((url, "", str(e)))
            print(f"  FAILED: {e}")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_clip.py <url> [--title 'Custom Title']")
        print("       python web_clip.py --batch urls.txt")
        sys.exit(1)

    if sys.argv[1] == "--batch":
        urls_file = sys.argv[2]
        with open(urls_file) as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        results = batch_clip(urls)
        print(f"\nBatch complete: {sum(1 for r in results if r[2]=='OK')}/{len(results)} success")
    else:
        url = sys.argv[1]
        title = None
        if "--title" in sys.argv:
            idx = sys.argv.index("--title")
            title = sys.argv[idx + 1]
        clip_url(url, title)
