#!/usr/bin/env python3
"""
Obsidian Vault Health Check & Lint Pipeline
Run weekly: python vault_lint.py
Generates: 10_Atlas/Health_Report.md
"""
import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

VAULT = Path(r"C:\Users\itg\Desktop\lpg-trading-knowledge-base")
REPORT_PATH = VAULT / "10_Atlas" / "Health_Report.md"

SCAN_DIRS = [
    "10_Atlas",
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]

REQUIRED_YAML_FIELDS = ["aliases", "tags", "date", "status"]
REQUIRED_SECTIONS_CONCEPT = [
    "Empirical Facts vs Analytical Assumptions",
    "Downside Risks",
]
VALID_STATUSES = ["seed", "incubating", "evergreen"]


def normalize_name(name):
    """Normalize note name: underscores ↔ spaces, case-insensitive."""
    return name.replace("_", " ").replace("-", " ").strip().lower()


def find_md_files():
    """Find all .md files in scan directories."""
    files = []
    for d in SCAN_DIRS:
        dirpath = VAULT / d
        if dirpath.exists():
            for f in dirpath.glob("*.md"):
                files.append(f)
    return files


def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter as dict."""
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end == -1:
        return None
    yaml_block = content[3:end].strip()
    fields = {}
    for line in yaml_block.split("\n"):
        if ":" in line:
            key = line.split(":")[0].strip()
            val = line.split(":", 1)[1].strip()
            fields[key] = val
    return fields


def extract_wikilinks(content):
    """Extract all [[WikiLink]] targets from content."""
    return set(re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]", content))


def extract_headings(content):
    """Extract all ## headings."""
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", content, re.MULTILINE)]


def check_contradictions(files_data):
    """Check for contradictory quantitative claims across notes."""
    issues = []
    # Extract numeric claims with context
    claims = defaultdict(list)
    patterns = [
        (r"(\d[\d,.]*)\s*(?:million\s+)?tonn", "tonnage"),
        (r"\$\s*([\d,.]+)\s*/\s*(?:mt|day)", "price_rate"),
        (r"([\d,.]+)\s*%", "percentage"),
        (r"~?\s*(\d{2,3})\s+(?:ships?|VLGCs?|vessels?)", "fleet_size"),
    ]
    for fpath, content in files_data.items():
        for pattern, category in patterns:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                val = m.group(1).replace(",", "")
                context = content[max(0, m.start()-40):m.end()+40].replace("\n", " ").strip()
                claims[category].append((fpath.stem, val, context))

    # Flag fleet size contradictions
    fleet_vals = set()
    for stem, val, ctx in claims.get("fleet_size", []):
        try:
            fleet_vals.add((stem, int(float(val))))
        except ValueError:
            pass
    unique_fleet = set(v for _, v in fleet_vals)
    if len(unique_fleet) > 1:
        details = "; ".join(f"{s}: {v}" for s, v in fleet_vals)
        issues.append(f"Fleet size inconsistency: {details}")

    return issues


def run_lint():
    """Run all lint checks and generate report."""
    files = find_md_files()
    all_note_names = {f.stem for f in files}
    all_note_names_normalized = {normalize_name(f.stem) for f in files}

    issues = {
        "critical": [],
        "warning": [],
        "info": [],
    }
    stats = {
        "total_files": len(files),
        "by_status": defaultdict(int),
        "by_dir": defaultdict(int),
        "orphan_notes": [],
        "broken_links": defaultdict(list),
        "missing_yaml": [],
        "missing_sections": [],
        "no_risk_links": [],
    }

    files_data = {}
    for f in files:
        content = f.read_text(encoding="utf-8", errors="replace")
        files_data[f] = content
        rel_dir = f.parent.name
        stats["by_dir"][rel_dir] += 1

        # --- YAML Frontmatter Check ---
        yaml = parse_yaml_frontmatter(content)
        if yaml is None:
            stats["missing_yaml"].append(f.stem)
            issues["critical"].append(f"`{f.stem}`: Missing YAML frontmatter")
        else:
            for field in REQUIRED_YAML_FIELDS:
                if field not in yaml:
                    issues["warning"].append(f"`{f.stem}`: Missing YAML field `{field}`")
            status = yaml.get("status", "").strip("[] ")
            if status and status in VALID_STATUSES:
                stats["by_status"][status] += 1
            elif status:
                issues["warning"].append(f"`{f.stem}`: Invalid status `{status}`")

        # --- WikiLink Check (normalize underscores/spaces) ---
        links = extract_wikilinks(content)
        for link_target in links:
            if normalize_name(link_target) not in all_note_names_normalized:
                stats["broken_links"][f.stem].append(link_target)

        # --- Section Check (non-entity, non-atlas) ---
        if rel_dir not in ("40_Entities", "10_Atlas"):
            headings = extract_headings(content)
            for section in REQUIRED_SECTIONS_CONCEPT:
                if not any(section.lower() in h.lower() for h in headings):
                    stats["missing_sections"].append((f.stem, section))
                    issues["warning"].append(
                        f"`{f.stem}`: Missing section `{section}`"
                    )

        # --- Risk Link Check ---
        risk_keywords = ["risk", "downside", "exposure", "loss", "margin call"]
        has_risk = any(kw in content.lower() for kw in risk_keywords)
        if not has_risk and rel_dir not in ("10_Atlas",):
            stats["no_risk_links"].append(f.stem)
            issues["info"].append(f"`{f.stem}`: No risk-related content detected")

    # --- Orphan Detection (normalize names) ---
    linked_targets_normalized = set()
    for f, content in files_data.items():
        for lt in extract_wikilinks(content):
            linked_targets_normalized.add(normalize_name(lt))
    for note_name in all_note_names:
        if normalize_name(note_name) not in linked_targets_normalized and note_name not in ("Master_Index", "Health_Report"):
            stats["orphan_notes"].append(note_name)
            issues["info"].append(f"`{note_name}`: Orphan note (not linked from anywhere)")

    # --- Cross-Note Contradiction Check ---
    contradictions = check_contradictions(files_data)
    for c in contradictions:
        issues["warning"].append(f"Data contradiction: {c}")

    # --- Broken Links Summary ---
    total_broken = sum(len(v) for v in stats["broken_links"].values())
    for src, targets in stats["broken_links"].items():
        for t in targets:
            issues["info"].append(f"`{src}` → `[[{t}]]`: Broken link (target note not found)")

    # --- Generate Report ---
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = []
    report.append("---")
    report.append("aliases: [Health Check, Lint Report]")
    report.append("tags: [vault-maintenance, automated]")
    report.append(f"date: {datetime.now().strftime('%Y-%m-%d')}")
    report.append("status: evergreen")
    report.append("---")
    report.append("")
    report.append(f"# Vault Health Report")
    report.append(f"> Auto-generated: {now}")
    report.append("")
    report.append("## Summary")
    report.append(f"- **Total notes**: {stats['total_files']}")
    report.append(f"- **Critical issues**: {len(issues['critical'])}")
    report.append(f"- **Warnings**: {len(issues['warning'])}")
    report.append(f"- **Info**: {len(issues['info'])}")
    report.append("")

    report.append("### Notes by Directory")
    for d, count in sorted(stats["by_dir"].items()):
        report.append(f"- `{d}/`: {count}")
    report.append("")

    report.append("### Notes by Status")
    for s, count in sorted(stats["by_status"].items()):
        report.append(f"- `{s}`: {count}")
    report.append("")

    if issues["critical"]:
        report.append("## Critical Issues")
        for i in issues["critical"]:
            report.append(f"- {i}")
        report.append("")

    if issues["warning"]:
        report.append("## Warnings")
        for i in issues["warning"]:
            report.append(f"- {i}")
        report.append("")

    if stats["orphan_notes"]:
        report.append("## Orphan Notes (not linked from any other note)")
        for o in sorted(stats["orphan_notes"]):
            report.append(f"- [[{o}]]")
        report.append("")

    total_broken = sum(len(v) for v in stats["broken_links"].values())
    if total_broken > 0:
        report.append(f"## Broken WikiLinks ({total_broken} total)")
        for src, targets in sorted(stats["broken_links"].items()):
            for t in targets:
                report.append(f"- `{src}` → [[{t}]]")
        report.append("")

    if stats["missing_sections"]:
        report.append("## Missing Required Sections")
        for note, section in stats["missing_sections"]:
            report.append(f"- `{note}`: missing `## {section}`")
        report.append("")

    report.append("---")
    report.append(f"*Next scheduled run: weekly*")

    report_text = "\n".join(report)
    REPORT_PATH.write_text(report_text, encoding="utf-8")
    return report_text, issues


if __name__ == "__main__":
    print("Running vault health check...")
    report, issues = run_lint()
    crit = len(issues["critical"])
    warn = len(issues["warning"])
    info = len(issues["info"])
    print(f"\nResults: {crit} critical, {warn} warnings, {info} info")
    print(f"Report saved to: {REPORT_PATH}")

    if crit > 0:
        sys.exit(1)
    sys.exit(0)
