#!/usr/bin/env python3
"""
Marp Slide Generator: Create presentation slides from wiki notes.
Usage:
  python slides.py --topic "LPG Market Overview"
  python slides.py --notes "LPG_Market_Fundamentals,Chinese_PDH_Margin"
  python slides.py --notes "VLGC_Freight_Dynamics" --output freight_deck.md
  python slides.py --all-strategies    # all trading strategy notes
"""
import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

VAULT = Path(r"C:\Users\itg\Desktop\lpg-trading-knowledge-base")
OUTPUT_DIR = VAULT / "50_Outputs" / "slides"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SCAN_DIRS = [
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]

MARP_HEADER = """---
marp: true
theme: default
paginate: true
header: "{title}"
footer: "LPG Trading Knowledge Base | {date}"
style: |
  section {{
    font-size: 24px;
  }}
  h1 {{
    color: #1a5276;
  }}
  h2 {{
    color: #2874a6;
  }}
  table {{
    font-size: 18px;
  }}
  blockquote {{
    border-left: 4px solid #2874a6;
    padding-left: 16px;
    color: #555;
  }}
---

# {title}

**{date}** | LPG Trading Knowledge Base

---

"""


def load_note(name):
    """Load a note by stem name (with or without underscores)."""
    normalized = name.replace(" ", "_")
    for d in SCAN_DIRS:
        path = VAULT / d / f"{normalized}.md"
        if path.exists():
            return path.read_text(encoding="utf-8", errors="replace"), path
    # Also check 10_Atlas
    path = VAULT / "10_Atlas" / f"{normalized}.md"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace"), path
    return None, None


def extract_sections(content):
    """Extract h2 sections from markdown content."""
    sections = []
    current_heading = None
    current_body = []

    # Skip YAML frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]

    for line in content.split("\n"):
        if line.startswith("## "):
            if current_heading:
                sections.append((current_heading, "\n".join(current_body).strip()))
            current_heading = line[3:].strip()
            current_body = []
        elif current_heading:
            current_body.append(line)

    if current_heading:
        sections.append((current_heading, "\n".join(current_body).strip()))

    return sections


def section_to_slide(heading, body, max_lines=15):
    """Convert a section into a Marp slide."""
    lines = body.split("\n")

    # If the body is a table, keep it intact
    if any("|" in line and "---" in line for line in lines):
        # Table slide
        table_lines = [l for l in lines if l.strip()]
        return f"## {heading}\n\n" + "\n".join(table_lines[:max_lines + 2])

    # For regular content, trim to max_lines
    content_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip TODOs and empty checkboxes
        if stripped.startswith("- [ ] TODO"):
            continue
        content_lines.append(line)
        if len(content_lines) >= max_lines:
            break

    return f"## {heading}\n\n" + "\n".join(content_lines)


def note_to_slides(name):
    """Convert a single note into slide pages."""
    content, path = load_note(name)
    if content is None:
        print(f"  Warning: Note '{name}' not found, skipping")
        return []

    # Extract title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else name.replace("_", " ")

    slides = []
    # Title slide for this note
    slides.append(f"## {title}\n\n*Source: {path.parent.name}/{path.name}*")

    # Section slides
    sections = extract_sections(content)
    skip_sections = {"q&a", "source"}  # Skip non-presentation sections
    for heading, body in sections:
        if heading.lower().split("(")[0].strip() in skip_sections:
            continue
        if not body.strip():
            continue
        slide = section_to_slide(heading, body)
        slides.append(slide)

    return slides


def generate_deck(title, note_names, output_path=None):
    """Generate a complete Marp slide deck from multiple notes."""
    date = datetime.now().strftime("%Y-%m-%d")
    deck = MARP_HEADER.format(title=title, date=date)

    for name in note_names:
        slides = note_to_slides(name)
        for slide in slides:
            deck += slide + "\n\n---\n\n"

    # Closing slide
    deck += "# Thank You\n\n"
    deck += f"Generated from the LPG Trading Knowledge Base\n\n"
    deck += f"**{len(note_names)} notes** | {date}\n"

    if output_path is None:
        slug = re.sub(r'[^a-zA-Z0-9]+', '_', title)[:60]
        output_path = OUTPUT_DIR / f"{slug}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(deck, encoding="utf-8")
    return output_path


def find_notes_by_dir(dir_name):
    """Find all notes in a directory."""
    dirpath = VAULT / dir_name
    if not dirpath.exists():
        return []
    return [f.stem for f in dirpath.glob("*.md")]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Marp slides from wiki notes")
    parser.add_argument("--topic", help="Slide deck title/topic")
    parser.add_argument("--notes", help="Comma-separated note names")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--all-market", action="store_true", help="All market fundamentals notes")
    parser.add_argument("--all-pricing", action="store_true", help="All pricing notes")
    parser.add_argument("--all-logistics", action="store_true", help="All logistics notes")
    parser.add_argument("--all-strategies", action="store_true", help="All strategy notes")
    parser.add_argument("--all-entities", action="store_true", help="All entity notes")
    parser.add_argument("--all", action="store_true", help="All notes")
    args = parser.parse_args()

    note_names = []
    topic = args.topic or "LPG Trading Knowledge Base"

    if args.notes:
        note_names = [n.strip() for n in args.notes.split(",")]
        if not args.topic:
            topic = note_names[0].replace("_", " ") if len(note_names) == 1 else "Selected Topics"

    if args.all_market:
        note_names += find_notes_by_dir("20_Market_Fundamentals")
        topic = topic if args.topic else "LPG Market Fundamentals"
    if args.all_pricing:
        note_names += find_notes_by_dir("21_Pricing_and_Valuation")
        topic = topic if args.topic else "LPG Pricing & Valuation"
    if args.all_logistics:
        note_names += find_notes_by_dir("22_Physical_Logistics")
        topic = topic if args.topic else "Physical Logistics & Freight"
    if args.all_strategies:
        note_names += find_notes_by_dir("30_Trading_Strategies")
        topic = topic if args.topic else "Trading Strategies"
    if args.all_entities:
        note_names += find_notes_by_dir("40_Entities")
        topic = topic if args.topic else "Key Entities & Infrastructure"
    if args.all:
        for d in SCAN_DIRS:
            note_names += find_notes_by_dir(d)
        topic = topic if args.topic else "LPG Trading — Complete Overview"

    if not note_names:
        print("No notes specified. Use --notes, --all, or --all-<category>")
        print("\nExamples:")
        print('  python slides.py --notes "LPG_Market_Fundamentals,Chinese_PDH_Margin"')
        print('  python slides.py --all-market --topic "Q2 Market Briefing"')
        print('  python slides.py --all --topic "LPG Trading Overview"')
        sys.exit(1)

    output_path = Path(args.output) if args.output else None
    result = generate_deck(topic, note_names, output_path)
    print(f"Generated: {result}")
    print(f"Notes: {len(note_names)}")
    print(f"\nTo render: npx @marp-team/marp-cli {result} --html --pdf")
