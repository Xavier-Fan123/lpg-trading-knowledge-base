#!/usr/bin/env python3
"""
Source Text Miner: Map-Reduce extraction pipeline for 00_Inbox/sources/.

Architecture:
  1. MAP    — For each source file, call LLM to extract hard data only
  2. ROUTE  — Match extracted facts to existing wiki notes via keyword scoring
  3. REDUCE — Append validated facts to target notes under ## Mined Data section

Usage:
  python miner.py --scan                       # preview: list sources and estimated targets
  python miner.py --run --limit 5              # process first 5 unprocessed files
  python miner.py --run --limit 20             # process next 20
  python miner.py --run                        # process ALL remaining
  python miner.py --run --dry-run --limit 3    # extract but don't write to wiki
  python miner.py --status                     # show progress stats
  python miner.py --run --file 02a90cd2.txt    # process a specific file

Environment:
  ANTHROPIC_API_KEY must be set, or placed in .env file in vault root.
"""
import os
import re
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

VAULT = Path(r"C:\Users\itg\Desktop\lpg-trading-knowledge-base")
SOURCES_DIR = VAULT / "00_Inbox" / "sources"
PROGRESS_FILE = VAULT / "00_Inbox" / ".miner_progress.json"
EXTRACTS_DIR = VAULT / "00_Inbox" / "extracts"
EXTRACTS_DIR.mkdir(parents=True, exist_ok=True)

# Minimum file size to process (skip tiny/empty files)
MIN_FILE_SIZE = 500
# Maximum chars to send to LLM (truncate very large files)
MAX_INPUT_CHARS = 30000

# All target wiki notes
WIKI_DIRS = [
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]

# ─── Routing index: keywords → note stem ───────────────────────────────
# Built from Master_Index.md topic descriptions
ROUTING_INDEX = {
    "LPG_Market_Fundamentals": [
        "lpg market", "must-take production", "gas processing", "supply inelasticity",
        "propane butane", "global lpg", "lpg production", "lpg demand", "lpg supply",
        "ngl", "natural gas liquids", "refinery output", "fractionation",
        "us shale", "middle east production", "lpg trade flow",
    ],
    "Chinese_PDH_Margin": [
        "pdh margin", "propane dehydrogenation", "pdh plant", "pdh economics",
        "propylene", "china propane", "pdh capacity", "pdh feedstock",
        "chinese petrochemical", "pdh operating rate", "pain threshold",
    ],
    "LPG_Supply_Chain_Structure": [
        "supply chain", "fractionation", "storage terminal", "distribution",
        "value chain", "midstream", "downstream", "upstream lpg",
        "pipeline", "cavern storage", "refrigerated storage",
    ],
    "Seasonal_Trading_Patterns": [
        "seasonal", "winter heating", "summer demand", "rvp blending",
        "turnaround", "refinery maintenance", "q1 q3", "heating season",
        "seasonal spread", "contango", "backwardation seasonal",
    ],
    "Saudi_Aramco_Contract_Price": [
        "saudi aramco cp", "contract price", "aramco pricing", "retroactive",
        "term contract", "monthly cp", "saudi cp", "official selling price",
        "aramco osp", "cp mechanism",
    ],
    "AFEI_Benchmark": [
        "afei", "argus far east", "far east index", "moc process",
        "platts ewindow", "m1 m2", "fei", "lpg benchmark asia",
        "argus propane", "argus butane",
    ],
    "Propane_Naphtha_Spread": [
        "propane naphtha", "pro-nap", "naphtha spread", "naphtha ratio",
        "steam cracker feedstock", "naphtha alternative", "butadiene",
        "cracker economics", "ethylene feedstock",
    ],
    "Feedstock_Switching_Economics": [
        "feedstock switching", "ncm yield", "switching friction",
        "naphtha cracker", "ethylene yield", "propylene yield",
        "cracker feedstock", "lpg feedstock", "china tax",
    ],
    "Physical_Hedging_Architecture": [
        "hedging", "delta hedging", "swap", "futures hedge",
        "paper position", "hedge ratio", "roll yield", "contango carry",
        "forward curve", "vega", "options hedge",
    ],
    "Basis_Risk_Management": [
        "basis risk", "physical paper basis", "mark to market", "mark to model",
        "averaging period", "settlement basis", "hedge effectiveness",
        "sof risk", "pricing window",
    ],
    "Position_Management_and_PnL": [
        "position management", "p&l attribution", "pnl", "taylor expansion",
        "margin mechanics", "variation margin", "initial margin",
        "mt103", "swift settlement", "mark to market pnl",
    ],
    "VLGC_Freight_Dynamics": [
        "vlgc", "freight rate", "very large gas carrier", "tonne-mile",
        "shipping rate", "freight cost", "vessel", "fleet size",
        "time charter", "voyage charter", "bunker cost", "freight market",
        "baltic", "lpg freight",
    ],
    "Demurrage_and_Laytime": [
        "demurrage", "laytime", "nor tendering", "notice of readiness",
        "wibon", "despatch", "loading time", "discharge time",
        "port congestion", "vessel waiting",
    ],
    "Physical_LPG_Contract_Logic": [
        "fob", "cif", "cfr", "des", "contract logic",
        "custody transfer", "hose connection", "sgs inspection",
        "bill of lading", "letter of credit", "trade finance",
        "contract terms", "physical contract",
    ],
    "Incoterms_in_LPG_Trading": [
        "incoterm", "fob cif", "documentary mechanics",
        "trade finance", "sofr", "letter of credit",
        "payment terms", "l/c", "shipping documents",
    ],
    "ETRM_Systems": [
        "etrm", "openlink", "endur", "tpm", "apm", "jvs",
        "cmotion", "gmotion", "risk engine", "trade capture",
        "commodity trading system", "ctrm",
    ],
    "Geographical_Arbitrage": [
        "geographical arbitrage", "arb window", "netback",
        "route optimization", "east west arb", "us asia arb",
        "arb economics", "trade route", "arbitrage opportunity",
    ],
    # Entities
    "Saudi_Aramco": [
        "saudi aramco", "ras tanura", "juaymah", "aramco",
        "saudi arabia oil", "saudi exports",
    ],
    "Petronas": [
        "petronas", "bintulu", "malaysia lng", "malaysia lpg",
    ],
    "Hengyi_Industries": [
        "hengyi", "brunei refinery", "pulau muara besar",
    ],
    "Argus_Media": [
        "argus media", "argus international lpg", "argus methodology",
    ],
    "S&P_Global_Platts": [
        "platts", "s&p global", "moc window", "platts lpg",
        "platts assessment", "seam benchmark",
    ],
    "Kpler": [
        "kpler", "cargo tracking", "vessel tracking kpler",
    ],
    "Vortexa": [
        "vortexa", "vortexa sdk", "energy analytics vortexa",
    ],
    "Vitol": [
        "vitol", "vitol group", "vitol trading",
    ],
    "Trafigura": [
        "trafigura", "trafigura group",
    ],
    "CME_Group": [
        "cme group", "cme lpg", "nymex", "cme futures",
        "propane futures", "lpg derivatives exchange",
    ],
    "Mont_Belvieu": [
        "mont belvieu", "mb propane", "opis", "ngl hub",
        "enterprise products", "mb butane",
    ],
    "US_Gulf_Coast_Export_Terminals": [
        "usgc", "gulf coast export", "enterprise terminal",
        "targa", "oneok", "export terminal us",
    ],
    "Ras_Tanura_Terminal": [
        "ras tanura", "juaymah terminal",
    ],
    "Panama_Canal": [
        "panama canal", "gatun lake", "transit slot",
        "panama transit", "canal drought",
    ],
    "Cape_of_Good_Hope_Route": [
        "cape of good hope", "cape route", "suez alternative",
    ],
    "Strait_of_Hormuz": [
        "strait of hormuz", "hormuz", "chokepoint middle east",
    ],
    "Chinese_PDH_Plants": [
        "chinese pdh plant", "china pdh", "pdh operator",
        "china propylene", "pdh overcapacity",
    ],
}


# ─── Smart content sampling for web-scraped files ────────────────────
LPG_KEYWORDS = [
    "lpg", "propane", "butane", "vlgc", "naphtha", "pdh", "mont belvieu",
    "aramco", "afei", "petrochemical", "freight rate", "demurrage",
    "arbitrage", "hedging", "ngl", "fob", "cif", "cfr", "netback",
    "cracker", "fractionat", "liquefied petroleum", "gas carrier",
    "shipping rate", "charter rate", "belvieu", "platts", "argus",
    "swap", "futures", "barrel", "cargo", "vessel", "terminal",
    "refinery", "ethylene", "propylene", "feedstock",
]


def smart_sample(content, max_chars=MAX_INPUT_CHARS):
    """Extract keyword-rich paragraphs from large files instead of blind truncation.

    For files where the first 30K chars are web navigation noise, this finds
    paragraphs containing LPG keywords and assembles them into a focused extract.
    """
    if len(content) <= max_chars:
        return content

    # Split into paragraphs (double newline or single newline with blank)
    paragraphs = re.split(r'\n\s*\n|\n(?=\s*\n)', content)

    # Score each paragraph by keyword hits
    scored = []
    for i, para in enumerate(paragraphs):
        para_lower = para.lower()
        if len(para.strip()) < 40:
            continue  # skip very short fragments
        hits = 0
        for kw in LPG_KEYWORDS:
            hits += para_lower.count(kw)
        if hits > 0:
            scored.append((hits, i, para))

    if not scored:
        # No keyword hits at all — fall back to head truncation
        return content[:max_chars] + "\n\n[... TRUNCATED ...]"

    # Sort by relevance (hit count), keep original order as tiebreaker
    scored.sort(key=lambda x: (-x[0], x[1]))

    # Assemble top paragraphs up to max_chars
    selected = []
    total_len = 0
    for hits, idx, para in scored:
        if total_len + len(para) + 2 > max_chars:
            if total_len > max_chars * 0.5:
                break  # enough content
            continue  # skip this one, try smaller ones
        selected.append((idx, para))
        total_len += len(para) + 2

    # Re-sort by original position for coherent reading order
    selected.sort(key=lambda x: x[0])
    result = "\n\n".join(para for _, para in selected)
    return result


# ─── Extraction prompt (the MAP function) ──────────────────────────────
EXTRACTION_PROMPT = """You are a quantitative research analyst extracting hard data from a raw source document about LPG/energy trading.

EXTRACT ONLY:
1. Specific numbers: prices ($X/mt), rates ($X/day), volumes (X mt/year), percentages
2. Formulas and equations (pricing, margin, netback, P&L)
3. Benchmark definitions and methodology details
4. Freight rates, vessel specifications, route economics
5. Counterparty-specific facts (capacity, location, operational details)
6. Regulatory or contractual mechanics (Incoterms, L/C terms, settlement)
7. Date-stamped market data points

IGNORE: subjective commentary, market sentiment, vague forecasts without numbers, filler text, navigation/UI elements, ads.

If the document contains NO extractable hard data relevant to LPG/energy trading, respond with exactly: NO_RELEVANT_DATA

Otherwise, respond in this exact JSON format:
{
  "title": "Brief descriptive title of the source",
  "domain": "one of: market_fundamentals | pricing | logistics | strategy | entity | regulation | other",
  "facts": [
    {
      "claim": "The specific factual claim, with exact numbers",
      "category": "one of: price | volume | rate | formula | specification | mechanism | entity_detail",
      "entities": ["list of entities/benchmarks mentioned"],
      "confidence": "high or medium"
    }
  ],
  "key_numbers": {
    "description_of_number": "the number with units"
  }
}

Keep facts atomic — one claim per entry. Maximum 20 facts per document. Prioritize unique, specific data over generic statements."""


# ─── Progress tracking ─────────────────────────────────────────────────
def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {
        "processed": {},   # filename → {status, target, facts_count, timestamp}
        "skipped": [],     # filenames with no relevant data
        "errors": [],      # filenames that failed
        "stats": {"total_facts": 0, "total_processed": 0, "total_skipped": 0},
    }


def save_progress(progress):
    PROGRESS_FILE.write_text(
        json.dumps(progress, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


# ─── MAP: Extract facts from a single source file ─────────────────────
def map_extract(filepath, client):
    """Call LLM to extract hard data from a single source file."""
    content = filepath.read_text(encoding="utf-8", errors="replace")

    # Skip tiny files
    if len(content.strip()) < MIN_FILE_SIZE:
        return {"status": "skip", "reason": "too_small"}

    # Smart sampling for large files (keyword-focused instead of blind truncation)
    if len(content) > MAX_INPUT_CHARS:
        content = smart_sample(content, MAX_INPUT_CHARS)

    for attempt in range(2):
        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": f"{EXTRACTION_PROMPT}\n\n---\nSOURCE DOCUMENT:\n{content}"}
                ],
            )
            result_text = response.content[0].text.strip()

            if "NO_RELEVANT_DATA" in result_text:
                return {"status": "no_data"}

            # Parse JSON from response (handle markdown code blocks)
            json_text = result_text
            if "```json" in json_text:
                json_text = json_text.split("```json")[1].split("```")[0]
            elif "```" in json_text:
                json_text = json_text.split("```")[1].split("```")[0]

            # Try to find JSON object if text wraps it
            json_text = json_text.strip()
            if not json_text.startswith("{"):
                brace = json_text.find("{")
                if brace != -1:
                    json_text = json_text[brace:]
                else:
                    return {"status": "no_data"}

            # Truncate at last complete JSON structure if unterminated
            try:
                extracted = json.loads(json_text)
            except json.JSONDecodeError:
                # Try to fix truncated JSON by finding last complete fact
                last_brace = json_text.rfind("}")
                if last_brace > 0:
                    # Close all open brackets
                    attempt = json_text[:last_brace+1] + "]}"
                    try:
                        extracted = json.loads(attempt)
                    except json.JSONDecodeError:
                        raise
                else:
                    raise

            return {"status": "ok", "data": extracted}

        except json.JSONDecodeError as e:
            if attempt == 0:
                time.sleep(1)
                continue  # retry once on JSON parse failure
            return {"status": "error", "reason": f"JSON parse: {e}", "raw": result_text[:500]}
        except Exception as e:
            return {"status": "error", "reason": str(e)}


# ─── ROUTE: Find best target wiki note for extracted data ──────────────
def route_to_note(extracted_data):
    """Score each wiki note against extracted facts and return best matches."""
    if not extracted_data or "facts" not in extracted_data:
        return []

    # Build a text blob from all facts + entities + title
    text_parts = [extracted_data.get("title", "").lower()]
    for fact in extracted_data.get("facts", []):
        text_parts.append(fact.get("claim", "").lower())
        text_parts.extend([e.lower() for e in fact.get("entities", [])])
    search_text = " ".join(text_parts)

    # Score each note
    scores = {}
    for note_stem, keywords in ROUTING_INDEX.items():
        score = 0
        for kw in keywords:
            count = search_text.count(kw.lower())
            if count > 0:
                # Longer keywords are more specific → higher weight
                weight = len(kw.split())
                score += count * weight * 5
        if score > 0:
            scores[note_stem] = score

    # Also use domain hint
    domain = extracted_data.get("domain", "")
    domain_boost = {
        "market_fundamentals": ["LPG_Market_Fundamentals", "Chinese_PDH_Margin", "LPG_Supply_Chain_Structure", "Seasonal_Trading_Patterns"],
        "pricing": ["AFEI_Benchmark", "Saudi_Aramco_Contract_Price", "Propane_Naphtha_Spread", "Feedstock_Switching_Economics", "Physical_Hedging_Architecture", "Basis_Risk_Management"],
        "logistics": ["VLGC_Freight_Dynamics", "Demurrage_and_Laytime", "Physical_LPG_Contract_Logic", "Incoterms_in_LPG_Trading", "ETRM_Systems"],
        "strategy": ["Geographical_Arbitrage"],
        "entity": list(ROUTING_INDEX.keys())[-17:],  # entity notes
    }
    for note in domain_boost.get(domain, []):
        scores[note] = scores.get(note, 0) + 3

    if not scores:
        return []

    # Return top matches — require minimum absolute score of 15
    # to avoid weak false-positive routing
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_score = ranked[0][1]
    if top_score < 15:
        return []  # no confident match
    threshold = max(15, top_score * 0.3)
    return [(stem, score) for stem, score in ranked if score >= threshold][:3]


# ─── REDUCE: Append mined data to target wiki note ────────────────────
def reduce_append(note_stem, facts, source_filename, dry_run=False):
    """Append extracted facts to a wiki note under ## Mined Data section."""
    # Find the note file
    note_path = None
    for d in WIKI_DIRS:
        candidate = VAULT / d / f"{note_stem}.md"
        if candidate.exists():
            note_path = candidate
            break

    if note_path is None:
        return False, f"Note not found: {note_stem}"

    # Format the facts as bullet points
    date = datetime.now().strftime("%Y-%m-%d")
    fact_lines = []
    for f in facts:
        claim = f.get("claim", "").strip()
        cat = f.get("category", "")
        conf = f.get("confidence", "")
        if claim:
            marker = "**" if conf == "high" else ""
            fact_lines.append(f"- {marker}{claim}{marker} `[{cat}]`")

    if not fact_lines:
        return False, "No facts to append"

    new_block = f"\n### From `{source_filename}` ({date})\n" + "\n".join(fact_lines) + "\n"

    if dry_run:
        return True, f"Would append {len(fact_lines)} facts to {note_stem}"

    content = note_path.read_text(encoding="utf-8", errors="replace")

    # Check if ## Mined Data section exists
    if "## Mined Data" in content:
        # Append to existing section (before the next ## heading or end)
        idx = content.index("## Mined Data")
        # Find the end of the Mined Data section
        next_h2 = content.find("\n## ", idx + 14)
        if next_h2 == -1:
            # Append before final ---
            last_hr = content.rfind("\n---")
            if last_hr > idx:
                content = content[:last_hr] + new_block + content[last_hr:]
            else:
                content = content + new_block
        else:
            content = content[:next_h2] + new_block + content[next_h2:]
    else:
        # Create new ## Mined Data section before the last ---
        section_header = "\n## Mined Data\n\n> Facts extracted from raw source documents by `miner.py`\n"
        last_hr = content.rfind("\n---")
        if last_hr > 10:
            content = content[:last_hr] + section_header + new_block + content[last_hr:]
        else:
            content = content + section_header + new_block

    note_path.write_text(content, encoding="utf-8")
    return True, f"Appended {len(fact_lines)} facts to {note_stem}"


# ─── Main pipeline ─────────────────────────────────────────────────────
def get_source_files():
    """Get all .txt source files sorted by name."""
    return sorted(SOURCES_DIR.glob("*.txt"), key=lambda f: f.name)


def run_pipeline(limit=None, dry_run=False, specific_file=None):
    """Run the full Map-Route-Reduce pipeline."""
    import anthropic

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        # Try .env file
        env_file = VAULT / ".env"
        if env_file.exists():
            for line in env_file.read_text().split("\n"):
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set. Set it via environment or .env file.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    progress = load_progress()
    files = get_source_files()

    if specific_file:
        files = [f for f in files if f.name == specific_file]
        if not files:
            print(f"File not found: {specific_file}")
            return

    # Filter already processed
    remaining = [f for f in files if f.name not in progress["processed"]
                 and f.name not in progress["skipped"]]

    if limit:
        remaining = remaining[:limit]

    if not remaining:
        print("All source files have been processed.")
        return

    print(f"\nProcessing {len(remaining)} source files...")
    print(f"{'='*60}")

    total_facts = 0
    total_appended = 0

    for i, filepath in enumerate(remaining):
        fname = filepath.name
        fsize = filepath.stat().st_size
        print(f"\n[{i+1}/{len(remaining)}] {fname} ({fsize:,} bytes)")

        sys.stdout.flush()
        # ── MAP ──
        print(f"  MAP: Extracting...", end=" ", flush=True)
        result = map_extract(filepath, client)

        if result["status"] == "skip":
            print(f"SKIP ({result['reason']})")
            progress["skipped"].append(fname)
            progress["stats"]["total_skipped"] += 1
            save_progress(progress)
            continue

        if result["status"] == "no_data":
            print("NO RELEVANT DATA")
            progress["skipped"].append(fname)
            progress["stats"]["total_skipped"] += 1
            save_progress(progress)
            continue

        if result["status"] == "error":
            print(f"ERROR: {result['reason'][:80]}")
            progress["errors"].append({"file": fname, "error": result["reason"][:200]})
            save_progress(progress)
            continue

        extracted = result["data"]
        facts = extracted.get("facts", [])
        title = extracted.get("title", "?")
        print(f"OK — {len(facts)} facts, \"{title[:50]}\"")

        # Save raw extract
        extract_path = EXTRACTS_DIR / f"{filepath.stem}.json"
        extract_path.write_text(json.dumps(extracted, indent=2, ensure_ascii=False), encoding="utf-8")

        # ── ROUTE ──
        targets = route_to_note(extracted)
        if not targets:
            print(f"  ROUTE: No matching wiki note found")
            progress["processed"][fname] = {
                "status": "unrouted",
                "facts_count": len(facts),
                "title": title,
                "timestamp": datetime.now().isoformat(),
            }
            total_facts += len(facts)
            save_progress(progress)
            continue

        primary_target = targets[0][0]
        print(f"  ROUTE: → {primary_target} (score: {targets[0][1]})", end="")
        if len(targets) > 1:
            print(f" + {', '.join(t[0] for t in targets[1:])}", end="")
        print()

        # ── REDUCE ──
        # Send facts to primary target only (avoid duplication)
        ok, msg = reduce_append(primary_target, facts, fname, dry_run=dry_run)
        prefix = "DRY" if dry_run else "REDUCE"
        print(f"  {prefix}: {msg}")

        if ok:
            total_appended += len(facts)

        progress["processed"][fname] = {
            "status": "ok" if ok else "route_fail",
            "target": primary_target,
            "all_targets": [t[0] for t in targets],
            "facts_count": len(facts),
            "title": title,
            "timestamp": datetime.now().isoformat(),
        }
        progress["stats"]["total_facts"] += len(facts)
        progress["stats"]["total_processed"] += 1
        total_facts += len(facts)
        save_progress(progress)

        sys.stdout.flush()
        # Rate limit: ~0.5s between calls to be respectful
        time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"Done. Extracted {total_facts} facts, appended {total_appended} to wiki notes.")
    print(f"Progress saved to {PROGRESS_FILE}")


def scan_preview():
    """Preview: list source files and their estimated size category."""
    files = get_source_files()
    progress = load_progress()

    processed = set(progress["processed"].keys()) | set(progress["skipped"])
    remaining = [f for f in files if f.name not in processed]

    print(f"\nSource files: {len(files)} total")
    print(f"  Processed:  {len(progress['processed'])}")
    print(f"  Skipped:    {len(progress['skipped'])}")
    print(f"  Errors:     {len(progress['errors'])}")
    print(f"  Remaining:  {len(remaining)}")

    if remaining:
        sizes = [f.stat().st_size for f in remaining]
        small = sum(1 for s in sizes if s < 1024)
        medium = sum(1 for s in sizes if 1024 <= s < 50000)
        large = sum(1 for s in sizes if s >= 50000)
        print(f"\n  Size distribution of remaining:")
        print(f"    <1KB (likely skip): {small}")
        print(f"    1-50KB:             {medium}")
        print(f"    >50KB:              {large}")
        total_mb = sum(sizes) / 1048576
        print(f"    Total:              {total_mb:.1f} MB")

    # Show routing stats for already processed
    if progress["processed"]:
        targets = defaultdict(int)
        unrouted = 0
        for info in progress["processed"].values():
            t = info.get("target")
            if t:
                targets[t] += 1
            else:
                unrouted += 1
        if targets:
            print(f"\n  Routing distribution (processed):")
            for t, count in sorted(targets.items(), key=lambda x: -x[1])[:15]:
                print(f"    {t}: {count} sources")
            if unrouted:
                print(f"    (unrouted): {unrouted}")


def show_status():
    """Show detailed pipeline status."""
    progress = load_progress()
    print(f"\n{'='*60}")
    print(f"  Miner Pipeline Status")
    print(f"{'='*60}")
    print(f"  Total processed: {progress['stats']['total_processed']}")
    print(f"  Total skipped:   {progress['stats']['total_skipped']}")
    print(f"  Total facts:     {progress['stats']['total_facts']}")
    print(f"  Errors:          {len(progress['errors'])}")

    files = get_source_files()
    processed = set(progress["processed"].keys()) | set(progress["skipped"])
    remaining = len([f for f in files if f.name not in processed])
    print(f"  Remaining:       {remaining}")

    if progress["errors"]:
        print(f"\n  Recent errors:")
        for err in progress["errors"][-5:]:
            print(f"    {err['file']}: {err['error'][:60]}")

    # Per-note breakdown
    targets = defaultdict(int)
    for info in progress["processed"].values():
        t = info.get("target")
        if t:
            targets[t] += 1

    if targets:
        print(f"\n  Facts routed to:")
        for t, count in sorted(targets.items(), key=lambda x: -x[1]):
            print(f"    {t}: {count} sources")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Source text mining pipeline")
    parser.add_argument("--scan", action="store_true", help="Preview: list sources and stats")
    parser.add_argument("--run", action="store_true", help="Run extraction pipeline")
    parser.add_argument("--status", action="store_true", help="Show pipeline status")
    parser.add_argument("--limit", type=int, help="Max files to process in this run")
    parser.add_argument("--dry-run", action="store_true", help="Extract but don't write to wiki")
    parser.add_argument("--file", help="Process a specific source file")
    parser.add_argument("--rescan-skipped", action="store_true", help="Re-process skipped files using smart sampling")
    parser.add_argument("--reset", action="store_true", help="Reset all progress")
    args = parser.parse_args()

    if args.rescan_skipped:
        # Move skipped files with LPG keywords back to "remaining"
        progress = load_progress()
        sources_dir = SOURCES_DIR
        skipped = progress.get("skipped", [])
        reinstated = []
        for fname in skipped:
            fp = sources_dir / fname
            if not fp.exists() or fp.stat().st_size < MIN_FILE_SIZE:
                continue
            try:
                text = fp.read_text(encoding="utf-8", errors="replace").lower()
            except Exception:
                continue
            hits = sum(text.count(kw) for kw in LPG_KEYWORDS)
            if hits >= 5:
                reinstated.append(fname)
        # Remove reinstated from skipped list
        progress["skipped"] = [f for f in skipped if f not in set(reinstated)]
        progress["stats"]["total_skipped"] -= len(reinstated)
        save_progress(progress)
        print(f"Reinstated {len(reinstated)} skipped files for re-processing.")
        print(f"Run --run to process them.")
        sys.exit(0)

    if args.reset:
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
        # Also clear extracts
        for f in EXTRACTS_DIR.glob("*.json"):
            f.unlink()
        print("Progress and extracts reset.")
        sys.exit(0)

    if args.status:
        show_status()
    elif args.scan:
        scan_preview()
    elif args.run:
        run_pipeline(limit=args.limit, dry_run=args.dry_run, specific_file=args.file)
    else:
        scan_preview()
        print("\nUse --run to start processing, --status for details.")
