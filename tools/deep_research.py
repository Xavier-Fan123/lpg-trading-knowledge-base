#!/usr/bin/env python3
"""
Deep Research Tool: Run GPT-Researcher to produce a research report,
then save it (and its source texts) to 00_Inbox/sources/ for miner.py.

Usage:
  python tools/deep_research.py "CTO MTO propylene cost curve China"
  python tools/deep_research.py "query" --mine              # auto-run miner after
  python tools/deep_research.py "query" --report-type outline_report
  python tools/deep_research.py --list                      # past sessions

Environment:
  TAVILY_API_KEY and ANTHROPIC_API_KEY in .env (vault root) or env vars.
  SMART_LLM / FAST_LLM / STRATEGIC_LLM for model selection.
"""
import os
import sys
import json
import asyncio
import hashlib
import argparse
from pathlib import Path
from datetime import datetime

VAULT = Path(r"C:\Users\chenx\Desktop\my_knowledge_base")
SOURCES_DIR = VAULT / "00_Inbox" / "sources"
SOURCES_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = VAULT / "00_Inbox" / ".deep_research_log.json"


def load_env():
    """Load .env vars into os.environ."""
    env_file = VAULT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and k not in os.environ:
                    os.environ[k] = v


def make_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()[:8]


def load_log():
    if LOG_FILE.exists():
        return json.loads(LOG_FILE.read_text(encoding="utf-8"))
    return []


def save_log(log):
    LOG_FILE.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")


async def run_research(query: str, report_type: str = "research_report"):
    """Execute GPT-Researcher and return the report + sources."""
    from gpt_researcher import GPTResearcher

    print(f"\n{'='*60}")
    print(f"  Deep Research: \"{query}\"")
    print(f"  Report type: {report_type}")
    print(f"{'='*60}\n")

    researcher = GPTResearcher(query=query, report_type=report_type)

    print("  [1/3] Conducting research (searching + analyzing)...")
    report = await researcher.conduct_research()

    print("  [2/3] Writing report...")
    report_text = await researcher.write_report()

    # Get sources used
    sources = researcher.get_source_urls() if hasattr(researcher, 'get_source_urls') else []
    research_context = researcher.get_research_context() if hasattr(researcher, 'get_research_context') else ""

    return report_text, sources, research_context


def save_results(query: str, report_text: str, sources: list, context: str):
    """Save report and context to 00_Inbox/sources/."""
    saved_files = []
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Save the main report
    report_hash = make_hash(f"report_{query}_{ts}")
    report_file = SOURCES_DIR / f"{report_hash}.txt"
    header = (
        f"# Deep Research Report: {query}\n"
        f"# Generated: {ts}\n"
        f"# Tool: GPT-Researcher\n"
        f"# Sources: {len(sources)}\n\n"
    )
    report_file.write_text(header + report_text, encoding="utf-8")
    saved_files.append(report_file.name)
    print(f"\n  [3/3] Saved report → {report_file.name} ({len(report_text)/1024:.1f}KB)")

    # Save research context (raw source content) if substantial
    if context and len(context) > 500:
        ctx_hash = make_hash(f"context_{query}_{ts}")
        ctx_file = SOURCES_DIR / f"{ctx_hash}.txt"
        ctx_header = (
            f"# Research Context for: {query}\n"
            f"# Generated: {ts}\n"
            f"# Raw source content aggregated by GPT-Researcher\n\n"
        )
        ctx_file.write_text(ctx_header + str(context), encoding="utf-8")
        saved_files.append(ctx_file.name)
        print(f"  Saved context → {ctx_file.name} ({len(str(context))/1024:.1f}KB)")

    # Log session
    log = load_log()
    log.append({
        "query": query,
        "timestamp": datetime.now().isoformat(),
        "sources_found": len(sources),
        "source_urls": sources[:20],
        "files_saved": saved_files,
    })
    save_log(log)

    print(f"\n  Sources used: {len(sources)}")
    for url in sources[:10]:
        print(f"    - {url}")
    if len(sources) > 10:
        print(f"    ... and {len(sources)-10} more")

    print(f"\n  Saved {len(saved_files)} files to 00_Inbox/sources/")
    print(f"  Next: python tools/miner.py --run --limit {len(saved_files)}")

    return saved_files


def list_sessions():
    """Show past research sessions."""
    log = load_log()
    if not log:
        print("No research sessions found.")
        return
    print(f"\n{'='*60}")
    print(f"  Past Research Sessions ({len(log)} total)")
    print(f"{'='*60}")
    for entry in log[-15:]:
        ts = entry.get("timestamp", "?")[:16]
        q = entry.get("query", "?")[:50]
        n = len(entry.get("files_saved", []))
        s = entry.get("sources_found", "?")
        print(f"  [{ts}] \"{q}\" → {n} files ({s} sources)")


def main():
    parser = argparse.ArgumentParser(description="Deep Research for LPG Knowledge Base")
    parser.add_argument("query", nargs="?", help="Research query")
    parser.add_argument("--report-type", default="research_report",
                        choices=["research_report", "outline_report", "detailed_report",
                                 "resource_report"],
                        help="Report type (default: research_report)")
    parser.add_argument("--mine", action="store_true",
                        help="Auto-run miner.py after saving results")
    parser.add_argument("--list", action="store_true", help="List past sessions")
    args = parser.parse_args()

    if args.list:
        list_sessions()
        return

    if not args.query:
        parser.print_help()
        return

    load_env()

    # Check keys
    if not os.environ.get("TAVILY_API_KEY"):
        print("ERROR: TAVILY_API_KEY not set. Add to .env or environment.")
        sys.exit(1)

    # Run research
    report_text, sources, context = asyncio.run(
        run_research(args.query, args.report_type)
    )

    # Save
    saved = save_results(args.query, report_text, sources, context)

    # Optionally run miner
    if args.mine and saved:
        import subprocess
        python = sys.executable
        miner = str(VAULT / "tools" / "miner.py")
        print(f"\n  Running miner on {len(saved)} new sources...")
        subprocess.run(
            [python, miner, "--run", "--limit", str(len(saved))],
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )


if __name__ == "__main__":
    main()
