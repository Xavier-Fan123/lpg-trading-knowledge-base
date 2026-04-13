#!/usr/bin/env python3
"""
Q&A Filing Tool: Save Q&A outputs back into the wiki.
Usage:
  python qa_file.py --question "What drives PDH margins?" --answer "Three factors..."
  python qa_file.py --interactive
  python qa_file.py --question "..." --answer "..." --target Chinese_PDH_Margin
"""
import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

VAULT = Path(r"C:\Users\itg\Desktop\lpg-trading-knowledge-base")

SCAN_DIRS = [
    "10_Atlas",
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]

QA_LOG = VAULT / "00_Inbox" / "qa_log.md"


def load_notes():
    """Load all note names and content for matching."""
    notes = {}
    for d in SCAN_DIRS:
        dirpath = VAULT / d
        if not dirpath.exists():
            continue
        for f in dirpath.glob("*.md"):
            content = f.read_text(encoding="utf-8", errors="replace")
            notes[f.stem] = {
                "path": f,
                "content": content,
                "title": f.stem.replace("_", " "),
                "dir": d,
            }
    return notes


def find_best_target(question, answer, notes):
    """Find the most relevant note for this Q&A pair."""
    text = (question + " " + answer).lower()
    scores = {}
    for stem, note in notes.items():
        score = 0
        title_lower = note["title"].lower()
        # Title word overlap
        for word in title_lower.split():
            if len(word) > 3 and word in text:
                score += 10
        # Content keyword overlap (sample first 500 chars of Q&A against note)
        note_lower = note["content"].lower()
        for word in text.split():
            if len(word) > 4 and word in note_lower:
                score += 1
        scores[stem] = score

    if not scores:
        return None
    best = max(scores, key=scores.get)
    if scores[best] < 5:
        return None  # No confident match
    return best


def append_qa_to_note(note_path, question, answer):
    """Append a Q&A section to an existing note."""
    content = note_path.read_text(encoding="utf-8", errors="replace")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    qa_block = f"""

## Q&A ({date})

**Q:** {question}

**A:** {answer}
"""
    # Insert before the last --- divider if it exists, otherwise append
    if content.rstrip().endswith("---"):
        # Insert before final ---
        last_hr = content.rstrip().rfind("---")
        if last_hr > 10:  # Not the YAML frontmatter
            new_content = content[:last_hr].rstrip() + "\n" + qa_block + "\n---\n"
        else:
            new_content = content + qa_block
    else:
        new_content = content + qa_block

    note_path.write_text(new_content, encoding="utf-8")
    return True


def log_qa(question, answer, target_note):
    """Append to the Q&A log file."""
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n### {date}\n- **Target**: [[{target_note}]]\n- **Q**: {question}\n- **A**: {answer}\n"

    if not QA_LOG.exists():
        header = "---\ntags: [qa-log]\ndate: {}\nstatus: evergreen\n---\n\n# Q&A Log\n\n".format(
            datetime.now().strftime("%Y-%m-%d")
        )
        QA_LOG.write_text(header + entry, encoding="utf-8")
    else:
        with open(QA_LOG, "a", encoding="utf-8") as f:
            f.write(entry)


def file_qa(question, answer, target_stem=None):
    """File a Q&A pair into the wiki."""
    notes = load_notes()

    if target_stem:
        # Normalize: try exact match, then underscore/space variants
        if target_stem in notes:
            target = target_stem
        else:
            normalized = target_stem.replace(" ", "_")
            if normalized in notes:
                target = normalized
            else:
                # Fuzzy: find closest
                target_lower = target_stem.lower().replace("_", " ")
                for stem in notes:
                    if stem.lower().replace("_", " ") == target_lower:
                        target = stem
                        break
                else:
                    print(f"Note not found: {target_stem}")
                    return False
    else:
        target = find_best_target(question, answer, notes)
        if not target:
            print("Could not determine target note. Use --target to specify.")
            return False

    note = notes[target]
    append_qa_to_note(note["path"], question, answer)
    log_qa(question, answer, target)
    print(f"Filed Q&A to: {note['dir']}/{note['path'].name}")
    return True


def interactive_mode():
    """Interactive Q&A filing."""
    notes = load_notes()
    print(f"Q&A Filing Tool — {len(notes)} notes loaded")
    print("Type 'q' to quit\n")

    while True:
        try:
            question = input("Question: ").strip()
            if question.lower() in ("q", "quit", "exit"):
                break
            answer = input("Answer: ").strip()
            if not question or not answer:
                print("Both question and answer required.\n")
                continue

            target = find_best_target(question, answer, notes)
            if target:
                print(f"  Best match: {target.replace('_', ' ')}")
                confirm = input(f"  File to [[{target}]]? (y/n/other): ").strip()
                if confirm.lower() == "n":
                    target_input = input("  Target note name: ").strip()
                    if target_input:
                        file_qa(question, answer, target_stem=target_input)
                    else:
                        print("  Skipped.\n")
                elif confirm.lower() == "y" or confirm == "":
                    file_qa(question, answer, target_stem=target)
                else:
                    file_qa(question, answer, target_stem=confirm)
            else:
                print("  No confident match found.")
                target_input = input("  Target note name: ").strip()
                if target_input:
                    file_qa(question, answer, target_stem=target_input)
            print()
        except (EOFError, KeyboardInterrupt):
            break

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Q&A into the wiki")
    parser.add_argument("--question", "-q", help="The question")
    parser.add_argument("--answer", "-a", help="The answer")
    parser.add_argument("--target", "-t", help="Target note name")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    args = parser.parse_args()

    if args.interactive or (not args.question and not args.answer):
        interactive_mode()
    elif args.question and args.answer:
        file_qa(args.question, args.answer, target_stem=args.target)
    else:
        print("Provide both --question and --answer, or use --interactive")
        sys.exit(1)
