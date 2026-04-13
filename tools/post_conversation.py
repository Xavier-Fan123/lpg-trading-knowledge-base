#!/usr/bin/env python3
"""
Claude Code Stop Hook: Detect knowledge gaps from conversations.

Runs after each Claude response. Parses the conversation transcript,
checks if the assistant flagged any knowledge gaps, and logs them
to 00_Inbox/knowledge_gaps.md.

Receives JSON on stdin: {"transcript_path": "...", "session_id": "...", ...}
"""
import json
import sys
import re
from pathlib import Path
from datetime import datetime

VAULT = Path(__file__).resolve().parent.parent
GAPS_FILE = VAULT / "00_Inbox" / "knowledge_gaps.md"

# Phrases that indicate a knowledge gap was mentioned in the response
GAP_INDICATORS = [
    "not yet in kb",
    "not currently in the kb",
    "not covered in the kb",
    "no results found",
    "no matching wiki note",
    "outside the knowledge base",
    "not currently covered",
    "the kb doesn't currently have",
    "the kb lacks",
    "knowledge base doesn't cover",
    "no wiki notes",
    "not in the knowledge base",
]


def ensure_gaps_file():
    """Create knowledge_gaps.md if it doesn't exist."""
    if not GAPS_FILE.exists():
        header = (
            "---\n"
            "tags: [knowledge-gaps, automated]\n"
            f"date: {datetime.now().strftime('%Y-%m-%d')}\n"
            "status: evergreen\n"
            "---\n\n"
            "# Knowledge Gaps Log\n\n"
            "> Auto-detected gaps from conversations. Review periodically and create/enrich notes.\n\n"
            "---\n"
        )
        GAPS_FILE.write_text(header, encoding="utf-8")


def extract_last_exchange(transcript_path):
    """Parse JSONL transcript and extract the last user question + assistant response."""
    lines = Path(transcript_path).read_text(encoding="utf-8", errors="replace").strip().split("\n")

    last_user = None
    last_assistant = None

    for line in lines:
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue

        role = entry.get("role", "")
        if role == "user":
            # Extract text content
            content = entry.get("content", "")
            if isinstance(content, list):
                content = " ".join(
                    block.get("text", "") for block in content
                    if isinstance(block, dict) and block.get("type") == "text"
                )
            if content.strip():
                last_user = content.strip()
        elif role == "assistant":
            content = entry.get("content", "")
            if isinstance(content, list):
                content = " ".join(
                    block.get("text", "") for block in content
                    if isinstance(block, dict) and block.get("type") == "text"
                )
            if content.strip():
                last_assistant = content.strip()

    return last_user, last_assistant


def check_for_gaps(assistant_text):
    """Check if the assistant response mentions knowledge gaps."""
    text_lower = assistant_text.lower()
    for indicator in GAP_INDICATORS:
        if indicator in text_lower:
            return indicator
    return None


def log_gap(question, indicator):
    """Append a gap entry to knowledge_gaps.md."""
    ensure_gaps_file()

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    # Truncate long questions
    q_short = question[:200] + "..." if len(question) > 200 else question

    entry = (
        f"\n### {date} -- Auto-detected gap\n"
        f"- Question: {q_short}\n"
        f"- Indicator: \"{indicator}\"\n"
        f"- Suggested action: Create or enrich relevant note\n"
        f"- Priority: medium\n"
    )

    with open(GAPS_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    try:
        hook_input = sys.stdin.read()
        if not hook_input.strip():
            sys.exit(0)

        data = json.loads(hook_input)
        transcript_path = data.get("transcript_path", "")

        if not transcript_path or not Path(transcript_path).exists():
            sys.exit(0)

        last_user, last_assistant = extract_last_exchange(transcript_path)

        if not last_user or not last_assistant:
            sys.exit(0)

        gap = check_for_gaps(last_assistant)
        if gap:
            log_gap(last_user, gap)

    except Exception:
        pass  # Never block the user experience

    sys.exit(0)


if __name__ == "__main__":
    main()
